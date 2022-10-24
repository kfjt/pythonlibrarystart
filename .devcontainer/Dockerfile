FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10-bullseye as base
ENV POETRY_HOME=/home/vscode/.local \
    POETRY_VERSION=1.2.2 \
    \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PATH="${POETRY_HOME}/bin:$PATH"
RUN su vscode -c "curl -sSL https://install.python-poetry.org | python3 -"
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

FROM base as development
RUN su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install 16 2>&1"

FROM base as production
ENV PYTHONPATH=/home/vscode/src:${PYTHONPATH}

WORKDIR /home/vscode/
COPY --chown=vscode:vscode pyproject.toml poetry.lock /home/vscode/
RUN su vscode -c "poetry install"
COPY --chown=vscode:vscode src/* /home/vscode/src/
USER vscode
# CMD [ "" ]
