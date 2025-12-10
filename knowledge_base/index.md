# 🗄️ SolarPunk Mandala Knowledge Base Index

This directory serves as the **Systemic Archetype Library** for the SolarPunk Mandala project. It contains all structured, foundational data, taxonomies, and content templates that ground the automated processes (AI Tools) and provide the philosophical context for the entire system.

The AI Logic Engine, located in the `/tools/` directory, references the files here to ensure all generated outputs are consistent, accurate, and aligned with the Mandala's core ontology.

---

## 1. Foundational Taxonomies (The Archetypes)

These CSV files contain the relational databases that define the core components of the Mandala. These are primarily read by AI models to map concepts, generate narratives, and structure projects.

| File | Description | Purpose / Reference Usage |
| :--- | :--- | :--- |
| [`mandala_rhizomes_archetypes.csv`](./mandala_rhizomes_archetypes.csv) | The master list of systemic archetypes, cross-referenced with SDGs, UDHR, and the Green New Deal. | **Project Grounding:** Used to link any new initiative to foundational global frameworks. |
| [`mandala_meta_narratives.csv`](./mandala_meta_narratives.csv) | Definitions and analysis of the **Necrocene** (Pathology) and **Symbiotic** (Solution) meta-narratives. | **Diagnostic Tool:** Used by AI models (Qwen/Deepseek) for systemic analysis and partial diagnosis (e.g., *The Sclerosis Trap*). |
| [`mandala_research_circles.csv`](./mandala_research_circles.csv) | The master list of all Research Circles, including core domains, pods, protocols, and key commons. | **Organizational Map:** Used to ensure internal system coherence and assign projects to the correct working group. |

---

## 2. Structural Documentation (Human/LLM Readable)

This subdirectory contains Markdown documentation detailing complex systemic components, making the information transparent for collaborators and easy for LLM-based tools to parse specific sections.

### Subdirectory: [`/circles/`](./circles/)

Contains dedicated Markdown files for each Research Circle, based on the data in `mandala_research_circles.csv`.

| Example File | Content Focus | Utility |
| :--- | :--- | :--- |
| [`accounting-and-regulation.md`](./circles/accounting-and-regulation.md) | Pod Mandate, Core Roles, Critical Protocol (e.g., The Integrity Check Protocol). | **Governance and Execution:** Provides the AI with the complete operational scope of a Research Circle. |
| [`beliefs-and-ideas.md`](./circles/beliefs-and-ideas.md) | Commons structure (e.g., Collective Mind Commons), and Key Artifacts. | **Knowledge Management:** Used by the AI to define where to source or deposit high-level philosophical artifacts. |

---

## 3. CMS Content Templates (AI-Driven Content Generation)

This subdirectory contains structural templates used by AI models (like Qwen, Deepseek, or Gemini) to ensure all generated content meets the exact field requirements for import into the Webflow/Airtable CMS.

### Subdirectory: [`/templates/`](./templates/)

| Template File | Output Type | Source CMS Collection |
| :--- | :--- | :--- |
| [`blog_post_cms_template.md`](./templates/blog_post_cms_template.md) | Structured Blog Post Content | **🧩 Blog Posts** (Requires fields like `Post Body` in Rich Text/HTML format) |
| [`food_recipe_cms_template.md`](./templates/food_recipe_cms_template.md) | Structured Food Recipe Content | **🍲 Food Recipes** (Requires detailed fields like `🍲 Ingredients` and `🍲 Recipe Instructions`) |

---

**Navigational Principle:**

1.  **If you need to know *what* a concept is or *how* it relates to others:** Check the **Foundational Taxonomies** (CSVs).
2.  **If you need the full mandate or protocol for a Research Circle:** Check the **Structural Documentation** (`/circles/`).
3.  **If you are generating new content for the website:** Reference the **CMS Content Templates** (`/templates/`).
