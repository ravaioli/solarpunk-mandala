# Data Synthesis Cheatsheet: From Raw Data to Scores

## Purpose & Workflow

This cheatsheet provides the step-by-step process for the **Visual Steward** (or whoever is synthesizing data) to turn the collected quantitative (Q) and qualitative (Ql) data into the five **Domain Scores** and the **Alpha (α) Coefficient**. Follow this sequence.

---

## Step 1: Gather Your Inputs

You should have:
1.  **Q Data:** Numbers from Domain Stewards for each capital's metric (e.g., "Soil % = 5.2", "Trees Planted = 12").
2.  **Ql Data:** The community's averaged scores (1-5 scale) for each capital from the qualitative poll.

## Step 2: Normalize All Data to a 1-10 Scale

All scores must be converted to a common 1-10 scale for calculation.

### A) Normalizing Q Data (Quantitative Metrics)
For each Q metric, use its specific formula from the [MVP Scorecards](../../dashboard-mvp/03-mvp-scorecards.md). The general principle is:
`Q_normalized = (Actual_Value / Target_Value) * 10`, **capped at 10**.

**Example: Regenerative Capital (Soil Organic Matter %)**
- *Target:* >5% is considered thriving (score of 10).
- *Formula:* `Q_norm = min((Soil_Percentage / 5) * 10, 10)`
- *If soil is 5.2%:* `min((5.2 / 5) * 10, 10) = min(10.4, 10) = 10`

**Example: Convivial Capital (Avg. Work Hours) - INVERSE METRIC**
- *Target:* <20 hours per week is high conviviality (score of 10).
- *Formula:* `Q_norm = min(((40 - Actual_Hours) / (40 - 20)) * 10, 10)` *[Assumes 40 as a max baseline]*
- *If avg. work is 35 hours:* `min(((40-35) / 20) * 10, 10) = min((5/20)*10, 10) = 2.5`

### B) Normalizing Ql Data (Poll Averages)
This is straightforward. The poll provides averages on a 1-5 scale.
`Ql_normalized = (Poll_Average_Score / 5) * 10`

**Example:** If the poll average for "Relational Capital" is 4.2 (on the 1-5 scale):
`Ql_norm = (4.2 / 5) * 10 = 8.4`

## Step 3: Calculate the 20 Capital Scores

For each of the 20 capitals:
`Capital_Score = (Q_normalized + Ql_normalized) / 2`

**Example for Regenerative Capital:**
- Q_norm (from soil): 10
- Ql_norm (from poll): 8.4
- **Capital_Score = (10 + 8.4) / 2 = 9.2**

## Step 4: Calculate the 5 Domain Scores

For each of the five domains (Politics, Economics, Culture, Ecology, Spirituality):
`Domain_Score = Average(Capital_1_Score, Capital_2_Score, Capital_3_Score, Capital_4_Score)`

**Example for Ecology Domain (with sample scores):**
- Regenerative Capital: 9.2
- Adaptive Capital: 7.5
- Biophilic Capital: 6.8
- Stewardship Capital: 8.0
- **Ecology Domain Score = (9.2 + 7.5 + 6.8 + 8.0) / 4 = 7.875**

**🔹 Output:** You should now have **five Domain Scores**, each a number between 1 and 10.

## Step 5: Calculate the Alpha (α) Coefficient

Use the five Domain Scores in this formula:
`α = (F / F_max) * B`

**A) Calculate F (Area of Your Regeneration Flower):**
1.  Plot your five Domain Scores as points on the axes of a pentagon or hexagon (in order: Politics, Economics, Culture, Ecology, Spirituality).
2.  Use an online "polygon area calculator" or the formula for the area of an irregular pentagon. *(As a simplification for MVP, you can use a radar chart tool that outputs area)*.
3.  **Simplified Approximation:** If using a regular pentagon with side length derived from scores, a rough area can be calculated. For now, using a visualization tool that calculates area is best.

**B) Calculate F_max (Maximum Possible Area):**
- This is the area if all five Domain Scores were 10. Use the same method as above with scores of [10, 10, 10, 10, 10].

**C) Determine B (Balance Penalty):**
1.  Calculate the **standard deviation** of your five Domain Scores.
    - Use a spreadsheet: `=STDEV.P(range_of_5_scores)`
2.  Apply the penalty:
    - If standard deviation **> 2.0**, set **B = 0.8**
    - If standard deviation **between 1.0 and 2.0**, set **B = 0.9**
    - If standard deviation **< 1.0**, set **B = 1.0**

**D) Final Calculation:**
`α = ( Your_Flower_Area / Max_Possible_Area ) * Balance_Penalty`

**Interpretation:**
- **α < 0.3:** Proto-System. Focus on foundations.
- **0.3 ≤ α < 0.7:** Differentiating System. Focus on integration.
- **α ≥ 0.7:** Integrated System. Focus on wisdom & balance.

---

**Your output for Week 2 is:** Five Domain Scores, one Alpha Coefficient, and a visualization of the Flower (see `visualization-guide.md`).
