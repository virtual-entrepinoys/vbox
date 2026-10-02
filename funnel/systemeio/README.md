# VBox AI — Systeme.io Custom HTML Snippets

8 funnel pages rebuilt as **body-only HTML snippets** that paste directly into
Systeme.io's **Custom HTML** block (or a page's *Custom HTML* field).

## Funnel order
| # | File | Use as |
|---|------|--------|
| 1 | `page1-optin.html` | Opt-in / lead capture page |
| 2 | `page2-bridge.html` | Bridge / thank-you after opt-in |
| 3 | `page3-sales.html` | Long-form sales page (Brand Foundation Package) |
| 4 | `page4-upsell1.html` | Upsell 1 — Marketing Suite |
| 5 | `page5-downsell.html` | Downsell — Social Media Asset Pack |
| 6 | `page6-upsell2.html` | Upsell 2 — Website Building |
| 7 | `page7-welcome.html` | Welcome / onboarding |
| 8 | `page8-optin-thankyou.html` | Lead-magnet delivery confirmation |

## Systeme.io compatibility
- **No** `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags — each file is a single wrapping `<div class="vb-root">`.
- **No** JS frameworks (no Tailwind CDN, React, jQuery). FAQ accordion uses native `<details>` — no JavaScript.
- **Google Fonts** loaded via `@import` inside the `<style>` tag (Inter + Space Grotesk).
- **Font Awesome 6.5.1** loaded via a `<link>` tag at the top of each snippet.
- All CSS is **scoped under `.vb-root`** so nothing leaks into the rest of the Systeme.io page.
- Dark theme `#080B14`, purple glow `#8B5CF6` / `#A78BFA`, glassmorphism cards, max width 900px centered, mobile responsive.

## How to use
1. In Systeme.io, add a **Custom HTML** element (or open the page's Custom HTML field).
2. Open the matching `.html` file, copy the **entire** contents, and paste.
3. Replace the marked placeholders:
   - `<!-- Replace this block with your Systeme.io opt-in form embed -->` (page 1)
   - `<!-- INSERT SYSTEME.IO ORDER FORM HERE -->` (pages 3, 4, 5, 6)
   - Update each `href="#"` button to point at the next funnel step (comments note the target).
   - Fill `[X business days]` and `$___` price placeholders.

> `_build.py` is the generator used to produce these files consistently — not needed in Systeme.io.
