# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 9999 for the FastAPI app
EXPOSE 9999

# Expose port 8501 for the Streamlit app
EXPOSE 8501

# Run the FastAPI app and Streamlit app
CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 9999 & streamlit run frontend.py"]
