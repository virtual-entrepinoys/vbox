#!/usr/bin/env python3
"""Builds website-home.html: the VBox AI main page as one Systeme.io-safe snippet."""
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, "_build.py")).read().split("pages = {}")[0]
ns = {"__file__": os.path.join(D, "_build.py")}
exec(src, ns)
snippet, NAV = ns["snippet"], ns["NAV"]

EXTRA = """
.vb-root{scroll-behavior:smooth;}
.vb-root .vb-wrap-w{max-width:1040px;margin:0 auto;position:relative;z-index:1;width:100%;}
.vb-root .vb-topnav{position:sticky;top:0;z-index:50;background:rgba(8,11,20,.82);backdrop-filter:blur(14px);border-bottom:1px solid rgba(255,255,255,.07);}
.vb-root .vb-topnav-in{max-width:1040px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:14px 20px;}
.vb-root .vb-links{display:flex;gap:28px;align-items:center;}
.vb-root .vb-links a{color:var(--muted);font-size:15px;font-weight:500;}
.vb-root .vb-links a:hover{color:#fff;}
.vb-root .vb-btn-sm{padding:10px 20px;font-size:14px;border-radius:10px;}
.vb-root .vb-btn-ghost{display:inline-block;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.04);color:#E7E9EF;border-radius:12px;padding:16px 28px;font-size:16px;font-weight:600;transition:all .2s;}
.vb-root .vb-btn-ghost:hover{border-color:rgba(167,139,250,.6);color:#fff;}
.vb-root .vb-grid-bg{position:absolute;inset:0;z-index:0;pointer-events:none;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:52px 52px;-webkit-mask-image:linear-gradient(to bottom,#000 0%,transparent 90%);mask-image:linear-gradient(to bottom,#000 0%,transparent 90%);}
.vb-root .vb-h1x{font-size:clamp(38px,7vw,72px);line-height:1.02;letter-spacing:-.045em;font-weight:700;background:linear-gradient(100deg,#fff 12%,#d8c7ff 52%,#9c7cff 100%);-webkit-background-clip:text;background-clip:text;color:transparent;}
.vb-root .vb-btnrow{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:34px;}
.vb-root .vb-trust{margin-top:18px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);font-weight:600;}
.vb-root .vb-tease{display:flex;align-items:center;gap:14px;text-align:left;padding:18px 20px;}
.vb-root .vb-tease .vb-icon{margin:0;flex:0 0 44px;width:44px;height:44px;}
.vb-root .vb-tease small{display:block;font-size:11px;letter-spacing:.13em;color:var(--dim);font-weight:600;}
.vb-root .vb-tease b{color:#fff;font-size:15px;}
.vb-root .vb-product{position:relative;display:flex;flex-direction:column;}
.vb-root .vb-product.vb-feat{border-color:rgba(167,139,250,.55);box-shadow:0 0 44px rgba(139,92,246,.2);transform:translateY(-8px);}
.vb-root .vb-tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--hl2);margin-bottom:10px;}
.vb-root .vb-pop{position:absolute;top:-13px;right:20px;background:linear-gradient(135deg,#7C3AED,#9333EA);color:#fff;font-size:11px;font-weight:700;letter-spacing:.08em;padding:5px 12px;border-radius:999px;box-shadow:0 0 20px rgba(139,92,246,.6);}
.vb-root .vb-product ul{margin:16px 0 22px;flex:1;}
.vb-root .vb-product ul li{font-size:14.5px;margin:9px 0;}
.vb-root .vb-quote{font-family:'Space Grotesk',sans-serif;font-size:clamp(22px,3vw,30px);line-height:1.35;color:#fff;font-weight:500;border-left:3px solid var(--purple);padding-left:22px;}
.vb-root .vb-split{display:grid;grid-template-columns:1.1fr 1fr;gap:48px;align-items:center;}
.vb-root .vb-bigcta{background:linear-gradient(180deg,rgba(124,58,237,.12),rgba(8,11,20,0));border:1px solid var(--border);border-radius:24px;padding:64px 28px;}
.vb-root .vb-foot4{max-width:1040px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;}
@media(max-width:760px){
 .vb-root .vb-links{display:none;}
 .vb-root .vb-split{grid-template-columns:1fr;gap:28px;}
 .vb-root .vb-product.vb-feat{transform:none;}
 .vb-root .vb-btn-ghost{width:100%;text-align:center;}
 .vb-root .vb-foot4{justify-content:center;text-align:center;}
}
"""

