# LangGraph-based AI Agent Chatbot

This project is a LangGraph-based AI Agent Chatbot deployed on Hugging Face Spaces. It uses FastAPI for the backend and Streamlit for the frontend.

## Features

- Define custom AI agents with system prompts.
- Select from a list of Groq models.
- Optionally allow the agent to perform web searches.
- Interact with the AI agent through a user-friendly interface.

## Requirements

- Docker
- Python 3.9+

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LangGraph-based-AI-Agent-Chatbot.git
cd LangGraph-based-AI-Agent-Chatbot
```

### 2. Create a `.env` File

Create a `.env` file in the root directory and add your API keys:

```plaintext
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Build and Run the Docker Container

```bash
docker build -t langgraph-ai-agent .
docker run -p 8501:8501 -p 9999:9999 langgraph-ai-agent
```

### 4. Access the Application

Open your browser and go to `http://localhost:8501` to access the Streamlit frontend.

## File Structure

- `frontend.py`: Streamlit app for the user interface.
- `backend.py`: FastAPI app for handling API requests.
- `ai_agent.py`: Logic for interacting with the AI agent.
- `Dockerfile`: Docker configuration for containerizing the application.
- `requirements.txt`: List of Python dependencies.

## Usage

1. Define your AI agent by entering a system prompt.
2. Select a Groq model from the list.
3. Optionally enable web search.
4. Enter your query and click "Ask Agent!" to get a response.

## License

This project is licensed under the MIT License.