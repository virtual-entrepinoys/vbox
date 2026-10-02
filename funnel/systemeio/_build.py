#!/usr/bin/env python3
"""Generate 8 Systeme.io-compatible custom HTML snippets for the VBox AI funnel.
Rules: body-only (no doctype/html/head/body), no external JS frameworks,
Google Fonts via @import, Font Awesome via <link>, all styles scoped under
.vb-root so nothing leaks into the Systeme.io page. Max width 900px, dark
theme (#080B14) with purple glow (#8B5CF6 / #A78BFA), mobile responsive.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FA = ('<link rel="stylesheet" '
      'href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">')

# ---- Shared, fully-scoped base styles (everything under .vb-root) ----
BASE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

.vb-root{
  --bg:#080B14; --purple:#8B5CF6; --purple-dark:#7C3AED; --purple2:#9333EA;
  --hl:#A78BFA; --hl2:#C4B5FD; --text:#FFFFFF; --body:#CBD5E1;
  --muted:#94A3B8; --dim:#64748B; --card:rgba(255,255,255,0.04);
  --border:rgba(124,58,237,0.25); --green:#22C55E;
  font-family:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif;
  color:var(--body); line-height:1.6; background:var(--bg);
  -webkit-font-smoothing:antialiased;
}
.vb-root *,.vb-root *::before,.vb-root *::after{box-sizing:border-box;margin:0;padding:0;}
.vb-root .vb-section{background:var(--bg);position:relative;overflow:hidden;padding:56px 20px;}
.vb-root .vb-hero{min-height:100vh;display:flex;align-items:center;}
.vb-root .vb-wrap{max-width:900px;margin:0 auto;position:relative;z-index:1;width:100%;}
.vb-root .vb-narrow{max-width:720px;}
.vb-root .vb-center{text-align:center;}
.vb-root a{color:var(--hl);text-decoration:none;}
.vb-root h1,.vb-root h2,.vb-root h3{color:var(--text);line-height:1.15;letter-spacing:-0.02em;font-family:'Space Grotesk','Inter',sans-serif;}
.vb-root h1{font-size:clamp(30px,5vw,50px);font-weight:700;}
.vb-root h2{font-size:clamp(25px,3.6vw,36px);font-weight:700;}
.vb-root h3{font-size:19px;font-weight:600;color:var(--text);}
.vb-root p{margin-bottom:0;}
.vb-root .vb-hl{color:var(--hl);}
.vb-root .vb-eyebrow{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--hl2);background:rgba(124,58,237,.12);border:1px solid var(--border);padding:7px 15px;border-radius:999px;margin-bottom:20px;}
.vb-root .vb-lead{font-size:19px;color:var(--body);max-width:620px;margin:18px auto 0;}
.vb-root .vb-glow-orb{position:absolute;border-radius:50%;pointer-events:none;z-index:0;filter:blur(24px);}
.vb-root .vb-orb-a{width:600px;height:600px;top:-220px;left:50%;transform:translateX(-50%);background:radial-gradient(circle,rgba(139,92,246,.40) 0%,rgba(139,92,246,0) 70%);}
.vb-root .vb-orb-b{width:420px;height:420px;bottom:-200px;right:-120px;background:radial-gradient(circle,rgba(147,51,234,.28) 0%,rgba(147,51,234,0) 70%);}
.vb-root .vb-btn-primary{background:linear-gradient(135deg,#7C3AED,#9333EA);box-shadow:0 0 32px rgba(139,92,246,.45);color:#fff;border:none;border-radius:12px;padding:16px 32px;font-size:16px;font-weight:600;cursor:pointer;display:inline-block;text-decoration:none;transition:all .2s ease;}
.vb-root .vb-btn-primary:hover{transform:translateY(-2px);box-shadow:0 0 44px rgba(147,51,234,.75);color:#fff;}
.vb-root .vb-btn-block{display:block;width:100%;text-align:center;}
.vb-root .vb-link-ghost{display:inline-block;margin-top:18px;color:var(--muted);font-size:15px;text-decoration:underline;}
.vb-root .vb-link-ghost:hover{color:var(--hl);}
.vb-root .vb-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:28px;backdrop-filter:blur(10px);transition:box-shadow .25s,border-color .25s;}
.vb-root .vb-card:hover{box-shadow:0 0 30px rgba(139,92,246,.22);border-color:rgba(167,139,250,.5);}
.vb-root .vb-grid{display:grid;gap:20px;}
.vb-root .vb-g2{grid-template-columns:repeat(2,1fr);}
.vb-root .vb-g3{grid-template-columns:repeat(3,1fr);}
.vb-root .vb-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--hl2);background:linear-gradient(135deg,rgba(139,92,246,.45),rgba(147,51,234,.2));border:1px solid var(--border);margin-bottom:16px;}
.vb-root .vb-check{list-style:none;}
.vb-root .vb-check li{position:relative;padding-left:34px;margin:13px 0;color:var(--body);}
.vb-root .vb-check li i{position:absolute;left:0;top:3px;width:22px;height:22px;border-radius:50%;background:rgba(139,92,246,.22);color:var(--hl2);font-size:11px;display:flex;align-items:center;justify-content:center;}
.vb-root .vb-callout{border:1px solid var(--purple);border-left:4px solid var(--purple);background:rgba(139,92,246,.08);border-radius:14px;padding:22px 26px;box-shadow:0 0 30px rgba(139,92,246,.16);color:var(--body);}
.vb-root .vb-placeholder{border:2px dashed var(--border);border-radius:14px;padding:26px;text-align:center;color:var(--muted);font-size:14px;background:rgba(139,92,246,.05);}
.vb-root .vb-price{color:var(--text);font-size:34px;font-weight:700;display:block;margin-top:6px;font-family:'Space Grotesk',sans-serif;}
.vb-root .vb-logo{color:var(--text);font-weight:700;font-size:22px;letter-spacing:-.02em;font-family:'Space Grotesk',sans-serif;}
.vb-root .vb-logo span{color:var(--hl);}
.vb-root .vb-nav{display:flex;justify-content:space-between;align-items:center;max-width:900px;margin:0 auto 10px;padding:4px 0;position:relative;z-index:2;}
.vb-root .vb-footer{border-top:1px solid rgba(255,255,255,.07);text-align:center;padding:28px 20px;font-size:13px;color:var(--muted);background:var(--bg);}
.vb-root .vb-input{width:100%;background:rgba(255,255,255,.05);border:1px solid var(--border);border-radius:10px;padding:15px 18px;color:var(--text);font-size:16px;margin-bottom:14px;font-family:inherit;}
.vb-root .vb-input::placeholder{color:var(--muted);}
.vb-root .vb-badge-ok{width:74px;height:74px;border-radius:50%;margin:0 auto 22px;display:flex;align-items:center;justify-content:center;font-size:32px;color:#fff;background:linear-gradient(135deg,#7C3AED,#9333EA);box-shadow:0 0 42px rgba(139,92,246,.6);}
.vb-root .vb-badge-ok.vb-green{background:linear-gradient(135deg,#16A34A,#22C55E);box-shadow:0 0 42px rgba(34,197,94,.5);}
.vb-root .vb-confirm-bar{display:inline-flex;align-items:center;gap:10px;background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.4);color:#86EFAC;font-weight:600;font-size:15px;padding:10px 18px;border-radius:999px;margin-bottom:24px;}
.vb-root .vb-small{font-size:14px;color:var(--muted);}
.vb-root .vb-hr{border:none;border-top:1px solid rgba(124,58,237,.25);max-width:900px;margin:8px auto;}
.vb-root .vb-sec-head{text-align:center;margin-bottom:38px;}
.vb-root .vb-step-num{font-size:12px;font-weight:700;color:var(--hl);letter-spacing:.12em;margin-bottom:8px;}
.vb-root .vb-mt{margin-top:28px;}
.vb-root .vb-mt-sm{margin-top:16px;}
.vb-root details.vb-faq{background:var(--card);border:1px solid var(--border);border-radius:14px;margin-bottom:12px;padding:0 22px;}
.vb-root details.vb-faq summary{cursor:pointer;list-style:none;padding:18px 0;color:var(--text);font-weight:600;font-size:17px;display:flex;justify-content:space-between;align-items:center;gap:14px;}
.vb-root details.vb-faq summary::-webkit-details-marker{display:none;}
.vb-root details.vb-faq summary::after{content:'\\002B';color:var(--hl);font-size:22px;font-weight:400;}
.vb-root details.vb-faq[open] summary::after{content:'\\2212';}
.vb-root details.vb-faq p{padding:0 0 18px;color:var(--body);}
.vb-root .vb-timeline{position:relative;}
.vb-root .vb-timeline::before{content:'';position:absolute;left:21px;top:12px;bottom:12px;width:2px;background:linear-gradient(var(--purple),rgba(139,92,246,.1));}
.vb-root .vb-tl-item{position:relative;display:flex;gap:20px;margin-bottom:24px;}
.vb-root .vb-tl-item:last-child{margin-bottom:0;}
.vb-root .vb-tl-num{flex:0 0 44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#7C3AED,#9333EA);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 0 20px rgba(139,92,246,.55);z-index:1;}
@media(max-width:760px){
  .vb-root .vb-section{padding:44px 16px;}
  .vb-root .vb-g2,.vb-root .vb-g3{grid-template-columns:1fr;}
  .vb-root .vb-btn-primary{width:100%;text-align:center;}
  .vb-root .vb-lead{font-size:17px;}
  .vb-root .vb-nav{flex-direction:column;gap:6px;}
}
"""

