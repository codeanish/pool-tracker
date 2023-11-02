# Use latest python image
FROM python:3.10-slim as base

# Install poetry
RUN pip install poetry

# Copy poetry files to docker container
COPY pyproject.toml ./

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

# Copy alembic.ini file to docker container - Used for migrations
COPY alembic.ini /app/alembic.ini
COPY ./alembic /app/alembic

# Not important to have this here, as it's also being replicated in the docker compose, but incase it's instantiated by itself, it's good to have it here
EXPOSE 8000
CMD ["uvicorn", "db.main:app", "--host", "0.0.0.0", "--port", "8000"]