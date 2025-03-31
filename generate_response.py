import os
import re
from google import generativeai as genai

# Set the API key
# the random_test.txt file should contain the API key
# Make sure to replace the API key with your own
# an API key should never be public for safety reasons
with open("random_test.txt", "r") as f:
    api_key_text = f.read().strip()
genai.configure(api_key = api_key_text)

def load_parsed_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
def generate_outreach_email(profile_data):
    prompt = f"""
    Based on the following LinkedIn profile data, generate a personalized, professional outreach email.
    Be concise, friendly, and tailor the message to the individual's background. Include a hook and a call to action.
    I'd also like it to just be a message, not a full email. There will be no email signature (no name, company, or contact info).
    Make sure I do not have to fill anything in, and it is ready to send.
    Profile Data:
    {profile_data}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def indent_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    indented = "\n".join(f"    {s.strip()}" for s in sentences if s.strip())
    return indented


if __name__ == "__main__":
    filename = input("Enter the filename of the parsed LinkedIn profile text file: ").strip()

    if not os.path.exists(filename):
        print("Error: File not found")
        exit()

    profile_data = load_parsed_data(filename)
    email = generate_outreach_email(profile_data)
    formatted_email = indent_sentences(email)

    base_name = os.path.splitext(filename)[0]
    output_file = f"{base_name}_email.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted_email)

    