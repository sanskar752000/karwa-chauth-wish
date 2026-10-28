# Karwa Chauth wish 🌙

A small, private, personal gift page: a single self-contained `index.html` (inline CSS + JS, no build step, no tracking, no backend).
It is published as a public repo only because free GitHub Pages needs one — it is **not** meant to be a public site (it is marked `noindex`).

## Change the names
- In `index.html`, at the top of the `<script>`: `HER_NAME` and `FROM_NAME`.
- Or per link: `index.html?to=Name&from=Name` (values are inserted with `textContent` only).

## Change the letter
Edit the `LETTER` array (and `MOON_LINES`, `CLOSING_LINE`, `CLOSING_SUB`) in the "EDIT ME" block.
Optional photos: add entries to `PHOTOS` (relative paths or `data:image/...` only).

## Security notes
- Strict Content-Security-Policy `<meta>`: scripts only via a SHA-256 hash of the inline script, no network connections, no forms, no `<base>`.
- **After you edit anything inside the `<script>`, run `python3 build_csp.py`** to refresh the hash, or the page will not run.
- User-controlled URL params are never used with `innerHTML`; `no-referrer`, `noindex,nofollow`.
- Only external request: optional Google Fonts (page falls back to system serif fonts).

No personal data beyond first names and the wedding date. Made with love.
