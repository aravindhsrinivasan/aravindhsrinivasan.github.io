# Aravindh Srinivasan - personal portfolio

A static portfolio covering my professional background, product principles and personal AI-PM projects.

The site follows my personal pitch: career introduction, a before/after workflow, achievement stories, product approach, role lenses, career path and interests. Independent projects remain clearly separate from employer work. Internal usage figures, employer roadmap details, uncleared awards and the original recording are excluded.

The guided pitch has captions and optional on-device English speech synthesis. It never selects a remote voice or plays automatically. This reads the revised public-safe script, not the original MP3. If a local voice is missing or fails, a visible status explains the captions-only fallback. Pause stops speech; resume restarts that section's narration. `P` plays/stops, `Space` pauses and `M` toggles voice when focus is not on another control.

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

Before publishing, check desktop and mobile layouts, keyboard tabs, all role-lens links and guided-pitch controls. Check both local-voice availability and the captions fallback, including interruption, Next, Pause and Stop. On narrow screens, confirm that the tour leaves enough room to scroll the footer above it. Print should include all tab panels but no tour controls. Without JavaScript, all tab panels remain visible and interactive tour controls are hidden.

## Project status

The documentation copilot has a local extractive baseline evaluated on 60 AI-drafted questions. All labels remain unreviewed: this is ungated development evidence, not a launch claim. The optional SDK stage is implemented, but live evaluation is pending. The triage agent and model-routing comparison remain planned. Supporting repositories are not public yet; add links only after publication.

The career facts are owner-supplied in the personal pitch. The project status comes from the local copilot's dated 2026-11-24 baseline report and implementation verification. Do not turn target outcomes into achieved results, or reintroduce workplace measurements without public evidence or explicit disclosure clearance.

Professional experience is presented separately from personal projects. No employer source code, datasets or confidential artifacts belong in this repository.

## Publishing

Live site: https://aravindhsrinivasan.github.io/

GitHub Pages deploys the repository root from `main`. The owner approved this public-safe pitch adaptation for publication. Confirm the authenticated GitHub account before pushing updates. Publish only the reviewed site, not original pitch files, audio or planning notes.

### Link previews

LinkedIn, Teams and other apps build the preview card from the Open Graph tags in `index.html` and `assets/share-card.jpg` (1200×627, made from the hero art and headline). After changing either, run the live URL through https://www.linkedin.com/post-inspector/ to refresh LinkedIn's cached preview.

No analytics or third-party scripts are included. GitHub Pages hosting has its own service policies.
