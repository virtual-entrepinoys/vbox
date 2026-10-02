# VBox AI

Funnel and website for VBox AI, a done-for-you brand setup service for real estate agents.

- `funnel/systemeio/` - Systeme.io-ready, body-only HTML snippets (`website-home.html` plus funnel pages 1-8). Paste into a Custom HTML block. See its README.
- `funnel/strategy/` - Step-by-step funnel strategy (md, pdf, docx).
- `website-mockup/` - Original design mockup screens (full HTML pages, for reference only; not Systeme.io-compatible) and design notes.

Regenerate snippets: `python3 funnel/systemeio/_build.py` and `python3 funnel/systemeio/_build_home.py`.
