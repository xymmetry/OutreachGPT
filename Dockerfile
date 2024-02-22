# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install packages for AWS Amplify
RUN apt-get update && apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y openssh-client
RUN apt-get install -y bash
RUN apt-get update && apt-get install -y nodejs
RUN rm -rf /var/lib/apt/lists/*


# Copy current directory contents into the container at /app
WORKDIR /app
COPY . /app

# Environment Variable
ENV NAME World

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app", "python", "app.py"]
