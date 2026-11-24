FROM python:3.12-slim
# Only the hash of the value is written into the image; the value never reaches a layer.
RUN --mount=type=secret,id=PROOF_SECRET,env=PROOF_SECRET \
    sh -c 'printf %s "$PROOF_SECRET" | sha256sum | cut -d" " -f1 > /secret.sha256'
WORKDIR /srv
COPY server.py .
EXPOSE 8080
CMD ["python", "server.py"]
