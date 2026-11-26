#!/usr/bin/env python3
"""Build index.html (English) and es/index.html (Spanish) from the templates,
inlining assets as data URIs.

Why data URIs: the GitHub connector available to this workspace can only push
UTF-8 text files, not binary files. Inlining the logo, photos, chart and hero
video keeps the site fully self-contained in text files (index.html +
es/index.html + styles.css) so it works on GitHub Pages exactly as built.

To replace an asset with a real file later (e.g. the hero video with real
footage): upload the file to assets/ in the repo and replace the matching
data URI in index.html / es/index.html / styles.css with the relative path
(assets/...).
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def data_uri(path: pathlib.Path, mime: str) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def build_page(template: pathlib.Path, output: pathlib.Path, chart: pathlib.Path) -> None:
    subs = {
        "__LOGO_B64__": data_uri(ASSETS / "logo.png", "image/png"),
        "__FAVICON_B64__": data_uri(ASSETS / "favicon.ico", "image/x-icon"),
        "__VIDEO_B64__": data_uri(ASSETS / "hero-video.mp4", "video/mp4"),
        "__COAST_B64__": data_uri(ASSETS / "photo-coast.jpg", "image/jpeg"),
        "__SITE_B64__": data_uri(ASSETS / "photo-site.jpg", "image/jpeg"),
        "__HILLS_B64__": data_uri(ASSETS / "photo-hills.jpg", "image/jpeg"),
        "__CHART_B64__": data_uri(chart, "image/png"),
        "__LOGO_HEADER_B64__": data_uri(ASSETS / "logo-header.png", "image/png"),
        "__CAROUSEL_1_B64__": data_uri(ASSETS / "carousel-1.png", "image/png"),
        "__CAROUSEL_2_B64__": data_uri(ASSETS / "carousel-2.png", "image/png"),
        "__CAROUSEL_3_B64__": data_uri(ASSETS / "carousel-3.png", "image/png"),
        "__CAROUSEL_4_B64__": data_uri(ASSETS / "carousel-4.png", "image/png"),
        "__CAROUSEL_5_B64__": data_uri(ASSETS / "carousel-5.png", "image/png"),
        "__CAROUSEL_6_B64__": data_uri(ASSETS / "carousel-6.png", "image/png"),
        "__CAROUSEL_7_B64__": data_uri(ASSETS / "carousel-7.png", "image/png"),
        "__ABOUT_CARLOS_B64__": data_uri(ASSETS / "about-carlos.jpg", "image/jpeg"),
    }
    html = template.read_text(encoding="utf-8")
    for key, val in subs.items():
        html = html.replace(key, val)
    for key in subs:
        assert key not in html, f"placeholder left: {key}"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"{output.relative_to(ROOT)}: {output.stat().st_size / 1e6:.2f} MB")


def main() -> None:
    # The CSS uses the hills/coast images too (closing background, reduced-motion
    # fallback), so apply the shared substitutions to it as well.
    shared = {
        "__LOGO_B64__": data_uri(ASSETS / "logo.png", "image/png"),
        "__FAVICON_B64__": data_uri(ASSETS / "favicon.ico", "image/x-icon"),
        "__VIDEO_B64__": data_uri(ASSETS / "hero-video.mp4", "video/mp4"),
        "__COAST_B64__": data_uri(ASSETS / "photo-coast.jpg", "image/jpeg"),
        "__SITE_B64__": data_uri(ASSETS / "photo-site.jpg", "image/jpeg"),
        "__HILLS_B64__": data_uri(ASSETS / "photo-hills.jpg", "image/jpeg"),
        "__LOGO_HEADER_B64__": data_uri(ASSETS / "logo-header.png", "image/png"),
    }
    css = (ROOT / "styles.template.css").read_text(encoding="utf-8")
    for key, val in shared.items():
        css = css.replace(key, val)
    for key in list(shared) + ["__CHART_B64__"]:
        assert key not in css, f"placeholder left in styles.css: {key}"
    (ROOT / "styles.css").write_text(css, encoding="utf-8")
    print(f"styles.css: {(ROOT / 'styles.css').stat().st_size / 1e3:.1f} KB")
    build_page(ROOT / "index.template.html", ROOT / "index.html", ASSETS / "chart.png")
    build_page(ROOT / "index.template.es.html", ROOT / "es" / "index.html", ASSETS / "chart-es.png")
    build_page(ROOT / "software.template.html", ROOT / "software" / "index.html", ASSETS / "chart.png")
    build_page(ROOT / "software.template.es.html", ROOT / "es" / "software" / "index.html", ASSETS / "chart-es.png")


if __name__ == "__main__":
    main()
