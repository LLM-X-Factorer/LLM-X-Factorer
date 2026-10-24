# Workshop artwork

The workshop illustration was created for this profile with OpenAI's built-in image generation tool on 2026-10-24. No reference artwork was supplied. The illustration is decorative, not a screenshot of a product or a real workspace.

- `workshop.png`: the original transparent illustration.
- `workshop.webp`: a 768 × 768 web delivery copy, encoded at quality 90 with alpha retained.
- `hero-*.svg`: self-contained desktop/mobile, light/dark, animated/still compositions. Each embeds the web image, so it makes no external image or font request.
- `nav-*.svg` and `icon-*.svg`: original vector pixel icons and bitmap lettering.
- `../scripts/build_art.py`: the standard-library-only generator for all SVG assets. Run `python3 scripts/build_art.py` from the repository root to rebuild them.

## Motion and interaction

The illustration floats slowly; small background pixels brighten and a decorative packet crosses the idea-to-tool line. These do not report live tasks or deployment status. Static assets omit all animation styles. The README chooses static assets through the outer `picture` element when reduced motion is requested; the animated SVGs also include a reduced-motion CSS guard.

The image itself has no JavaScript, embedded links, or hover behavior. The README wraps the navigation assets in real links and uses native `details` controls for the drawers.

## Generation prompt

> Use case: stylized-concept. Asset type: original pixel-art illustration for a playful developer GitHub profile, to be embedded beside real HTML text and animated vector accents. Create a beautifully crafted, compact isometric cutaway developer workshop on a small floating platform, isolated on a genuinely transparent background. Cozy, inventive, premium indie-game pixel art, visibly crisp square pixels, carefully controlled pixel clusters, no blurred edges, not a 3D render. Main subject: a dark navy workbench with two small luminous mint and lavender monitors, a tiny friendly cream-and-teal robot assistant beside it, a short server rack, a shelf of research notebooks, a small printer ejecting one page, a potted green plant and a warm desk lamp. These should read as one coherent small workshop, not disconnected icons. Use deep ink navy, warm ivory, muted lilac, soft peach and vivid mint accents; highlight readable silhouettes with restrained highlights. Isometric three-quarter view, all objects fully visible with generous transparent padding, roughly square overall footprint suitable for the right half of a wide website hero. The scene should feel like a charming engineer's world with depth and careful detail, while staying legible as a 420px-wide illustration. No people, no text, no letters, no numbers, no logos, no interface chrome, no watermark. Transparent outside the platform, no opaque background, no checkerboard pattern.

## Re-encoding the web copy

Optional authoring dependency: Pillow. Rebuild the delivery image from the original with:

```python
from PIL import Image

Image.open('assets/workshop.png').resize(
    (768, 768), Image.Resampling.LANCZOS
).save('assets/workshop.webp', format='WEBP', quality=90, method=6)
```

Then rerun the SVG generator and inspect the result in the GitHub renderer.
