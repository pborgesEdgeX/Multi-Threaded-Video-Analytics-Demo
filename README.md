# Multi-Threaded-Video-Analytics-Demo

Multi-threaded video analytics demo: a Flask + Kafka (Python) server that
consumes video streams from Raspberry Pi camera clients.

## Source layout

- **[`app/`](app/)** — server-side application. Flask dashboard plus the Kafka
  producers/consumers that move video frames through the pipeline:
  - `main.py`, `dashboard.py` — Flask web server / analytics dashboard
    (renders `app/templates/index.html`)
  - `producer*.py` — Kafka producers that publish camera frames
  - `consumer*.py` — Kafka consumers that read frames per topic
  - `yttest.py` — helper/test script
  - `requirements.txt`, `Dockerfile` — dependencies and container build
- **[`raspberryPi/`](raspberryPi/)** — client-side Raspberry Pi camera streamer
  (`raspberryPi/main.py`). See [`raspberryPi/README.md`](raspberryPi/README.md).

## Running the server app

```
$ cd app
$ python3 -m venv venv && source venv/bin/activate
$ pip install -r requirements.txt
$ python3 main.py
```

> Virtual environments (`venv/`, `.venv/`) and Python caches (`__pycache__/`)
> are intentionally not committed — see `.gitignore`.
