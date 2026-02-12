# Change Management Policy & Procedures (Norfolk Industries)

## 1. Purpose
This document establishes the Change Management policy and procedures for Norfolk Industries to ensure that changes to Information Technology (IT), cloud, and supporting infrastructure services are planned, assessed, approved, implemented, validated, and recorded in a controlled manner. The objectives are to:
- Reduce the likelihood and impact of incidents caused by change.
- Protect confidentiality, integrity, and availability of services.
- Maintain compliance with the Information Security Management System (ISMS), SOX, GDPR, and audit requirements.
- Enable timely delivery of improvements with appropriate risk-based governance.

## 2. Scope
### 2.1 In scope
Change Management applies to all changes that can affect services delivered by **IT Infrastructure Services**, including:
- Cloud (Microsoft Azure primary; AWS secondary), on-prem data centers, networks, identity (Active Directory and Entra ID (Azure AD)), endpoints (Microsoft Intune and ConfigMgr), monitoring, backup, and related platforms.
- Security tooling and configurations (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk) when the change could affect service availability, detection/response, access, or compliance.
- Integrations and connectivity between **Operational Technology (OT)** and **Information Technology (IT)** environments, including remote access pathways and segmentation controls.

### 2.2 Out of scope
- Purely informational documentation updates that do not alter a Configuration Item (CI) behavior or risk posture (may be handled as documentation tasks).
- Business process changes that do not affect IT services or CIs (handled by business governance), unless they drive an IT change.

### 2.3 Environments
This policy applies to production and non-production environments. Production-impacting changes require stricter control and evidence.

## 3. Definitions (Glossary)
Norfolk Industries uses the following canonical terms (selected):
- **Change Advisory Board (CAB):** The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI):** Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Information Security Management System (ISMS):** The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Operational Technology (OT):** Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.
- **Service Level Objective (SLO):** A target level of service reliability or performance, measured by agreed metrics.

Additional Change Management terms used in this document:
- **Change Record:** The authoritative record in the ITSM tool for the lifecycle of a change, including approvals, risk, evidence, and outcomes.
- **Emergency Change:** A change required to restore service or address an active high-risk vulnerability or security incident with insufficient time for normal governance, subject to defined expedited controls and subsequent review.
- **Normal Change:** A change that requires assessment and approval, typically presented to the CAB.
- **Standard Change:** A pre-approved, low-risk, repeatable change executed using an approved procedure without case-by-case CAB review.

## 4. Policy Statement
Norfolk Industries requires that:
1. All in-scope changes are recorded and managed through the ITIL-aligned ITSM tool.
2. Each change is categorized (Standard, Normal, Emergency) and risk-assessed prior to implementation.
3. Required artifacts are documented and attached/linked to the Change Record before implementation, with limited, explicitly approved exceptions for Emergency Changes.
4. Approvals follow risk-based thresholds and the CAB process.
5. Changes are implemented by authorized personnel, during approved windows, with communications executed as planned.
6. Post-implementation validation is completed and recorded.
7. Evidence is retained in a time-bound, attributable, repeatable manner consistent with ISMS and audit expectations.

## 5. Governance, Roles, and Responsibilities
### 5.1 Governance model
- **Global IT Operations** defines global standards, minimum control requirements, and operating metrics.
- **Regional IT Operations** executes changes aligned to global governance, considering local operational needs and maintenance windows.
- The **Change Advisory Board (CAB)** provides cross-functional oversight for Normal Changes and governance for Emergency Changes.

### 5.2 RACI (aligned to raci_master.csv)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

### 5.3 Role responsibilities (operational)
- **Head of IT Infrastructure Services:** Accountable for Change Management effectiveness and CAB outcomes across IT Infrastructure Services.
- **ITSM Process Owner:** Owns Change Enablement practice design, workflow, controls, metrics, and continual improvement.
- **IT Operations Manager:** Coordinates operational readiness, implementation execution, on-call coverage, and major change communications.
- **Service Owner:** Accountable for service risk, service impacts, and service-level outcomes; ensures change aligns with service roadmap and SLOs.
- **Platform Owner:** Ensures technical design, standards compliance, and engineering readiness; validates test/rollback feasibility.
- **CISO / Security Engineer:** Ensures security risks, ISMS controls, and detection/response impacts are assessed; validates security-relevant changes.
- **IT Governance Manager:** Ensures compliance alignment, exception handling, evidence quality, and auditability.

