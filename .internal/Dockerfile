FROM python:3.7-slim
WORKDIR /my_awesome_ds_project
COPY . /my_awesome_ds_project
RUN echo "* Installing Base Packages" && \
    apt-get update && apt-get install -y \
    bash \
    build-essential \
    ca-certificates \
    coreutils \
    curl \
    dumb-init \
    gcc \
    g++ \
    git \
    gosu \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    make \
    openssl \
    libsrt-openssl-dev && \
    # adding appuser for gosu
    adduser --disabled-password --no-create-home appuser

RUN make requirements

ENTRYPOINT ["python3", "hello_world.py"]
