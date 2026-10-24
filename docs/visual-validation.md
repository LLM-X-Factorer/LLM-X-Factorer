# Pixel workshop verification

Date: 2026-10-24.

## Local checks completed

- GitHub's Markdown API accepted the README, including the `picture` source conditions, links and native drawers.
- Browser previews covered desktop (1200 px viewport) and mobile (390 px viewport), light and dark, with default and reduced motion: all eight combinations selected the expected asset and had no horizontal document overflow.
- Page screenshots taken 1.2 seconds apart differed in the four animated cases and were identical in the four static cases. The comparison used page screenshots; element screenshots were not a reliable animation probe in the local runner.
- All three `details` drawers were present; the toolbox was opened and closed in every combination.
- Every SVG parses as XML. Static variants contain no animation style or animation elements. Assets contain no scripts, `foreignObject`, external image references or external font requests.
- All README asset paths resolve to tracked delivery candidates.
- Visual review covered desktop light/dark and mobile compositions. It led to removing repeated section banners, shortening the identity sentence, centering the navigation, and removing a decorative element that could be mistaken for a button.

## Live GitHub checks

- The public candidate branch rendered all image assets and kept the `picture` media conditions. The signed-in account used GitHub's automatic color mode; browser media emulation exercised light/dark and reduced-motion selection without changing account preferences.
- A 390 px viewport selected the mobile composition; the live light-mode layout was visually inspected. Dark mobile with reduced motion selected `hero-dark-mobile-still.svg`. Desktop checks selected `hero-dark.svg` with motion and `hero-light-still.svg` with reduced motion.
- Two live desktop screenshots showed changing pixels within the animated hero. Two further screenshots of the reduced-motion hero were pixel-identical within its bounding rectangle.
- GitHub generates a leading hyphen in section slugs when the heading starts with an inline image. Navigation was corrected to `#-agent-bay`, `#-workflow-shelf`, and `#-quest-board`; all three links reached their respective headings.
- The native toolbox drawer opened and closed on GitHub, exposing the expected text.
- A final compatibility change separates theme visibility from responsive and reduced-motion selection: two theme-marked anchors wrap two complete `picture` elements in a single paragraph. The final Markdown API output preserved both wrappers and all six sources. On the live candidate, exactly one theme wrapper was visible.
- Opposing theme conditions were tested by temporarily changing the page's root `data-color-mode` attribute through browser development tooling, without changing the account setting: desktop GitHub dark with system light displayed only the dark desktop hero; 390 px GitHub light with system dark and reduced motion displayed only the light mobile still hero. The hidden hero occupied zero width. The root attribute, media emulation, and viewport override were restored afterward.

## Published profile read-back

- Published the verified iteration to `main` at `6311a639259385687abf28019dcdfc8ed6a5eea1`.
- Read the README, desktop light hero, and mobile dark still hero back through GitHub's API; their bytes matched the local files.
- Opened the public profile after publication. It displayed the new workshop and three navigation links, retained the reviewed bio and six pins, and loaded `raw/main/assets/hero-light.svg`. The dark wrapper occupied zero width.
- Saved a screenshot of the published profile with its surrounding GitHub interface for the owner.

Browser checks establish the combinations above, not a guarantee across every browser or future GitHub renderer change.
