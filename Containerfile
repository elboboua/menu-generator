FROM python:3.11.9-slim-bullseye

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Run the application
CMD ["python", "menu-generator.py"]