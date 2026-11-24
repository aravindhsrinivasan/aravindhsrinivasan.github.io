# Aravindh Srinivasan - personal portfolio

A static portfolio covering my professional background, product principles and planned personal AI-PM projects.

The site is adapted from my personal pitch. It deliberately excludes internal usage figures, employer roadmap details and the original narration. The guided pitch uses captions only; revised audio will be added after review.

## Run locally

From the repository root:

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000 in a browser. No build tools, model credentials or external scripts are required.

## Check

```powershell
python -m unittest discover -s tests -v
```

Before publishing, check desktop and mobile layouts, keyboard tabs, role-lens links and the guided-caption controls. On narrow screens, confirm that the tour leaves enough room to scroll the footer above it. Print should include all tab panels but no tour controls. Without JavaScript, all tab panels remain visible and interactive tour controls are hidden.

## Project status

The documentation copilot, triage agent and model-routing comparison are planned, not completed products. Their supporting repositories are planned too. Add code and demo links only when the corresponding work exists; add results only after measurement.

Professional experience is presented separately from personal projects. No employer source code, datasets or confidential artifacts belong in this repository.

## Publishing

The intended home is GitHub Pages for `aravindhsrinivasan`. Confirm the authenticated GitHub account and inspect any existing repository before creating or updating it. Publish only this reviewed site, not the original pitch files or planning notes.

No analytics or third-party scripts are included. GitHub Pages hosting has its own service policies.
