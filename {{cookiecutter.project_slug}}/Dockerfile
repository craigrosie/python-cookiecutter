FROM python:3.5.2-slim
RUN groupadd {{cookiecutter.docker_user}} && useradd --create-home --home-dir /home/{{cookiecutter.docker_user}} -g {{cookiecutter.docker_user}} {{cookiecutter.docker_user}} \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        python3-dev \
        libpq-dev \
        libxml2-dev \
        libxslt-dev \
    && rm -rf /var/lib/apt/lists/*
    # && apt-get purge -y --auto-remove gcc and-build-dependencies

# Install the Python requirements
COPY requirements.txt /opt/{{cookiecutter.project_slug}}/
RUN pip install -r /opt/{{cookiecutter.project_slug}}/requirements.txt

# Work in the place that we will add the code in
WORKDIR /opt/{{cookiecutter.project_slug}}/

# Add in the latest code and reinstall it
COPY . /opt/{{cookiecutter.project_slug}}/
RUN pip install -e .

USER {{cookiecutter.docker_user}}
