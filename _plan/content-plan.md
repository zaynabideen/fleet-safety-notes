# Fleet Safety Notes: content plan and run log

This folder is not published (GitHub Pages ignores folders that start with `_`).

## Site rules (never break these)
- Brand-only site. No personal names, biographies, employers, education or personal experience anywhere. Byline is always "By the Fleet Safety Notes editorial team".
- Global English audience (US, UK, Canada, Australia, EU). When rules differ by country, say so and link the official regulator page for each.
- Accuracy first: research every factual claim on the web, link primary sources in a "Sources" section at the end of each article. No invented statistics, quotes, testimonials, prices or experiences.
- Original, genuinely useful content written for readers, not for search engines. Each article ~1,200–1,800 words, with a table, checklist or worked example where useful. Max 2 new evergreen articles + 1 weekly roundup per week (avoid "scaled content").
- No affiliate links or ads code until the owner sets those up.

## How to add a page
1. Write the page body to `_build/src/<slug>.html`, copying the structure of `_build/src/what-is-fleet-telematics.html` (header band, meta line, toc, prose, Sources).
2. Add it to `PAGES` in `_build/build.py`, and add a card to `_build/src/index.html` (newest first in the Guides grid).
3. From the repo root run `python3 _build/build.py _build/src .` to rebuild all pages, sitemap.xml and robots.txt.
4. Mark the topic done below and add a line to the run log.

## Topic backlog (pick the first unchecked item in priority order)
### Telematics & tracking
- [x] What is fleet telematics? A beginner's guide
- [x] GPS fleet tracking: costs, contracts and hidden fees explained
- [x] OBD-II plug-in vs hard-wired trackers: which is right for you?
- [ ] Electronic logging devices (ELDs) explained for small US carriers
- [ ] Tachographs explained for UK and EU operators
### Dash cams & video
- [x] How to choose a dash cam for a small fleet
- [ ] Forward-facing vs dual-facing dash cams: privacy, cost and benefits
- [ ] How to use dash cam footage in an insurance claim
- [ ] Dash cam installation checklist for vans and trucks
- [ ] AI dash cam alerts explained: what they detect and how accurate they are
### Driver safety
- [x] Driver risk scores explained
- [ ] How to run a driver coaching programme that drivers accept
- [ ] Driver fatigue: warning signs, rules and prevention for fleets
- [ ] Distracted driving and phone use: policies that work
- [ ] Writing a fleet driver safety policy (with free template)
- [ ] Reducing reversing and low-speed collisions in delivery fleets
### Fuel & costs
- [x] Fleet fuel cost calculator (tool)
- [ ] 10 proven ways to cut fleet fuel costs
- [ ] Idling: what it really costs and how to reduce it
- [ ] Total cost of ownership for fleet vehicles explained
- [ ] Tool: cost-per-mile / cost-per-km calculator
- [ ] Fuel cards: how they work and what to look for
### Fleet management & EVs
- [ ] Preventive maintenance schedules for small fleets
- [ ] Tool: vehicle maintenance interval planner
- [ ] Switching a small fleet to electric vans: a practical checklist
- [ ] Fleet vehicle inspection (walkaround) checklist
- [ ] How to choose fleet management software

## Weekly roundup
- Every Monday: "Fleet Weekly Roundup – <date>": 4–6 genuinely notable items from the past week (regulation changes, recalls, safety research, technology launches) across US/UK/EU/AU, each summarised in our own words with a link to the original source. Never copy text. Slug: `fleet-weekly-roundup-YYYY-MM-DD.html`. Add a "Roundups" card only once there are 2+ roundups.

## Run log
- 2026-11-24: Site made brand-only and global. Added telematics guide, editorial standards page, global fuel calculator.
- 2026-11-25: gps-fleet-tracking-costs.html, GPS fleet tracking costs: contracts and hidden fees explained (logged retrospectively).
- 2026-11-27: obd-vs-hardwired-trackers.html, OBD-II plug-in vs hard-wired trackers: which is right for your fleet?