def snippet(name, body, extra_css=""):
    css = BASE + (("\n/* page-specific */\n" + extra_css) if extra_css else "")
    return (f"<!-- VBox AI | Systeme.io Snippet | {name} -->\n"
            f"{FA}\n"
            f"<style>\n{css}\n</style>\n\n"
            f"<div class=\"vb-root\">\n{body}\n</div>\n")

FOOT = ('<div class="vb-footer">&copy; 2026 VBox AI &middot; vbox-ai.com '
        '&middot; hello@vbox-ai.com</div>')
NAV = ('<div class="vb-nav"><div class="vb-logo">VBox <span>AI</span></div>'
       '{right}</div>')

pages = {}

# ---------------- PAGE 1 : OPT-IN ----------------
pages["page1-optin.html"] = snippet("Page 1 - Opt-in / Lead Capture", f"""
<div class="vb-section vb-hero">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-glow-orb vb-orb-b"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='<div class="vb-small">For Real Estate Agents</div>')}
    <div style="padding-top:28px">
      <div class="vb-eyebrow"><i class="fa-solid fa-star"></i>&nbsp; Free Checklist</div>
      <h1>Is Your Online Presence <span class="vb-hl">Costing You Clients?</span></h1>
      <p class="vb-lead"><em>Grab the free checklist every real estate agent needs before they
      update another profile.</em></p>
      <div class="vb-card" style="max-width:480px;margin:34px auto 0;text-align:left">
        <!-- ===== Replace this block with your Systeme.io opt-in form embed ===== -->
        <input class="vb-input" type="text" placeholder="First Name">
        <input class="vb-input" type="email" placeholder="Email Address">
        <a href="#" class="vb-btn-primary vb-btn-block">Send Me the Checklist&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
        <!-- ===== END Systeme.io form block ===== -->
        <p class="vb-small vb-center" style="margin-top:14px"><i class="fa-solid fa-lock"></i>&nbsp; No spam. Just the good stuff.</p>
      </div>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 2 : BRIDGE ----------------
pages["page2-bridge.html"] = snippet("Page 2 - Bridge / Thank You", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='')}
    <div style="padding-top:22px">
      <div class="vb-badge-ok vb-green"><i class="fa-solid fa-check"></i></div>
      <h1>Your checklist is <span class="vb-hl">on its way!</span></h1>
      <p class="vb-lead">Keep an eye on your inbox &mdash; it should land in the next few minutes.</p>
    </div>
  </div>
  <div class="vb-wrap vb-narrow" style="padding-top:36px">
    <div class="vb-card">
      <h2 style="margin-bottom:16px;font-size:26px">We get it. You're busy.</h2>
      <p style="margin-bottom:16px">You're showing homes, answering texts at 9pm, and juggling
      closings. Updating your bios, fixing your Google profile, and getting your brand consistent?
      That always slides to the bottom of the to-do list.</p>
      <p style="margin-bottom:16px"><em>Most agents download this checklist, scan it, and realize
      they have work to do &mdash; but no idea when they'll get to it. That's where VBox AI comes in.
      We take the whole thing off your plate, build it correctly the first time, and hand you
      finished files ready to paste.</em></p>
      <p><strong style="color:#fff">VBox AI</strong> is a done-for-you brand and profile service
      built just for real estate agents &mdash; verified, Fair Housing compliant, and written in
      your voice.</p>
      <div class="vb-center vb-mt">
        <!-- Link this button to your Sales Page (page3) -->
        <a href="#" class="vb-btn-primary">See How VBox AI Works&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 3 : SALES ----------------
pages["page3-sales.html"] = snippet("Page 3 - Sales Page (Brand Foundation Package)", f"""
<!-- HERO -->
<div class="vb-section vb-hero" style="min-height:auto;padding-top:48px;padding-bottom:70px">
  <div class="vb-glow-orb vb-orb-a"></div><div class="vb-glow-orb vb-orb-b"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='<a href="#vb-pricing" class="vb-small" style="color:var(--hl2)">Get Started &rarr;</a>')}
    <div style="padding-top:34px">
      <div class="vb-eyebrow"><i class="fa-solid fa-star"></i>&nbsp; The Brand Foundation Package</div>
      <h1>Your brand, <span class="vb-hl">done for you.</span></h1>
      <p class="vb-lead">Bios, profiles, brand voice, and visibility &mdash; researched, written,
      and verified for you. One less thing on your plate.</p>
      <div class="vb-mt"><a href="#vb-pricing" class="vb-btn-primary">Get the Brand Foundation Package&nbsp; <i class="fa-solid fa-arrow-right"></i></a></div>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- PROBLEM -->