## 6. Change Types and Categorization
### 6.1 Standard Change
A Standard Change is:
- Low risk, pre-authorized, repeatable, and follows an approved procedure (runbook).
- Implemented using a predefined implementation plan, rollback plan, test/validation steps, and communications approach.

Requirements:
- Must be linked to an approved Standard Change template and procedure.
- Must meet predefined risk criteria (see Appendix B).
- No CAB review required per instance; subject to periodic review and monitoring.

Examples (non-exhaustive):
- Adding a user to a pre-approved Entra ID group via approved workflow where no privileged access is granted.
- Routine certificate renewal using an approved method where service interruption is avoided or minimal and pre-communicated.
- Deployment of a pre-approved endpoint configuration profile through Microsoft Intune that is known low-risk.

### 6.2 Normal Change
A Normal Change is any change that is not Standard or Emergency and:
- Requires risk assessment and approval (often CAB).
- Includes planned outages, material risk, broad impact, or first-time procedures.

Requirements:
- Full required artifacts (Section 8).
- Risk scoring (Section 7).
- CAB review based on risk/impact and thresholds (Section 9).

### 6.3 Emergency Change
An Emergency Change is used only when immediate action is required to:
- Restore a critical service.
- Address an active or imminent security threat (e.g., active exploitation) where delay increases risk materially.
- Prevent significant business disruption or safety risk, including OT/IT boundary protections.

Requirements:
- Minimum artifacts documented prior to implementation (Section 8.3).
- Expedited approvals per Appendix C.
- Mandatory Post-Implementation Review (PIR) within required timelines (Section 14).

## 7. Risk Scoring and Change Assessment
### 7.1 Risk scoring objective
Every Normal and Emergency Change must be risk scored to determine approval path, governance level, communications, and validation rigor.

### 7.2 Risk dimensions
Risk score is calculated using:
- **Impact (1–5):** Business/service impact if change fails (availability, integrity, confidentiality, safety, compliance).
- **Likelihood (1–5):** Probability of failure or adverse outcome based on complexity and novelty.
- **Exposure modifiers:** Increase risk where applicable:
  - Production affecting
  - Identity/PAM related (Active Directory, Entra ID, CyberArk)
  - Network segmentation / OT remote access pathways
  - Security monitoring/detection changes (SIEM/EDR)
  - SOX-relevant systems
  - Broad endpoint fleet impact

### 7.3 Required assessment inputs
Change assessment must document:
- Affected services and CIs (CMDB references where available).
- Backout feasibility and rollback time.
- Test coverage and success criteria.
- Dependencies (upstream/downstream services).
- Security and privacy considerations (GDPR where personal data could be impacted).
- Operational readiness (staffing, monitoring, on-call coverage).

## 8. Required Artifacts and Documentation
### 8.1 Required artifacts for Normal Changes (minimum)
Each Normal Change must include the following artifacts, attached or linked within the Change Record:
1. **Implementation Plan**
   - Step-by-step tasks, responsible roles, sequence, and timing.
   - Automation references (pipelines/scripts) with version identifiers.
2. **Rollback Plan**
   - Conditions to invoke rollback.
   - Steps to restore prior state, including configuration and data considerations.
   - Expected time to complete rollback and validation steps post-rollback.
3. **Test Plan**
   - Pre-change checks (baseline).
   - Post-change validation steps and success criteria.
   - Evidence to capture (screenshots/log outputs/monitoring checks).
4. **Communications Plan**
   - Stakeholders, channels, timing, and customer-facing message (if applicable).
   - Planned maintenance window and expected impact.
