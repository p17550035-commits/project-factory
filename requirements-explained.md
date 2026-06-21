<!-- 
  FILE: requirements-explained.md
  PURPOSE: Human-readable explanation of each dependency in requirements.txt
  AUTO-GENERATED: No
  PROTECTED: No
  LAST UPDATED: 06/21/2026 03:00 PM EDT
  VERSION: 1.1.0
-->

# Requirements Explained

This document explains the purpose of each dependency listed in requirements.txt.  
It helps maintainers understand why each package exists and whether it is safe to update or remove.

---

# Dependencies

## fastapi
Used to build the backend API.  
Provides routing, request handling, and async support.

## uvicorn
ASGI server used to run the FastAPI backend.  
Lightweight, fast, and production-ready.

## groq
Client library for interacting with the Groq API.  
Handles authentication and request formatting.

## python-dotenv
Loads environment variables from a .env file.  
Used for API keys, secrets, and configuration.

## jinja2
Template engine used for generating HTML pages.  
Supports variables, loops, and dynamic rendering.

## pydantic
Used for data validation and structured models.  
Ensures clean, typed request/response objects.

---

# Notes

Only add dependencies when necessary.  
Document all new packages here to maintain clarity.

<!-- END OF requirements-explained.md (50 lines) -->