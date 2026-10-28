"""Streamlit navigation, footer contacts, project facts, and images."""

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

from portfolio import PROFILE, PROJECTS, SKILLS

HAS_STREAMLIT = importlib.util.find_spec("streamlit") is not None
if HAS_STREAMLIT:
    from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parents[1] / "app.py"
SECTIONS = ["About", "Projects", "Skills"]


@unittest.skipUnless(HAS_STREAMLIT, "Install requirements.txt to run AppTest")
class StreamlitAppTests(unittest.TestCase):
    def setUp(self):
        self.app = AppTest.from_file(str(APP), default_timeout=30).run()

    def navigate(self, section):
        self.app.radio(key="section").set_value(section).run()
        self.assertEqual(len(self.app.exception), 0)

    def table_rows(self):
        return [
            " ".join(str(value) for value in row)
            for table in self.app.table
            for row in table.value.itertuples(index=False, name=None)
        ]

    def test_every_section_has_footer_contacts_without_removed_controls(self):
        self.assertEqual(self.app.title[0].value, "Ycany Ashra Sanchez")
        for section in SECTIONS:
            with self.subTest(section=section):
                self.navigate(section)
                self.assertEqual(self.app.radio(key="section").options, SECTIONS)
                for kind in ["download_button", "text_input", "text_area", "selectbox", "multiselect", "slider", "checkbox", "form"]:
                    self.assertEqual(len(self.app.get(kind)), 0, f"{kind} should be absent on {section}")
                contacts = [link for link in self.app.get("link_button") if link.proto.label in ("GitHub", "LinkedIn")]
                self.assertEqual(len(contacts), 2)
                self.assertEqual(
                    {link.proto.label: link.proto.url for link in contacts},
                    {"GitHub": PROFILE["github"], "LinkedIn": PROFILE["linkedin"]},
                )
                self.assertFalse(any(element.type == "link_button" for element in self.app.sidebar))

    def test_projects_show_all_entries_with_roles_and_awards_in_tables(self):
        self.navigate("Projects")
        self.assertEqual([item.value for item in self.app.subheader], [project["name"] for project in PROJECTS])
        rows = self.table_rows()
        for role in ["Ideator", "API Integrator", "Backend Developer", "Workflow Developer"]:
            self.assertTrue(any(role in row for row in rows), role)
        for recognition in ["Top 25 qualifier", "Best Logo"]:
            matches = [row for row in rows if recognition in row]
            self.assertTrue(matches, recognition)
            self.assertTrue(all("Central Visayas" in row for row in matches), recognition)
        self.assertTrue(any("Iloilo AI Fest" in row and "Top 5 finalist" in row for row in rows))
        self.assertFalse(any(
            "Top 25" in element.value and "Best Logo" in element.value
            for element in self.app.markdown
        ), "Award lists must not return as a single run-on paragraph.")

    def test_navigation_button_opens_projects(self):
        next(button for button in self.app.button if button.label == "View projects").click().run()
        self.assertEqual(self.app.radio(key="section").value, "Projects")
        self.assertEqual(len(self.app.exception), 0)

    def test_projects_display_all_three_announcements(self):
        self.navigate("Projects")
        self.assertEqual(len(self.app.get("image")), 3)
        for details in self.app.expander:
            self.assertFalse(any(element.type == "image" for element in details), "Project photos must be visible outside collapsed details.")

    def test_content_edits_reach_about_tables(self):
        with patch.dict(PROFILE, {"section": "Updated Section"}), patch.dict(PROJECTS[0]["awards"][0], {"title": "Updated Recognition"}):
            self.app.run()
            captions = "\n".join(element.value for element in self.app.caption)
            table_text = "\n".join(self.table_rows())
            self.assertIn("Updated Section", captions)
            self.assertNotIn("Section F2", captions)
            self.assertIn("Updated Recognition", table_text)
            self.assertNotIn("Top 25", table_text)

    def test_skills_always_show_all_five_ratings(self):
        self.navigate("Skills")
        table = self.app.table[0].value
        self.assertEqual(list(zip(table["Skill"], table["Rating"])), SKILLS)
        self.assertEqual(table["Scale"].tolist(), [5] * len(SKILLS))

    def test_old_contact_selection_returns_to_about(self):
        old_session = AppTest.from_file(str(APP), default_timeout=30)
        old_session.session_state["section"] = "Contact"
        old_session.run()
        self.assertEqual(len(old_session.exception), 0)
        self.assertEqual(old_session.radio(key="section").value, "About")
        self.assertEqual(old_session.radio(key="section").options, SECTIONS)


if __name__ == "__main__":
    unittest.main()
