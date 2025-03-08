FROM hashicorp/terraform:latest

WORKDIR /app

COPY . /app

ENTRYPOINT ["terraform"]
