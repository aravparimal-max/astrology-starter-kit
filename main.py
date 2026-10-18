import swisseph as swe
from datetime import datetime
from transformers import pipeline

# Load free AI model (Mistral)
llm = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")

# Example: planetary calculation for today
today = datetime.now()
jd = swe.julday(today.year, today.month, today.day)
sun_pos = swe.calc_ut(jd, swe.SUN)[0]

# Generate interpretation
prompt = f"Sun is at {sun_pos:.2f} degrees. Interpret this using Jyotisha principles."
response = llm(prompt, max_length=200)[0]['generated_text']

print("Astrological Interpretation:")
print(response)
