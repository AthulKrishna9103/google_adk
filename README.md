# Voice News Agent using Google ADK

A Python-based news agent that leverages the Google ADK to answer questions and perform tasks using voice commands (simulated in this version) and summarize the information. It utilizes Google Search to retrieve relevant information.

## Key Features

* **Voice Command Simulation:** Accepts text-based instructions as a stand-in for voice commands.
* **Question Answering:** Can answer questions based on information retrieved from the web.
* **Task Execution:** Capable of performing tasks based on user instructions.
* **Summarization:** Condenses retrieved information into concise summaries using the Google ADK's language model capabilities.
* **Google Search Integration:** Uses the `google_search` tool from the Google ADK to find relevant information.

## Built With

* [Google ADK](https://developers.generativeai.google/tools/adk)
* Python 3.x

## Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-github-username/your-repository-name.git](https://github.com/your-github-username/your-repository-name.git)
    cd your-repository-name
    ```
    *(Replace `your-github-username/your-repository-name` with the actual URL of your repository after you publish it.)*

2.  **Install Google ADK:**
    ```bash
    pip install google-adk
    ```


## Usage

1.  **Ensure your `instructions.txt` file is in the same directory as your `agent.py` file.** This file should contain the initial instructions or prompt you want the voice agent to follow. For example:
    ```
    Summarize the top 3 news stories about the Indian economy today.
    ```

2.  **Run the `adk enviorment` script:**
    ```bash
    adk web
    ```

    The script will:
    * Load the instructions from `instructions.txt`.
    * Initialize the `LlmAgent` with the specified model (`gemini-2.0-flash-exp`) and the `google_search` tool.
    * Run the agent with the loaded instructions.
    * Print the response from the agent.

## Code Structure

* `agent.py`: Contains the main logic for creating and running the `LlmAgent`.
* `.util.py`: (Based on your import) Likely contains utility functions, including `load_instruction_from_file`.
* `instructions.txt`: Holds the initial instructions for the voice agent.

## Example Interaction (Simulated)

**Content of `instructions.txt`:**
