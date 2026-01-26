# Wi-Fi Risk Awareness Dashboard – Scope Definition

## 1. Project Purpose

This project provides a simple, public-facing web application that helps small business owners understand potential Wi-Fi-related risks based on structured questions.

The goal is **awareness and education**, not security enforcement or technical auditing.

The system uses **rule-based logic** to classify risk levels and provide plain-English explanations and recommended next steps.

---

## 2. Target Users

- Small business owners
- Non-technical users
- Individuals with limited networking or cybersecurity knowledge

This tool is designed to be usable without technical expertise.

---

## 3. In-Scope Functionality

The application will:

- Collect user input via a simple web form
- Accept the following inputs:
  - Business type
  - Whether Wi-Fi is public or private
  - Whether Wi-Fi is password protected
  - Whether staff and customers share the same network
  - Approximate router age
- Evaluate inputs using deterministic, rule-based logic
- Classify risk into:
  - Low
  - Medium
  - High
- Provide:
  - Plain-English explanation of the risk
  - Practical, non-technical recommendations
- Return consistent results for the same inputs
- Be publicly accessible via a web browser

---

## 4. Out-of-Scope Functionality

The application will NOT:

- Perform network scanning
- Attempt to access or probe Wi-Fi networks
- Conduct penetration testing
- Verify technical accuracy of user inputs
- Enforce security changes
- Store sensitive user data
- Act as a compliance or audit tool

This project does not interact with real networks in any way.

---

## 5. Risk Model Characteristics

- Rule-based (not AI-driven)
- Deterministic (same input → same output)
- Explainable and transparent
- Designed for clarity over complexity

Rules are stored externally in structured data (JSON).

---

## 6. Assumptions

- Users provide honest and approximate answers
- Router age is estimated, not exact
- Recommendations are advisory only
- The system does not replace professional security assessments

---

## 7. Ethical and Safety Boundaries

This tool is intentionally designed to:
- Avoid intrusive behavior
- Avoid encouraging hacking or misuse
- Promote safe and responsible awareness

---

## 8. Scope Freeze (Phase 1)

The scope defined in this document is frozen for Phase 1.
New features or changes may be considered only in later phases.