<div class="vb-section">
  <div class="vb-wrap">
    <div class="vb-sec-head"><h2>You know you need this.<br><span class="vb-hl">You just don't have time for it.</span></h2></div>
    <div class="vb-grid vb-g3">
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-house"></i></div><h3>Your Zillow bio is from 2019</h3><p style="margin-top:8px">Outdated stats, old designations, and a bio that doesn't sound like you anymore.</p></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-arrows-left-right"></i></div><h3>Every profile says something different</h3><p style="margin-top:8px">LinkedIn, Realtor.com, Instagram &mdash; inconsistent info makes clients (and AI search) hesitate.</p></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-location-crosshairs"></i></div><h3>Google Business? Neglected.</h3><p style="margin-top:8px">It's where local buyers find you first, and it's been on your list for months.</p></div>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- HOW IT WORKS -->
<div class="vb-section">
  <div class="vb-wrap">
    <div class="vb-sec-head"><h2>One package. Everything set up.<br><span class="vb-hl">Nothing left to figure out.</span></h2></div>
    <div class="vb-grid vb-g3">
      <div class="vb-card"><div class="vb-step-num">STEP 01</div><h3>Complete Intake</h3><p style="margin-top:8px">Answer a simple form about you, your market, and your goals &mdash; at your own pace.</p></div>
      <div class="vb-card"><div class="vb-step-num">STEP 02</div><h3>We Build It</h3><p style="margin-top:8px">We verify your info, write every piece, and check it all for accuracy and compliance.</p></div>
      <div class="vb-card"><div class="vb-step-num">STEP 03</div><h3>Copy. Paste. Done.</h3><p style="margin-top:8px">You get finished files plus a checklist that walks you through every platform.</p></div>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- WHAT'S INCLUDED -->
