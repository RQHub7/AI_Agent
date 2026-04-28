import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

def generate_content(client, messages, detailed=None):
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages
        )

    if response.usage_metadata != None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        raise RuntimeError("API request likely failed. No usage metadata found")
    return


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No key found. Check the api_key again")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now accessible: `args.user_prompt`

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])] # essentially the chatbot conversation as of now.
    client = genai.Client(api_key=api_key) #gemini api LLM is the client
    detailed = args.verbose

    generate_content(client, messages, detailed)

if __name__ == "__main__":
    main()
