"""Run with: python -m streamlit run app.py"""

from datetime import datetime
from html import escape
from pathlib import Path

import pandas as pd
import streamlit as st

from portfolio import (
    CERTIFICATIONS, PROFILE, PROJECTS, SKILLS, biography_text, project_outcome,
)


ROOT = Path(__file__).resolve().parent
SECTIONS = ["About", "Projects", "Skills"]


def eyebrow(text):
    st.markdown(f'<p class="eyebrow">{escape(text)}</p>', unsafe_allow_html=True)


def tags(items):
    st.markdown(
        '<div class="tag-list">' + ''.join(f'<span>{escape(item)}</span>' for item in items) + '</div>',
        unsafe_allow_html=True,
    )


def go_to(section):
    st.session_state["section"] = section


def render_sidebar():
    with st.sidebar:
        st.markdown(f'<div class="wordmark">{escape(PROFILE["short_name"])}</div>', unsafe_allow_html=True)
        st.caption(f"{PROFILE['program']} · {PROFILE['year']}")
        st.divider()
        st.radio("Pages", SECTIONS, key="section")
        st.divider()
        st.caption(PROFILE["school"])
        st.caption("CSIT 349 · Applied AI")


def render_identity():
    eyebrow("Autobiography & portfolio")
    st.title(PROFILE["name"])
    st.caption(f"{PROFILE['program']} · {PROFILE['year']} · Section {PROFILE['section']}  /  {PROFILE['school']}")
    st.divider()


def render_project_facts(project, *, include_role=True):
    rows = []
    if include_role:
        rows.append(("My role", project["role"].replace(" · ", ", ")))
    rows.extend((award["event"], award["title"]) for award in project["awards"])
    if rows:
        columns = ["Detail", "Information"] if include_role else ["Event", "Recognition"]
        st.table(
            pd.DataFrame(rows, columns=columns), hide_index=True,
            hide_header=include_role, border="horizontal", width="stretch",
            alt=f"{project['name']} roles and recognition" if include_role else f"{project['name']} event recognition",
        )


def render_recognition():
    for project in PROJECTS:
        if project["awards"]:
            st.markdown(f"**{project['name']}**")
            render_project_facts(project, include_role=False)
            if project.get("photos"):
                with st.expander(f"{project['name']}: event announcements"):
                    render_project_photos(project)


def render_project_photos(project):
    photos = project.get("photos", [])
    if not photos:
        return
    frames = st.columns(len(photos), gap="large") if len(photos) > 1 else [st.container()]
    for photo, frame in zip(photos, frames):
        with frame:
            st.image(
                str(ROOT / "assets" / photo["file"]),
                width="stretch" if len(photos) > 1 else 420,
                caption=photo["caption"], alt=photo["alt"],
            )


def render_about():
    parola, bantai = PROJECTS[:2]
    copy, artwork = st.columns([2.4, 1], gap="large", vertical_alignment="center")
    with copy:
        st.markdown('<div class="intro-heading">Computer science student.<br>Backend developer.</div>', unsafe_allow_html=True)
        st.write(PROFILE["intro"])
        st.button("View projects", on_click=go_to, args=("Projects",))
    with artwork:
        st.image(str(ROOT / "assets" / "profile.png"), width=180, alt=PROFILE["name"])
    st.divider()

    story, education, recognition = st.tabs(["About me", "Education", "Awards"])
    with story:
        text, interests = st.columns([1.7, 1], gap="large")
        with text:
            st.markdown(biography_text())
        with interests:
            st.markdown("**Interests**")
            for interest in PROFILE["interests"]:
                st.write(interest)
        st.subheader("Milestones")
        with st.expander(f"{PROFILE['education_dates']} · College"):
            st.write(f"{PROFILE['program_full']} at {PROFILE['school']}.")
            st.caption(f"Current year: {PROFILE['year']} · Section {PROFILE['section']}")
        for project in [bantai, parola]:
            title = f"{project['year']} · {project['name']}" if project.get("year") else project["name"]
            with st.expander(title):
                render_project_facts(project)
    with education:
        st.subheader(PROFILE["school"])
        st.write(f"{PROFILE['program_full']} · {PROFILE['education_dates']}")
        st.caption(f"Current year: {PROFILE['year']} · Section {PROFILE['section']}")
        st.markdown("**Academic recognition**")
        st.table(pd.DataFrame(PROFILE["academic_achievements"]), hide_index=True, border="horizontal", width="stretch", alt="Senior high honors, College Scholar tuition coverage, and Dean’s List recognition")
        st.subheader("Certifications")
        st.table(pd.DataFrame(CERTIFICATIONS).rename(columns={"name": "Certification", "issuer": "Issuer", "date": "Date"}), hide_index=True, border="horizontal", width="stretch", alt="Certifications, issuers, and completion dates")
    with recognition:
        render_recognition()