<div class="vb-section">
  <div class="vb-wrap">
    <div class="vb-sec-head"><div class="vb-eyebrow">What's Included</div><h2>Everything your brand needs, <span class="vb-hl">in one place.</span></h2></div>
    <div class="vb-card">
      <div class="vb-grid vb-g2" style="gap:0 40px">
        <ul class="vb-check">
          <li><i class="fa-solid fa-check"></i>Verified Professional Profile</li>
          <li><i class="fa-solid fa-check"></i>Master Bio</li>
          <li><i class="fa-solid fa-check"></i>5 Platform Bios &mdash; Zillow, Realtor.com, LinkedIn, Google, Instagram</li>
          <li><i class="fa-solid fa-check"></i>Email Signature</li>
          <li><i class="fa-solid fa-check"></i>Elevator Pitch</li>
          <li><i class="fa-solid fa-check"></i>Brand Foundation Guide</li>
        </ul>
        <ul class="vb-check">
          <li><i class="fa-solid fa-check"></i>Brand Story &amp; Voice</li>
          <li><i class="fa-solid fa-check"></i>Visual Direction</li>
          <li><i class="fa-solid fa-check"></i>Content Pillars</li>
          <li><i class="fa-solid fa-check"></i>Local Visibility Audit</li>
          <li><i class="fa-solid fa-check"></i>Implementation Checklist</li>
        </ul>
      </div>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- TRUST -->
