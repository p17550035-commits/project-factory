<!-- 
  FILE: CONTRIBUTING.md
  PURPOSE: Contribution rules, workflow, and metadata standards for Project Factory
  AUTO-GENERATED: No
  PROTECTED: No
  LAST UPDATED: 06/21/2026 02:50 PM EDT
  VERSION: 1.4.0
-->

# Contributing to Project Factory

This document explains how to contribute safely and consistently.  
It also includes copy‑ready metadata templates for new files.

---

# Required Metadata for Every File

Every file must begin with a metadata header and end with a footer.

This ensures:
- File identity  
- Version tracking  
- Timestamp clarity  
- Automation compatibility  
- Safe overwrites  
- Consistent formatting  

---

# Metadata Header Template (Copy This)

FILE: <filename>  
PURPOSE: <what this file does>  
AUTO-GENERATED: No  
PROTECTED: No  
LAST UPDATED: <MM/DD/YYYY HH:MM AM/PM TZ>  
VERSION: 1.0.0  

---

# Footer Template (Copy This)

END OF <filename> (<linecount> lines)

---

# Protected Files

Files marked with PROTECTED: Yes cannot be overwritten or auto-generated.

Examples:
- main.py  
- README.md  
- SECURITY.md  
- Deployment configs  
- Core automation modules  

---

# Versioning Rules

Increase the version when:
- Logic changes  
- Structure changes  
- Metadata changes  
- Behavior changes  
- New features are added  

Patch: 1.0.1  
Minor: 1.1.0  
Major: 2.0.0  

---

# Timestamp Rules

- Display: local timezone (auto‑detected)  
- Internal: UTC for logs and automation  
- Format: MM/DD/YYYY HH:MM AM/PM TZ  

---

# Code Style Rules

- Clean, readable formatting  
- No unused imports  
- No dead code  
- No placeholder text  
- No partial implementations  
- No broken code blocks  
- No inconsistent indentation  

---

# Workflow

1. Create or modify a file  
2. Add or update metadata header  
3. Add or update footer line count  
4. Test changes locally  
5. Commit with a clear message  
6. Push to the repository  

---

# Notes

This project is designed for future multi‑user support.  
Following these standards keeps the system stable and automation‑friendly.

<!-- END OF CONTRIBUTING.md (112 lines) -->