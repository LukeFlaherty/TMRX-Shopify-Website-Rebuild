from __future__ import annotations

import json
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUTPUT = ROOT / "generated-pdp-images"
W = H = 1200

NAVY = (17, 48, 63)
BLUE = (34, 128, 174)
GREEN = (61, 111, 95)
INK = (24, 31, 35)
MUTED = (84, 93, 98)
BG = (246, 248, 249)
WHITE = (255, 255, 255)
LINE = (215, 224, 228)
RED = (165, 38, 38)

FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"


PRODUCTS = [
    {
        "handle": "mito-revive",
        "title": "MITO-REVIVE",
        "format": "Capsules",
        "benefit": "Supports cellular energy and mitochondrial renewal.",
        "audience": "For adults focused on energy, stamina, and healthy aging.",
        "expect": ["Steady daily routine", "Cellular energy support", "Long-term vitality support"],
        "use": ["Take as directed", "Pair with meals", "Use consistently", "Review label guidance"],
        "checks": ["Doctor recommended", "Targeted mitochondrial support", "Clean daily formula"],
        "avoid": ["Generic energy blends", "Unclear ingredient purpose", "Overstimulating routines"],
    },
    {
        "handle": "creatine-hcl",
        "title": "Creatine HCL",
        "format": "Powder",
        "benefit": "Supports strength, power output, and training performance.",
        "audience": "For active adults who want efficient creatine support.",
        "expect": ["Training support", "Strength routine support", "Daily performance habit"],
        "use": ["Mix with water", "Take daily", "No loading needed", "Follow serving size"],
        "checks": ["Doctor recommended", "Creatine HCL format", "No unnecessary fillers"],
        "avoid": ["Overcomplicated stacks", "Guesswork dosing", "Artificial clutter"],
    },
    {
        "handle": "secretropin",
        "title": "SECRETROPIN",
        "format": "Spray",
        "benefit": "Supports a consistent vitality and wellness routine.",
        "audience": "For adults looking for easy daily support.",
        "expect": ["Simple daily use", "Routine-friendly support", "Long-term wellness habit"],
        "use": ["Use as directed", "Keep routine steady", "Store as labeled", "Ask your clinician"],
        "checks": ["Doctor recommended", "Convenient spray format", "Purposeful daily support"],
        "avoid": ["Inconsistent use", "One-size-fits-all claims", "Unclear routines"],
    },
    {
        "handle": "bone-broth-protein",
        "title": "BONE BROTH PROTEIN",
        "format": "Powder",
        "benefit": "Supports daily protein intake with a clean, simple formula.",
        "audience": "For wellness-focused adults prioritizing protein and recovery.",
        "expect": ["Protein routine support", "Recovery nutrition", "Daily consistency"],
        "use": ["Mix into liquid", "Shake until smooth", "Use daily as needed", "Follow label serving"],
        "checks": ["Doctor recommended", "Protein-forward nutrition", "Clean ingredient mindset"],
        "avoid": ["Sugary protein habits", "Unnecessary additives", "Low-protein routines"],
    },
    {
        "handle": "myos-md-vanilla",
        "title": "Myos MD Vanilla",
        "format": "Powder",
        "benefit": "Supports muscle health as part of a protein-rich routine.",
        "audience": "For adults focused on strength, mobility, and healthy aging.",
        "expect": ["Daily protein habit", "Muscle health support", "Strength routine support"],
        "use": ["Blend or shake", "Take consistently", "Pair with training", "Follow label guidance"],
        "checks": ["Doctor recommended", "Muscle-focused nutrition", "Vanilla daily-use format"],
        "avoid": ["Skipping protein", "Inconsistent routines", "Unclear ingredient purpose"],
    },
    {
        "handle": "methylation-support",
        "title": "METHYLATION SUPPORT",
        "format": "Capsules",
        "benefit": "Supports methylation pathways and daily wellness foundations.",
        "audience": "For adults looking for targeted foundational support.",
        "expect": ["Foundational support", "Daily pathway support", "Long-term wellness routine"],
        "use": ["Take as directed", "Use consistently", "Pair with meals", "Ask your clinician"],
        "checks": ["Doctor recommended", "Targeted methylation support", "Purposeful nutrient stack"],
        "avoid": ["Random wellness blends", "Unclear dosing", "Low-quality forms"],
    },
    {
        "handle": "n1o1-nitric-oxide-lozenges",
        "title": "N1O1 Nitric Oxide Lozenges",
        "format": "Lozenges",
        "benefit": "Supports nitric oxide availability and circulation-focused routines.",
        "audience": "For performance and wellness-minded adults.",
        "expect": ["Routine circulation support", "Performance habit support", "Daily wellness support"],
        "use": ["Use as directed", "Let dissolve", "Stay consistent", "Follow label timing"],
        "checks": ["Doctor recommended", "Nitric oxide support", "Convenient lozenge format"],
        "avoid": ["Messy mixing", "Guesswork timing", "Unclear performance products"],
    },
    {
        "handle": "essential-aminos",
        "title": "ESSENTIAL AMINOS",
        "format": "Powder",
        "benefit": "Supports muscle recovery and daily amino acid intake.",
        "audience": "For active adults focused on recovery and lean muscle support.",
        "expect": ["Workout recovery support", "Amino intake support", "Daily training consistency"],
        "use": ["Mix with water", "Use around training", "Take daily as needed", "Follow serving size"],
        "checks": ["Doctor recommended", "Essential amino support", "Clean training routine"],
        "avoid": ["Under-fueling recovery", "Unnecessary additives", "Random gym blends"],
    },
    {
        "handle": "true-greens",
        "title": "SUPERGREENS",
        "format": "Powder",
        "benefit": "Supports daily micronutrient and greens intake.",
        "audience": "For busy adults building a cleaner wellness routine.",
        "expect": ["Daily greens habit", "Micronutrient support", "Foundational wellness routine"],
        "use": ["Mix with water", "Shake well", "Take daily", "Follow label serving"],
        "checks": ["Doctor recommended", "Daily greens support", "Clean wellness foundation"],
        "avoid": ["Missing daily plants", "Sugar-heavy drinks", "Unfocused wellness blends"],
    },
    {
        "handle": "vitamin-d-k2",
        "title": "VITAMIN D+K2",
        "format": "Capsules",
        "benefit": "Supports vitamin D status, bone health, and immune wellness.",
        "audience": "For adults maintaining foundational nutrient support.",
        "expect": ["Daily nutrient support", "Bone health routine", "Immune wellness support"],
        "use": ["Take as directed", "Pair with food", "Use consistently", "Check labs with clinician"],
        "checks": ["Doctor recommended", "D3 plus K2 pairing", "Foundational daily support"],
        "avoid": ["Guessing nutrient status", "Inconsistent dosing", "Single-purpose thinking"],
    },
    {
        "handle": "dna-support",
        "title": "DNA SUPPORT",
        "format": "Capsules",
        "benefit": "Supports antioxidant defenses and cellular wellness routines.",
        "audience": "For adults focused on long-term cellular health support.",
        "expect": ["Cellular support habit", "Antioxidant routine support", "Long-term wellness mindset"],
        "use": ["Take as directed", "Use daily", "Pair with meals", "Ask your clinician"],
        "checks": ["Doctor recommended", "Cellular wellness support", "Purposeful daily formula"],
        "avoid": ["Generic antioxidant blends", "Unclear ingredient purpose", "Inconsistent routines"],
    },
    {
        "handle": "liver-support",
        "title": "LIVER SUPPORT",
        "format": "Capsules",
        "benefit": "Supports liver wellness and natural detoxification pathways.",
        "audience": "For adults building a cleaner foundational health routine.",
        "expect": ["Daily liver support", "Detox pathway support", "Wellness routine consistency"],
        "use": ["Take as directed", "Pair with meals", "Hydrate daily", "Follow label guidance"],
        "checks": ["Doctor recommended", "Liver pathway support", "Clean daily routine"],
        "avoid": ["Detox fads", "Unclear blends", "Ignoring daily habits"],
    },
    {
        "handle": "hormone-support",
        "title": "HORMONE SUPPORT",
        "format": "Capsules",
        "benefit": "Supports hormone balance routines and everyday vitality.",
        "audience": "For adults looking for steady foundational support.",
        "expect": ["Daily balance support", "Vitality routine support", "Long-term consistency"],
        "use": ["Take as directed", "Use consistently", "Pair with meals", "Ask your clinician"],
        "checks": ["Doctor recommended", "Targeted hormone support", "Purposeful wellness formula"],
        "avoid": ["Extreme claims", "Random blends", "Inconsistent routines"],
    },
    {
        "handle": "calm",
        "title": "CALM",
        "format": "Capsules",
        "benefit": "Supports relaxation, stress resilience, and a calmer routine.",
        "audience": "For adults who want steady nervous-system support.",
        "expect": ["Relaxation routine", "Stress resilience support", "Daily calm habit"],
        "use": ["Take as directed", "Use consistently", "Pair with wind-down", "Follow label timing"],
        "checks": ["Doctor recommended", "Calm routine support", "Clean daily formula"],
        "avoid": ["Overstimulating routines", "Unclear calming blends", "Inconsistent use"],
    },
    {
        "handle": "true-omega",
        "title": "PREMIUM OMEGA 180",
        "format": "Softgels",
        "benefit": "Supports heart, brain, and inflammatory balance routines.",
        "audience": "For adults prioritizing foundational omega-3 support.",
        "expect": ["Daily omega habit", "Heart health support", "Brain wellness support"],
        "use": ["Take with meals", "Use daily", "Store as labeled", "Follow serving size"],
        "checks": ["Doctor recommended", "Foundational omega support", "Clean daily softgels"],
        "avoid": ["Low-quality oils", "Inconsistent omega intake", "Unclear sourcing"],
    },
    {
        "handle": "true-creatine",
        "title": "CREATINE 400G",
        "format": "Powder",
        "benefit": "Supports strength, power, and lean muscle performance.",
        "audience": "For active adults who want simple daily creatine support.",
        "expect": ["Training energy support", "Strength routine support", "Lean muscle support"],
        "use": ["Mix with water", "Take daily", "No loading needed", "Follow serving size"],
        "checks": ["Doctor recommended", "Micronized creatine", "Simple performance support"],
        "avoid": ["Overcomplicated formulas", "Guesswork dosing", "Unnecessary additives"],
    },
]


