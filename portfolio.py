"""Editable portfolio content and dependency-free behavior.

Sources: the owner's existing portfolio and the project READMEs linked below.
Roles, current school details, PSC/IBPAP awards, and ratings were supplied by Ycany.
"""

# PERSONAL DETAILS — edit here to personalize the whole app.
PROFILE = {
    "name": "Ycany Ashra Sanchez",
    "short_name": "Ycany",
    "program": "BSCS",
    "program_full": "Bachelor of Science in Computer Science",
    "year": "3rd year",
    "section": "F2",
    "school": "Cebu Institute of Technology – University",
    "education_dates": "2024–2028",
    "github": "https://github.com/Ycany-Sanchez",
    "linkedin": "https://www.linkedin.com/in/ycany-ashra-sanchez-bb987937a/",
    "intro": "Most of my project work is on the backend: building application logic, connecting APIs, and setting up automated workflows.",
    "biography": (
        "I’m a third-year BSCS student at Cebu Institute of Technology, in section F2. "
        "My main role in group projects is backend development.\n\n"
        "For Team TIKI’s Parola, I contributed to the idea, backend, API integrations, "
        "and automated workflows. For BantAI Buddy, I worked as a backend developer "
        "and ideator on a browser extension for screening harmful messages.\n\n"
        "I also worked on the backend of IMentia, a face-recognition application for "
        "people with dementia and their caregivers. For FoodPantry, I handled "
        "full-stack development on an Android app that suggests recipes from pantry ingredients."
    ),
    "interests": ["Backend development", "API integration", "Applied AI", "Workflow automation"],
}

# SELF-ASSESSED SKILLS — the five ratings approved by the owner, on a 1–5 scale.
SKILLS = [
    ("Backend Development", 5),
    ("AI Integration", 4),
    ("Product Ideation", 4),
    ("API Integration", 4),
    ("Workflow Automation", 3),
]

CERTIFICATIONS = [
    {"name": "Java OOP", "issuer": "CodeChum", "date": "May 2026"},
    {"name": "AI Ready ASEAN", "issuer": "ASEAN Foundation", "date": "December 2025"},
    {"name": "Graphic Design Essentials", "issuer": "Canva", "date": "September 2025"},
]

