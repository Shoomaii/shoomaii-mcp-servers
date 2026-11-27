#!/usr/bin/env python3
"""Stamp your Apify Affiliate (?fpr=CODE) onto all Apify Store links in Shoomaii repos.

Usage:
  python3 scripts/apply_apify_affiliate.py --fpr YOUR_CODE --dry-run
  python3 scripts/apply_apify_affiliate.py --fpr YOUR_CODE
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

APIFY_URL_RE = re.compile(r'https://apify\.com/shoomaii(?:/[a-z0-9-]+)?(?:\?[^\s)\]`"\'<>]*)?')
TARGET_EXTS = {'.md', '.txt'}


def add_fpr(url: str, fpr: str) -> str:
    parts = urlsplit(url)
    params = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k != 'fpr']
    params.append(('fpr', fpr))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(params), parts.fragment))


def process_roots(roots: list[Path], fpr: str, dry_run: bool) -> tuple[int, int]:
    files_changed = 0
    links_updated = 0
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob('*')):
            if '.git' in path.parts or not path.is_file() or path.suffix.lower() not in TARGET_EXTS:
                continue
            original = path.read_text(encoding='utf-8')
            count = 0

            def _repl(match: re.Match[str]) -> str:
                nonlocal count
                old = match.group(0)
                new = add_fpr(old, fpr)
                if new != old:
                    count += 1
                return new

            updated = APIFY_URL_RE.sub(_repl, original)
            if count > 0:
                files_changed += 1
                links_updated += count
                action = 'WOULD UPDATE' if dry_run else 'UPDATED'
                print(f'{action}: {path} ({count} link(s))')
                if not dry_run:
                    path.write_text(updated, encoding='utf-8')
    return files_changed, links_updated


def main() -> None:
    parser = argparse.ArgumentParser(description='Append ?fpr=CODE to Apify Store links in docs.')
    parser.add_argument('--fpr', required=True, help='Your Apify Affiliate ?fpr= code (e.g. shoomaii).')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without editing files.')
    parser.add_argument(
        'paths',
        nargs='*',
        help='Optional repo paths (defaults to shoomaii-mcp-servers and sibling n8n-templates).',
    )
    args = parser.parse_args()
    fpr = args.fpr.strip()
    if not re.fullmatch(r'[A-Za-z0-9_-]{2,64}', fpr):
        raise SystemExit(f'Invalid --fpr code: {fpr!r}')

    repo_root = Path(__file__).resolve().parent.parent
    roots = [Path(p) for p in args.paths] if args.paths else [repo_root, repo_root.parent / 'n8n-templates']
    files_changed, links_updated = process_roots(roots, fpr, args.dry_run)
    print(f'Done: {files_changed} file(s), {links_updated} link(s).')


if __name__ == '__main__':
    main()
