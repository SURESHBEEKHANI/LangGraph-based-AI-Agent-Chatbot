from pydantic import BaseModel  # type: ignore # Import BaseModel from Pydantic for request validation
from typing import List  # Import List for type hinting
from fastapi import FastAPI, HTTPException  # type: ignore # Import FastAPI and HTTPException for API handling
from ai_agent import get_response_from_ai_agent  # Import function to handle AI responses

# Step 1: Define a Pydantic model for request validation
class RequestState(BaseModel):
    model_name: str  # Name of the AI model to be used
    model_provider: str  # Name of the AI model provider
    system_prompt: str  # System-wide prompt to guide AI behavior
    messages: List[str]  # List of messages exchanged in the chat
    allow_search: bool  # Flag to allow AI model to use external search

# Define a set of allowed model names to ensure only supported models are used
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192", 
    "mixtral-8x7b-32768", 
    "llama-3.3-70b-versatile",
    "gemma2-9b-it"
]

# Initialize FastAPI application with a title for better documentation
app = FastAPI(title="LangGraph AI Agent")

# Define a POST endpoint for AI chat interaction
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the AI chatbot using LangGraph and optional search tools.
    It dynamically selects the AI model specified in the request and processes user messages.
    """
    # Validate if the requested model is in the allowed list
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(status_code=400, detail=f"Model name {request.model_name} not supported")
    
    # Extract parameters from the request
    llm_id = request.model_name  # AI model identifier
    query = request.messages  # User messages sent to the model
    allow_search = request.allow_search  # Boolean flag for enabling search capabilities
    system_prompt = request.system_prompt  # System-wide guiding prompt for AI
    provider = request.model_provider  # AI model provider name
    
    # Call the AI response function to generate a reply
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    
    return response  # Return AI-generated response to the client

# Step 3: Run FastAPI application and enable API documentation (Swagger UI)
if __name__ == "__main__":
    import uvicorn  # type: ignore # Import Uvicorn for running the FastAPI application
    uvicorn.run(app, host="127.0.0.1", port=9999)  # Start server on localhost with port 9999