def font(size: int, bold: bool = False, black: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BLACK if black else FONT_BOLD if bold else FONT, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width or not current:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill, width: int, leading: int = 8) -> int:
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def rounded(draw, box, radius=18, fill=WHITE, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def product_cutouts(handle: str) -> list[Path]:
    return sorted(ASSETS.glob(f"*-{handle}-*.png"))


def contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    copy = ImageOps.exif_transpose(im).convert("RGBA")
    copy.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    return copy


def paste_shadow(base: Image.Image, im: Image.Image, x: int, y: int, shadow=True):
    if shadow:
        alpha = im.getchannel("A")
        shadow_im = Image.new("RGBA", im.size, (0, 0, 0, 120))
        shadow_im.putalpha(alpha.filter(ImageFilter.GaussianBlur(18)))
        base.alpha_composite(shadow_im, (x + 18, y + 30))
    base.alpha_composite(im, (x, y))


def canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGBA", (W, H), BG + (255,))
    draw = ImageDraw.Draw(im)
    return im, draw


def pill(draw, x, y, label, fill=GREEN):
    f = font(24, bold=True)
    pad_x, pad_y = 22, 13
    bbox = draw.textbbox((0, 0), label, font=f)
    rounded(draw, (x, y, x + bbox[2] + pad_x * 2, y + bbox[3] + pad_y * 2), 999, fill=fill)
    draw.text((x + pad_x, y + pad_y - 2), label, font=f, fill=WHITE)


def draw_check(draw, cx, cy, color=GREEN):
    draw.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), outline=color, width=6)
    draw.line((cx - 14, cy, cx - 3, cy + 13, cx + 18, cy - 15), fill=color, width=7, joint="curve")


