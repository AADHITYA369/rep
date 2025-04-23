FROM python:3.11-slim

WORKDIR /app

COPY req.txt requirements.txt
COPY main.py main.py


# Install the required Python libraries
RUN pip install -r requirements.txt

# Run the Python script when the container starts
# ✅ Do this
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9002"]
