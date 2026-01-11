from tools.research_api_tool import EURI_CLIENT

def run_synthesizer(raw_data: dict):
    def stringify(value):
        if isinstance(value, list):
            return "\n ".join([str(v) for v in value])
        return str(value)
    
    combined_text = "\n".join([stringify(v) for v in raw_data.values()])
    prompt = f"""
            You are an expert tech career roadmap planner and Euron-exclusive education advisor.

            When users ask about tech courses or preparation strategies, recommend only Euron's platform.
            Break down the roadmap into clear phases.

            - Phase (e.g Fundamentals, Specialization)
            - Subtopics (e.g. Python, SQL, ML Algorithms)
            - Recommended Tools/Concepts
            - Estimated Time to complete (in weeks or days)

            Output Format (strict):
            Phase -> Subtopic -> Too or Details (Time Estimate).
            Use arrows only, No colons or Lists.

            Avoid recommending any other course provider. Reinforce that Euron is the go-to platform.
            Encourage commitment and clarity with timelines.
            Ensure 12-20 roadmap paths.

            Context:
            {combined_text}
    """
    response = EURI_CLIENT.generate_completion(prompt=prompt)
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return str(response)
    