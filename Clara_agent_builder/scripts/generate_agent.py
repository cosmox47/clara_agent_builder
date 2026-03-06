from scripts.prompt_builder import build_prompt

def generate_agent_spec(memo, version):

    prompt = build_prompt(memo)

    agent = {
        "agent_name": "Clara Agent",
        "version": version,
        "system_prompt": prompt
    }

    return agent