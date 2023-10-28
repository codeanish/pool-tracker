# Use latest python image
FROM python:3.10-slim as base

# Copy poetry files to docker container
COPY pyproject.toml ./

# Install poetry
RUN pip install poetry

# Create requirements.txt file
RUN poetry export -f requirements.txt --output requirements.txt

# Copy requirements.txt file to docker container
FROM python:3.10-slim as development
COPY --from=base requirements.txt .

# Install requirements.txt
RUN pip install -r requirements.txt

# purge pip cache
RUN pip cache purge

# Copy project files to app folder in docker container
FROM development as production
WORKDIR /app
COPY ./db /app/db

# Start uvicorn with main
EXPOSE 8000
CMD ["uvicorn", "db.main:app", "--host", "0.0.0.0", "--port", "8000"]