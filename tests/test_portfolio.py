"""Owner-approved identity, skills, and regional recognition."""

import unittest

from portfolio import PROFILE, PROJECTS, SKILLS, project_outcome


class PortfolioTests(unittest.TestCase):
    def test_identity_and_approved_skill_ratings(self):
        self.assertEqual(PROFILE["section"], "F2")
        self.assertEqual(dict(SKILLS), {
            "Backend Development": 5, "AI Integration": 4,
            "Product Ideation": 4, "API Integration": 4,
            "Workflow Automation": 3,
        })

    def test_project_awards_use_the_confirmed_event_scopes(self):
        parola = next(project for project in PROJECTS if project["id"] == "parola")
        top_25 = next(award for award in parola["awards"] if "Top 25" in award["title"])
        best_logo = next(award for award in parola["awards"] if "Best Logo" in award["title"])
        self.assertEqual(top_25["title"], "Top 25 qualifier")
        self.assertEqual(top_25["event"], "Philippine Startup Challenge 11 — Central Visayas")
        self.assertEqual(best_logo["event"], top_25["event"])
        iloilo = next(award for award in parola["awards"] if "Top 5" in award["title"])
        self.assertIn("Iloilo AI Fest", iloilo["event"])
        self.assertNotEqual(iloilo["event"], top_25["event"])
        bantai = next(project for project in PROJECTS if project["id"] == "bantai")
        self.assertIn("Top 2", project_outcome(bantai))
        self.assertIn("IBPAP Can You HackIt? Challenge", project_outcome(bantai))
        self.assertNotIn("Top 25", project_outcome(bantai))


if __name__ == "__main__":
    unittest.main()
