<!-- 
  FILE: README.md
  PURPOSE: Project overview, architecture documentation, standards, and contributor guide
  AUTO-GENERATED: No
  PROTECTED: Yes
  LAST UPDATED: 06/21/2026 01:15 PM EDT
  VERSION: 1.0.0
-->

Project Factory — AI App Builder
A modular backend + automation system for generating code, scaffolding projects, and building app templates using Groq LLMs.

This system is designed to scale from a single‑user local tool into a multi‑user, multi‑service automation platform.  
It emphasizes clean structure, metadata integrity, file safety, and future‑proofing.

---

📌 Overview

Project Factory is an AI‑powered development engine that:

- Generates code, scripts, and project templates  
- Provides a command‑console style UI (chat.html)  
- Communicates with Groq’s LLM API  
- Enforces strict file metadata standards  
- Supports protected files and safe‑overwrite rules  
- Uses UTC internally with auto‑detected timezone conversion  
- Is designed for future automation, multi‑user support, and modular expansion  

This is not just a backend — it’s the foundation of a self‑building development ecosystem.

---

🧱 Core Components

1. FastAPI Backend (main.py)
Handles:

- Groq API requests  
- Code generation  
- Project scaffolding  
- File routing  
- System commands (restart, test, etc.)  

Protected file — cannot be overwritten without authorization.

2. Frontend Command Console (chat.html)
A lightweight UI that:

- Sends prompts to the backend  
- Displays AI responses  
- Supports code blocks, copy buttons, timestamps  
- Includes a dropdown command menu  
- Uses metadata + footer integrity checks  

3. Metadata System
Every file in the project follows a strict metadata block:

`
FILE: <name>
PURPOSE: <description>
AUTO-GENERATED: Yes/No
PROTECTED: Yes/No
LAST UPDATED: MM/DD/YYYY HH:MM AM/PM <TZ>
VERSION: X.Y.Z
`

And ends with:

`
END OF <filename> (<linecount> lines)
`

This ensures:

- File identity  
- Version tracking  
- Timestamp clarity  
- Safe overwrites  
- Automation compatibility  
- Human readability  

---

🛡 Protected File Rules

Some files are marked:

`
PROTECTED: Yes
`

These files:

- Cannot be overwritten by automation  
- Cannot be regenerated without credentials  
- Must be manually approved for modification  
- Are critical to system stability  

Examples:

- main.py  
- README.md  
- Deployment configs  
- Security‑sensitive modules  

---

⏱ Timestamp Strategy

The system uses:

- UTC internally (industry standard)  
- Auto‑detected user timezone for display  
- Fallback: America/New_York  
- MM/DD/YYYY HH:MM AM/PM formatting  

This ensures:

- Accurate logs  
- Consistent metadata  
- Multi‑user compatibility  
- Zero daylight‑savings issues  

---

🔧 Automation Roadmap

Automation will eventually handle:

- Metadata injection  
- Timestamp updates  
- Version bumping  
- File generation  
- Protected file enforcement  
- Project scaffolding  
- Multi‑file builds  
- Deployment scripts  
- Background services  

The system is designed so these features can be added without rewriting existing code.

---

📂 File Structure (Current)

`
project-factory/
│
├── main.py          # FastAPI backend (PROTECTED)
├── chat.html        # Frontend command console
├── README.md        # Project documentation (PROTECTED)
└── requirements.txt # Dependencies (future)
`

This will expand as automation grows.

---

🧭 Contribution Rules (Future‑Proofed)

Even if you're the only contributor now, the project is structured for multi‑user collaboration.

Rules:

- All files must include metadata headers  
- All files must include footer line counts  
- Protected files require authorization  
- Version numbers must increment on change  
- Timestamps must reflect local time (auto‑detected)  
- Code must follow clean, senior‑engineer formatting  

---

🚀 Vision

Project Factory is designed to evolve into:

- A full AI‑powered development environment  
- A modular automation engine  
- A multi‑user code generation platform  
- A self‑maintaining system with metadata‑aware rebuilds  
- A tool that can generate apps, APIs, scripts, and UIs on demand  

This README will expand as the system grows.

---

<!-- END OF README.md (142 lines) -->
