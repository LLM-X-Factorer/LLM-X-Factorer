# Pixel workshop: design research

Research date: 2026-10-24. Scope: the `LLM-X-Factorer` GitHub Profile README.

## Direction

The intended audience is technical peers and potential open-source collaborators. The owner chose a playful developer profile with pixel art, illustration, and a sense of interaction.

The previous profile established the engineering story, but its static terminal banner and repeated bilingual paragraphs made the page feel like a long document. This iteration turns that story into a small developer workshop: a recognisable scene, three work areas, and real paths into the code.

## References inspected

These references informed the design principles. Their artwork, source assets, personal biographies, and visual identities are not reused.

| Reference | Observed in the public source | Adopted principle |
| --- | --- | --- |
| [skulitom / skulitom](https://github.com/skulitom/skulitom) | The README combines a pixel workbench hero, individual illustrated tool scenes, normal text, and links. Its `picture` sources include mobile and motionless variants. The hero still was rendered and inspected during research. | Create one coherent world, give each work area a visual role, and keep project descriptions as real text. Use separate compositions for small screens and explicit still assets. |
| [MishManners / MishManners](https://github.com/mishmanners/MishManners) | The README opens with a looping illustration of a gaming room. The [original GIF](https://github.com/mishmanners/MishManners/blob/master/Gamer%20room%20compress%20loop%20new%20larger.gif) was inspected. This is illustrated artwork, not pixel art. | Make the scene feel personal and inhabited. Restrict movement to a few details so the scene can be recognised at a glance. |
| [marcizhu / marcizhu](https://github.com/marcizhu/marcizhu) | Its chess board offers links that prepare an Issue; the repository explains that a GitHub Action processes the move and updates the README. The README and mechanism were inspected; no move was submitted. | An invitation should lead to a real action. Our navigation jumps to actual sections; project and quest links open existing repositories, contribution guides, and issues. |

The chess example is a reference for honest interaction, not a requirement to add a game or an issue-processing service to this profile.

## Platform constraints and evidence

- **The README is a filtered document, not a custom web application.** GitHub's [markup pipeline description](https://github.com/github/markup#github-markup) explains that the generated HTML is sanitised, including scripts, inline styles, and certain attributes. Layout cannot depend on a page-level stylesheet or JavaScript.
- **Images and GIFs are supported profile content.** GitHub documents these in [About your profile](https://docs.github.com/en/account-and-profile/concepts/personal-profile). The animated SVG approach additionally has working public-source examples, but that does not replace checking this profile's own files in GitHub's renderer.
- **Expandable drawers use a supported control.** GitHub documents [`details` and `summary`](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections). These remain keyboard-accessible native controls rather than pictures of buttons.
- **Mobile and reduced-motion selection need explicit testing.** The [skulitom README](https://github.com/skulitom/skulitom/blob/main/README.md) selects mobile and still SVGs in outer `picture` elements. Its [wrapper source](https://github.com/skulitom/skulitom/blob/main/art/tools/wrap.py) notes that an SVG displayed as an image should not rely only on its internal reduced-motion query. This is implementation evidence from that project, not a compatibility guarantee for ours.
- **Image links have one destination.** Navigation graphics are individually wrapped in native anchors. The large hero is an illustration; objects inside it are not presented as working buttons or draggable controls.

## Applied design decisions

1. Replace the terminal-window motif with original pixel workshop artwork. The visual narrative should support building and improving useful AI tools.
2. Use one hero with desktop/mobile and light/dark variants, plus genuine static alternatives. The initial image must already contain a complete, meaningful composition.
3. Keep the personal positioning concise, then offer three section links: **Agent bay**, **Workflow shelf**, and **Quest board**.
4. Keep project names, descriptions, maturity labels, and contribution instructions in native Markdown. Avoid two-column project tables that compress text on phones.
5. Use small, purposeful ambient motions. Do not imply a live task, real-time deployment status, or measured business result through decorative animation.
6. Put the wider toolkit, other projects, and social links in optional drawers. Keep the main path focused on public engineering work.
7. Reuse the already-reviewed public project facts: LocalBuddy is an engineering alpha; DeepFlow is a teaching reference; the two Skills are workflow examples; `md2wechat` is a fork. Do not mix private product features into public examples.
8. Offer concrete collaboration starting points: a reproducible failed agent run, an independent SQL evaluation case, and the existing Chinese research-source discussion in [topic2md #14](https://github.com/LLM-X-Factorer/topic2md/issues/14). These are invitations, not claims that tasks have been assigned or accepted.

## Verification before calling the iteration complete

The following are checks to perform on this implementation, not results established by the research:

- Confirm every asset path, section anchor, repository link, and contribution link.
- Inspect the GitHub-rendered README on a wide viewport and a narrow phone viewport; check text legibility, wrapping, clipping, and navigation.
- Verify the chosen light/dark and mobile hero sources, including every reduced-motion combination. Static variants must contain no running animation.
- Compare more than one point in the animated loop to confirm that the intended details move while text remains stable.
- Confirm native navigation and expandable drawers work, rather than only resembling controls.
- After publication, read back the committed files and inspect the live GitHub page. A local preview alone is not proof of the production result.
