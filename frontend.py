# Import necessary libraries
import streamlit as st 

# If not using pipenv, uncomment the following to load environment variables from a .env file
# from dotenv import load_dotenv
# load_dotenv()

# Step 1: Setup UI with Streamlit (model provider, model, system prompt, web_search, query)
st.set_page_config(page_title="LangGraph Agent ", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# Text area for the system prompt where the user can define the behavior of the agent
system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

# List of available Groq models
MODEL_NAMES_GROQ = [
    "llama3-70b-8192", 
    "mixtral-8x7b-32768", 
    "llama-3.3-70b-versatile",
    "gemma2-9b-it"
]

# Radio button to select the provider (Only Groq option is enabled here)
provider = st.radio("Select Provider:", ("Groq",))

# Since only Groq is supported, we directly present Groq models for selection
selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

# Checkbox to allow the agent to perform a web search if checked
allow_web_search = st.checkbox("Allow Web Search")

# Text area for the user to enter their query
user_query = st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

# Backend API URL for making requests (ensure the API is running on this URL)
API_URL = "http://127.0.0.1:9999/chat"

# Step 2: When the user clicks "Ask Agent!", this block is executed
if st.button("Ask Agent!"):
    if user_query.strip():  # Ensure the query is not empty
        # Import the requests library to make HTTP requests
        import requests # type: ignore

        # Prepare the payload with all necessary data to send to the backend API
        payload = {
            "model_name": selected_model,  # Selected model from Groq
            "model_provider": provider,  # Groq provider
            "system_prompt": system_prompt,  # System prompt to customize agent behavior
            "messages": [user_query],  # User query message
            "allow_search": allow_web_search  # Whether to allow web search
        }

        # Make the POST request to the API with the payload
        response = requests.post(API_URL, json=payload)

        # If the response is successful (status code 200), display the result
        if response.status_code == 200:
            response_data = response.json()

            # Check for any errors in the response
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                # Display the response from the agent
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
