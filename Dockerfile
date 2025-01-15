# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port and run server
EXPOSE 8000
CMD ["gunicorn", "ashker_credit_solution.wsgi:application", "--bind", "0.0.0.0:8000"]
