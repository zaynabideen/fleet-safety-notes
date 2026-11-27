"""Assemble the static site: shared header/footer + page bodies -> ../site/*.html"""
import pathlib, sys

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
SITE = "Fleet Safety Notes"
DOMAIN = "https://fleetsafetynotes.co.uk"

# file, title, description, nav key
PAGES = [
    ("index.html", "Fleet Safety Notes: practical guides on fleet safety, dash cams and telematics",
     "Plain-English guides and free tools on fleet safety, dash cams, telematics, driver risk scores and fuel costs.", "home"),
    ("dash-cam-guide.html", "How to choose a dash cam for a small fleet",
     "A buyer's checklist for fleet dash cams: camera types, AI alerts, connectivity, installation rules, data protection and total cost.", "guides"),
    ("driver-risk-scores.html", "Driver risk scores explained: how fleet safety scoring works",
     "How fleet driver risk scores are calculated, why events are normalised per 1,000 miles, and how to use scores fairly.", "guides"),
    ("what-is-fleet-telematics.html", "What is fleet telematics? A beginner's guide for small fleets",
     "How fleet telematics works, what it tracks, the main device types, benefits, compliance, driver privacy and how to choose a system.", "guides"),
    ("gps-fleet-tracking-costs.html", "GPS fleet tracking costs: contracts and hidden fees explained",
     "What GPS fleet tracking really costs: hardware, installation, subscriptions, contract terms, hidden fees, network switch-offs, and a worksheet to compare quotes.", "guides"),
    ("obd-vs-hardwired-trackers.html", "OBD-II plug-in vs hard-wired trackers: which is right for your fleet?",
     "Plug-in OBD trackers vs hard-wired units compared: installation, tamper resistance, theft recovery, vehicle data, security, trucks and ELDs, with a decision checklist.", "guides"),
    ("fuel-cost-calculator.html", "Fleet fuel cost calculator (miles or km, mpg or L/100km, any currency)",
     "Work out weekly, monthly and yearly fuel cost for your fleet, and what a small mpg improvement would save.", "tools"),
    ("about.html", "About Fleet Safety Notes", "Our mission, what we cover and how Fleet Safety Notes stays independent.", "about"),
    ("editorial-standards.html", "Editorial standards", "How Fleet Safety Notes researches, reviews, corrects and funds its content.", "about"),
    ("contact.html", "Contact Fleet Safety Notes", "How to get in touch with Fleet Safety Notes.", "contact"),
    ("privacy.html", "Privacy policy and disclaimer", "How Fleet Safety Notes uses cookies, advertising and your data.", "privacy"),
]

NAV = [("index.html", "Home", "home"), ("index.html#guides", "Guides", "guides"),
       ("fuel-cost-calculator.html", "Tools", "tools"), ("about.html", "About", "about"),
       ("contact.html", "Contact", "contact")]

LOGO = ('<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true">'
        '<rect x="1" y="1" width="28" height="28" rx="6" fill="none" stroke="#fff" stroke-width="2.5"/>'
        '<path d="M15 6 L23 22 H7 Z" fill="#fff"/><rect x="14" y="12" width="2" height="5" fill="#1d4f91"/>'
        '<rect x="14" y="18.5" width="2" height="2" fill="#1d4f91"/></svg>')

def page(fname, title, desc, key, body):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == key else ""}>{t}</a>' for h, t, k in NAV)
    canon = DOMAIN + "/" + ("" if fname == "index.html" else fname)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Overpass:wght@700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<!-- AdSense: paste your AdSense <script> tag here after you sign up (see README) -->
</head>
<body>
<header class="top"><div class="wrap">
<a class="logo" href="index.html">{LOGO}<span>{SITE}</span></a>
<nav aria-label="Main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<span>&copy; 2026 {SITE}. Independent guides for fleet operators.</span>
<nav aria-label="Footer"><a href="about.html">About</a><a href="contact.html">Contact</a><a href="editorial-standards.html">Editorial standards</a><a href="privacy.html">Privacy policy</a><a href="privacy.html#disclaimer">Disclaimer</a></nav>
</div></footer>
</body>
</html>
"""

OUT.mkdir(parents=True, exist_ok=True)
for fname, title, desc, key in PAGES:
    body = (SRC / fname).read_text(encoding="utf-8")
    (OUT / fname).write_text(page(fname, title, desc, key, body), encoding="utf-8")

urls = "".join(f"<url><loc>{DOMAIN}/{'' if f == 'index.html' else f}</loc></url>" for f, *_ in PAGES)
(OUT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("built", len(PAGES), "pages")
