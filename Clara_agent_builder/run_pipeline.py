import os
import json

from scripts.llm_extract import extract_with_llm
from scripts.generate_agent import generate_agent_spec

DEMO_DIR = "transcripts/demo"
OUTPUT_DIR = "outputs"

print("Looking for transcripts in:", DEMO_DIR)

if not os.path.exists(DEMO_DIR):
    print("Demo folder not found.")
    exit()

files = os.listdir(DEMO_DIR)

print("Files found:", files)

for file in files:

    if not file.endswith(".txt"):
        continue

    print("Processing transcript:", file)

    account_id = file.replace(".txt", "")

    with open(os.path.join(DEMO_DIR, file)) as f:
        transcript = f.read()

    memo = extract_with_llm(transcript, account_id)

    agent = generate_agent_spec(memo, "v1")

    path = os.path.join(OUTPUT_DIR, account_id)

    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "memo.json"), "w") as f:
        json.dump(memo, f, indent=2)

    with open(os.path.join(path, "agent.json"), "w") as f:
        json.dump(agent, f, indent=2)

    print("Created output for:", account_id)

print("Pipeline finished.")
