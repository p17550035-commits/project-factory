<!-- 
  FILE: SECURITY.md
  PURPOSE: Security policy, vulnerability reporting, and protected file rules
  AUTO-GENERATED: No
  PROTECTED: Yes
  LAST UPDATED: 06/21/2026 02:55 PM EDT
  VERSION: 1.1.0
-->

# Security Policy

This document defines how security issues are handled within Project Factory.  
It also explains how to report vulnerabilities and which files are protected.

---

# Reporting Vulnerabilities

If you discover a vulnerability:

- Do not open a public issue  
- Contact the project owner privately  
- Provide steps to reproduce  
- Include environment details  
- Include logs if possible  
- Describe expected vs actual behavior  

This ensures sensitive information is not exposed publicly.

---

# Protected Files

Files marked with PROTECTED: Yes cannot be:

- Auto-generated  
- Overwritten  
- Replaced  
- Modified without explicit approval  

Protected files include:

- main.py  
- README.md  
- SECURITY.md  
- Deployment scripts  
- Core automation modules  

These files are critical to system stability and security.

---

# API Keys and Secrets

- Never commit secrets to the repository  
- Use .env files for local development  
- Use environment variables in production  
- Rotate keys if exposure is suspected  
- Treat all credentials as sensitive  

---

# Dependency Security

- Review dependencies before adding them  
- Document new dependencies in requirements-explained.md  
- Avoid unnecessary packages  
- Prefer stable releases  
- Update dependencies when security patches are released  

---

# General Security Practices

- Validate all input  
- Sanitize user data  
- Avoid exposing internal errors  
- Use HTTPS in production  
- Log security events  
- Monitor for suspicious activity  

---

# Notes

Security is a core part of the system’s architecture.  
This document will expand as the project grows.

<!-- END OF SECURITY.md (89 lines) -->