# PROJECTS — keep personal roles distinct from the team's overall features.
PROJECTS = [
    {
        "id": "parola", "name": "Parola", "category": "AI and fisheries",
        "subtitle": "Fishing advisories from ocean and satellite data.",
        "role": "Ideator · API Integrator · Backend Developer · Workflow Developer",
        "description": "A Team TIKI project for Filipino fisherfolk. Parola uses ocean and satellite data to identify potential fishing grounds, with SMS advisories for people without reliable internet access.",
        "tools": ["Python", "Machine Learning", "API Integration", "Satellite Data", "n8n", "SMS Integration"],
        "awards": [
            {"title": "Top 25 qualifier", "event": "Philippine Startup Challenge 11 — Central Visayas"},
            {"title": "Special Awardee — Best Logo", "event": "Philippine Startup Challenge 11 — Central Visayas"},
            {"title": "Top 5 finalist", "event": "Iloilo AI Fest Hackathon Championship 2026"},
        ],
        "story": "Developed by Team TIKI, Parola combines machine learning with oceanographic and satellite datasets to predict potential fishing grounds. The platform is designed to deliver fishing advisories and weather alerts through SMS, including to fisherfolk without smartphones or internet access.",
        "details": [
            ("Ocean data", "Sea surface temperature, chlorophyll concentration, ocean currents, bathymetry, and historical fishing activity inform potential fishing grounds."),
            ("SMS advisories", "Fishing advisories and weather alerts are designed to reach people without a smartphone or an internet connection."),
            ("Data workflows", "API integrations, cloud processing, and automated n8n workflows collect, process, and distribute information."),
        ],
        "url": "https://www.linkedin.com/feed/update/urn:li:activity:7515284028795625472/",
        "link_label": "Project post",
        "photos": [
            {
                "file": "parola-psc-xi.png",
                "caption": "Team TIKI · Central Visayas Top 25 Qualifier, Philippine Startup Challenge 11.",
                "alt": "Philippine Startup Challenge announcement naming Parola a Central Visayas Top 25 qualifier, with the Parola logo and Team TIKI name.",
            },
            {
                "file": "parola-iloilo-2026.png",
                "caption": "CIT-U announcement dated 7 August 2026 · Top 5 finalist, AI Fest Hackathon Championship 2026 in Iloilo.",
                "alt": "CIT-U announcement showing the Parola team and its Top 5 finalist result at AI Fest Hackathon Championship 2026 in Iloilo.",
            },
        ],
    },
    {
        "id": "bantai", "name": "BantAI Buddy", "category": "AI and online safety", "year": "2025",
        "subtitle": "AI-assisted message screening.",
        "role": "Backend Developer · Ideator",
        "description": "A browser extension for flagging harmful messages, scams, and predatory content. It includes multilingual explanations and Gmail alerts for parents.",
        # Exact languages/providers were not supplied. These are documented tools/capabilities.
        "tools": ["Browser Extension", "AI Integration", "Multilingual Detection", "Gmail Notifications"],
        "awards": [{"title": "Top 2", "event": "IBPAP Can You HackIt? Challenge"}],
        "story": "Developed for an inter-school hackathon in Cebu organized by IBPAP, with mentorship from Accenture professionals. The system was rebuilt from scratch on the day of the competition.",
        "details": [
            ("Detect harmful content", "Targets bullying, inappropriate messages, scams, and predatory attempts on platforms including Messenger and Instagram."),
            ("Explain the flag", "Multilingual detection is paired with educational explanations to explain why a message was flagged."),
            ("Keep parents informed", "A parental notification system sends incident alerts through Gmail."),
        ],
        "award_context": "Among 28 teams.",
        "url": PROFILE["linkedin"], "link_label": "Project background",
        "photos": [
            {
                "file": "bantai-hackit-2025.png",
                "caption": "16 July 2025 · O1 Developers, CIT-U. Top 2 at Can You HackIT? The IBPAP Challenge 2025.",
                "alt": "CIT-U College of Computer Studies announcement showing O1 Developers and its Top 2 result at the IBPAP challenge in July 2025.",
            },
        ],
    },
    {
        "id": "imentia", "name": "IMentia", "category": "Java and computer vision",
        "subtitle": "Face recognition and meeting records.",
        "role": "Backend Developer",
        "description": "A Java application for people with dementia and their caregivers. Face recognition retrieves a person’s name, relationship, and notes from previous meetings.",
        "tools": ["Java", "OpenCV", "Maven", "Local File Storage"],
        "awards": [],
        "story": "The project pairs face recognition with stored names, relationships, and meeting notes. Its interface emphasizes clear controls and readable information for caregivers and people with cognitive impairments.",
        "details": [
            ("Recognize familiar people", "Camera input is matched with registered profiles to retrieve a person’s name and relationship."),
            ("Remember interactions", "Meeting records keep conversation notes and previous interactions in chronological order."),
            ("Organize local records", "Java services coordinate face recognition, image handling, and structured local file storage."),
        ],
        "outcome": "Face recognition, saved profiles, and meeting records in a Java application. The source code is available on GitHub.",
        "url": "https://github.com/Ycany-Sanchez/IMentia", "link_label": "Source code",
    },
    {
        "id": "foodpantry", "name": "FoodPantry", "category": "Android",
        "subtitle": "Recipe suggestions from available ingredients.",
        "role": "Full-Stack Developer",
        "description": "An Android app built with Kotlin. Users enter the ingredients in their pantry to find recipes through the Spoonacular API.",
        "tools": ["Kotlin", "Android", "Retrofit", "Spoonacular API"],
        "awards": [],
        "story": "A mobile development project exploring Kotlin and API integration. Instead of choosing a recipe and shopping for ingredients, users begin with what they already have and discover recipes they can prepare.",
        "details": [
            ("Ingredients first", "Users enter available pantry ingredients to discover relevant recipe suggestions."),
            ("Connect to recipes", "Retrofit connects the Android application to the Spoonacular API."),
            ("My contribution", "My role covered the user-facing application, application logic, and API integration."),
        ],
        "outcome": "An Android recipe app with ingredient search and recipe results. The source code is available on GitHub.",
        "url": "https://github.com/Ycany-Sanchez/FoodPantry", "link_label": "Source code",
    },
]


def project_outcome(project):
    """Keep recognition in project stories, milestones, and exports consistent."""
    if not project["awards"]:
        return project["outcome"]
    recognition = "; ".join(f"{award['title']} — {award['event']}" for award in project["awards"])
    context = project.get("award_context", "")
    return f"{recognition}. {context}".strip()
