# pb-img

Tiny container fixtures for testing Dockerfile builds on a hosting platform. One build context per directory. Nothing here is for production use.

| directory | what it checks |
| --- | --- |
| `py/` | FastAPI on `python:3.12-slim`, runs as root, writes `/data/probe` |
| `go/` | multi-stage Go build on distroless `nonroot` (uid 65532) |
| `named/` | `USER app`, uid 1234 |
| `nouser/` | `USER ghost`, which the image does not define |
| `secret/` | a BuildKit secret mount that writes only the value's sha256; the app prints it as `sha=` |
| `unhealthy/` | answers 500 on every path, by design |
| `nodockerfile/` | no Dockerfile at all |

Each app listens on port 8080, answers `/healthz`, and its `/` reads `PB-IMG <uid>` on the first line, then `data=ok` when it could write `/data/probe`.
