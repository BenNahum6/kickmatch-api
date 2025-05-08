# Use a basic Python image
FROM python:3.12-slim

# Define the section where all the code will be installed
WORKDIR /app

# Copy requirements.txt into the image
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the image
COPY . .

# Expose the port on which FastAPI will run
EXPOSE 8000

# Configure the FastAPI startup command with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]