<div class="vb-section">
  <div class="vb-wrap">
    <div class="vb-grid vb-g3">
      <div class="vb-card vb-center"><div class="vb-icon" style="margin:0 auto 14px"><i class="fa-solid fa-scale-balanced"></i></div><h3>Fair Housing Compliant</h3><p class="vb-small" style="margin-top:6px">Every word reviewed against Fair Housing guidelines.</p></div>
      <div class="vb-card vb-center"><div class="vb-icon" style="margin:0 auto 14px"><i class="fa-solid fa-circle-check"></i></div><h3>AI-Verified Accuracy</h3><p class="vb-small" style="margin-top:6px">A dedicated verification step catches errors before you see them.</p></div>
      <div class="vb-card vb-center"><div class="vb-icon" style="margin:0 auto 14px"><i class="fa-solid fa-shield-halved"></i></div><h3>Built on Real Info</h3><p class="vb-small" style="margin-top:6px">Nothing invented. Only your real credentials and experience.</p></div>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- PRICING -->
<div class="vb-section" id="vb-pricing" style="position:relative;overflow:hidden">
  <div class="vb-glow-orb vb-orb-a" style="top:-140px"></div>
  <div class="vb-wrap vb-center">
    <h2>Brand Foundation <span class="vb-hl">Package</span></h2>
    <div class="vb-card" style="max-width:520px;margin:28px auto 0">
      <!-- ===== INSERT SYSTEME.IO ORDER FORM HERE ===== -->
      <div class="vb-placeholder">Your price / payment plan goes here<span class="vb-price">$___</span></div>
      <!-- ===== END order form ===== -->
      <a href="#" class="vb-btn-primary vb-btn-block" style="margin-top:22px">Get Started&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
    </div>
  </div>
</div>
<hr class="vb-hr">