def render_project(project, number):
    with st.container(key=f"project_{project['id']}"):
        st.divider()
        eyebrow(f"{number:02d} · {project['category']}")
        st.subheader(project["name"])
        st.write(project["description"])
        render_project_facts(project)
        tags(project["tools"])
        if not project["awards"]:
            st.write(project_outcome(project))
        st.link_button(project["link_label"], project["url"])
        render_project_photos(project)
        with st.expander(f"Details: {project['name']}"):
            st.write(project["story"])
            for title, body in project["details"]:
                st.markdown(f"**{title}**")
                st.write(body)


def render_projects():
    st.header("Projects")
    st.write("School and competition projects, with my role and the tools used for each.")
    for number, project in enumerate(PROJECTS, 1):
        render_project(project, number)


def render_skills():
    st.header("Skills")
    st.write("Backend development is my strongest area. These are my own ratings, based on my project work.")
    st.caption("Scale: 1 = beginning, 3 = developing, 5 = my strongest area.")
    summary, chart = st.columns([1, 2], gap="large")
    with summary:
        st.metric(SKILLS[0][0], f"{SKILLS[0][1]} / 5")
    frame = pd.DataFrame(SKILLS, columns=["Skill", "Rating"])
    with chart:
        st.bar_chart(frame, x="Skill", y="Rating", color="#78a9ed", horizontal=True, height=300, x_label="Self-assessed proficiency / 5", y_label="", sort=False, alt="Self-assessed skill ratings on a five-point scale")
    st.table(frame.assign(Scale=5), hide_index=True, border="horizontal", width="stretch", alt="Five self-assessed skills rated on a five-point scale")
    st.divider()
    st.subheader("Examples from my projects")
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("**Backend development**")
        st.write("I worked on the backend for Parola, BantAI Buddy, and IMentia, and handled full-stack development for FoodPantry.")
    with right:
        st.markdown("**APIs and automation**")
        st.write("For Parola, I worked on API integration and automated workflows. FoodPantry uses the Spoonacular API to find recipes.")


def render_footer():
    st.divider()
    with st.container(key="contact_footer"):
        identity, github, linkedin = st.columns([3, 1, 1], gap="small", vertical_alignment="center")
        with identity:
            st.caption(f"© {datetime.now().year} {PROFILE['name']}")
        with github:
            st.link_button("GitHub", PROFILE["github"], width="stretch")
        with linkedin:
            st.link_button("LinkedIn", PROFILE["linkedin"], width="stretch")


def main():
    st.set_page_config(page_title=f"{PROFILE['name']} | Portfolio", layout="wide", initial_sidebar_state="auto")
    st.markdown(f"<style>{(ROOT / 'assets' / 'styles.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    if st.session_state.get("section") not in SECTIONS:
        st.session_state["section"] = "About"
    render_sidebar()
    render_identity()
    {"About": render_about, "Projects": render_projects, "Skills": render_skills}[st.session_state.section]()
    render_footer()


if __name__ == "__main__":
    main()
