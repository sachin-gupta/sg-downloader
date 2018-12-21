# Idea is when Travis CI had completed building of package, then install its binary in same anaconda enviornment
# and execute the code. Watch output on console for same.

# PHASE-1: Without Conda, Run App from Source in Docker
# PHASE-2: Without Conda, Run App+Flask from Source in Docker
# PHASE-3: Without Conda, Install App+Flask from Travis Built in Docker & RUN
# PHASE-3: With Conda (RStudioDevEnv) and Missing PIP, Run App+Flask from Source in Docker
# PHASE-4: With Conda (RStudioDevEnv) and Missing PIP, Install App+Flask from Travis Built in Docker & RUN

# NOTE: In this paticular run, i'll copy application by source and execute it in docker container on
# travis-ci. Shall not be deploying application package into conda and then execute it inside conda

# [MiniConda3](https://hub.docker.com/r/continuumio/miniconda3/) is Docker container with a bootstrapped installation
# of Miniconda (based on Python 3.5) into /opt/conda and ensures that the default user has the conda command in their path

# Set the base image continuumio/miniconda3:4.5.11
FROM continuumio/miniconda3:4.5.11

# Author or maintainer of this image file
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>

# All packages must work in noninteractive mode.
ENV DEBIAN_FRONTEND noninteractive
RUN export DEBIAN_FRONTEND=noninteractive

# Ass quite essential items into ubuntu including sudo, curl, wget
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \
    apt-utils \
    ca-certificates \
    curl \
    wget \
    sudo > /dev/null \
    && rm -rf /var/lib/apt/lists/*

# After essentials more essentials which require above packahges
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \
    openssh-client \
    procps \
    autoconf \
    automake \
    gcc \
    make \
    p7zip \
    unace \
    zip \
    unzip \
    xz-utils \
    sharutils \
    uudeview \
    mpack \
    arj \
    cabextract \
    file-roller > /dev/null \
    && rm -rf /var/lib/apt/lists/*

# Install some libraries for Gcc
RUN apt-get -qq -y update && apt-get install -qq -y --no-install-recommends \
    libbz2-dev \
    libc6-dev \
    libcurl4-openssl-dev \
    libdb-dev \
    libevent-dev \
    libffi-dev \
    libgdbm-dev \
    libgeoip-dev \
    libglib2.0-dev \
    libjpeg-dev \
    libkrb5-dev \
    liblzma-dev \
    libmagickcore-dev \
    libmagickwand-dev \
    libncurses-dev \
    libpng-dev \
    libpq-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libtool \
    libwebp-dev \
    libxml2-dev \
    libxslt-dev \
    libxslt1-dev \
    libyaml-dev \
    patch \
    xz-utils \
    zlib1g-dev \
    build-essential \
    libqt4-dev \
    xvfb \
    checkinstall \
    yum  > /dev/null \
    && rm -rf /var/lib/apt/lists/*

# Define name of application and its version
LABEL Name=sg-downloader Version=0.0.1

# Define WORKDIR: Set the working directory for any subsequent ADD, COPY, CMD, ENTRYPOINT,
# or RUN instructions that follow it in the Dockerfile.
WORKDIR /app

# Adding application source code to folder /app (COPY & ADD SAME BUT ADD EXTRACTS TAR AND DOWNLOADS FROM HTTP)
# Thus using COPY, WORKDIR mentions where everything will be copies
ADD data/ /app/data/
ADD src/ /app/src/
ADD main.py /app
ADD setup.py /app
ADD CHANGES.txt /app
ADD LICENSE /app
ADD README.md /app
ADD requirements.txt /app
ADD requirements-dev.txt /app
ADD environment.yml /app

# Copy docs not to WORKDIR (different location)
ADD docs/_build/html /app/www/docs

# Change Execute Bit on Python Files
RUN find ./**/*.py -type f -exec chmod 755 {} \;

# Echo the present directory to console
RUN echo "Current Directory Is:" && \
    pwd

# Watch content of anaconda (/opt/conda/envs) directory
RUN ls -lh /opt/conda/envs

# Watch content of /app directory
RUN ls -lh /app/www/docs

# Watch the contents of /app
RUN ls -lah /app

# Update enviorment as per development of app (condaenv)
# RUN conda env update -n base -f environment.yml 

# Print information of conda enviornment
RUN conda info

# Print content of conda enviornment
RUN conda env list

# Print content of existing pip modules
RUN python3 --version

# Upgrade pip to latest
RUN pip install --no-cache-dir --upgrade pip > /dev/null
RUN pip --version

# Print installed modules on system
RUN pip freeze

# Echo python version and use pip to install dependencies into image
RUN pip install  --no-cache-dir  --upgrade --ignore-installed  -r requirements.txt > /dev/null
RUN pip install  --no-cache-dir  --upgrade --ignore-installed  -r requirements-dev.txt > /dev/null

# Execute application (execution default or ENTRYPOINT)
CMD ["/bin/bash", "-c", "cd /app && echo 'Current Directory:' && pwd && python3 /app/main.py"]

# EXPOSE 5000

# Using pip:
#RUN python3 -m pip install -r requirements.txt
#CMD ["python3", "-m", "sg-downloader"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "sg-downloader"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m sg-downloader"
