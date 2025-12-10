# Workspace Integration Engine: Schedule & Link Protocol

**Goal:** Automate the creation of structured data required for scheduling, project management, and cross-platform publishing, ensuring **SolarPunkSangha.com** is the canonical, single point of promotion.

## 1. Universal AI Handoff Specification

[MANDALA CONTEXT]
* **Framework Version:** SolarPunk Mandala v3.0
* **Core Logic:** System 2 (Coordination). Ensure content is ready for seamless transfer between scheduling and project management tools.
* **Canonical URL:** **MUST** integrate the **SolarPunkSangha.com** URL for all Call-to-Actions and links.
* **Tool Focus:** Gemini is preferred for its superior integration and output structure compatibility with Google Workspace (Sheets, Docs) and ClickUp tasks.

## 2. Primary Task for Integration Engine (Gemini)

**Input:**
1.  **Source Content:** [Paste the desired social media/blog post text from a previous generation (e.g., the 4-Part Narrative from the Social Media Generator).]
2.  **Target Platform:** [Specify: Instagram, LinkedIn, Blog Post]
3.  **Content Owner/Approver:** [User Input: e.g., "Gaia/VSM System 5"]

**Action:**
1.  **Generate Structured CSV:** Create a **CSV (Comma Separated Values)** output block containing the necessary fields for scheduling tools (like a Google Sheet content calendar) and ClickUp task creation.
2.  **Generate ClickUp Task Description:** Create a rich text description ready for a ClickUp task, ensuring all links use the Canonical URL.

## 3. Mandatory CSV Output Structure (For Scheduling/Google Sheets)

Generate a clean CSV block using the following fields. Note the use of the Canonical URL in the CTA Link:

| CSV Field | Description | Content Constraint |
| :--- | :--- | :--- |
| **Task Name** | The name of the scheduling task. | Must include the **Target Platform** and the **Source Content Title**. |
| **Publish Date** | The suggested publication date. | Use a placeholder: **[YYYY-MM-DD]** |
| **Content Body** | The full, formatted content ready for the platform. | Paste the full text input from the Source Content. |
| **Platform** | The target social platform. | Use the Target Platform input. |
| **Approval Status** | The initial approval state. | Default to: **Needs Review** |
| **Project** | The associated project name. | Default to: **Hype: Hearts & Minds** |
| **CTA Link** | The single, universal call-to-action link. | **MUST** be: `https://SolarPunkSangha.com/[slug-for-course]` |
| **Owner** | The person responsible for publishing. | Use the Content Owner/Approver input. |

## 4. Mandatory ClickUp Task Description Output Structure

Create a rich text block suitable for a ClickUp task description field. This ensures all context is available to the publisher:

* **Header:** `[Target Platform] Content: [Source Content Title]`
* **Body:** Paste the full **Content Body** here.
* **Checklist (Pre-Flight):**
    * [ ] Verify Foundation Stability of source course content.
    * [ ] Confirm publish date: [YYYY-MM-DD]
    * [ ] **Crucial:** Verify all links point to **SolarPunkSangha.com**.
* **Final Link:** The canonical CTA link: `https://SolarPunkSangha.com/[slug-for-course]`

## 5. Final Constraint

The output **MUST** consist of two separate, complete blocks: the CSV table and the ClickUp Task Description. Do not include any other explanatory text.
