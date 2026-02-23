##########################
## Build env
##########################

FROM python:3.13-slim-trixie AS BUILD

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
#RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    ca-certificates pkg-config make \
    libssl-dev libffi-dev libpq-dev

# python packages
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


##########################
## Final image
##########################
FROM python:3.13-slim-trixie

LABEL maintainer "CRG System Developers"
LABEL org.label-schema.schema-version="2.0"
LABEL org.label-schema.vcs-url="https://github.com/EGA-archive/beacon-2.x/"

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update && apt-get upgrade -y

COPY --from=BUILD /usr/local/lib/python3.13/site-packages      /usr/local/lib/python3.13/site-packages

USER 65534

COPY beacon beacon

ENTRYPOINT ["python","-m","beacon"]