5. **Risk Assessment**
   - Risk score, rationale, and mitigation steps.
6. **Implementation Window**
   - Start/end times in UTC and applicable regions; blackout conflicts checked.
7. **Monitoring Plan**
   - What signals will be monitored (metrics/logs/alerts) and for how long after change.
8. **Approvals**
   - Recorded approvals according to Section 9.

### 8.2 Required artifacts for Standard Changes
Standard Changes must:
- Reference the approved Standard Change procedure/template.
- Include required execution evidence (e.g., automation run output, validation checklist completion).
- Record pre/post validation results in the Change Record.

### 8.3 Minimum artifacts for Emergency Changes (prior to implementation)
Before executing an Emergency Change, the Change Record must include at minimum:
- Problem statement and urgency driver.
- Scope of change and affected services/CIs (best available information).
- High-level implementation steps and immediate rollback approach.
- Communications decision (who will be informed immediately).
- Approvals per Appendix C (expedited).

Full artifact completion is required after stabilization, prior to closure, including test/validation evidence and PIR.

## 9. Approvals and CAB Process
### 9.1 Approval principles
- Approval authority is commensurate with risk.
- Segregation of duties is maintained where feasible (requestor vs approver vs implementer), especially for SOX-relevant systems.
- CAB decisions and conditions are recorded in the Change Record.

### 9.2 CAB scope
CAB reviews:
- High and Medium risk Normal Changes per the risk matrix (Appendix B).
- Changes with cross-region impact or shared platform impact (e.g., identity, core network, SIEM/EDR platform).
- Changes affecting OT/IT connectivity controls.
- Changes with expected downtime above service thresholds or that may breach SLOs.

### 9.3 CAB participants (minimum)
- **CAB Chair:** Head of IT Infrastructure Services (or formally delegated chair)
- **Service Owner** (for the impacted service)
- **Platform Owner** (for the impacted platform/domain)
- **IT Operations Manager**
- **ITSM Process Owner**
- **CISO delegate** (CISO or Security Engineer) for security-impacting changes
- **Regional IT Operations** representation when regional execution is involved

### 9.4 CAB decision outcomes
CAB may:
- Approve as planned.
- Approve with conditions (e.g., added testing, narrower scope, additional comms, increased monitoring).
- Defer pending more information.
- Reject (with reasons and required remediation).

### 9.5 Emergency approval path
Emergency Changes follow the Emergency Change workflow (Appendix C) and must be reviewed by CAB retrospectively.

## 10. Change Windows, Maintenance, and Communications
### 10.1 Maintenance windows and blackout periods
- Standard and Normal Changes must be scheduled within approved maintenance windows aligned to regional business needs and 24×7 operations.
- Blackout periods (financial close, peak manufacturing periods, major plant events) must be checked prior to approval.
- For OT-related changes, plant maintenance windows and OT change constraints must be honored.

### 10.2 Communications requirements
Communications must:
- Be included in the Communications Plan.
- Clearly state impact, timing (UTC and local), expected user actions (if any), and support contacts.
- Include escalation path if issues occur.

Minimum notifications:
- Service Desk for any user-visible or potentially user-visible change.
- Global IT Operations and impacted Regional IT Operations teams for shared platform changes.
- Information security stakeholders for changes that modify security controls, monitoring, identity, PAM, or segmentation.

## 11. Detailed Procedures (End-to-End)
### 11.1 Submit a Change
1. Requestor creates a Change Record in the ITSM tool.
2. Select Change type (Standard/Normal/Emergency).
3. Identify impacted services and CIs.
4. Attach/link required artifacts per Section 8.
5. Propose implementation window, monitoring period, and communications plan.
6. For Standard Changes, select the Standard Change template/procedure reference.

**Minimum quality gate:** A change cannot proceed to approval without required artifacts, except Emergency Changes meeting Section 8.3.

### 11.2 Assess and Risk Score
1. Service Owner and Platform Owner review scope, dependencies, and technical readiness.
2. Perform risk scoring using Appendix B.
3. Identify security/privacy considerations:
   - Identity and access impact (Active Directory/Entra ID/CyberArk)
   - Logging/detection impact (SIEM/EDR)
   - Personal data impact (GDPR)
