# Repository hero guidelines

Repo-complete public repositories need a README hero that survives GitHub and Telegram downscaling.

## Required qualities

- Crisp at normal GitHub README width; no fuzzy/glassy rendering.
- Not too zoomed out: primary title and one short subtitle must dominate the image.
- Calm composition: no busy grid, no dense micro-diagrams, no decorative clutter.
- Text stays inside cards and does not overlap decorative lines.
- No tiny labels that become unreadable below roughly 700 px rendered width.
- Prefer vector SVG with real text for repo heroes.
- Avoid SVG filters, gaussian blur, heavy drop shadows, large soft glows, and low-contrast micro-lines.
- Use 1 primary accent color, strong contrast, and large type.

## Practical SVG rules

- Use a compact canvas, roughly `1000×360` or similar, instead of a very wide/zoomed-out scene.
- Keep important text at least ~24 px in source SVG; card values should be larger.
- Keep labels short.
- Put decorative lines behind content, never through text/cards.
- Use integer coordinates where practical.
- Use common fonts such as `Arial, Helvetica, sans-serif` so GitHub rendering is predictable.

## Verification

Before shipping:

1. Open the SVG locally in a browser.
2. Visually inspect at GitHub README scale.
3. Check for:
   - fuzzy text;
   - text overflow;
   - decorative lines crossing text;
   - overbusy background;
   - too much unused/zoomed-out space.
4. Run `make check`.

Do not accept a hero only because the raw SVG is valid; visual QA is part of repo-complete.
