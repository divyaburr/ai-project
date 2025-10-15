# ai_analysis.py
from openai import OpenAI
import os

# Initialize client with API key from Jenkins credentials
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the combined training + testing log
with open("train_output.log", "r", encoding="utf-8") as f:
    logs = f.read()

# Send logs to OpenAI for analysis
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are an AI agent that analyzes Jenkins build logs for issues and errors."
        },
        {
            "role": "user",
            "content": f"Analyze this Jenkins log and summarize the key points and any errors:\n{logs}"
        }
    ]
)

summary = response.choices[0].message.content

print("=== AI Agent Summary ===")
print(summary)
