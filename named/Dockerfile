FROM python:3.12-slim
RUN groupadd --gid 1234 app && useradd --uid 1234 --gid 1234 --no-create-home app
WORKDIR /srv
COPY server.py .
USER app
EXPOSE 8080
CMD ["python", "server.py"]
