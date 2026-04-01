from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------
# Personas and Prompt Types
# -------------------------
personas = [
    "pcp",
    "diagnostic_specialist",
    "evidence_based_researcher",
    "patient_safety_qa_lead",
    "care_coordinator",
    "documentation_assistant",
    "risk_management_analyst",
    "health_educator",
    "empathetic_health_coach"
]

prompt_types = [
    "zero_shot",
    "few_shot",
    "chain_of_thought",
    "tree_of_thoughts",
    "chain_of_verification",
    "self_consistency",
    "role_prompting",
    "re2",
    "rag"
]

# -------------------------
# Load and prepare prompts
# -------------------------
def load_prompt(persona: str, prompt_type: str) -> str:
    path = f"clinical_prompt_library/{persona}/{prompt_type}.txt"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r") as f:
        return f.read()

def prepare_prompt(prompt: str, patient_data: str, additional_context: str = "") -> str:
    prompt = prompt.replace("<INSERT_PATIENT_DATA>", patient_data)
    if additional_context:
        prompt += f"\n\nReference Data:\n{additional_context}"
    return prompt

def generate_response(prompt: str, model: str = "gpt-4") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for healthcare."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def self_consistent_response(prompt: str, n: int = 3) -> str:
    outputs = [generate_response(prompt) for _ in range(n)]
    output_counts = {o: outputs.count(o) for o in outputs}
    best = max(output_counts, key=output_counts.get)
    return best

def tree_of_thoughts(prompt: str, branches: int = 3) -> str:
    thoughts = []
    for i in range(branches):
        branch_prompt = f"{prompt}\n\nThink step-by-step path {i+1}:"
        thoughts.append(generate_response(branch_prompt))
    final_prompt = "Summarize the best reasoning path from the following:\n" + "\n---\n".join(thoughts)
    return generate_response(final_prompt)

def rag_response(prompt: str, reference_docs: list) -> str:
    reference_text = "\n\n".join(reference_docs)
    full_prompt = prepare_prompt(prompt, patient_data="", additional_context=reference_text)
    return generate_response(full_prompt)

def batch_workflow(personas, prompt_types, patient_data, reference_docs=None):
    all_results = {}
    for persona in personas:
        all_results[persona] = {}
        for prompt_type in prompt_types:
            try:
                prompt = load_prompt(persona, prompt_type)
                prompt = prepare_prompt(prompt, patient_data, additional_context="\n".join(reference_docs) if reference_docs else "")
                
                if prompt_type == "self_consistency":
                    output = self_consistent_response(prompt, n=3)
                elif prompt_type == "tree_of_thoughts":
                    output = tree_of_thoughts(prompt, branches=3)
                elif prompt_type == "rag":
                    output = rag_response(prompt, reference_docs or [])
                else:
                    output = generate_response(prompt)
                
                all_results[persona][prompt_type] = output
            except FileNotFoundError as e:
                print(e)
    return all_results

if __name__ == "__main__":
    patient_data = """
    Name: John Doe
    Age: 65
    Conditions: Type 2 Diabetes, Hypertension
    Latest Labs: A1C 8.2%, BP 150/95
    Medications: Metformin, Lisinopril
    """
    
    reference_docs = [
        "ADA 2024 Guidelines for Type 2 Diabetes Management",
        "Hypertension Clinical Practice Guidelines 2023"
    ]
    
    results = batch_workflow(personas, prompt_types, patient_data, reference_docs)
    
    for persona, prompts in results.items():
        for prompt_type, output in prompts.items():
            print(f"\n=== {persona} | {prompt_type} ===\n{output}\n{'-'*80}")