<!-- FAQ -->
<div class="vb-section">
  <div class="vb-wrap vb-narrow">
    <div class="vb-sec-head"><h2>Questions? <span class="vb-hl">Answered.</span></h2></div>
    <details class="vb-faq"><summary>How long does it take?</summary><p>Once your intake form is complete, your files are delivered within [X business days]. The intake itself takes about 15&ndash;20 minutes.</p></details>
    <details class="vb-faq"><summary>Do I need tech skills?</summary><p>None. You'll get finished text and a step-by-step checklist. If you can copy and paste, you're set.</p></details>
    <details class="vb-faq"><summary>Is it compliant?</summary><p>Yes. Everything is reviewed against Fair Housing guidelines and checked for accurate licensing and brokerage disclosures.</p></details>
    <details class="vb-faq"><summary>What happens after I pay?</summary><p>You'll get a confirmation email with your intake form link. Complete it, and we take it from there.</p></details>
    <details class="vb-faq"><summary>What if my info changes?</summary><p>Your Master Bio and Brand Guide make updates simple. Just reach out at hello@vbox-ai.com and we'll help you refresh.</p></details>
  </div>
</div>
<hr class="vb-hr">

<!-- CLOSING CTA -->
<div class="vb-section" style="position:relative;overflow:hidden">
  <div class="vb-glow-orb vb-orb-a" style="top:-100px"></div>
  <div class="vb-wrap vb-center">
    <h2>Ready to check this <span class="vb-hl">off your list?</span></h2>
    <p class="vb-lead">Hand it over. We'll take it from here.</p>
    <div class="vb-mt"><a href="#vb-pricing" class="vb-btn-primary">Get the Brand Foundation Package&nbsp; <i class="fa-solid fa-arrow-right"></i></a></div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 4 : UPSELL 1 ----------------
pages["page4-upsell1.html"] = snippet("Page 4 - Upsell 1 (Marketing Suite)", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='<div class="vb-small">Step 2 of 3 &middot; Customize your order</div>')}
    <div style="padding-top:26px">
      <div class="vb-confirm-bar"><i class="fa-solid fa-circle-check"></i> Your Brand Foundation is confirmed!</div>
      <p class="vb-lead" style="margin-top:0">Now that your brand identity is set &mdash; here's how to put it to work.</p>
      <h1 style="margin-top:18px">Add the Marketing Suite &mdash; and <span class="vb-hl">show up professionally from day one.</span></h1>
    </div>
  </div>
  <div class="vb-wrap" style="padding-top:36px">
    <div class="vb-grid vb-g2">
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-table-columns"></i></div><h3>Listing Presentation</h3><p style="margin-top:6px">A polished, on-brand deck to win the listing appointment.</p></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-house-chimney-window"></i></div><h3>Open House Kit</h3><p style="margin-top:6px">Sign-in sheets, flyers, and follow-up copy, ready to print.</p></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-shapes"></i></div><h3>Social Media Asset Pack</h3><p style="margin-top:6px">Branded templates and captions for just listed, sold, and more.</p></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-envelope"></i></div><h3>Email Templates</h3><p style="margin-top:6px">Nurture, check-in, and past-client emails written in your voice.</p></div>
    </div>
    <div class="vb-callout vb-mt"><strong style="color:#fff"><i class="fa-solid fa-bolt"></i> Why now?</strong> <em>Everything is built to match your brand &mdash; this is the fastest way to get client-ready materials.</em></div>
    <div class="vb-card vb-center" style="max-width:520px;margin:34px auto 0">
      <!-- ===== INSERT SYSTEME.IO ONE-CLICK UPSELL / ORDER FORM HERE ===== -->
      <div class="vb-placeholder">Marketing Suite price goes here<span class="vb-price">$___</span></div>
      <!-- ===== END order form ===== -->
      <a href="#" class="vb-btn-primary vb-btn-block" style="margin-top:22px">Yes &mdash; Add the Marketing Suite&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
      <!-- Link to page5 Downsell -->
      <a href="#" class="vb-link-ghost">No thanks, I'll come back to this later</a>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 5 : DOWNSELL ----------------
