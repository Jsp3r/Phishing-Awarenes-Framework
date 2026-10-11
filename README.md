# 🧪 Phishing Awareness Training Framework (Homelab Edition)

> **⚠️ LEGAL DISCLAIMER & TERMS OF USE**  
> This project and its documentation were created strictly for **educational purposes, authorized security awareness training, and testing within an isolated homelab environment**.  
> Deploying phishing simulations or targeting individuals/organizations without prior explicit written permission is illegal and prohibited. **The author accepts no responsibility or liability for any misuse, unauthorized deployments, or damages resulting from this material.**

---

## 🔬 Homelab Context & Purpose

This project was built and validated in a personal homelab to simulate security awareness workflows and analyze phishing.

* **Controlled Environment:** All email delivery and web redirection tests were executed in an isolated local network (homelab domain/sandboxed email server).
* **Safe Design:** No actual credentials (e.g., Google passwords) are harvested, stored, or processed.
* **Educational Intent:** Created to demonstrate how red team/blue team tools interact with user awareness training in a hands-on learning lab.
* **Setup**
  * Import templates/password_expiration.html into your lab simulation tool (e.g., GoPhish).
  * Host/Import landing_pages/awareness.html on a local web server or into your lab simulation tool.

---

## 💡 Key Security Awareness Rules

When reviewing phishing exercises or training lab users, highlight these core indicators:

* 🚨 **Be cautious of unexpected password-expiration messages.**
* 🔗 **Check links before clicking them.**
* 🔒 **Never provide your password through an unexpected email link.**
* 📞 **Verify suspicious requests to official channels & notify the IT deparment**.**

---
