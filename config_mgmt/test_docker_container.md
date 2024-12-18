### Test Docker Container

```bash

FROM myapp:latest

RUN pip install pytest pydoc

RUN apt update && apt install -y jq curl netcat

WORKDIR /opt/myapp

CMD pytest .

```

```bash

docker run -it myapp:test

docker run -it -v ./testdata:/data myapp:test

docker exec -it c47da2b409a1 /bin/sh

docker start c47da2b409a1

docker exec -it c47da2b409a1 /bin/sh

```
