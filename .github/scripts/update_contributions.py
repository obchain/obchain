#!/usr/bin/env python3
"""Regenerate the Protocol Contributions section of README.md from public PR data.

Queries every public PR authored by the configured user via the `gh` CLI,
filters out PRs in the user's own org, groups them by org and repo, and
renders collapsible <details> cards. Replaces content between the
PROTOCOL_CONTRIBUTIONS markers in README.md.

Run locally (requires `gh` auth):
    GH_TOKEN=$(cat ~/.github_token) python .github/scripts/update_contributions.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
USER = "obchain"
START = "<!-- PROTOCOL_CONTRIBUTIONS:START -->"
END = "<!-- PROTOCOL_CONTRIBUTIONS:END -->"

# Display metadata per org: (emoji, display_name, description). Lookup is
# case-insensitive against the org slug returned by GitHub.
ORG_META: dict[str, tuple[str, str, str]] = {
    "mahaxyz":       ("🟣", "MahaXYZ",            "Core contributor · stablecoin mechanics, governance, cross-chain expansion"),
    "mahadao":       ("🟠", "MahaDAO",            "DAO governance contracts"),
    "zerolend":      ("🟢", "ZeroLend",           "Lending protocol · core, governance, oracles, timelocks"),
    "digital-asset": ("🔵", "Digital Asset · DAML", "stdlib docs + `damlc` build inference (official DAML smart contract language)"),
    "tinyhumansai":  ("🟡", "TinyHumansAI · OpenHuman", "Personal AI assistant: cron, planner, weekly review, install"),
}

# Optional per-repo subtitle.
REPO_NOTE: dict[str, str] = {
    "mahaxyz/contracts":         "EVM core protocol",
    "mahaxyz/solana-contracts":  "Anchor / Rust",
    "mahaxyz/timelocks":         "Multi-chain timelock infrastructure",
    "digital-asset/daml":        "Official DAML smart contract language",
}


def fetch_prs() -> list[dict[str, Any]]:
    """Fetch up to 200 most-recent PRs authored by USER."""
    out = subprocess.check_output(
        [
            "gh", "search", "prs",
            "--author", USER,
            "--limit", "200",
            "--json", "repository,number,title,state,url,createdAt",
        ],
        text=True,
    )
    return json.loads(out)


def is_external(repo_full: str) -> bool:
    owner = repo_full.split("/", 1)[0]
    return owner.lower() != USER.lower()


def fetch_repo_meta(repo_full: str) -> tuple[int, int]:
    """Return (stars, forks) for a repo. Best-effort; (0, 0) on failure."""
    try:
        out = subprocess.check_output(
            ["gh", "api", f"repos/{repo_full}", "--jq", "[.stargazers_count, .forks_count]"],
            text=True,
        )
        stars, forks = json.loads(out)
        return int(stars), int(forks)
    except Exception:
        return 0, 0


def render_section(prs: list[dict[str, Any]]) -> str:
    by_org: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for pr in prs:
        full = pr["repository"]["nameWithOwner"]
        org, _ = full.split("/", 1)
        by_org[org][full].append(pr)

    org_order = sorted(
        by_org.keys(),
        key=lambda o: (-sum(len(v) for v in by_org[o].values()), o.lower()),
    )

    blocks: list[str] = []
    for org in org_order:
        meta = ORG_META.get(org.lower())
        if meta:
            emoji, display, desc = meta
        else:
            emoji, display, desc = ("⚪", org, "")
        repos = by_org[org]
        total = sum(len(v) for v in repos.values())
        repo_order = sorted(repos.keys(), key=lambda r: (-len(repos[r]), r.lower()))

        summary = f"<strong>{emoji} {display}</strong>"
        if desc:
            summary += f": {desc}"
        summary += f" · <em>{total} PR{'s' if total != 1 else ''}</em>"

        body: list[str] = []
        for repo_full in repo_order:
            stars, forks = fetch_repo_meta(repo_full)
            note = REPO_NOTE.get(repo_full, "")
            header = f"**[{repo_full}](https://github.com/{repo_full})**"
            badges: list[str] = []
            if stars:
                badges.append(f"⭐ {stars}")
            if forks:
                badges.append(f"{forks} fork{'s' if forks != 1 else ''}")
            if badges:
                header += " &nbsp;·&nbsp; " + " · ".join(badges)
            if note:
                header += f" &nbsp;·&nbsp; {note}"
            body.append(header)
            body.append("")
            body.append("| # | Title | Status |")
            body.append("|---|-------|--------|")
            for pr in sorted(repos[repo_full], key=lambda p: -p["number"]):
                title = pr["title"].replace("|", "\\|")
                state = pr["state"].lower()
                body.append(f"| [#{pr['number']}]({pr['url']}) | {title} | `{state}` |")
            body.append("")

        block = "\n".join(
            [
                "<details>",
                f"<summary>{summary}</summary>",
                "",
                "<br>",
                "",
                *body,
                "</details>",
            ]
        )
        blocks.append(block)

    return "\n\n".join(blocks)


def main() -> int:
    if not README.exists():
        print(f"ERROR: {README} not found", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print(f"ERROR: markers {START!r} / {END!r} not found in README.md", file=sys.stderr)
        return 1

    prs = [p for p in fetch_prs() if is_external(p["repository"]["nameWithOwner"])]
    new_section = render_section(prs)

    pre, _, rest = text.partition(START)
    _, _, post = rest.partition(END)
    new_text = f"{pre}{START}\n\n{new_section}\n\n{END}{post}"

    if new_text == text:
        print("README unchanged.")
        return 0

    README.write_text(new_text, encoding="utf-8")
    print(f"README updated — rendered {len(prs)} external PRs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