def draw_x(draw, cx, cy, color=RED):
    draw.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), outline=color, width=6)
    draw.line((cx - 15, cy - 15, cx + 15, cy + 15), fill=color, width=6)
    draw.line((cx + 15, cy - 15, cx - 15, cy + 15), fill=color, width=6)


def draw_icon(draw, kind: str, cx: int, cy: int):
    draw.ellipse((cx - 48, cy - 48, cx + 48, cy + 48), outline=BLUE, width=8)
    if kind == "water":
        pts = [(cx, cy - 30), (cx - 23, cy + 5), (cx, cy + 34), (cx + 23, cy + 5)]
        draw.polygon(pts, fill=BLUE)
        draw.arc((cx - 13, cy + 3, cx + 10, cy + 28), 100, 180, fill=WHITE, width=5)
    elif kind == "clock":
        draw.line((cx, cy, cx, cy - 28), fill=BLUE, width=7)
        draw.line((cx, cy, cx + 22, cy + 18), fill=BLUE, width=7)
        for a in range(0, 360, 30):
            r = math.radians(a)
            draw.ellipse((cx + math.cos(r) * 34 - 3, cy + math.sin(r) * 34 - 3, cx + math.cos(r) * 34 + 3, cy + math.sin(r) * 34 + 3), fill=BLUE)
    elif kind == "calendar":
        draw.rounded_rectangle((cx - 28, cy - 24, cx + 28, cy + 30), radius=4, outline=BLUE, width=6)
        draw.rectangle((cx - 28, cy - 24, cx + 28, cy - 6), fill=BLUE)
        for dx in [-15, 0, 15]:
            for dy in [5, 18]:
                draw.rectangle((cx + dx - 4, cy + dy - 4, cx + dx + 4, cy + dy + 4), fill=BLUE)
    else:
        draw.line((cx - 25, cy - 25, cx + 25, cy + 25), fill=BLUE, width=8)
        draw.line((cx + 25, cy - 25, cx - 25, cy + 25), fill=BLUE, width=8)


