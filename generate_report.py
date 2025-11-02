from openai import OpenAI
from config import OPENAI_API_KEY, INDUSTRY, BRAND, OUTPUT_FILE

# Instantiate OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_strategy_report():
    prompt = f"""
You are a market research analyst. Generate a mini strategy report for {BRAND} in the {INDUSTRY} industry. Include:
1. Key competitors and positioning
2. Top 3 customer pain points or trends
3. 3 actionable strategy recommendations
Make it 2-3 pages long, professional, and concise.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=1000
    )

    # Extract the generated text
    report_text = response.choices[0].message.content.strip()

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"Strategy report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_strategy_report()