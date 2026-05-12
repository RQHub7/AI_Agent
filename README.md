## AI AGENT Project
### The Agent
* Built an agent that can read, write and execute python files in a specified directory to solve a task within a tight agentic feedback loop, currently 20 iterations. This project was built with the intention of furthering my understanding of AI agents and their usefulness. **See the Security & Limitations section below**. This was a guided Boot.Dev project.
***
### What Does this Agent Do?
1. Accepts a coding task within the project's directory (debug or adds a small new feature if your okay with that)
2. Chooses from 4 defined functions to work on the task (based on the task provided on run)
    * Scan the files in a directory 
    * Read a file's contents 
    * Overwrite a file's contents 
    * Execute the Python interpreter on a file 
3. Carries out different functions up to 20 times in order to complete the task 
***
### Security & Limitations
This agent has some security guardrails to limit what files it looks over, but was not built to be production ready.  
<u>Current guardrails</u>
* Path checks restricting file access to be within the working directory
    * Enforced in the call_function() & each function in the functions directory *(see the Project Skeleton)*
* A 30 second timeout on script execution  

For real world or public use, the code execution should run within an isolated environment such as a Docker Container w/ no network access & strict resource limits, or a virtual machine. This is a potential future improvement to my project.

***
### Project Skeleton
* System Prompt - tone setting message for the conversation w/ an LLM AI API (prompts.py)
    * Provides context for the conversation
    * Sets the "rules" for the conversation
    * Gives instructions on how to behave
    * Sets the personality of the AI
***
1. >running main calls main() 
1. >main() calls generate_content() 
    - finds the api_key which is hosted in a seperate ignored file stored to the variable being fetched through os.environ.get()
    - sets up the parser using **argparse** - seperate from genai
        - arguments added (user prompt and verbose(enables details))
            - user prompt is whats called after running the file and generates the conversation stored in messages
    - stores the user prompt and caries this to other functions in a sense by calling generate_content(client, messages, verbose check)

1. >generate_content() calls call_function()
    - generate_content is the main's helper function that really does the heavy lifting
    - generate_content is where the agentic loop lives
    - generate_content

1. >call_function() has a function map and calls a function within this map
    - each function defined in it's own file and has a declaration describing use and functionality for the llm powered agent to keep in mind as it assesses the task when creating a plan.
        - ***the declarations help guide the conversation.*** 
    - call_function() stores the relative path from the project directory. This is fed into all function calls and overwrites any directory if provided via args in said function call. It is one of the guardrails to keep the AI Agent in the project directory. 

1. >these functions are called by the agent to find a solution to the initial prompt provided 
    - has to follow rules provided in **system prompt**
***
### Dependencies
*This project is hosted with the uv manager in a venv*

* Google AI Studio account w/ a billing account for significant usage
    * google-genai==1.12.1
        * types
    * model="gemini-2.5-flash"
    * a newly created api key placed in your ignored .env file storing the the key as `GEMINI_API_KEY=<insert_key_here>`
    * note: the gemini llm api can be very busy at times, hampering usage

* A Virtual Environment & .env 
    * python-dotenv==1.1.0
        * used to load the specified .env and reference **your** api key
    * uv handles creation of the virtual environment or venv
***
### Usage Examples
* basic calc one
    1. insert a bug within calculator.py
    1. Run the agent with command explaining the bug or incorrect functionality and the task to fix this bug
 
  
https://github.com/user-attachments/assets/373def0d-8e9a-4a28-b0a2-a9d06a8012b8

* Outside project example usage
    1. copying the outside project directory to the AI_Agent directory & environment  
    1. updating the system prompt to fit the task at hand
    1. updating the working_directory variable to the newly added outside project subdir
    1. run with a command asking for a new feature with specifications. `uv run main.py "task at hand"`

https://github.com/user-attachments/assets/02e7c16e-c20d-44d9-a0ea-416717588609



Asteroids Before:



https://github.com/user-attachments/assets/7aff2f47-72be-4189-8dc8-71fc0c1ebd42





Asteroids After:



https://github.com/user-attachments/assets/bd96fc30-1f3a-4eb7-b504-65cf05aa224f




Note: See [Asteroids repo](https://github.com/RQHub7/Asteroids) for the Agentic made "feature: Asteroid-Asteroid Collision"