pages["page5-downsell.html"] = snippet("Page 5 - Downsell (Social Media Asset Pack)", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center" style="max-width:620px">
    {NAV.format(right='')}
    <div style="padding-top:22px">
      <div class="vb-eyebrow">Totally understand</div>
      <h1>Just the essentials &mdash; <span class="vb-hl">at a smaller investment.</span></h1>
      <p class="vb-lead">Not ready for the full suite? Start with the piece most agents use every single week.</p>
      <div class="vb-card" style="margin-top:32px;text-align:left">
        <h3>Social Media Asset Pack</h3>
        <ul class="vb-check" style="margin-top:10px">
          <li><i class="fa-solid fa-check"></i>Branded post templates for just listed, under contract, and sold</li>
          <li><i class="fa-solid fa-check"></i>Ready-to-use captions written in your brand voice</li>
          <li><i class="fa-solid fa-check"></i>Profile and highlight graphics that match your visual direction</li>
        </ul>
        <!-- ===== INSERT SYSTEME.IO DOWNSELL ORDER FORM HERE ===== -->
        <div class="vb-placeholder" style="margin-top:18px">Downsell price goes here<span class="vb-price" style="font-size:30px">$___</span></div>
        <!-- ===== END order form ===== -->
        <a href="#" class="vb-btn-primary vb-btn-block" style="margin-top:22px">Yes, I'll grab just this&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
        <!-- Link to page6 Upsell 2 -->
        <div class="vb-center"><a href="#" class="vb-link-ghost">No thanks, continue to my order &rarr;</a></div>
      </div>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 6 : UPSELL 2 ----------------
pages["page6-upsell2.html"] = snippet("Page 6 - Upsell 2 (Website Building)", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='<div class="vb-small">Step 3 of 3 &middot; Last step</div>')}
    <div style="padding-top:26px">
      <div class="vb-eyebrow">One more thing &mdash; your brand deserves a home.</div>
      <h1>Add a professional website &mdash; <span class="vb-hl">built around everything we just created.</span></h1>
    </div>
  </div>
  <div class="vb-wrap" style="padding-top:30px">
    <div class="vb-callout"><strong style="color:#fff"><i class="fa-solid fa-bolt"></i> Why it's easy now:</strong> <em>Your bios, brand story, and visual direction are already done &mdash; your website practically builds itself from here.</em></div>
    <div class="vb-grid vb-g3 vb-mt">
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-house"></i></div><h3>Homepage</h3></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-user"></i></div><h3>About Page</h3></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-arrows-left-right"></i></div><h3>Buyer &amp; Seller Pages</h3></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-location-crosshairs"></i></div><h3>Local SEO Foundation</h3></div>
      <div class="vb-card"><div class="vb-icon"><i class="fa-solid fa-scale-balanced"></i></div><h3>Compliance Disclosures</h3></div>
      <div class="vb-card" style="border-style:dashed"><div class="vb-icon"><i class="fa-solid fa-star"></i></div><h3>Matches your brand guide</h3></div>
    </div>
    <div class="vb-card vb-center" style="max-width:520px;margin:34px auto 0">
      <!-- ===== INSERT SYSTEME.IO ONE-CLICK UPSELL / ORDER FORM HERE ===== -->
      <div class="vb-placeholder">Website Building price goes here<span class="vb-price">$___</span></div>
      <!-- ===== END order form ===== -->
      <a href="#" class="vb-btn-primary vb-btn-block" style="margin-top:22px">Yes &mdash; Build My Website&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
      <!-- Link to page7 Welcome -->
      <a href="#" class="vb-link-ghost">No thanks, take me to my welcome page</a>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 7 : WELCOME ----------------