4. Confirm test plan adequacy and rollback feasibility.
5. Confirm operational readiness: staffing, on-call, monitoring, and Service Desk readiness.

### 11.3 Approve
1. Route approvals based on risk tier:
   - Low risk: Service Owner + Platform Owner approvals (and CISO delegate if security-impacting).
   - Medium/High: CAB review and approval.
2. Record approvals and any conditions in the Change Record.
3. If conditions are imposed, update artifacts accordingly and re-validate readiness before implementation.

### 11.4 Implement
1. Execute implementation steps as documented.
2. Capture execution evidence:
   - Automation outputs, command logs, pipeline run IDs, configuration diffs, or screenshots as appropriate.
3. Maintain real-time coordination with IT Operations Manager for changes with service impact.
4. Follow safety and access constraints for any OT/IT boundary work, including strict remote access controls.

### 11.5 Validate (Post-Implementation)
1. Execute validation steps from the test plan.
2. Verify:
   - Service health and monitoring signals
   - Authentication/authorization flows (where applicable)
   - Logging/telemetry continuity (SIEM/EDR) for security-impacting changes
3. Document validation results and attach evidence.

### 11.6 Close the Change
1. Confirm communications were sent (completion notice if applicable).
2. Update Change Record with:
   - Actual start/end time
   - Implementation outcome (successful/with issues/rolled back)
   - Evidence links/attachments
   - Any incidents/problems raised as a result
3. Ensure CMDB/CI updates are completed when the change alters CI attributes or relationships.

### 11.7 Post-Implementation Review (PIR)
PIR is required when:
- Change caused an incident, outage, security event, or near miss.
- Emergency Change was executed.
- High-risk change, or CAB requested PIR.

PIR steps:
1. Conduct review within the timelines in Section 14.
2. Document:
   - What was intended vs what occurred
   - Root cause of any issues
   - Corrective and preventive actions
   - Whether the change should become a Standard Change (if repeatable and low risk)
3. Link PIR record and actions to Problem Management where appropriate.

## 12. Emergency Change Procedures
Emergency Changes must follow Appendix C workflow, including:
- Immediate risk-based approvals.
- Rapid communications to key stakeholders.
- Mandatory stabilization validation.
- Retrospective CAB review and PIR.

Emergency Changes must not be used to bypass normal governance for convenience.

## 13. Change Evidence and Recordkeeping
### 13.1 Evidence requirements
Evidence must follow the principles in standards.json:
- Time-bound, attributable, repeatable.
- Includes approvals, logs, and validation artifacts where applicable.

### 13.2 Retention and accessibility
- Change Records and evidence must be retained in the ITSM tool and approved repositories in accordance with Norfolk Industries record retention practices, ISMS requirements, and audit needs.
- Evidence must be accessible for Internal Audit and compliance reviews.

### 13.3 Evidence examples
- CAB meeting minutes/decision record.
- Approval logs from ITSM workflow.
- Pipeline run records and artifacts.
- Pre/post monitoring snapshots.
- Validation checklist completion.

## 14. Metrics, Monitoring, and Continual Improvement
### 14.1 Key metrics (minimum)
Tracked by Global IT Operations and the ITSM Process Owner:
- Change success rate (% without incident or rollback).
- Emergency Change rate (% of total changes).
- Change-related incident rate.
- Mean time to implement and validate changes.
- CAB deferral rate (quality indicator).
- Standard Change adoption rate.

### 14.2 PIR timelines
- Emergency Change PIR: within 5 business days of implementation.
- High-risk change PIR (if required): within 10 business days.
- Corrective actions tracked to completion and reviewed for effectiveness.

## 15. Exceptions and Risk Acceptance
- Exceptions to this policy (including bypassing required artifacts or approvals) require documented risk acceptance.
- High-risk exceptions follow the “Exception approval (high risk)” RACI line and must include:
  - Risk description and justification
  - Compensating controls
  - Expiration date and review schedule
  - Approver names and dates in the Change Record

