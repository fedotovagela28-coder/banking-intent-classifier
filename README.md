# ML Project Template

Production-ready template for building scable ML applications.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FasrAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Tests](https://img.shields.io/badge/tests-pytest-brightgreen)
![Code Style](https://img.shields.io/badge/code%20style-black-black)
![Lint](https://img.shields.io/badge/lint-ruff-purple)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
---

## Why this project?

Starting a new ML project often requires setting up the same infrastructure repeatedly: project structure, configuration management, logging, testing, Docker, CI pipelines, and API boilerplate.

This template provides a production-oriented foundation, allowing you to focus on developing ml solutions instead of rebuilding infrastructure for every new project.

---

## Features

- Modular project architecture
- Enviroment-based configuration
- Structured logging
- REST API with FastAPI
- Docker support
- Automated testing
- Continuous Integration

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.11 |
| API | FastAPI |
| Configuration | Pydantic Settings, YAML |
| ML | ... |
| Testing | Pytest |
| Formatting | Ruff, Black |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |

---

## Architecture

The template follows a layered architecture that separates API logic, service orchestration, ML components and model artifacts.

The architecture separates infrastructure from business logic.

Each layer has a single responsibility, making the template easer to maintain, test and extend.

```mermaid
flowchart TD
    Client[Client / API Consumer] --> API[FastAPI API Layer]
    API --> Service[Service Layer]
    Service --> ML[ML Pipeline Layer]
    ML --> Artifacts[Model Artifacts]
    
    API --> Core[Core: Config, Logging, Exceptions]
    Service --> Core
    ML --> Core
```

---

## Project Structure

| Directory | Purpose |
|-----------|---------|
| src/api | FastAPI application and request handing |
| src/services | Business logic |
| src/ml | ML pipeline |
| src/core | Configuration and infrastructure |
| tests | Automated tests |

---

## Getting Started

---

## Development

---

## Docker

---

## CI/CD

---

## Roadmap

---

## Lincense