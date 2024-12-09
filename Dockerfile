FROM ubuntu:latest
WORKDIR /usr/app/src
RUN apt-get update && \
    apt-get install -y \
    gcc \
    make \
    tor \
    python3 \
    python3-dev \
    git \
    wget \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY os.py ./

# Run the Python script
CMD ["python3", "os.py"]
