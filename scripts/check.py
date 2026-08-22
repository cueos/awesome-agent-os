#!/usr/bin/env python3
"""Check every entry in README.md, and refresh star counts with --update.

    scripts/check.py            report only; exit 1 if anything is broken
    scripts/check.py --update   rewrite the star counts in place, then report

A GitHub entry fails when the repository is gone, archived, or has not been
pushed to in a year. Every other link fails on an error response. Needs `gh`
authenticated, or GH_TOKEN in the environment.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
STALE_DAYS = 365
WORKERS = 8

# Links to our own repositories are navigation, not entries.
SKIP_OWNERS = {"cueos"}

REPO_LINK = re.compile(r"https://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)")
ANY_LINK = re.compile(r"https://[^\s)\"'`<>\]]+")
STAR_BADGE = re.compile(r"`⭐ [^`]*`")


def human_stars(count: int) -> str:
    if count >= 100_000:
        return f"{count // 1000}k"
    if count >= 1_000:
        return f"{count / 1000:.1f}k"
    return str(count)


def gh_repo(slug: str) -> dict | None:
    """Repository metadata, or None when GitHub does not have it."""
    try:
        completed = subprocess.run(
            ["gh", "api", f"repos/{slug}"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None
    if completed.returncode != 0:
        return None
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError:
        return None


def check_repo(slug: str) -> tuple[str, str, str | None]:
    """Return (status, message, refreshed star text)."""
    data = gh_repo(slug)
    if data is None:
        return "GONE", f"{slug} — GitHub has no such repository", None
    if data.get("archived"):
        return "ARCHIVED", f"{slug} — archived upstream", None

    pushed = data.get("pushed_at")
    age_days = None
    if pushed:
        moment = datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
        age_days = (datetime.now(UTC) - moment).days
        if age_days > STALE_DAYS:
            return "STALE", f"{slug} — no push in {age_days} days", None

    stars = human_stars(int(data.get("stargazers_count") or 0))
    seen = "unknown" if age_days is None else f"{age_days}d ago"
    return "ok", f"{slug} — ⭐ {stars}, pushed {seen}", stars


def check_url(url: str) -> tuple[str, str, None]:
    request = urllib.request.Request(
        url, headers={"User-Agent": "awesome-agent-os link check"}
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return "ok", f"{url} — {response.status}", None
    except urllib.error.HTTPError as error:
        # A few hosts refuse robots they do not recognise; that is not a dead link.
        if error.code in (403, 405, 429):
            return "ok", f"{url} — {error.code} (refused the checker, not dead)", None
        return "DEAD", f"{url} — {error.code}", None
    except Exception as error:  # noqa: BLE001 - any failure to reach it is a failure
        return "DEAD", f"{url} — {type(error).__name__}", None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update", action="store_true", help="rewrite star counts in README.md"
    )
    args = parser.parse_args()

    text = README.read_text(encoding="utf-8")

    slugs = sorted(
        {
            f"{owner}/{name}"
            for owner, name in REPO_LINK.findall(text)
            if owner not in SKIP_OWNERS
        }
    )
    urls = sorted(
        {
            url.rstrip(".,;")
            for url in ANY_LINK.findall(text)
            if not url.startswith("https://github.com/")
            and "shields.io" not in url
            and "awesome.re" not in url
        }
    )

    problems = 0
    stars_by_slug: dict[str, str] = {}

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for slug, (status, message, stars) in zip(
            slugs, pool.map(check_repo, slugs), strict=True
        ):
            print(f"{status:<9} {message}")
            if status != "ok":
                problems += 1
            elif stars:
                stars_by_slug[slug] = stars

        for status, message, _ in pool.map(check_url, urls):
            print(f"{status:<9} {message}")
            if status != "ok":
                problems += 1

    if args.update and stars_by_slug:
        lines = text.splitlines(keepends=True)
        changed = 0
        for index, line in enumerate(lines):
            match = REPO_LINK.search(line)
            if not match:
                continue
            slug = f"{match.group(1)}/{match.group(2)}"
            stars = stars_by_slug.get(slug)
            if not stars:
                continue
            updated = STAR_BADGE.sub(f"`⭐ {stars}`", line)
            if updated != line:
                lines[index] = updated
                changed += 1
        if changed:
            README.write_text("".join(lines), encoding="utf-8")
            print(f"\nrefreshed {changed} star counts in {README.name}")
        else:
            print("\nstar counts already current")

    print(f"\nchecked {len(slugs)} repositories and {len(urls)} links, {problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