def tease(n, icon, name):
    return f'<a href="#products" class="vb-card vb-tease"><div class="vb-icon"><i class="fa-solid {icon}"></i></div><div><small>{n}</small><b>{name}</b></div></a>'

def prod(tag, icon, title, desc, items, feat=False):
    lis = "".join(f'<li><i class="fa-solid fa-check"></i>{i}</li>' for i in items)
    pop = '<div class="vb-pop">MOST POPULAR</div>' if feat else ""
    return f'''<div class="vb-card vb-product{" vb-feat" if feat else ""}">{pop}
  <div class="vb-icon"><i class="fa-solid {icon}"></i></div>
  <div class="vb-tag">{tag}</div><h3>{title}</h3>
  <p style="margin-top:10px;font-size:15px">{desc}</p>
  <ul class="vb-check">{lis}</ul>
  <!-- Link to the matching funnel / product page -->
  <a href="#get-started" class="vb-btn-ghost" style="text-align:center;padding:13px 20px;font-size:15px">Learn More &rarr;</a>
</div>'''

step = lambda n, ic, t, d: f'<div class="vb-card"><div class="vb-icon"><i class="fa-solid {ic}"></i></div><div class="vb-step-num">STEP {n}</div><h3>{t}</h3><p style="margin-top:8px;font-size:15px">{d}</p></div>'

