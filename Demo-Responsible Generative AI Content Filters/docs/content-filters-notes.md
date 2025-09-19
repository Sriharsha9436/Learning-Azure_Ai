# Notes on Custom Content Filters

## 🔹 Key Learnings
- Default filters are already enabled in Azure AI Foundry.
- Sensitivity levels can be **customized** (Low, Medium, High) for each category.
- The system logs flagged prompts and responses for review and traceability.
- After applying filters, harmful prompts returned **safe, controlled responses**.

---

## 🔹 Four-Stage Process for Responsible AI with Generative Models

1. **Map**  
   Identify potential harms that may arise from the solution.  
   Example: bias, offensive content, or misuse of generated text.

2. **Measure**  
   Assess and test the outputs of the generative model to detect the presence of these harms.  
   Example: prompt testing for hate speech, violence, or unsafe suggestions.

3. **Mitigate**  
   Apply safeguards at multiple layers (data, model, content filters, UI) to minimize risks and clearly communicate potential limitations to users.  
   Example: using **Azure AI content filters** with different sensitivity levels.

4. **Manage**  
   Ensure long-term responsible usage by defining operational readiness, monitoring in production, and updating safeguards as risks evolve.  
   Example: periodic review of logs, refining filter settings, and compliance checks.

---

## ✅ Conclusion
By applying custom content filters and following the four-stage Responsible AI framework (Map, Measure, Mitigate, Manage), we can ensure safer and more reliable generative AI solutions in Azure AI Foundry.
