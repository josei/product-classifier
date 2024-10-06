FROM python:3.11

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock* ./
RUN pip install --no-cache-dir pipenv && pipenv install --deploy --system
COPY src ./src

VOLUME ["/usr/src/app/data"]
VOLUME ["/usr/src/app/models"]

ENV HF_HOME=/usr/src/app/models/.hf_cache
ENV HF_HUB_CACHE=/usr/src/app/models/.hf_cache
ENV TOKENIZERS_PARALLELISM=false

EXPOSE 8000

ENTRYPOINT ["python", "src/cli.py"]