def render_family(product: dict, cutouts: list[Path]):
    im, draw = canvas()
    draw.rectangle((0, 0, W, 220), fill=NAVY)
    draw.text((70, 70), product["title"], font=font(64, black=True), fill=WHITE)
    draw.text((74, 148), product["format"] + " | Practitioner-grade daily support", font=font(30), fill=(215, 232, 238))
    pill(draw, 865, 70, "Doctor Recommended")

    draw.ellipse((210, 865, 990, 1018), fill=(0, 0, 0, 28))
    selected = cutouts[:3] if len(cutouts) >= 3 else cutouts * 3
    sizes = [(355, 520), (450, 650), (355, 520)]
    positions = [(210, 360), (375, 285), (655, 360)]
    for idx, path in enumerate(selected[:3]):
        item = contain(Image.open(path), *sizes[idx])
        paste_shadow(im, item, positions[idx][0], positions[idx][1])

    draw.text((90, 1015), product["benefit"], font=font(38, bold=True), fill=NAVY)
    text_block(draw, (90, 1070), product["audience"], font(30), MUTED, 840, 10)
    im.save(OUTPUT / f"tmrx-pdp-{product['handle']}-01-family.png", optimize=True)


def render_science(product: dict, cutouts: list[Path]):
    im, draw = canvas()
    draw.rectangle((0, 0, 550, H), fill=NAVY)
    draw.text((70, 80), "The Practitioner-\nRecommended\nUpgrade", font=font(58, bold=True), fill=WHITE, spacing=12)
    y = 360
    for heading, body in [
        ("Purpose-built:", product["benefit"]),
        ("Made for:", product["audience"]),
        ("Clean standard:", "Chosen to fit a deliberate health routine, without unnecessary noise."),
    ]:
        draw.text((80, y), heading, font=font(33, bold=True), fill=WHITE)
        y = text_block(draw, (80, y + 48), body, font(31), (235, 244, 247), 370, 10) + 45

    rounded(draw, (625, 90, 1125, 1110), 24, fill=WHITE, outline=LINE, width=2)
    cutout = contain(Image.open(cutouts[0]), 390, 575)
    paste_shadow(im, cutout, 680 + (390 - cutout.width) // 2, 220)
    draw.text((675, 830), product["title"], font=font(36, bold=True), fill=NAVY)
    text_block(draw, (675, 885), "A doctor-recommended formula for people who want clear, confident daily support.", font(24), MUTED, 390, 7)
    im.save(OUTPUT / f"tmrx-pdp-{product['handle']}-02-science.png", optimize=True)


def render_expect(product: dict):
    im, draw = canvas()
    draw.text((170, 80), f"What to Expect\nWith {product['title']}", font=font(62, black=True), fill=NAVY, spacing=10, align="center")
    draw.text((250, 250), "Daily consistency matters more than a dramatic first dose.", font=font(34), fill=INK)
    draw.line((230, 390, 970, 390), fill=(139, 181, 200), width=5)
    for x in [230, 600, 970]:
        draw.line((x, 390, x, 445), fill=(139, 181, 200), width=5)

    labels = ["Week 1", "30 Days", "Long Term"]
    for i, (label, body) in enumerate(zip(labels, product["expect"])):
        x = 55 + i * 385
        rounded(draw, (x, 480, x + 320, 920), 18, fill=WHITE, outline=LINE)
        draw.text((x + 35, 525), label, font=font(43, bold=True), fill=BLUE)
        text_block(draw, (x + 35, 590), body + ".", font(29), INK, 250, 8)
        mini_y = 735
        draw.rounded_rectangle((x + 35, mini_y, x + 285, mini_y + 145), radius=12, fill=(229, 236, 239))
        draw.line((x + 65, mini_y + 105, x + 255, mini_y + 40), fill=(150, 171, 180), width=12)
        draw.ellipse((x + 80, mini_y + 35, x + 140, mini_y + 95), fill=(73, 126, 113))
        draw.rectangle((x + 170, mini_y + 55, x + 230, mini_y + 105), fill=(28, 76, 96))

    text_block(draw, (70, 1025), "Results vary. Use as directed and consult your healthcare provider before starting any new supplement routine.", font(24), MUTED, 1010, 8)
    im.save(OUTPUT / f"tmrx-pdp-{product['handle']}-03-expect.png", optimize=True)


def render_use_compare(product: dict, cutouts: list[Path]):
    im, draw = canvas()
    draw.text((70, 55), "How to Use", font=font(60, black=True), fill=NAVY)
    icon_kinds = ["water" if product["format"] == "Powder" else "calendar", "clock", "x", "calendar"]
    card_positions = [(70, 200), (630, 200), (70, 555), (630, 555)]
    for i, pos in enumerate(card_positions):
        x, y = pos
        rounded(draw, (x, y, x + 500, y + 270), 18, fill=WHITE, outline=LINE)
        draw_icon(draw, icon_kinds[i], x + 410, y - 10)
        draw.text((x + 55, y + 58), product["use"][i].split(" ", 1)[0] + (" " + product["use"][i].split(" ", 1)[1] if " " in product["use"][i] else ""), font=font(30, bold=True), fill=INK)
        body = {
            "Mix with water": "Add to water or your preferred beverage and shake well.",
            "Blend or shake": "Blend into a smoothie or shake until smooth.",
            "Take with meals": "Take with a meal for a steady daily omega routine.",
            "Let dissolve": "Let each lozenge dissolve as directed on the label.",
            "Use as directed": "Follow the label directions for daily use.",
            "Take as directed": "Follow the serving instructions on the label.",
        }.get(product["use"][i], "Keep the routine simple and consistent.")
        text_block(draw, (x + 55, y + 110), body, font(29), INK, 360, 8)

    y0 = 900
    draw.text((75, y0), "TMRX Standard", font=font(34, bold=True), fill=NAVY)
    draw.text((675, y0), "Typical Approach", font=font(34, bold=True), fill=NAVY)
    for i, copy in enumerate(product["checks"]):
        draw_check(draw, 105, y0 + 78 + i * 58)
        draw.text((155, y0 + 56 + i * 58), copy, font=font(25), fill=INK)
    for i, copy in enumerate(product["avoid"]):
        draw_x(draw, 705, y0 + 78 + i * 58)
        draw.text((755, y0 + 56 + i * 58), copy, font=font(25), fill=INK)

    im.save(OUTPUT / f"tmrx-pdp-{product['handle']}-04-use.png", optimize=True)


def make_contact_sheet(files: list[Path]):
    cols = 4
    tw, th = 240, 240
    rows = math.ceil(len(files) / cols)
    sheet = Image.new("RGB", (cols * tw, rows * (th + 34)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(files):
        x = (i % cols) * tw
        y = (i // cols) * (th + 34)
        thumb = Image.open(path).convert("RGB")
        thumb.thumbnail((tw - 10, th - 10), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x + (tw - thumb.width) // 2, y + 5))
        draw.text((x + 8, y + th + 5), re.sub(r"^tmrx-pdp-|\\.png$", "", path.name)[:30], fill=INK, font=font(12))
    sheet.save(ROOT / "generated-pdp-images-contact-sheet.jpg", quality=92)


def main():
    OUTPUT.mkdir(exist_ok=True)
    for old in OUTPUT.glob("tmrx-pdp-*.png"):
        old.unlink()

    rendered = []
    for product in PRODUCTS:
        cutouts = product_cutouts(product["handle"])
        if not cutouts:
            raise RuntimeError(f"No product cutout found for {product['handle']}")
        render_family(product, cutouts)
        render_science(product, cutouts)
        render_expect(product)
        render_use_compare(product, cutouts)
        rendered.extend(sorted(OUTPUT.glob(f"tmrx-pdp-{product['handle']}-*.png")))

    manifest = [
        {
            "handle": p["handle"],
            "title": p["title"],
            "assets": [f"tmrx-pdp-{p['handle']}-{idx:02d}-{slug}.png" for idx, slug in enumerate(["family", "science", "expect", "use"], 1)],
        }
        for p in PRODUCTS
    ]
    (ROOT / "generated-pdp-images-manifest.json").write_text(json.dumps(manifest, indent=2))
    make_contact_sheet(sorted(OUTPUT.glob("tmrx-pdp-*.png")))
    print(f"Generated {len(list(OUTPUT.glob('tmrx-pdp-*.png')))} PDP media images")


if __name__ == "__main__":
    main()
