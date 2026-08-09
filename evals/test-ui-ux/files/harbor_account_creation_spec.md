# Harbor account creation

## Target user and task

A first-time operations manager needs to create a workspace, invite one colleague, and reach the empty project dashboard in under two minutes on desktop or mobile.

## Flow

1. The landing page has one primary action, **Create workspace**, and a secondary **Sign in** link.
2. Create workspace opens a form with persistent labels for work email, workspace name, and password. It explains the password requirements before entry and exposes programmatic field names, descriptions, and error associations.
3. The form validates without clearing entered values. Focus moves to an error summary linking to each invalid field. Errors use text and an icon, not color alone.
4. After valid submission, a progress state says **Creating Harbor workspace**. The button is disabled while the request is active and repeated submissions are idempotent.
5. Success opens an optional colleague-invite step. **Skip for now** appears beside **Send invite** with equal keyboard access. The invite can also be completed later from the dashboard.
6. The dashboard confirms **Workspace created** and presents one primary action, **Create first project**.

## Interaction and accessibility provisions

- All interactive elements use native HTML controls in logical DOM and tab order.
- Every state change is announced through a polite live region; submission errors use an assertive summary.
- Text and meaningful controls meet WCAG 2.2 AA contrast. Focus indicators remain visible and unobscured.
- Controls meet the 24-by-24 CSS-pixel minimum target size, with larger 44-pixel primary actions on touch viewports.
- The layout reflows at 320 CSS pixels without horizontal scrolling.
- Motion respects reduced-motion preferences.

## Reliability provisions

- Account creation has a 2-second p95 service objective and a 10-second timeout with an explicit retry action.
- A network failure preserves every entered field and explains that no workspace was created.
- Duplicate email responses link to **Sign in** and password recovery.
- The team will test keyboard-only, VoiceOver/Safari, NVDA/Chrome, 200% zoom, 400% reflow, slow network, duplicate submission, and service failure before release.

## Deliberate weakness

The success screen uses the generic sentence **You're all set!** and no visual or copy detail reflects the new workspace name. The experience is functional and accessible, but its completion moment is not yet attentive or distinctive.
