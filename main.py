import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

def generate_content(client, messages, verbose=None):
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            ),
        )
    if response.usage_metadata == None:
        raise RuntimeError("API request likely failed. No usage metadata found")
    if verbose == True:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for call in response.function_calls:
            function_call_result = call_function(call, verbose)
            if not function_call_result.parts:
                raise Exception(f"{call.name} part not found")
            if function_call_result.parts[0] == None:
                raise Exception(f"{call.name} .function_response is unexpectedly 'None'")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception(f"{call.name} .function_response.response is unexpectedly 'None'")
            function_results = []
            function_results.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    else:
        print(response.text)

        



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

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])] # essentially the chatbot conversation as of now.
    client = genai.Client(api_key=api_key) # gemini api LLM is the client
    detailed = args.verbose # specifiable option on call ( uv run main.py "What is the meaning of life?" --verbose )

    generate_content(client, messages, detailed)

if __name__ == "__main__":
    main()
