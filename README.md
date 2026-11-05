<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" align="right" height="64px"/>

# FastAPI Lab

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat&logo=uv&logoColor=white)
![License](https://img.shields.io/github/license/avcaliani/lab-fast-api?style=flat&logo=opensourceinitiative&logoColor=white&color=green)

Personal [FastAPI](https://fastapi.tiangolo.com/) learning sandbox: one full app (the Office-themed Rewards API).  
Small isolated experiments live in [scratchpad](https://github.com/avcaliani/scratchpad/tree/main/back-end/fast-api).

## Structure

```text
.
├── .github/                    ci workflow + pr and issue templates
└── pocs/
    ├── rewards-api/            fastapi, mongodb, jwt: earn and spend Schrute Bucks
    └── rewards-ui/             front end: static html/css/js, calls rewards-api
```

## How to run

Every project owns its `pyproject.toml`: run commands from its folder, always through `uv` (never outside the virtual env).

- Rewards API: see [pocs/rewards-api/](pocs/rewards-api/)
- Rewards UI: see [pocs/rewards-ui/](pocs/rewards-ui/) (static page, open `index.html`)

> **PS.:** This is an unofficial fan project for learning FastAPI, not affiliated with or endorsed by NBCUniversal.

---

[FastAPI: docs](https://fastapi.tiangolo.com/) / [uv: docs](https://docs.astral.sh/uv/)
