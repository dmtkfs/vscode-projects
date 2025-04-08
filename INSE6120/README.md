# Vulnerability Assessment of Autostart Applications on Windows

> A security & privacy assessment of startup applications using real-world tools in isolated environments.

---

## Project Overview

This project focused on performing a **structured vulnerability assessment** of user-installed applications that leverage **autostart mechanisms** on:

- **Windows**: Startup Items, Registry, Scheduled Tasks  

The goal: Identify **security violations** (e.g., privilege escalation, unauthorized persistence) and **privacy violations** (e.g., telemetry, PII leakage).

### Application Categories

- Browsers & Communication  
- Cloud Storage & Backup  
- Security & Privacy Tools  
- Gaming & Game Launchers  
- Productivity & Collaboration  
- Media & Streaming  
- System Utilities & Performance  

---

<details>
<summary>Methodology & Workflow</summary>

### Isolated Testing Environments
- Used **VirtualBox** VMs with pre/post snapshot system for clean rollback.
- Snapshots taken:
  - After tool installation
  - After app installation
  - After test execution

### Tool-Driven Assessment

| Category                   | Tools Used                                                   |
|----------------------------|--------------------------------------------------------------|
| Persistence & Startup      | Autoruns, OSQuery, Process Explorer                          |
| Privilege & System Changes | Attack Surface Analyzer (ASA)                                |
| Telemetry & Network        | Wireshark, Fiddler, Burp Suite, BrowserLeaks                 |

### Testing Phases

1. **Startup Persistence**
   - Registry keys, AppData executables, Scheduled Tasks, UWP toggles.
2. **Privilege Escalation**
   - SYSTEM services, drivers, elevated installers.
3. **Telemetry & Privacy**
   - Captured traffic for encrypted and plaintext PII.

</details>

---

<details>
<summary>Risk Evaluation Criteria</summary>

### Security Risks
- Use of SYSTEM-level services or drivers
- Registry persistence that bypasses user control
- Auto-elevated scheduled tasks or service dependencies

### Privacy Risks
- Silent telemetry or tracking
- Session IDs, geolocation, device fingerprinting
- Transmission of PII without user consent

</details>

---

<details>
<summary>Key Trends & General Findings</summary>

- **Registry persistence** is being replaced with **modern methods** like Scheduled Tasks and UWP flags.
- **Encrypted traffic** often conceals sensitive data like session tokens or device IDs.
- Even **trusted vendors** introduced moderate or high risks.
- **SYSTEM-level integrations** were found in unexpected apps, leading to hidden escalation potential.
- **Web tech-based apps** often use **QUIC/WebSocket** protocols for telemetry, increasing leak surfaces.

</details>

---

## Skills & Knowledge Gained

- Mastery of **VM-based testing workflows**
- Use of GUI-based analysis tools with minimal setup
- Structured documentation of security/privacy risks
- Real-world PII inspection & traffic decryption skills

---

## Project Value

This project delivered:

- Hands-on experience with **security & privacy auditing**
- Reusable methodology for assessing **startup and persistence risks**
- A solid **portfolio discussion topic** for cybersecurity roles

---

## Future Work

- Automate tool output parsing (e.g., Autoruns CSV to JSON risk summary)  
- Expand to mobile, containerized, or cross-platform apps  
- Integrate with SIEM or security orchestration pipelines  
- Research & develop mitigations for detected startup risks  

---

## Disclaimer

This assessment was conducted **strictly for educational & research purposes** in isolated VMs.  
All applications were legally obtained and tested in compliance with licensing terms.  
No unauthorized interaction with external systems occurred.

**Findings are not publicly disclosed** here for security and ethical reasons.  
Requests for detailed reports can be made upon professional verification.