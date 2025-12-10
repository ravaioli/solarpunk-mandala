# Food Recipe CMS Content Template (Webflow/Airtable Format)

## Purpose
This template defines the exact field structure and expected content for a new food recipe entry to be imported into the CMS. The final output must be machine-readable, ideally in CSV or structured JSON format.

## Required Fields (CSV Header Order)

| Field Name | Data Type | Purpose | Notes |
| :--- | :--- | :--- | :--- |
| **Name** | String | The recipe name. | Must be unique. |
| **Slug** | String | The URL slug. | Must be all lowercase, hyphenated (e.g., `lentil-dahl-caribbean-style`). |
| **Collection ID / Item ID / Archived / Draft / Created On / Updated On / Published On** | System | System fields. | Leave blank or use placeholder values (`PENDING`, `False`, `True`, etc.). |
| **🗺️ Country of Origin** | String | Primary cultural origin. | Example: `🇬🇾 Guyana`, `🇮🇳 India`. |
| **Regional Cuisine** | String | Specific regional style. | Example: `Carribean`, `West African`. |
| **Food Group** | String | Main ingredient type. | Example: `Vegetables`, `Grains`. |
| **🍽️ Meal Time** | String | Suggested serving time. | Example: `Lunch`, `Dinner`, `Dessert`. |
| **🍽️ Serving Amount** | Number | Number of servings. | |
| **Preparation Time** | Number | Minutes required for preparation. | |
| **Cook Time** | Number | Minutes required for cooking. | |
| **🍲 Background** | Rich Text (HTML/Markdown) | Context, history, or personal story of the recipe. | Must use HTML paragraph tags (`<p>`) or Markdown for formatting. |
| **🍲 Ingredients** | Rich Text (HTML/Markdown) | Detailed, formatted ingredient list. | Use HTML unordered lists (`<ul>`) with `<h4>` titles for groups (e.g., `<h4>Veggies</h4>`). |
| **🍲 Recipe Instructions** | Rich Text (HTML/Markdown) | Step-by-step instructions. | Use HTML ordered lists (`<ol>`) with `<h4>` titles for phases (e.g., `<h4>Cook Aromatics</h4>`). |
| **🍲 Storage Instructions / 🍲 Recipe FAQs** | Rich Text (HTML/Markdown) | Additional practical notes. | Can be left blank if not applicable. |
| **🔪 Kitchenware** | String | List of required tools. | |
| **Spotify Song Embed Code / 🍲 Related Recipes / Recipe Image / Video Link** | String/URL | Media and reference fields. | Leave blank or use placeholder data. |
| **Featured Recipe** | Boolean | Featured status. | Default: `False`. |
