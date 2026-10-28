# Ycany Ashra T. Sanchez · Streamlit Portfolio

A personal portfolio for **BSCS, 3rd year, section F2**, created for **CSIT 349 · Applied AI**. Dark gray surfaces with blue accents, a personal portrait, four projects, event announcements, and five self-rated skills.

## Run locally

Requires Python 3.12 or newer. Double-click **run_app.cmd** to install dependencies and start the app. The first setup needs an internet connection.

Alternatively, run these commands from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL printed by Streamlit, usually http://localhost:8501. On macOS/Linux, use `.venv/bin/python` instead of `.\.venv\Scripts\python.exe`.

## App contents

- **About:** autobiography, education, certifications, interests, milestones, awards, and a personal portrait.
- **Projects:** all four projects, their roles, tools, outcomes, links, and corresponding event images.
- **Skills:** all five personal ratings in a table and blue bar chart.

GitHub and LinkedIn appear in a shared footer on every page. Navigation has three sections: About, Projects, and Skills. Roles and awards use compact tables in milestones and project details. The browser tab uses the default Streamlit icon; the portrait remains in About.

Parola's two announcements appear side by side on wider screens and stack on mobile. BantAI Buddy's announcement appears directly in its project entry. Images are bundled locally and displayed without cropping.

## Projects and recognition

| Project | Personal role | Recognition or outcome |
|---|---|---|
| Parola | Ideator, API Integrator, Backend Developer, Workflow Developer | Top 25 qualifier and Special Awardee — Best Logo at Philippine Startup Challenge 11 — Central Visayas; Top 5 finalist — Iloilo AI Fest Hackathon Championship 2026 |
| BantAI Buddy | Backend Developer, Ideator | Top 2 — IBPAP Can You HackIt? Challenge |
| IMentia | Backend Developer | Face recognition, saved profiles, and meeting records |
| FoodPantry | Full-Stack Developer | Kotlin Android recipe discovery using the Spoonacular API |

Both **Top 25 qualifier** and **Special Awardee — Best Logo** belong to **Philippine Startup Challenge 11 — Central Visayas**. The Iloilo AI Fest award is a separate event.

## Personalize

- **portfolio.py:** identity, autobiography, links, roles, tools, awards, photo captions, certifications, and skill ratings.
- **assets/profile.png:** the personal portrait. The other PNGs are the original event announcements supplied by the owner.
- **.streamlit/config.toml:** the dark theme and blue primary accent.
- **assets/styles.css:** typography, spacing, and small visual adjustments.

The polling file watcher and automatic reruns keep imported project content current. If a long-running local server still shows old content, stop it with Ctrl+C and start it again.

## Verify

The full test suite in `tests/` is kept locally and is not tracked by Git. Run it from the original working folder:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

AppTest checks three-section navigation, footer contacts on every page, compact role/award tables, visible project images, all five skill ratings, and the absence of removed controls. It also checks that an old Contact-page selection safely returns to About. Content checks verify the approved ratings and both PSC XI awards' Central Visayas scope. AppTest is explicitly skipped if Streamlit is not installed.

The GitHub Actions workflow compiles the app and smoke-checks each page on Python 3.12 and 3.14 without requiring the local test folder. For optional local browser checks, follow the commands in `tests/browser-check.cjs`.

## Package the submission

```powershell
python tools/package_submission.py
```

The ZIP is created next to the project folder. It includes the app and all four original PNGs, and excludes virtual environments, Git metadata, caches, artifacts, and secrets.

Submission comment:

> Ycany Ashra T. Sanchez — BSCS, 3rd year, F2

## Community Cloud deployment

1. Upload the project files to [Ycany-Portfolio-Autobiography](https://github.com/Ycany-Sanchez/Ycany-Portfolio-Autobiography), including `assets/` and `.streamlit/config.toml`.
2. Sign in at [Streamlit Community Cloud](https://share.streamlit.io) with GitHub and select **Create app**.
3. Choose repository **Ycany-Sanchez/Ycany-Portfolio-Autobiography**, branch **main**, and entrypoint **app.py**.
4. Choose **Python 3.12** in advanced settings and deploy. No API keys or secrets are needed.
5. Check all three sections, footer contacts, role/award tables, and project photos in a private/incognito window, then submit the public **.streamlit.app** link.

[Official deployment instructions](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)

## Content sources

- [Original portfolio](https://github.com/Ycany-Sanchez/ycany-portfolio/blob/main/content.mjs): education, certifications, and project descriptions.
- [IMentia README](https://github.com/Ycany-Sanchez/IMentia/blob/main/README.md) and [build configuration](https://github.com/Ycany-Sanchez/IMentia/blob/main/pom.xml).
- [FoodPantry README](https://github.com/Ycany-Sanchez/FoodPantry/blob/main/README.md) and [build configuration](https://github.com/Ycany-Sanchez/FoodPantry/blob/main/build.gradle.kts).
- The owner supplied current school details, personal roles, skill ratings, award updates, the portrait, and all three event announcements.

Review the autobiographical writing before submission so it reflects your own words and work.