## 16. Compliance, Audit, and Control Mapping
### 16.1 Control mapping overview
This policy supports Norfolk Industries compliance with ISO/IEC 27001 (ISMS), ISO/IEC 22301 (BCMS), ITIL 4, COBIT 2019, NIST CSF, SOC 2, GDPR, and SOX through controlled change governance, evidence, and risk management.

### 16.2 Conceptual mappings (control-to-evidence)
| Framework | Area | Change Management Alignment | Typical Evidence |
|---|---|---|---|
| ISO/IEC 27001 | Annex A control areas (conceptual) | Controlled change processes, access governance impacts assessed, logging maintained | Change Records, approvals, test/rollback plans, validation evidence, CAB minutes |
| NIST CSF | Protect / Detect / Respond | Changes are reviewed for security impact; monitoring maintained; emergency changes handled with governance | Risk scoring, security review notes, SIEM/EDR validation, PIR |
| SOC 2 TSC | Security, Availability, Confidentiality | Authorized changes reduce unauthorized modification risk; availability protected by planning and rollback | Approval logs, maintenance communications, success/rollback rates, incident linkage |
| ITIL 4 | Change Enablement | Standard/Normal/Emergency workflows, CAB governance | ITSM workflow states, CAB outcomes, PIR records |
| COBIT 2019 | BAI / DSS / MEA | Managed change delivery, operational stability, monitoring of performance | KPI reports, audit trails, exception tracking |
| SOX | Financial controls | Segregation of duties, approvals, audit trails for in-scope systems | Approval routing, evidence of testing, access control attestations |
| GDPR | Privacy | Assessment of personal data impacts and minimized risk | Change assessment notes, data flow impact statements where applicable |

## 17. Tools, Integrations, and CMDB Requirements
### 17.1 ITSM tool usage
- The ITSM tool is the system of record for Change Records, approvals, CAB decisions, and evidence references.
- Work notes must be sufficient to reconstruct what was done, by whom, when, and with what result.

### 17.2 CMDB and CIs
- Changes must reference impacted CIs when those CIs exist in the CMDB.
- If a change modifies CI attributes, relationships, or service dependencies, updates must be made as part of change closure.

### 17.3 Monitoring and security tooling validation
For changes impacting monitoring/security:
- Validate continued telemetry ingestion to the SIEM (e.g., Microsoft Sentinel).
- Validate EDR health and policy compliance (e.g., Microsoft Defender for Endpoint).
- Validate vulnerability scanning coverage (e.g., Tenable/Nessus) if network paths or credentials are changed.

## 18. Training and Awareness
- All personnel involved in requesting, approving, implementing, or reviewing changes must complete Change Management process training at onboarding and annually thereafter (or per ISMS training cadence).
- CAB participants must be trained on risk scoring, evidence expectations, and emergency governance.
- Specialized training is required for OT/IT boundary changes and strict remote access controls.

## 19. Document Control
### 19.1 Ownership
- **Accountable:** Head of IT Infrastructure Services  
- **Responsible (process design and lifecycle):** ITSM Process Owner  
- **Compliance oversight:** IT Governance Manager, CISO (ISMS alignment)  

### 19.2 Review and maintenance
- Reviewed at least annually and upon significant changes to tooling, governance, or audit requirements.
- Updates require documented review and approval consistent with the governance model.

---

## Appendix A: Change Record Templates (Markdown)

