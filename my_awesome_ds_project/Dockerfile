FROM python:3.7-slim
WORKDIR /my_awesome_ds_project
COPY . /my_awesome_ds_project
RUN echo "* Installing Base Packages" && \
    apt-get update && apt-get install -y \
    bash \
    build-essential \
    make

RUN chmod +x /my_awesome_ds_project/entrypoint.sh
RUN make requirements
#ENTRYPOINT ["python3", "src/hello_world.py"]

ENTRYPOINT ["./entrypoint.sh"]
