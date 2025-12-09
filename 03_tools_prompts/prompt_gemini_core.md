# High-Value Prompts (Gemini / GPT)

Purpose
- Store, refine, and version prompts that reliably produce high-value outputs for the project.

Prompt pattern: "Design brief + constraints + examples + format"
Example prompt
```
Design a mandala-based motif inspired by solarpunk aesthetics. Constraints:
- Color palette: warm green (#6B8E23), soft gold (#D4AF37), terracotta accent (#C04E3E)
- Output: a short description (3 sentences) + 4 bullet variations with color and shape guidance
- Tone: hopeful, community-centered, eco-technical
Provide JSON with keys: title, description, variations (array of {name, palette, shapeNotes})
```

Prompt-editing tips
- Keep a “system” or context block that includes canonical definitions from /01_core_model.
- Record seed outputs and a short rubric for acceptance.
