# Embodied Foundation Assessor: Personalized Learning Pallet

**Goal:** Generate a personalized 7-day action plan, journal prompts, and learning pallet based on a user's self-reported Foundation Stability scores (N, C, R, M).

## 1. Universal AI Handoff Specification

[MANDALA CONTEXT]
* **Framework Version:** SolarPunk Mandala v3.0
* **Core Logic:** Focus entirely on **0D (Point Identity)** stabilization. The output is a personalized "First-Aid" plan.
* **Score Constraint:** The action plan must be weighted toward the **lowest** reported score.
* **Tool Focus:** Gemini is preferred for generating clear, daily, and motivational instructions.

## 2. Primary Task for Assessor (Gemini)

**Input:**
1.  **User's N/C/R/M Scores:** [User Input: e.g., N=4, C=2, R=1, M=3]
2.  **Current Stressor:** [User Input: Brief description of the immediate issue, e.g., "Burnout from too many meetings."]

**Action:**
1.  **Diagnosis:** Identify the single weakest Foundation.
2.  **Generate Plan:** Create a 7-day schedule with a specific **Ritual** and **Journal Prompt** for each day, focusing on the weakest foundation.

## 3. Mandatory Output Structure (Rich Text for Journal/App)

Generate a rich text output that begins with the diagnosis and then lists the 7-Day Plan:

1.  **Foundation Diagnosis:** [State the weakest foundation and its likely effect on the user's 0D stability.]
2.  **The 7-Day Stabilization Pallet:** (Must focus on one N/C/R/M foundation)
    * **Day 1: The Anchor:** [Simple physical somatic action, 5 minutes.]
    * **Day 2: The Inquiry:** [Journal prompt focused on **Dissociation** related to the foundation.]
    * **Day 3: The Policy Shift:** [Recommendation for one small, immediate governance change in the user's life (e.g., "No phone use after 9 PM").]
    * **Day 4-7: (The Practice):** [Continuation of practice with new prompts.]
