<!-- 
  FILE: INSTALLATION.md
  PURPOSE: Instructions for installing and running Project Factory
  AUTO-GENERATED: No
  PROTECTED: No
  LAST UPDATED: 06/21/2026 04:05 PM EDT
  VERSION: 2.0.0
-->

# Installation Guide

This document explains how to install and run Project Factory on your system.

---

# Requirements

- Python 3.10 or newer
- pip
- Terminal or command line
- Internet access

---

# Setup Steps

## 1. Clone the repository

Run this command in your terminal:

    git clone https://github.com/your-username/project-factory.git

## 2. Navigate to the project directory

    cd project-factory

## 3. Install dependencies

    pip install -r requirements.txt

## 4. Create a .env file

    GROQ_API_KEY=your_api_key_here

## 5. Run the backend

    uvicorn main:app --reload

## 6. Open the UI

Open this in your browser:

    http://localhost:8000

---

# Notes

Installation steps may change as the project evolves.

<!-- END OF INSTALLATION.md (61 lines) -->