### A.1 Normal Change Record Template
| Field | Required | Guidance |
|---|---:|---|
| Change title | Yes | Use clear, action-oriented title including platform/service. |
| Change type | Yes | Standard / Normal / Emergency. |
| Requestor | Yes | Named individual. |
| Service Owner | Yes | Accountable for service impact. |
| Platform Owner | Yes | Accountable for technical readiness. |
| Affected services | Yes | Include customer-facing impacts where applicable. |
| Affected CIs | Yes | Reference CMDB CIs and relationships. |
| Region(s) | Yes | North America / Europe / APAC; note cross-region dependencies. |
| Planned window (UTC + local) | Yes | Include start/end and maintenance window alignment. |
| Implementation plan | Yes | Attach/link; include step owner per step. |
| Rollback plan | Yes | Attach/link; include rollback triggers and timing. |
| Test plan | Yes | Attach/link; include pre/post checks and success criteria. |
| Monitoring plan | Yes | Signals, dashboards, alerts, duration. |
| Communications plan | Yes | Audience, channel, send times, message text. |
| Risk score (Impact × Likelihood) | Yes | Include rationale and mitigations. |
| Security impact assessment | Yes | Identity/PAM/logging/data considerations; CISO delegate review if needed. |
| Approvals | Yes | Workflow approvals + CAB decision where applicable. |
| Implementation evidence | Yes | Logs, pipeline run IDs, config diffs, screenshots. |
| Validation evidence | Yes | Proof of success criteria; monitoring snapshots. |
| Actual start/end | Yes | For audit trail and metrics. |
| Outcome | Yes | Successful / Successful with issues / Rolled back / Failed. |
| Related incidents/problems | Conditional | Link if created or referenced. |
| PIR required | Conditional | Mandatory for Emergency and as defined in Section 11.7. |
| Closure notes | Yes | Summary of what was delivered and final status. |

### A.2 Emergency Change Record Template (Minimum Pre-Implementation)
| Field | Required | Guidance |
|---|---:|---|
| Change title | Yes | Include “Emergency” and impacted service/platform. |
| Urgency driver | Yes | Outage, active exploit, containment, safety risk, etc. |
| Scope (high level) | Yes | What will be changed immediately. |
| Affected services/CIs | Yes | Best available; refine post-stabilization. |
| Implementation steps (high level) | Yes | Minimum viable steps to stabilize. |
| Rollback approach (high level) | Yes | Immediate backout approach and triggers. |
| Communications decision | Yes | Who is notified now; who is notified after stabilization. |
| Approvals obtained | Yes | Record names, times, and method per Appendix C. |
| Validation approach | Yes | How stabilization will be confirmed. |

### A.3 Standard Change Template (Definition Record)
| Field | Required | Guidance |
|---|---:|---|
| Standard Change name | Yes | Unique, descriptive. |
| Scope and prerequisites | Yes | Conditions that must be true to use as Standard. |
| Step-by-step procedure | Yes | Repeatable steps; tooling references; versioning. |
| Risk classification | Yes | Must meet Low risk criteria. |
| Validation checklist | Yes | Explicit success criteria. |
| Rollback procedure | Yes | Repeatable rollback steps and triggers. |
| Communications | Yes | Whether notification is required and standard message. |
| Approvers for template | Yes | Standard approval per governance. |
| Review cadence | Yes | Periodic review to confirm remains low-risk and current. |

---

## Appendix B: Risk Scoring Matrix (Impact × Likelihood)

### B.1 Impact scale (1–5)
| Score | Impact description (service/business) |
|---:|---|
| 1 | Negligible: no user impact; no compliance/security impact. |
| 2 | Minor: limited user impact; easily reversible; no material compliance risk. |
| 3 | Moderate: partial service degradation or limited outage; possible minor compliance exposure. |
| 4 | Major: significant outage/degradation, multi-site impact, or security control impairment. |
| 5 | Critical: enterprise-wide outage, safety risk, significant data/security event potential, or major compliance/SOX exposure. |

### B.2 Likelihood scale (1–5)
| Score | Likelihood description (probability of adverse outcome) |
|---:|---|
| 1 | Rare: proven runbook; extensive automation; repeatedly successful. |
| 2 | Unlikely: minor variation from known procedure; good testing coverage. |
| 3 | Possible: moderate complexity; some manual steps; limited prior history. |
| 4 | Likely: complex, multi-component dependencies; limited test fidelity. |
| 5 | Almost certain: highly novel, time-constrained, or unstable prerequisites. |

