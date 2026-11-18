#!/usr/bin/env python3
"""Build index.html from index.template.html by inlining assets as data URIs.

Why data URIs: the GitHub connector available to this workspace can only push
UTF-8 text files, not binary files. Inlining the logo, photos, chart and hero
video keeps the site fully self-contained in two text files (index.html +
styles.css) so it works on GitHub Pages exactly as built.

To replace an asset with a real file later (e.g. the hero video with real
footage): upload the file to assets/ in the repo and replace the matching
data URI in index.html / styles.css with the relative path (assets/...).
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def data_uri(path: pathlib.Path, mime: str) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def main() -> None:
    subs = {
        "__LOGO_B64__": data_uri(ASSETS / "logo.png", "image/png"),
        "__FAVICON_B64__": data_uri(ASSETS / "favicon.ico", "image/x-icon"),
        "__VIDEO_B64__": data_uri(ASSETS / "hero-video.mp4", "video/mp4"),
        "__COAST_B64__": data_uri(ASSETS / "photo-coast.jpg", "image/jpeg"),
        "__SITE_B64__": data_uri(ASSETS / "photo-site.jpg", "image/jpeg"),
        "__HILLS_B64__": data_uri(ASSETS / "photo-hills.jpg", "image/jpeg"),
        "__CHART_B64__": data_uri(ASSETS / "chart.png", "image/png"),
        "__LOGO_HEADER_B64__": data_uri(ASSETS / "logo-header.png", "image/png"),
    }
    html = (ROOT / "index.template.html").read_text(encoding="utf-8")
    css = (ROOT / "styles.template.css").read_text(encoding="utf-8")
    for key, val in subs.items():
        html = html.replace(key, val)
        css = css.replace(key, val)
    for key in subs:
        assert key not in html and key not in css, f"placeholder left: {key}"
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    (ROOT / "styles.css").write_text(css, encoding="utf-8")
    print(f"index.html: {(ROOT / 'index.html').stat().st_size / 1e6:.2f} MB")
    print(f"styles.css: {(ROOT / 'styles.css').stat().st_size / 1e3:.1f} KB")


if __name__ == "__main__":
    main()
