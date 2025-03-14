# Penetration Testing of the AppLoki SmartLock
**INSE 6170 Cybersecurity Project | Smart Home Security Assessment**

This repository provides an **overview** of a **penetration testing** study conducted on the **AppLoki Smart Lock** and its associated **Tuya smartphone application**. The objective of this project was to **assess the security posture** of the system, particularly **authentication, encryption, and network communication**.

**Note**: The **full technical report** detailing vulnerabilities, testing methodology, and recommendations is **available upon request**.

---

## ⚠️ **Disclaimer**
This research was conducted **for educational and ethical cybersecurity purposes only**. **No vulnerabilities were exploited maliciously**. The **findings do not imply real-world exploits**, and the project adheres to **responsible disclosure principles**.

## **Project Overview**
Smart home technologies bring convenience but also **new cybersecurity risks**. The **AppLoki Smart Lock** is a Bluetooth (BLE) controlled lock, paired with the **Tuya Smart Home** mobile app. This project **evaluated** the lock's **firmware, Bluetooth security, mobile application, and network protocols** for potential vulnerabilities.

### **Methodology**
A combination of **static analysis, dynamic testing, and network traffic inspection** was used to **identify and validate** security weaknesses. The assessment was divided into three phases:

1. **Static Analysis**  
   - **Decompilation & Code Review** (JADX, APKTool)
   - **Dependency Scanning** (OWASP Dependency-Check)
   - **Automated Security Scans** (SpotBugs, AndroBugs)

2. **Dynamic Testing**  
   - **Network Traffic Analysis** (Wireshark, Burp Suite)
   - **Bluetooth Sniffing & Replay Attacks** (nRF Connect, Bettercap)
   - **Proxy Interception** (Burp Suite, Android Debugging)

3. **Hardware & Firmware Testing**  
   - **Smart Lock Hardware Inspection**  
   - **DoS Testing & Device Resilience**  

---

## **Key Security Findings**
**AES-128 Encryption Successfully Implemented**  
- Secure communication channels with **session keys** prevented **BLE replay attacks**.  

**No Internet Connectivity**  
- The lock does **not communicate over the internet**, reducing **remote attack risks**.  

**Denial-of-Service (DoS) Test: Limited Impact**  
- Flooding the lock with BLE requests **momentarily slowed operations** but **did not disrupt functionality**.  

**Potential Firmware Security Concerns**  
- Due to hardware limitations, **firmware security** was **not fully evaluated**. However, secure update mechanisms **should be reinforced**.  

**Proxy Detection Mechanism Bypassed**  
- The Tuya app detected proxies, but **alternative attack paths could still exist** if dynamic analysis was expanded.  

### **General Observations**
- The lock **resisted replay attacks** and demonstrated **good Bluetooth security**.  
- **Static code analysis** did not reveal **hardcoded credentials** or **high-risk misconfigurations**.  
- **Firmware and hardware** security were **out of scope due to hardware limitations**, requiring further research.  

---

## **Recommendations**
- **Perform periodic security audits** for **firmware updates** and **app patches**.  
- **Ensure robust logging** for **intrusion detection & threat analysis**.  
- **Expand testing** with a **rooted Android device** to explore deeper **dynamic attack vectors**.  