### B.3 Risk tiering and required approvals
Risk Score = Impact × Likelihood.

| Risk score | Tier | Default change type guidance | Approval path |
|---:|---|---|---|
| 1–4 | Low | Standard (if pre-approved) or Normal | Service Owner + Platform Owner; CISO delegate if security-impacting |
| 5–9 | Medium | Normal | CAB review required; conditions likely |
| 10–25 | High | Normal (or Emergency if urgent) | CAB approval required; heightened comms and validation; exception handling if artifacts incomplete |

### B.4 Exposure modifiers (increase governance)
If any of the following apply, treat as at least **Medium** unless explicitly justified and documented:
- Affects Active Directory, Entra ID, or CyberArk privileged access pathways
- Alters network segmentation or OT remote access controls
- Reduces logging, alerting, or telemetry for SIEM/EDR
- Impacts SOX-relevant services or financial reporting systems
- Broad endpoint fleet changes (e.g., Intune policy affecting security baseline)
- Cross-region shared platform impacts (Global IT Operations coordination required)

---

## Appendix C: Emergency Change Workflow (Runbook)

### C.1 Trigger conditions (must meet at least one)
- Active production outage with material business impact.
- Active security incident containment/eradication requirement.
- High-severity vulnerability with credible active exploitation requiring immediate mitigation.
- OT/IT boundary risk requiring immediate containment consistent with strict remote access controls.

### C.2 Workflow steps
1. **Declare emergency**
   - IT Operations Manager confirms emergency criteria and initiates Emergency Change Record.
2. **Rapid assessment (10–30 minutes target)**
   - Service Owner + Platform Owner confirm minimum scope and stabilization plan.
   - Security Engineer engaged if security-related.
3. **Expedited approvals**
   - Obtain approvals via the ITSM emergency workflow or recorded communications.
   - Minimum approval set:
     - Head of IT Infrastructure Services (or delegated CAB Chair)
     - Service Owner
     - CISO (or Security Engineer delegate) for security-impacting emergencies
4. **Execute change**
   - Implement minimum necessary steps to stabilize.
   - Capture execution evidence as feasible.
5. **Validate stabilization**
   - Confirm service restoration and monitoring stability.
   - Confirm security telemetry continuity if applicable.
6. **Communicate**
   - Send immediate stakeholder update; provide user-facing update if required.
7. **Retrospective governance**
   - Present to next CAB for review:
     - Was Emergency classification appropriate?
     - Were risks managed and documented?
     - What preventive actions are required?
8. **PIR**
   - Complete within 5 business days; track actions to completion.

### C.3 Emergency change safeguards
- Limit scope to stabilization; defer improvements to a Normal Change.
- Document any missing artifacts and complete them after stabilization.
- If rollback is not feasible, document compensating controls and increased monitoring.

---

## Appendix D: Evidence List (Audit-Ready)
The following evidence types are required to demonstrate control operation and compliance alignment:

| Evidence item | Applies to | Minimum requirement |
|---|---|---|
| Change Record with unique ID | All changes | Complete lifecycle states, timestamps, and ownership |
| Risk score and rationale | Normal/Emergency | Recorded and tied to approval path |
| Implementation plan | Normal | Attached/linked and version-identified |
| Rollback plan | Normal | Triggers, steps, and estimated time |
| Test plan and validation results | Standard/Normal/Emergency | Success criteria and proof captured |
| Communications plan and sent notifications | Normal/Emergency | Message content and send timestamps |
| Approval logs | All changes | Approver identity, time, decision, conditions |
| CAB decision record/minutes | CAB-reviewed changes | Decision outcome and conditions documented |
| Execution evidence | All changes | Logs/pipeline IDs/config diffs where applicable |
| Monitoring evidence | Medium/High/Emergency | Pre/post snapshots and observation period |
| PIR report | Emergency and required cases | Findings, actions, owners, due dates |
| Exception/risk acceptance record | Exceptions | Justification, compensating controls, expiry, approvals |