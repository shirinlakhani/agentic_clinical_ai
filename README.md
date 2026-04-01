# Agentic Clinical AI

## Overview
**Agentic Clinical AI** is a Python-based framework for building multi-persona, reusable prompt libraries to guide AI in clinical workflows. It supports high-stakes medical decision-making, patient engagement, and administrative efficiency by leveraging structured prompt templates and agentic workflows.

This project demonstrates:

- Designing reusable prompts for various clinical personas.
- Using prompt engineering techniques such as Zero-Shot, Few-Shot, Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), Self-Consistency, Role Prompting, RE2, and Retrieval-Augmented Generation (RAG).
- Integrating these prompts into agentic AI workflows using Python.

---

## Folder Structure

\`\`\`text
agentic_clinical_ai/
│
├─ clinical_prompt_library/           # Contains all persona-specific prompts
│   ├─ pcp/
│   │   ├─ zero_shot.txt
│   │   ├─ few_shot.txt
│   │   └─ ...
│   ├─ diagnostic_specialist/
│   ├─ evidence_based_researcher/
│   ├─ patient_safety_qa_lead/
│   ├─ care_coordinator/
│   ├─ documentation_assistant/
│   ├─ risk_management_analyst/
│   ├─ health_educator/
│   └─ empathetic_health_coach/
│
└─ agentic_clinical_workflow.py      # Python script to run agentic workflows
\`\`\`

---

## Features

- **Multi-Persona Prompt Library:** Includes PCP, Diagnostic Specialist, Evidence-Based Researcher, Patient Safety QA Lead, Care Coordinator, Documentation Assistant, Risk Management Analyst, Health Educator, and Empathetic Health Coach.  
- **Prompt Styles:** Zero-Shot, Few-Shot, Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), Chain-of-Verification (CoVe), Self-Consistency, R- **Prompt StyleE2, Retrieval-Augmented Generation (RAG).  
- **Agentic Workflows:** Automates multi-step reasoning and decision-making processes for clinical AI applications.  
- **Structured Output:** Encourages consistent, reliable, and interpretable AI outputs for clinical decision support.  

---

## Getting Started

1. **Clone the repository**
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/agentic_clinical_ai.git
cd agentic_clinical_ai
\`\`\`

2. **Install Python dependencies** (if any)
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. **Run the agentic workflow**
\`\`\`bash
python agentic_clinical_workflow.py
\`\`\`

4. **Add or update prompts**
- Add new personas or prompt types under \`clinical_prompt_library/\`.
- Follow the placeholder and template format for reusability.

---

## Future Enhancements

- Integration with live LLM APIs (OpenAI GPT, Ollama, Anthropic Claude).  
- Expand to other healthcare domains and administrative workflows.  
- Automate evaluation of AI outputs for accuracy, tone, and relevance.

---

## License
MIT License

---

## Author
Shirin Lakhani  
[LinkedIn](https://www.linkedin.com/in/shirin-lakhani786) | [GitHub](https://github.com/shirinlakhani)
