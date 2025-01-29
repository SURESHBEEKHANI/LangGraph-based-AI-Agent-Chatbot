import os
from langchain_groq import ChatGroq  # type: ignore  # Importing the ChatGroq class for interacting with Groq's LLM
from langchain_community.tools.tavily_search import TavilySearchResults  # type: ignore  # Importing TavilySearchResults for searching capabilities
from langgraph.prebuilt import create_react_agent  # type: ignore  # Importing a function to create a React agent for LLM interaction
from langchain_core.messages.ai import AIMessage  # type: ignore  # Importing the AIMessage class to handle AI-specific messages

# Retrieve API keys from environment variables for secure access
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Fetch the Groq API key from the environment
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")  # Fetch the Tavily API key from the environment

# Create an instance of TavilySearchResults tool with a max of 2 search results per query
search_tool = TavilySearchResults(max_results=2)

# Function to get a response from an AI agent
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Check if the provider is Groq, since other providers are not supported in this function
    if provider != "Groq":
        raise ValueError("Only 'Groq' provider is supported.")

    # Initialize the ChatGroq model with the given LLM ID
    llm = ChatGroq(model=llm_id)
    
    # If searching is allowed, initialize TavilySearchResults tool, otherwise, keep it empty
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create a React agent using the LLM and the search tool (if any), and the system prompt for state management
    agent = create_react_agent(
        model=llm,  # Using the Groq LLM for processing
        tools=tools,  # Including the search tool if allowed
        state_modifier=system_prompt  # Providing system-level prompt modification to manage agent behavior
    )

    # Set up the initial state with the user query
    state = {"messages": query}
    
    # Invoke the agent with the initial state to get a response
    response = agent.invoke(state)
    
    # Extract the messages from the response
    messages = response.get("messages")

    # Filter the AI messages from the response (ignoring non-AI messages)
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    
    # Return the last AI message if available, else return None
    return ai_messages[-1] if ai_messages else None
