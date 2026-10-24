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

Pending the candidate-branch rendering check and final profile read-back. Local preview results do not establish the behavior of GitHub's theme-selection component or its image proxy.
