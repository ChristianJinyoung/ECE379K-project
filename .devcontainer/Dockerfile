FROM mcr.microsoft.com/vscode/devcontainers/python:3.11-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"
