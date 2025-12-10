# Blog Post CMS Content Template (Webflow/Airtable Format)

## Purpose
This template defines the exact field structure and expected content for a new blog post entry to be imported into the CMS. The final output must be machine-readable, ideally in CSV or structured JSON format.

## Required Fields (CSV Header Order)

| Field Name | Data Type | Purpose | Notes |
| :--- | :--- | :--- | :--- |
| **Name** | String | The title of the blog post. | Must be unique and engaging. |
| **Slug** | String | The URL slug (used as the filename). | Must be all lowercase, hyphenated (e.g., `the-great-solarpunk-garden`). |
| **Collection ID** | String | CMS system ID. | Leave blank or use a placeholder value (e.g., `PENDING`). |
| **Item ID** | String | CMS item ID. | Leave blank or use a placeholder value (e.g., `PENDING`). |
| **Archived** | Boolean | Status flag. | Default: `False`. |
| **Draft** | Boolean | Status flag. | Default: `True` (for new content). |
| **Created On / Updated On / Published On** | Date/String | Timestamps. | Leave blank or use current date/time string. |
| **🪘 Category** | String | Primary content topic. | Example: `🎋 Sustainability Research`, `🌿 Regeneration Practice`. |
| **🔮 Cicles Category** | String | Link to the Mandala Research Circles. | Must be a slug from the `/knowledge_base/mandala_research_circles.csv` file. |
| **Blog Date** | Date/String | The publish date. | Use current date/time string. |
| **Post Body** | Rich Text (HTML/Markdown) | The full body content. | Must use HTML paragraph tags (`<p>`) or Markdown for formatting. |
| **Post Summary** | String | A brief, engaging summary. | Max 160 characters for SEO. |
| **Main Image** | URL | URL of the primary hero image. | Leave blank or use a placeholder URL. |
| **Thumbnail image** | URL | URL of the thumbnail image. | Leave blank or use a placeholder URL. |
| **Featured?** | Boolean | Featured status. | Default: `False`. |