body = f'''
<!-- ========== NAV ========== -->
<div class="vb-topnav"><div class="vb-topnav-in">
  <div class="vb-logo">VBox <span>AI</span></div>
  <div class="vb-links">
    <a href="#how-it-works">How It Works</a><a href="#products">Products</a><a href="#why">Why VBox AI</a>
    <!-- Link this to your opt-in page (funnel page 1) -->
    <a href="#get-started" class="vb-btn-primary vb-btn-sm" style="color:#fff">Get Started</a>
  </div>
</div></div>

<!-- ========== HERO ========== -->
<div class="vb-section" style="padding-top:90px;padding-bottom:80px">
  <div class="vb-grid-bg"></div>
  <div class="vb-glow-orb vb-orb-a" style="width:900px;height:700px;top:-120px"></div>
  <div class="vb-glow-orb vb-orb-b"></div>
  <div class="vb-wrap-w vb-center">
    <div class="vb-eyebrow"><i class="fa-solid fa-circle" style="font-size:7px;color:var(--hl)"></i>&nbsp; Built for modern real estate agents</div>
    <h1 class="vb-h1x">Your brand,<br>done for you.</h1>
    <p class="vb-lead" style="font-size:20px;max-width:700px;color:#A7B0C0">The complete AI-powered setup for real estate agents who are too busy building their business to build their brand.</p>
    <div class="vb-btnrow">
      <!-- Link to opt-in page -->
      <a href="#get-started" class="vb-btn-primary">Get Started&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
      <a href="#how-it-works" class="vb-btn-ghost"><i class="fa-regular fa-circle-play" style="color:var(--hl)"></i>&nbsp; See How It Works</a>
    </div>
    <p class="vb-trust"><i class="fa-solid fa-bolt" style="color:var(--hl)"></i>&nbsp; Powered by AI. Delivered like a pro.</p>
    <p class="vb-trust" style="margin-top:64px;margin-bottom:14px;font-size:11px">Your complete visibility system</p>
    <div class="vb-grid vb-g3">
      {tease("01","fa-fingerprint","Brand Foundation")}
      {tease("02","fa-bullhorn","Marketing Suite")}
      {tease("03","fa-globe","Website Building")}
    </div>
  </div>
</div>

<!-- ========== HOW IT WORKS ========== -->
<div class="vb-section" id="how-it-works" style="background:#0A0E1A">
  <div class="vb-glow-orb vb-orb-b" style="left:-160px;right:auto"></div>
  <div class="vb-wrap-w">
    <div class="vb-sec-head"><div class="vb-eyebrow">How it works</div><h2>Simple by design.</h2>
    <p class="vb-lead">No tech skills. No VA needed. Just answer a few questions and we handle the rest.</p></div>
    <div class="vb-grid vb-g3">
      {step(1,"fa-clipboard-list","Complete the Intake","Answer a short form about your business, brand, and goals.")}
      {step(2,"fa-wand-magic-sparkles","We Build It","Our AI-powered system creates your verified bios, brand guide, and materials.")}
      {step(3,"fa-copy","Copy. Paste. Done.","Everything is labeled, formatted, and ready to place on your profiles.")}
    </div>
  </div>
</div>

<!-- ========== PRODUCTS ========== -->
<div class="vb-section" id="products">
  <div class="vb-glow-orb vb-orb-a" style="top:-300px;opacity:.7"></div>
  <div class="vb-wrap-w">
    <div class="vb-sec-head"><div class="vb-eyebrow">The system</div><h2>One system. Three powerful products.</h2>
    <p class="vb-lead">Built to work together &mdash; or on their own.</p></div>
    <div class="vb-grid vb-g3" style="align-items:stretch">
      {prod("Start Here","fa-fingerprint","Business &amp; Brand Foundation","Your verified professional identity, platform-ready bios, brand strategy, and visibility audit &mdash; all in one complete package.",["Verified Profile &amp; Bio Suite","Brand Foundation Guide","Local Visibility Audit","Implementation Checklist"])}
      {prod("Show Up Professionally","fa-bullhorn","Real Estate Marketing Suite","Listing presentations, open house kits, social media templates, and email sequences &mdash; aligned to your brand.",["Listing Presentation","Open House Kit","Social Media Asset Pack","Email Templates"],True)}
      {prod("Your Online Home","fa-globe","Website Building","A clean, search-ready personal website built around your verified bios, brand story, and service focus.",["Homepage &amp; About Page","Buyer &amp; Seller Pages","Local SEO Foundation","Compliant Disclosures"])}
    </div>
  </div>
</div>

<!-- ========== WHY ========== -->
<div class="vb-section" id="why" style="background:#0A0E1A">
  <div class="vb-glow-orb" style="width:560px;height:560px;left:-220px;top:0;background:radial-gradient(circle,rgba(139,92,246,.25),transparent 70%)"></div>
  <div class="vb-wrap-w">
    <div class="vb-sec-head" style="text-align:left;max-width:640px"><div class="vb-eyebrow">Why VBox AI</div><h2>Built for the agent who doesn't have time for this.</h2></div>
    <div class="vb-split">
      <p class="vb-quote">You didn't become a real estate agent to spend weekends writing bios and updating Zillow. VBox AI takes that off your plate &mdash; completely.</p>
      <ul class="vb-check">
        <li><i class="fa-solid fa-check"></i>No tech skills required</li>
        <li><i class="fa-solid fa-check"></i>AI-verified accuracy &mdash; no guesswork</li>
        <li><i class="fa-solid fa-check"></i>Fair Housing compliant by design</li>
        <li><i class="fa-solid fa-check"></i>Every deliverable is labeled and ready to paste</li>
        <li><i class="fa-solid fa-check"></i>Built on your real information, not generic templates</li>
      </ul>
    </div>
  </div>
</div>

<!-- ========== CTA ========== -->
<div class="vb-section" id="get-started" style="padding-top:80px;padding-bottom:90px">
  <div class="vb-glow-orb vb-orb-a" style="top:auto;bottom:-340px;width:800px"></div>
  <div class="vb-wrap-w vb-center">
    <div class="vb-bigcta">
      <h2 style="font-size:clamp(28px,4.5vw,46px)">Ready to check this off your list?</h2>
      <p class="vb-lead">Start with the Foundation and build from there.</p>
      <div class="vb-mt"><!-- Link to opt-in page or Brand Foundation sales page -->
        <a href="#" class="vb-btn-primary" style="padding:18px 44px;font-size:18px">Get Started&nbsp; <i class="fa-solid fa-arrow-right"></i></a></div>
      <p class="vb-small" style="margin-top:22px">Have questions? Email us at <a href="mailto:hello@vbox-ai.com">hello@vbox-ai.com</a></p>
    </div>
  </div>
</div>

<!-- ========== FOOTER ========== -->
<div class="vb-footer"><div class="vb-foot4">
  <div class="vb-logo" style="font-size:18px">VBox <span>AI</span></div>
  <div class="vb-links"><a href="#how-it-works">How It Works</a><a href="#products">Products</a><a href="#get-started">Get Started</a></div>
  <div>&copy; 2026 VBox AI &middot; vbox-ai.com</div>
</div></div>
'''
out = os.path.join(D, "website-home.html")
open(out, "w").write(snippet("Website - Main Page", body, EXTRA))
print(out)
