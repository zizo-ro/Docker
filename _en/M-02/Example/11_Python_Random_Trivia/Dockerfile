FROM ubuntu:20.04
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    libexpat1 \
    libsqlite3-0 \
    libssl1.1 \
    python3-pip \
    python3 \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p  /app 
WORKDIR /app
COPY ./requirements.txt /app/
COPY ./trivia.csv /app/
RUN pip install -r /app/requirements.txt
COPY ./app.py /app/
CMD ["python3", "app.py"]