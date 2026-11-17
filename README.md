# CLEARPATH — website

Single-page website for CLEARPATH, construction cost control in Los Cabos.
English. Static site, no build step, no framework, no trackers.

**Live site:** https://aom-privacy.github.io/clearpath/
(Planned custom domain: clearpath.mx)

## Files

- `index.html` — the whole page. Images and the hero video are inlined as
  data URIs (see note below), so the page works with just this file plus
  `styles.css`.
- `styles.css` — the built stylesheet (generated from `styles.template.css`
  by `build.py`, with the background photos inlined).
- `index.template.html`, `styles.template.css`, `build.py` — sources. Rebuild with
  `python3 build.py` after editing the template or stylesheet.
- `assets/` — original asset files (logo, photos, chart, hero video), kept
  in the local workspace copy for reference and for future replacement.
  They are not pushed to the repo (binary files cannot be pushed through
  the GitHub connector used here).

## Content

- Hero: AI-generated placeholder video (aerial over Los Cabos villas at
  golden hour) with a real site photo as poster. Replace with real footage
  when available: put the new file in `assets/`, rebuild, or upload it to
  the repo and point the `<video>` `src` at it.
- Services: the 11 scopes from the CLEARPATH proposal, grouped in three
  blocks, plus the four weekly report formats and what the client provides.
- Pricing: $2,500 USD + IVA / month, flat monthly fee, 3-month minimum.
- Contact: WhatsApp +52 228 133 6525, c.aguirreriano@gmail.com.

## Note on inlined assets

The GitHub connector used to publish this site can only push UTF-8 text
files, not binary files. That is why the logo, photos, chart and video are
embedded in the HTML/CSS as base64 data URIs instead of living in an
`assets/` folder on the repo. The originals are kept in `assets/` in the
local workspace copy.
If binary upload becomes possible, the data URIs can be swapped for plain
`assets/...` paths.

## GitHub Pages

Deploy from the `main` branch, root folder:
repository Settings → Pages → Build and deployment → Deploy from a branch →
`main` / `/ (root)`. The site then serves at
https://aom-privacy.github.io/clearpath/
