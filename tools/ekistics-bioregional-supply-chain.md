# Ekistics Bioregional Supply Chain Mapper

**Goal:** Analyze a physical project's resource needs through the **Nourishment** Foundation, generating a structured, data-ready CSV list for bioregional sourcing.

## 1. Universal AI Handoff Specification

[MANDALA CONTEXT]
* **Framework Version:** SolarPunk Mandala v3.0
* **Core Logic:** Ekistics (Shells) and **Nourishment** Foundation (Resource Inflow).
* **Output Constraint:** Output must be a **CSV** table suitable for import into Google Sheets.
* **Tool Focus:** Gemini is preferred for CSV generation and data workflow design.

## 2. Primary Task for Supply Chain Mapper (Gemini)

**Input:**
1.  **Physical Project:** [User Input: e.g., "100 sq ft Modular Community Kitchen"]
2.  **Key Resource Categories:** [User Input: e.g., "Wood," "Ceramics," "Local Produce"]
3.  **Estimated Scale:** [User Input: e.g., "Small/Medium/Large"]

**Action:**
1.  **Nourishment Assessment:** Analyze the project's resource list, focusing on low-energy, circular metabolism sourcing.
2.  **Generate Sourcing Data:** Create the CSV output block with the required fields.

## 3. Mandatory CSV Output Structure (Google Sheets Ready)

Generate a clean CSV block using the following field headers, listing five potential resource needs for the input project:

| CSV Field | Description |
| :--- | :--- |
| **Resource Item** | The specific material or input (e.g., Pine Lumber, Solar Panel). |
| **Quantity/Scale** | The estimated quantity needed (e.g., 20 boards, 4 units). |
| **Foundation Link** | Always: **Nourishment (Inflow)** |
| **Sourcing Locality (Bioregion)** | Suggested local source type (e.g., 'Local Wood Mill within 50 miles', 'Community Farm'). |
| **Circulation Status** | Status regarding the Cleansing foundation (e.g., 'Fully Recyclable', 'Compostable', 'End-of-life Waste'). |
| **ClickUp Task Link** | Placeholder for follow-up action: **[LINK TO CLICKUP TASK]** |
