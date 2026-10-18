# 🚀 Trabajo Práctico Integrador: Ciclo de Vida y Despliegue Continuo de una API REST (DevOps)

> **Estado del Proyecto:** `CI/CD: GitHub Actions (Passing)` | `Docker Hub: devops-tp-api:latest / v1.0.0` | `Python: 3.11` | `FastAPI`

## 📋 Tabla de Contenidos

1. [Descripción General y Arquitectura](#-descripción-general-y-arquitectura)
2. [Estrategia de Branching y Gestión de Cambios](#-estrategia-de-branching-y-gestión-de-cambios)
3. [Empaquetado y Optimización con Docker](#-empaquetado-y-optimización-con-docker)
4. [Pipeline de CI/CD (GitHub Actions)](#-pipeline-de-cicd-github-actions)
5. [Observabilidad, Logs y Monitoreo (Golden Signals)](#-observabilidad-logs-y-monitoreo-golden-signals)
6. [Aplicación de la Filosofía DevOps (The Three Ways)](#-aplicación-de-la-filosofía-devops-the-three-ways)
7. [Análisis de Desperdicios Lean (Muda)](#-análisis-de-desperdicios-lean-muda)
8. [Guía de Ejecución Local y Pruebas](#-guía-de-ejecución-local-y-pruebas)

---

## 📐 Descripción General y Arquitectura

Este proyecto implementa el ciclo de vida completo de una **API REST moderna desarrollada con Python y FastAPI**, automatizada y monitoreada bajo principios y metodologías **DevOps, CI/CD y Lean Software Development**.

### 🛠️ Tecnologías Utilizadas

* **Lenguaje & Framework:** Python 3.11, FastAPI, Uvicorn.
* **Documentación Interactiva:** OpenAPI / Swagger UI (disponible nativamente en `/docs`).
* **Pruebas y Calidad:** Pytest, TestClient.
* **Contenedores:** Docker (Multi-stage build), Docker Compose.
* **CI/CD:** GitHub Actions, Docker Hub Registry.
* **Estrategia de Commits & Versionado:** Conventional Commits, Semantic Versioning (SemVer `v1.0.0`).
* **Observabilidad:** Logs estructurados en JSON (`timestamp`, `level`, `path`, `status_code`, `duration_ms`), script generador de tráfico para medición de Golden Signals.

---

## 🔀 Estrategia de Branching y Gestión de Cambios

### Reglas de Git & Branch Protection

* **Protección de `main`:** Queda estrictamente prohibido realizar `git push` directo a la rama principal.
* **Feature Branches:** Todo desarrollo o corrección se realiza en ramas independientes con prefijos descriptivos:
  * `feat/*`: Nuevas características (ej: `feat/docker-setup`, `feat/ci-cd-pipeline`).
  * `fix/*`: Corrección de errores.
  * `ci/*` / `docs/*`: Ajustes en pipelines o documentación.

### Conventional Commits

Cada commit dentro del repositorio sigue el estándar de **Conventional Commits**:

```text
feat: add task management endpoints
fix: correct json logger status code mapping
ci: add github actions workflow for testing and docker build
docs: write comprehensive technical readme report