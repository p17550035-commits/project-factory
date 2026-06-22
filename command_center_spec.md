# Groq Command Center — Master Specification (v1.0)
Unified Control Deck for Multi‑Environment Systems

## 1. Purpose
A single, touch‑optimized command center that:
- Swipes between environments (panels)
- Controls global system state (Pause All, Kill All, Restart All)
- Triggers repair/safe/diagnostic modes
- Prevents meltdown via pause/kill logic
- Provides a unified command console

## 2. Environment Panels
Each environment is a full‑screen swipe panel with its own controls.

Panels include:
- Core API
- Database
- Cache
- Auth
- Background Workers
- Tunnel/Proxy
- Logs/Monitoring
- SSH Terminal
- AI Assistant
- File System

Each panel displays:
- Status Light — ACTIVE, PAUSED, KILLED, RESTARTING, IDLE, ERROR
- Mode Indicator — NORMAL, SAFE, REPAIR, DIAGNOSTIC
- Local Controls — pause, resume, kill, restart, mode switch
- Quick Actions — logs, health check, tail, clear, etc.

## 3. Global Master Controls (Dropdown Menu)
Global Commands:
- Pause All — freeze all environments, stop outgoing calls, retries, loops
- Resume All — bring everything back online respecting boot order
- Kill All — hard stop all processes, tunnels, workers, servers
- Restart All — Kill All → then boot in defined sequence
- Test All — run health checks across every environment
- System Status — overview of all environments + states + last errors

## 4. Boot Order & Recovery Logic
Default Boot Sequence:
1. Core Services
2. Database
3. Cache
4. Auth
5. API
6. UI
7. Background Workers
8. Monitoring
9. Tunnel/Proxy

Rules:
- Restart All follows this order
- Resume All respects dependencies
- If a dependency fails, environment enters SAFE or REPAIR mode
- No environment wakes until prerequisites are green

## 5. Environment Modes
NORMAL — full functionality  
PAUSED — no outgoing calls, retries, loops; still listening  
SAFE MODE — minimal functionality, no heavy tasks  
REPAIR MODE — repair scripts, migrations, cleanup tasks  
DIAGNOSTIC MODE — high‑detail logging, health checks, debug info  

## 6. Command Protocol
Per‑Environment Commands:
- env:<name>:pause
- env:<name>:resume
- env:<name>:kill
- env:<name>:restart

Mode Commands:
- env:<name>:mode:normal
- env:<name>:mode:paused
- env:<name>:mode:safe
- env:<name>:mode:repair
- env:<name>:mode:diagnostic

Diagnostics:
- env:<name>:health:check
- env:<name>:logs:tail
- env:<name>:logs:clear
- env:<name>:status

Global Commands:
- system:pause_all
- system:resume_all
- system:kill_all
- system:restart_all
- system:test_all
- system:status

## 7. Swipe UI Behavior
Gestures:
- Horizontal swipe → switch environments
- Double‑tap → zoom into details
- Long‑press → quick actions
- Swipe up → advanced controls
- Swipe down → environment summary

Panel Layout:
- Header: name, status light, mode
- Body: environment‑specific UI
- Footer: quick actions (pause/resume/kill/restart/mode)

## 8. Status Lights
🟢 ACTIVE  
🟡 PAUSED  
🔴 KILLED / ERROR  
🔵 RESTARTING  
⚪ IDLE  
🟣 SAFE / REPAIR / DIAGNOSTIC  

## 9. Safety & Confirmation
- Kill All → confirmation required
- Restart All → confirmation required
- Repair/Safe Mode → optional confirmation
- Logs Clear → confirmation

## 10. Future Expansion
- SSH/WebSocket terminal integration
- Real health checks per environment
- Configurable boot order
- Per‑environment repair scripts
- Command history + autocomplete
- Full‑screen modal viewer for logs/images
- Multi‑node cluster support
- Remote machine discovery
- Auto‑recovery logic

# End of Spec v1.0