pages["page7-welcome.html"] = snippet("Page 7 - Welcome / Onboarding", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='')}
    <div style="padding-top:22px">
      <div class="vb-badge-ok"><i class="fa-solid fa-check"></i></div>
      <h1>Welcome to VBox AI.<br><span class="vb-hl">You just made a great call.</span> &#127881;</h1>
      <p class="vb-lead">Your brand is officially off your plate. Here's exactly what happens next.</p>
    </div>
  </div>
  <div class="vb-wrap vb-narrow" style="padding-top:34px">
    <div class="vb-card">
      <h3 style="margin-bottom:24px">What happens next</h3>
      <div class="vb-timeline">
        <div class="vb-tl-item"><div class="vb-tl-num">1</div><div><h3>Check your email</h3><p style="margin-top:4px">Your confirmation and intake form link are waiting for you.</p></div></div>
        <div class="vb-tl-item"><div class="vb-tl-num">2</div><div><h3>Complete the intake form</h3><p style="margin-top:4px">About 15&ndash;20 minutes, at your own pace. Save and come back anytime.</p></div></div>
        <div class="vb-tl-item"><div class="vb-tl-num">3</div><div><h3>VBox AI gets to work</h3><p style="margin-top:4px">Your files are delivered within [X business days].</p></div></div>
        <div class="vb-tl-item"><div class="vb-tl-num">4</div><div><h3>Review, approve, and paste</h3><p style="margin-top:4px">Your checklist walks you through every platform, step by step.</p></div></div>
      </div>
    </div>
    <div class="vb-center vb-mt">
      <!-- Link to your intake form -->
      <a href="#" class="vb-btn-primary">Start Your Intake Form&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
      <p class="vb-small" style="margin-top:20px">Questions? Email us at <a href="mailto:hello@vbox-ai.com">hello@vbox-ai.com</a></p>
      <p style="margin-top:24px;color:var(--hl2)"><em>We're excited to build something great for your business.</em></p>
    </div>
  </div>
</div>
{FOOT}""")

# ---------------- PAGE 8 : OPT-IN THANK YOU ----------------
pages["page8-optin-thankyou.html"] = snippet("Page 8 - Lead Magnet Delivery (Opt-in Thank You)", f"""
<div class="vb-section">
  <div class="vb-glow-orb vb-orb-a"></div>
  <div class="vb-wrap vb-center">
    {NAV.format(right='')}
    <div style="padding-top:22px">
      <div class="vb-badge-ok vb-green"><i class="fa-solid fa-check"></i></div>
      <h1>You're in! <span class="vb-hl">Check your inbox.</span></h1>
      <p class="vb-lead">Your checklist is on the way. (Can't find it? Peek in your promotions or spam folder.)</p>
    </div>
  </div>
  <div class="vb-wrap vb-narrow" style="padding-top:34px">
    <div class="vb-card">
      <h3>What's inside your checklist</h3>
      <ul class="vb-check" style="margin-top:10px">
        <li><i class="fa-solid fa-check"></i>The profile audit every agent should run across Zillow, Realtor.com, Google &amp; LinkedIn</li>
        <li><i class="fa-solid fa-check"></i>The consistency checks that help clients (and AI search) trust you</li>
        <li><i class="fa-solid fa-check"></i>The compliance must-haves your bios and profiles should never skip</li>
      </ul>
    </div>
    <div class="vb-center vb-mt">
      <p style="color:#fff;font-size:18px;margin-bottom:18px">While you wait &mdash; here's what agents do after they see the results.</p>
      <!-- Link to page2 Bridge or page3 Sales -->
      <a href="#" class="vb-btn-primary">See What's Next&nbsp; <i class="fa-solid fa-arrow-right"></i></a>
    </div>
  </div>
</div>
{FOOT}""")

for fname, content in pages.items():
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(content)
    print("wrote", fname, len(content), "bytes")

print("done")
