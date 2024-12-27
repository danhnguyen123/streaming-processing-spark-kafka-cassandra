FROM bitnami/spark:3.4

USER root

# Install prerequisites
RUN apt-get update && apt-get install -y curl make gcc wget

RUN apt-get install -y --no-install-recommends \
    rsync && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
