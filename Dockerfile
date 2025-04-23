FROM python:3.11-slim

WORKDIR /app

# Rename and copy your requirements file properly
COPY req.txt requirements.txt
COPY main.py main.py

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 9002

# Run the app on container startup
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9002"]
