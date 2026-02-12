# IT Infrastructure Governance Policy (Norfolk Industries)

## 1) Document Control

### 1.1 Document Metadata

| Field | Value |
|---|---|
| Document Title | IT Infrastructure Governance Policy (Norfolk Industries) |
| Document Owner | IT Governance Manager |
| Executive Sponsor | Head of IT Infrastructure Services |
| Security Oversight | CISO |
| Applicability | Norfolk Industries (all regions; all IT Infrastructure Services activities; interfaces with Operational Technology (OT)) |
| Confidentiality | Internal |
| Effective Date | 2025-12-26 |
| Next Scheduled Review | 2026-12-26 |
| Review Cadence | At least annually and upon significant change to operating model, regulatory obligations, or material incident/audit finding |
| Authoring System | Norfolk Industries Official Documentation Authoring System |

### 1.2 Version History

| Version | Date | Author | Summary of Changes | Approved By |
|---|---:|---|---|---|
| 1.0 | 2025-12-26 | IT Governance Manager | Initial release of IT Infrastructure Governance Policy establishing governance bodies, policy hierarchy, decision flows, standards alignment, and control-to-evidence requirements. | Head of IT Infrastructure Services |

### 1.3 Approval Authority

| Approval Item | Approver Role | Notes |
|---|---|---|
| Policy approval | CIO (A), Head of IT Infrastructure Services (R) | Per RACI master: CIO accountable for approval; Head of IT Infrastructure Services responsible for ensuring readiness and implementation. |
| Security governance alignment | CISO (C) | Consulted for ISMS alignment and risk posture. |
| Audit readiness and evidence sufficiency | Internal Audit (I/A for evidence coordination) | Internal Audit independently assesses; evidence coordination responsibility per RACI master. |

### 1.4 Distribution & Communication

| Audience | Distribution Channel | Minimum Requirement |
|---|---|---|
| Global IT Operations | ITSM knowledge base + governance repository | Read and apply to all governed activities |
| Regional IT Operations | ITSM knowledge base + regional operational briefings | Read and apply to regional execution |
| Service Owners / Platform Owners | Governance repository + CAB/ARB communications | Apply controls, evidence, and decisioning |
| Information Security stakeholders | ISMS portal + Security Steering communications | Validate alignment, receive metrics |
| Internal Audit | Audit portal / evidence index | Access to evidence catalog and decision logs |

---

## 2) Purpose & Objectives

### 2.1 Purpose
This policy establishes a consistent governance framework for IT Infrastructure Services at Norfolk Industries to ensure reliable, secure, compliant, and auditable delivery of infrastructure platforms and operations across North America, Europe, and APAC. The policy aligns governance with ISO/IEC 27001 (ISMS), ISO/IEC 22301 (BCMS), ITIL 4, COBIT 2019, NIST CSF and NIST SP 800-53 concepts, SOC 2 Trust Services Criteria, GDPR, and SOX requirements.

### 2.2 Objectives
This policy’s objectives are to:

1. **Standardize governance** across Global IT Operations and Regional IT Operations while enabling regional execution.
2. **Define decision rights and accountability** for infrastructure architecture, change, risk, and operational performance.
3. **Reduce operational risk** through controlled change, secure architecture, and consistent control implementation.
4. **Ensure auditability** through evidence principles: time-bound, attributable, repeatable, with approvals, logs, and validation artifacts where applicable.
5. **Integrate IT and OT boundaries** with strict remote access controls and segmented networks to protect Operational Technology (OT).
6. **Support 24×7 operations** through clear escalation paths, incident governance, and service continuity alignment.
7. **Enable continual improvement** driven by metrics, audit findings, problem management insights, and risk reviews.

---

## 3) Scope & Applicability (IT + OT Boundary)

### 3.1 In Scope
This policy applies to all Norfolk Industries personnel and third parties performing activities that design, implement, operate, or change IT Infrastructure Services, including:

- Hybrid cloud infrastructure (Microsoft Azure primary; AWS secondary)
- On-prem data centers
- Identity services: Active Directory and Entra ID (Azure AD) (first mention), then Entra ID
- Endpoint management: Microsoft Intune and ConfigMgr where needed
- Security tooling integrated with IT Infrastructure Services (SIEM such as Microsoft Sentinel; EDR such as Microsoft Defender for Endpoint; vulnerability scanning such as Tenable/Nessus; PAM such as CyberArk)
- Monitoring and event management platforms
- Backup and recovery platforms and processes
- Network services (LAN/WAN/Wi-Fi, DNS, DHCP, IPAM, firewalls, remote access)
- Configuration and asset management practices (CMDB and Configuration Items (CIs))
- Governance activities: Change Advisory Board (CAB), Architecture Review Board (ARB), Security Steering Committee (SSC), metrics reviews, risk reviews
- Interactions with the ITIL-aligned ITSM tool (for example, ServiceNow)

### 3.2 Out of Scope (but interfaces defined)
- Business application development governance, except where application changes impact infrastructure CIs or shared platforms.
- Facility systems not connected to IT networks, except where risk assessments require review.
- OT engineering governance within plant operations, except where OT connects to IT networks or uses IT-managed identity, remote access, monitoring, or backup services.

### 3.3 IT and OT Boundary
Norfolk Industries operates integrated environments where OT (SCADA, MES, plant networks) interfaces with IT. This policy applies to IT Infrastructure Services that:

- Provide **connectivity** to or from OT zones
- Provide **identity** services used by OT operators, engineers, or service accounts
- Provide **remote access** solutions to OT environments
- Provide **monitoring, logging, vulnerability management**, or **backup** capabilities that include OT assets
- Provide **segmentation controls** and gateway services between IT and OT networks

#### 3.3.1 Boundary Principles
1. **Segmentation First:** OT networks remain segmented from IT networks, with explicitly approved and monitored connections.
2. **Least Privilege and PAM:** Privileged access to OT-connected infrastructure uses PAM controls and is time-bound.
3. **Controlled Remote Access:** Remote access to OT is restricted, logged, monitored, and subject to CAB-approved change for material modifications.
4. **Operational Safety:** Where safety and uptime requirements conflict with standard IT practices (e.g., patch timing), exceptions must be documented and risk accepted per Exceptions Management.

---

## 4) Definitions & Acronyms (Aligned to glossary.json)

### 4.1 Definitions (Canonical)
| Term | Definition |
|---|---|
| IT Infrastructure Services | The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations. |
| Global IT Operations | Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure. |
| Regional IT Operations | Regional teams executing day-to-day operations, local support, and implementation aligned to global governance. |
| Information Security Management System (ISMS) | The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001. |
| Change Advisory Board (CAB) | The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management. |
| Configuration Item (CI) | Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references. |
| Operational Technology (OT) | Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks. |
| Service Level Objective (SLO) | A target level of service reliability or performance, measured by agreed metrics. |
| Recovery Point Objective (RPO) | Maximum tolerable amount of data loss measured in time. |
| Recovery Time Objective (RTO) | Target time to restore a service after disruption. |

### 4.2 Acronyms
| Acronym | Meaning |
|---|---|
| ARB | Architecture Review Board |
| BCMS | Business Continuity Management System (ISO/IEC 22301-aligned program) |
| CAB | Change Advisory Board |
| CI | Configuration Item |
| CMDB | Configuration Management Database |
| COBIT | Control Objectives for Information and Related Technologies |
| DPO | Data Protection Officer (DPO) |
| EDR | Endpoint Detection and Response |
| GDPR | General Data Protection Regulation |
| IAM | Identity and Access Management |
| ISMS | Information Security Management System (ISMS) |
| ITIL | Information Technology Infrastructure Library |
| KPI | Key Performance Indicator |
| MES | Manufacturing Execution System |
| OT | Operational Technology |
| PAM | Privileged Access Management |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SCADA | Supervisory Control and Data Acquisition |
| SIEM | Security Information and Event Management |
| SLO | Service Level Objective |
| SOX | Sarbanes-Oxley Act |
| SOC 2 | Service Organization Control 2 |

---

## 5) Governance & Ownership

### 5.1 Governance Model Overview
Norfolk Industries uses **centralized governance with regional execution**:

- **Global IT Operations** establishes common policies, standards, architectural guardrails, and global oversight mechanisms.
- **Regional IT Operations** executes operations, implements approved changes, maintains local runbooks, and supports service continuity and incident response within defined guardrails.
- Governance decisions are made through defined bodies (CAB, ARB, SSC) with documented decision logs and evidence.

### 5.2 Governance Bodies (Required Charters)

#### 5.2.1 Change Advisory Board (CAB)
**Purpose:** Ensure changes to IT Infrastructure Services are assessed for risk, approved appropriately, scheduled responsibly, communicated clearly, and validated post-implementation.

**Scope:** Normal and Emergency Changes affecting infrastructure CIs, including cloud, network, identity, endpoint, monitoring, backup, and OT-connected gateways.

**Authority:** Approves, rejects, defers, or requests changes to submitted change records; mandates risk mitigations and backout plans.

**Cadence:**
- Standard CAB: Weekly (per region scheduling) with global coordination for cross-region impacts.
- Emergency CAB: Convened within 60 minutes when required for urgent risk mitigation.

**Minimum Inputs:**
- Change record with scope, affected CIs, risk rating, backout plan, validation plan, communications plan.

**Minimum Outputs:**
- Decision (approve/reject/defer) and documented conditions; implementation window; evidence requirements.

#### 5.2.2 Architecture Review Board (ARB)
**Purpose:** Ensure infrastructure architecture decisions align to Norfolk Industries standards, security requirements, reliability goals, and operational supportability.

**Scope:**
- New platforms, material design changes, network segmentation design, identity architecture, cloud landing zones, monitoring/backup architecture, OT/IT integration pathways.

**Authority:**
- Approves architecture patterns and exceptions; mandates remediation plans for non-compliant designs; escalates risk acceptance requests.

**Cadence:**
- Bi-weekly standard ARB
- Ad-hoc ARB for critical initiatives or high-risk designs

**Minimum Inputs:**
- Architecture decision proposal, diagrams, threat/risk considerations, operational model, cost model, and compliance mapping.

**Minimum Outputs:**
- Architecture Decision Record (ADR) with decision and rationale; required guardrails; implementation conditions and verification steps.

#### 5.2.3 Security Steering Committee (SSC)
**Purpose:** Provide security governance direction for infrastructure risk posture aligned to the ISMS, ensuring prioritized remediation, consistent control operation, and effective oversight.

**Scope:**
- ISMS-aligned control posture for IT Infrastructure Services, security tooling health, vulnerability remediation, incident trends, audit readiness, GDPR/SOX implications for infrastructure controls.

**Authority:**
- Prioritizes remediation; endorses risk acceptance recommendations; escalates material risk to CIO; sets security-related metrics expectations.

**Cadence:**
- Monthly

**Minimum Inputs:**
- Risk register extracts, vulnerability metrics, incident trends, audit findings and remediation status, exceptions log.

**Minimum Outputs:**
- Approved security priorities; decisions on risk acceptance path; directives for control validation and evidence capture.

### 5.3 Policy Hierarchy and Relationship (Policy → Standard → Procedure)
Norfolk Industries uses a three-tier documentation hierarchy:

1. **Policy** (this document): states mandatory outcomes and governance requirements; must be approved and reviewed per document control.
2. **Standards**: define mandatory controls, configurations, and technical requirements (e.g., identity baseline, network segmentation standard).
3. **Procedures / Runbooks**: step-by-step operational execution instructions (e.g., CAB meeting procedure, firewall change runbook).

**Rules:**
- Standards and procedures must not conflict with policy.
- Where regional execution requires regional procedures, they must align to global standards and include region-specific operational details.
- All tiers must be stored in the governance repository and linked from the ITSM knowledge base.

### 5.4 RACI Matrix (Aligned to roles.json + raci_master.csv)
The following RACI applies to IT Infrastructure governance activities. Where raci_master.csv is authoritative, it is followed.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

---

## 6) Policy Statements

### 6.1 Governance is Mandatory for All Material Infrastructure Activities
All material changes, designs, and operational decisions affecting IT Infrastructure Services must follow the governance bodies and processes defined in this policy, including documentation, approvals, and evidence retention.

### 6.2 Decision Rights and Accountability
- The **Head of IT Infrastructure Services** is accountable for infrastructure governance effectiveness and operational outcomes.
- **Service Owners** are accountable for end-to-end service performance, risk posture, and compliance for their services.
- **Platform Owners** are accountable for architecture and engineering standards in their technical domains.
- **IT Operations Manager** is responsible for operational execution readiness, including 24×7 operations and incident coordination.
- The **CISO** provides ISMS oversight and ensures security requirements are integrated into governance.
- The **IT Governance Manager** owns governance process integrity, policy lifecycle, compliance tracking, and audit coordination.

### 6.3 Standardized Change Enablement
All changes to production infrastructure CIs must be recorded in the ITSM tool and follow Change Enablement practices, including risk assessment, testing, backout, communications, and post-implementation validation.

### 6.4 Security by Design and Default
Infrastructure services must be designed, implemented, and operated to meet ISMS requirements and align with NIST CSF functions: Identify, Protect, Detect, Respond, Recover. Control operation must be evidenced.

### 6.5 OT/IT Integration Requires Enhanced Controls
Any connectivity, identity integration, remote access, or shared services involving Operational Technology (OT) requires ARB review (for architecture) and CAB approval (for change), with enhanced logging, segmentation, and access controls.

### 6.6 Evidence is a Required Output of Governance
For all governed activities, evidence must be produced and retained. Evidence must be **time-bound, attributable, and repeatable**, including approvals, logs, and validation artifacts where applicable.

### 6.7 Regional Execution Within Global Guardrails
Regional IT Operations must execute within Global IT Operations governance guardrails. Variations require formal exceptions.

### 6.8 Supplier and Third-Party Governance
Third parties operating or changing infrastructure must follow this policy, including CAB participation when applicable, and must provide evidence artifacts suitable for audits.

---

## 7) Detailed Processes (Governance Decision Flows, Escalation Paths)

### 7.1 Governance Decision Taxonomy
Decisions fall into four categories:

1. **Architecture Decisions** (ARB): patterns, designs, material platform choices, network segmentation, landing zones, identity architecture.
2. **Change Decisions** (CAB): implementation and modification of production CIs; scheduling and risk approvals.
3. **Security Risk Decisions** (SSC + ISMS): control posture, vulnerability remediation priorities, risk acceptance recommendations.
4. **Operational Performance Decisions** (Operations Reviews): SLO attainment, incident/problem trends, reliability improvements, service continuity readiness.

### 7.2 Decision Flow: Architecture → Change → Validation
| Stage | Trigger | Governing Body | Required Artifacts | Output |
|---|---|---|---|---|
| Architecture Intake | New service/platform; material redesign; OT integration | ARB | Architecture proposal, diagrams, operational model, control considerations | ADR with decision and conditions |
| Change Planning | Implementation of approved architecture | CAB | Change record(s), risk assessment, test plan, backout plan | Approved schedule and conditions |
| Implementation | Execution in production | Regional IT Operations / Platform teams | Implementation logs, configuration changes, peer review evidence | Completed change with notes |
| Validation | Post-change verification | CAB (post-implementation review) | Validation evidence, monitoring confirmation | Change closure approval; follow-ups |

### 7.3 Escalation Paths
#### 7.3.1 Operational Escalation (24×7)
- **Service Desk Manager** escalates major incidents to **IT Operations Manager**.
- **IT Operations Manager** escalates to **Head of IT Infrastructure Services** for cross-region or high-impact infrastructure events.
- Security-impacting incidents are escalated to the **CISO** and **Security Engineer** (operational integration).
- OT-impacting incidents require coordination with plant stakeholders via established plant incident channels while maintaining segmentation and access controls.

#### 7.3.2 Governance Escalation
- CAB cannot approve high-risk exceptions to standards without routing to **Head of IT Infrastructure Services** and **CISO** (consulted) and, for high-risk exceptions, **CIO** accountable per RACI.
- ARB escalates unresolved architecture risk decisions to the **Head of IT Infrastructure Services** and SSC.
- SSC escalates material risk posture issues to the **CIO**.

### 7.4 “3 Lines of Defense” Model (Norfolk Industries Alignment)
Norfolk Industries applies a “3 Lines of Defense” model to IT Infrastructure governance:

| Line of Defense | Primary Responsibility | Norfolk Industries Mapping (Infrastructure) |
|---|---|---|
| First Line | Own and manage risk through operational controls | IT Infrastructure Services (Service Owners, Platform Owners, IT Operations Manager, engineers) operate controls daily and generate evidence |
| Second Line | Set policy/standards and oversee risk/control effectiveness | IT Governance Manager and CISO (ISMS oversight) provide governance, monitoring, and compliance tracking |
| Third Line | Independent assurance | Internal Audit assesses control design and operating effectiveness |

---

## 8) Step-by-Step Procedures (Governance Meetings, CAB Cadence, Exception Handling)

### 8.1 CAB Meeting Procedure (Standard CAB)
1. **Preparation (T-2 business days)**
   - ITSM Process Owner ensures change calendar is current.
   - Service Owners confirm change records include: scope, affected CIs, implementation plan, backout plan, test evidence, validation steps, communications plan.
   - IT Operations Manager confirms resource readiness and conflict checks.

2. **Pre-CAB Triage (T-1 business day)**
   - IT Governance Manager reviews completeness and evidence expectations.
   - Security Engineer flags changes with security control impact.
   - Platform Owners validate technical feasibility and standards alignment.

3. **CAB Session (weekly)**
   - Chaired by Head of IT Infrastructure Services (accountable for CAB chairing per RACI).
   - Agenda follows the CAB Agenda Template (Appendix B).
   - Each change is reviewed for risk, customer impact, OT impact, and rollback readiness.

4. **Decision Recording**
   - Decisions are recorded in ITSM and in the Decision Log Template (Appendix C).
   - Any conditional approvals must list measurable conditions and verification steps.

5. **Implementation Coordination**
   - Regional IT Operations schedules execution, ensures communications, and ensures on-call readiness.
   - Service Desk Manager prepares user-facing notices where required.

6. **Post-Implementation Review**
   - Validate monitoring, service health, and business confirmation as applicable.
   - Capture evidence: logs, configuration diffs, screenshots, test output, monitoring dashboards, approvals.

### 8.2 Emergency CAB Procedure (eCAB)
1. **Trigger**
   - Active incident requiring urgent mitigation or security containment.
2. **Convene**
   - IT Operations Manager requests eCAB; Head of IT Infrastructure Services chairs or delegates to a designated CAB chair.
3. **Minimum Required Information**
   - Risk statement, urgency, planned action, rollback approach, expected impact, and monitoring plan.
4. **Decision**
   - Approve/reject with conditions; record in ITSM immediately.
5. **After Action**
   - Within 2 business days, perform a retrospective and document follow-up actions; route to CAB for formal closure review.

### 8.3 ARB Procedure
1. Intake submission with architecture proposal and diagrams.
2. Platform Owner presents; Security Engineer provides security considerations.
3. ARB evaluates against architecture principles (Section 9) and control impacts (Section 10–12).
4. Decision documented as an ADR; exceptions routed to Exceptions Management if required.

### 8.4 Security Steering Committee Procedure
1. IT Governance Manager compiles metrics (Section 16) and exceptions log (Section 13).
2. CISO reviews risk posture and ISMS alignment items.
3. Decisions recorded; prioritized remediation actions assigned to Service Owners/Platform Owners.

### 8.5 Exception Handling Procedure (Operational Steps)
1. **Identify non-compliance or required deviation** (standard or policy requirement).
2. **Document exception request** using the Exception Request Form (Appendix E).
3. **Risk assessment**
   - Service Owner and Platform Owner identify security, availability, privacy, and SOX impacts.
   - Security Engineer provides control impact analysis.
4. **Approval routing**
   - Low/medium risk: Head of IT Infrastructure Services approves; CISO consulted.
   - High risk: routed for exception approval (high risk) per RACI: CIO accountable; Head of IT Infrastructure Services and CISO responsible.
5. **Implement compensating controls**
   - Must be explicitly listed with validation evidence.
6. **Record and track**
   - Exceptions are time-bound, include review date, and are tracked to closure or renewal.

---

## 9) Technical Standards & Requirements (Architecture Principles; standards.json alignment)

### 9.1 Architecture Principles (Mandatory)
1. **Security-by-Default:** Default configurations must minimize exposure; privileged access is controlled and logged.
2. **Resilience and Recoverability:** Services must meet defined RTO/RPO requirements and validate backups and recovery procedures.
3. **Least Privilege:** Access granted only as needed; administrative operations use PAM.
4. **Segmentation and Zero Trust Concepts:** Network segmentation, identity-based access, continuous verification; OT boundary controls are explicit.
5. **Standard Platforms First:** Prefer approved patterns and shared services from Global IT Operations.
6. **Observability:** All critical infrastructure must be monitored with actionable alerting and integrated logging to the SIEM.
7. **Configuration as a CI:** Infrastructure configurations must be represented as Configuration Items (CIs) and traceable to change records.
8. **Automation with Controls:** Automation is encouraged but must preserve approvals, logging, and traceability.

### 9.2 Minimum Technical Requirements by Domain (Policy-Level Requirements)

| Domain | Minimum Requirements (Policy-Level) |
|---|---|
| Identity (AD / Entra ID) | Centralized identity governance; MFA for privileged access; PAM for privileged roles; logging of authentication and admin actions; periodic access review evidence |
| Network | Segmentation between IT and OT; firewall rule governance; documented IP addressing and DNS standards; change-controlled routing and security policies |
| Cloud (Azure/AWS) | Approved landing zones; guardrails for network/security; logging enabled; resource tagging; least privilege IAM; drift detection where feasible |
| Endpoint | Managed via Intune/ConfigMgr; baseline hardening; EDR enforced; patch compliance measured; device inventory evidenced |
| Monitoring/SIEM | Central log aggregation; alert triage process; time synchronization; retention aligned to security and compliance needs |
| Backup/Recovery | Defined RPO/RTO per service; regular restore testing; immutable or tamper-resistant backups where feasible; evidence of test restores |
| Vulnerability Management | Scanning coverage; remediation SLAs; documented exceptions and compensating controls; reporting to SSC |
| OT/IT Integration | Approved remote access patterns; strong authentication; session recording for privileged access where feasible; monitoring of gateways; CAB/ARB required |

### 9.3 Alignment to Governance & Standards (standards.json)
This policy enforces alignment to:

- **ITIL 4 practices:** Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, Supplier Management, Service Continuity Management.
- **NIST CSF functions:** Identify, Protect, Detect, Respond, Recover.
- **COBIT 2019 domains:** EDM, APO, BAI, DSS, MEA.
- **SOC 2 Trust Services Criteria:** Security, Availability, Confidentiality, Processing Integrity, Privacy.
- **ISO/IEC 27001:** Annex A control areas conceptually; with control-to-evidence mapping in Section 12.

---

## 10) Security & Compliance Considerations (ISO 27001, SOC 2, NIST mapping)

### 10.1 Security Outcomes
IT Infrastructure governance must ensure:

- Protection of confidentiality, integrity, and availability of infrastructure services
- Traceable approvals and accountable decisions (auditability)
- Timely detection and response to security events via integrated monitoring/SIEM
- Controlled privileged access via PAM with evidence and review
- GDPR-aligned handling of personal data in logs, monitoring, and identity systems
- SOX-aligned controls for systems supporting financial reporting (where applicable)

### 10.2 Conceptual Mapping: NIST CSF
| NIST CSF Function | Governance Mechanisms in this Policy |
|---|---|
| Identify | CMDB/CI governance, ARB decisions, risk registers, service ownership, asset inventory expectations |
| Protect | Standards, access controls, PAM, change enablement, segmentation, baseline configurations |
| Detect | Monitoring/event management, SIEM integration, alerting SLOs, log retention and review evidence |
| Respond | Incident escalation paths, emergency CAB, coordinated containment changes with evidence |
| Recover | Backup/restore testing, service continuity alignment, RTO/RPO targets, post-incident improvements |

### 10.3 SOC 2 Trust Services Criteria (Conceptual Alignment)
| SOC 2 Criterion | Policy Enablers |
|---|---|
| Security | Access control governance, change control, monitoring, vulnerability remediation governance |
| Availability | SLOs, capacity/availability governance, service continuity, incident and problem management |
| Confidentiality | Encryption expectations via standards, logging controls, data minimization in telemetry |
| Processing Integrity | Change validation, configuration integrity, controlled deployments |
| Privacy | GDPR-aware logging and retention, DPO engagement where personal data is involved |

---

## 11) Roles & Responsibilities (Aligned to roles.json)

### 11.1 Role Responsibilities Summary
| Role | Responsibilities (Governance Context) |
|---|---|
| CIO | Executive owner of IT strategy and governance for Norfolk Industries; accountable for policy approval and high-risk exception approval. |
| Head of IT Infrastructure Services | Accountable for infrastructure governance effectiveness; chairs CAB; approves standards; ensures resources for compliance and reliability. |
| CISO | Accountable for information security program and ISMS oversight; responsible for high-risk exception approval and security governance direction. |
| IT Governance Manager | Owns governance processes, policy lifecycle, compliance tracking, and audit coordination; maintains decision logs and evidence indexes. |
| Service Owner | Accountable for end-to-end service performance, roadmap, risk posture, and compliance; ensures SLOs and continuity targets are met and evidenced. |
| Platform Owner | Accountable for technical platform architecture and engineering standards; provides ARB inputs and ensures standards are implementable and auditable. |
| IT Operations Manager | Responsible for operational execution, shift/on-call readiness, and incident response coordination; ensures eCAB execution and post-implementation validation. |
| Network Engineer | Implements and supports network infrastructure per standards and procedures; produces implementation evidence for governed changes. |
| Systems Engineer | Implements and supports server/compute infrastructure per standards and procedures; maintains CI accuracy and change evidence. |
| Cloud Engineer | Implements and supports cloud infrastructure per standards and procedures; ensures guardrails, logging, and tagging are applied and evidenced. |
| Endpoint Engineer | Implements and supports endpoint and device management; ensures baseline compliance and evidence reporting. |
| IAM Engineer | Implements and supports identity and access management controls and lifecycle; ensures access control evidence and periodic review outputs. |
| Security Engineer | Implements security tooling and integrations; validates control effectiveness; supports investigations; provides evidence of monitoring and response controls. |
| ITSM Process Owner | Owns ITIL-aligned process design (Change/Incident/Problem/CMDB); ensures governance workflows in ITSM are effective and measured. |
| Service Desk Manager | Owns incident intake and communications; coordinates user communications for changes/outages; supports major incident coordination. |
| Internal Audit | Independently assesses control design and operating effectiveness; accountable for audit evidence coordination as defined in RACI master. |
| Data Protection Officer (DPO) | Oversees privacy governance and GDPR alignment; consulted when infrastructure telemetry or identity/log data involves personal data. |

---

## 12) Risk & Control Mapping (Controls → Evidence)

### 12.1 Control-to-Evidence Principles (Authoritative)
Evidence must be:
1. **Time-bound** (dated; relevant period)
2. **Attributable** (who performed/approved)
3. **Repeatable** (process can be executed consistently)
4. Include **approvals, logs, and validation artifacts** where applicable

### 12.2 Control Catalog for IT Infrastructure Governance (Detailed)
The catalog below maps governance controls to evidence artifacts and aligns conceptually to ISO/IEC 27001 Annex A control areas, NIST CSF functions, and SOC 2 criteria.

#### 12.2.1 Governance and Policy Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| GOV-01 | Governance bodies (CAB, ARB, SSC) operate with defined charters, cadence, and documented decisions. | Head of IT Infrastructure Services, IT Governance Manager | Meeting schedules, agendas, attendance, decision logs, ADRs | Organizational controls | Identify | Security, Availability |
| GOV-02 | Policies, standards, and procedures follow lifecycle management with annual review and approvals. | IT Governance Manager, Head of IT Infrastructure Services | Version history, approval records, review attestations | Organizational controls | Identify | Security |
| GOV-03 | Decision rights and accountability are defined via RACI and enforced. | Head of IT Infrastructure Services, IT Governance Manager | Published RACI, evidence of assignment in ITSM (Service Owner mapping) | Organizational controls | Identify | Security |
| GOV-04 | Exceptions are time-bound, risk-assessed, approved, and tracked to closure/renewal. | IT Governance Manager, Service Owner, CISO | Exception register, approved forms, compensating control validation | Risk management controls | Identify/Protect | Security |

#### 12.2.2 Change Enablement and Release Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| CHG-01 | All production changes to infrastructure CIs are recorded in ITSM and approved according to risk. | ITSM Process Owner, Service Owner | Change records, approvals, risk rating, CI links | Change management controls | Protect | Security, Availability |
| CHG-02 | Changes include backout plans and validation steps; closure requires validation evidence. | IT Operations Manager, Platform Owner | Backout plan, validation checklist, monitoring confirmation | Change management controls | Protect/Recover | Availability |
| CHG-03 | Emergency changes are authorized through eCAB and reviewed post-implementation. | IT Operations Manager, Head of IT Infrastructure Services | eCAB records, incident linkage, retrospective notes | Change management controls | Respond | Security, Availability |
| CHG-04 | Segregation of duties is enforced for high-risk changes (approval separate from implementation where feasible). | ITSM Process Owner, IT Governance Manager | ITSM role assignments, approval logs, peer review evidence | Access and change controls | Protect | Security |

#### 12.2.3 Configuration and Asset (CI/CMDB) Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| CFG-01 | Critical infrastructure CIs are identified, owned, and maintained in the CMDB. | Service Owner, Platform Owner | CMDB reports, CI ownership fields, periodic attestation | Asset management controls | Identify | Security, Availability |
| CFG-02 | CI relationships and dependencies are maintained for critical services. | Platform Owner, Systems Engineer | CMDB relationship mappings, dependency reviews | Asset management controls | Identify | Availability |
| CFG-03 | Configuration baselines are defined in standards and validated periodically. | Platform Owner, Security Engineer | Baseline documents, compliance scans, drift reports | Configuration management controls | Protect/Detect | Security |

#### 12.2.4 Access Control and Privileged Access Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| ACC-01 | Identity services enforce least privilege; privileged access uses PAM and MFA. | IAM Engineer, Security Engineer | PAM reports, MFA policy evidence, privileged group membership reports | Access control controls | Protect | Security |
| ACC-02 | Administrative actions are logged and retained; logs are protected from tampering. | Security Engineer, Platform Owner | SIEM ingestion proof, log retention config, access to logs | Logging and monitoring controls | Detect | Security |
| ACC-03 | Periodic access reviews are performed for privileged roles and key services. | Service Owner, IAM Engineer | Access review outputs, approvals, remediation actions | Access governance controls | Protect | Security, Confidentiality |

#### 12.2.5 Monitoring, Event, and Incident Integration Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| MON-01 | Critical infrastructure services are monitored with alert thresholds and on-call response procedures. | IT Operations Manager, Service Owner | Monitoring dashboards, alert policies, on-call schedules, incident links | Monitoring controls | Detect/Respond | Availability |
| MON-02 | Security events are centralized in SIEM with defined triage and escalation. | Security Engineer, IT Operations Manager | SIEM rules, incident tickets, escalation records | Monitoring controls | Detect/Respond | Security |
| INC-01 | Major incidents follow documented escalation, communications, and post-incident review processes. | IT Operations Manager, Service Desk Manager | Major incident records, comms logs, PIR reports | Incident management controls | Respond/Recover | Availability |

#### 12.2.6 Vulnerability and Patch Governance Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| VUL-01 | Vulnerability scanning coverage is maintained and reported; remediation follows defined targets. | Security Engineer, Platform Owner | Scan reports, coverage metrics, remediation tickets | Vulnerability management controls | Identify/Protect | Security |
| VUL-02 | Patch compliance is measured; exceptions are documented and risk-accepted. | Platform Owner, IT Operations Manager | Patch reports, change records, exceptions | Vulnerability management controls | Protect | Security, Availability |

#### 12.2.7 Backup, Recovery, and Continuity Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| BCP-01 | Services have documented RTO/RPO and recovery procedures. | Service Owner, IT Operations Manager | Service continuity docs, RTO/RPO records, runbooks | Continuity controls | Recover | Availability |
| BCP-02 | Backup success is monitored; restore tests are performed and evidenced. | Systems Engineer, IT Operations Manager | Backup reports, restore test results, screenshots/logs | Continuity controls | Recover | Availability |

#### 12.2.8 OT/IT Integration Governance Controls
| Control ID | Control Statement | Primary Owner Roles | Evidence (Minimum) | ISO/IEC 27001 (Conceptual) | NIST CSF | SOC 2 |
|---|---|---|---|---|---|---|
| OTG-01 | OT/IT connectivity designs are reviewed by ARB and include segmentation, access controls, and logging. | Platform Owner, Security Engineer | ADRs, network diagrams, firewall rule reviews | Network security controls | Protect/Detect | Security, Availability |
| OTG-02 | Remote access to OT-connected environments is controlled, approved, and monitored. | IAM Engineer, Security Engineer | PAM session logs, access approvals, SIEM alerts | Access and monitoring controls | Protect/Detect | Security |
| OTG-03 | OT-impacting changes require CAB review and include operational safety considerations. | IT Operations Manager, Service Owner | Change records, safety impact statements, comms with plant stakeholders | Change controls | Protect/Respond | Availability |

---

## 13) Exceptions Management (Process + Forms)

### 13.1 Policy Requirement
Any deviation from this policy or from approved standards requires an approved exception. Exceptions are not indefinite; they must be time-bound and reviewed.

### 13.2 Exception Risk Rating
Exceptions are categorized:

| Risk Level | Characteristics | Approval Path |
|---|---|---|
| Low | Minimal impact; compensating controls fully mitigate | Head of IT Infrastructure Services approves; CISO consulted |
| Medium | Moderate control gap; partial mitigation | Head of IT Infrastructure Services approves; CISO consulted; SSC notified |
| High | Material security/availability/compliance impact; SOX/GDPR implications likely | CIO accountable; Head of IT Infrastructure Services and CISO responsible; SSC reviews; Internal Audit informed |

### 13.3 Exception Register Requirements
The IT Governance Manager maintains an exception register containing:
- Exception ID, requestor, Service Owner, Platform Owner
- Affected CIs/services
- Requirement being excepted
- Risk rating and rationale
- Compensating controls
- Approval records
- Expiry date and review date
- Closure evidence

### 13.4 Exception Request Form
See Appendix E (Exception Request Form).

---

## 14) Training & Awareness

### 14.1 Required Training
| Audience | Training | Frequency | Evidence |
|---|---|---|---|
| Service Owners / Platform Owners | Governance fundamentals (CAB/ARB/SSC), evidence principles, exception handling | On assignment and annually | Training completion report; attestation |
| Engineers (Network/Systems/Cloud/Endpoint/IAM/Security) | Change enablement procedure, evidence capture, secure configuration baselines | On assignment and annually | LMS report; team roster attestation |
| IT Operations (24×7) | eCAB procedure, escalation paths, major incident governance | On assignment and semi-annually drills | Drill reports; on-call readiness checklist |
| Regional IT Operations | Regional execution guardrails; OT/IT boundary governance | On assignment and annually | Regional sign-off evidence |
| Service Desk | Communications standards for changes/incidents | On assignment and annually | Training record |

### 14.2 Awareness Mechanisms
- Quarterly governance bulletins summarizing key changes, common audit issues, and metrics trends
- CAB and ARB “top findings” and recurring failure patterns
- Lessons learned from major incidents and emergency changes

---

## 15) Monitoring & Enforcement

### 15.1 Monitoring Mechanisms
- Automated reports from ITSM for change compliance (approval rates, lead times, emergency change percentage)
- CMDB accuracy and completeness reporting for critical CIs
- SIEM and monitoring platform health checks
- Vulnerability scanning coverage and remediation trend reporting
- Exception register status reporting (count, aging, risk distribution)

### 15.2 Enforcement Actions
Non-compliance may result in:
1. Mandatory remediation plan with deadlines
2. Temporary suspension of change implementer permissions for repeated violations
3. Escalation to Head of IT Infrastructure Services and CISO for material risk
4. Audit finding tracking and follow-up verification

Enforcement must be consistent, documented, and tied to measurable requirements.

---

## 16) Metrics & KPIs (Governance KPIs; Compliance KPIs)

### 16.1 Governance KPIs
| KPI | Definition | Target/Expectation | Owner Roles |
|---|---|---|---|
| Change approval compliance | % of production changes with correct approvals and risk classification | High and stable; investigated if trending down | ITSM Process Owner, IT Governance Manager |
| Emergency change rate | % of total changes executed as emergency | Controlled; reviewed monthly | IT Operations Manager |
| Change success rate | % of changes without rollback or incident within defined window | High and improving | Service Owner |
| CAB throughput | # changes reviewed and decisioned per CAB | Sufficient to avoid backlog | Head of IT Infrastructure Services |
| ARB decision latency | Time from submission to ADR | Predictable and improving | Platform Owner, IT Governance Manager |

### 16.2 Compliance KPIs
| KPI | Definition | Target/Expectation | Owner Roles |
|---|---|---|---|
| Exception aging | Average age of open exceptions and % overdue | Low; none overdue | IT Governance Manager |
| CMDB critical CI completeness | % of critical services with owned CIs and dependencies recorded | High and improving | Service Owner |
| Vulnerability remediation timeliness | % remediated within defined targets (by severity class) | Measured; SSC sets priority | Security Engineer, Platform Owner |
| Backup restore test completion | % of required restore tests completed with evidence | High; no missed cycles | IT Operations Manager |
| Privileged access review completion | % of required privileged reviews completed on time | High | IAM Engineer, Service Owner |

---

## 17) Audit & Evidence Requirements (What to Show Auditors)

### 17.1 Evidence Pack Expectations
For audits aligned to ISO/IEC 27001, SOC 2, SOX, and GDPR, Norfolk Industries must be able to produce:

- Policy/standards/procedures with approvals and review records
- CAB records, change samples with approvals, risk ratings, test/backout/validation evidence
- ARB ADRs and architecture compliance checklists
- Access control evidence: PAM logs, MFA policies, access reviews
- Monitoring and incident evidence: SIEM ingestion, alerting rules, incident tickets, PIR reports
- Vulnerability evidence: scan reports, remediation tickets, exception approvals
- Backup and continuity evidence: restore test results, RTO/RPO documentation, continuity exercises
- Exception register and supporting risk acceptance evidence
- Metrics and management review outputs (SSC minutes, dashboards)

### 17.2 Sampling Guidance (Internal Use)
Evidence should be organized to support sampling by:
- Region (North America, Europe, APAC)
- Service domain (identity, network, cloud, endpoint, monitoring, backup)
- Risk tier (high-impact services; SOX-relevant systems)
- Time periods (quarterly and annual coverage)

### 17.3 Evidence Retention Expectations
Evidence must be retained in accordance with Norfolk Industries retention requirements and must be accessible, immutable where appropriate, and attributable. Logs and security telemetry retention must consider GDPR data minimization and lawful basis where personal data is present, with DPO consultation as required.

---

## 18) Continuous Improvement

### 18.1 Inputs to Improvement
- Major incident post-incident reviews and corrective actions
- Problem Management trends (recurring incidents and root causes)
- Audit findings and management action plans
- Vulnerability management trend analysis
- CAB and ARB decision patterns (common rejections/deferrals)
- Exception trends and repeat exceptions indicating standards gaps

### 18.2 Improvement Governance
- IT Governance Manager maintains a governance improvement backlog.
- SSC reviews security-related improvements monthly.
- Head of IT Infrastructure Services reviews overall governance health quarterly.
- Improvements resulting in policy/standard changes must follow document lifecycle controls and approvals.

---

## 19) Appendices (Templates, Checklists, Runbooks)

## Appendix A: Governance Charter Template (CAB / ARB / SSC)

### A.1 Charter Document Control
| Field | Value |
|---|---|
| Charter Name | Governance Body Charter |
| Owner | IT Governance Manager |
| Sponsor | Head of IT Infrastructure Services |
| Review Cadence | Annual |

### A.2 Governance Body Charter (Template)
#### A.2.1 Name
- Governance body name (CAB / ARB / SSC)

#### A.2.2 Purpose
- Clear statement of outcomes and decision types

#### A.2.3 Scope
- In-scope decisions, systems, and CIs
- OT/IT integration boundaries if applicable

#### A.2.4 Membership and Quorum
- Required roles (by role name from roles.json)
- Quorum definition (minimum roles present)
- Delegation rules (who may delegate to whom and how)

#### A.2.5 Cadence and Scheduling
- Meeting frequency
- Emergency convening rules (if applicable)

#### A.2.6 Inputs
- Required artifacts, submission deadlines, and formats

#### A.2.7 Decision Outputs
- Decision types (approve/reject/defer/conditions)
- Documentation requirements (ITSM updates, Decision Log, ADRs)

#### A.2.8 Escalation
- Escalation path for unresolved decisions or high-risk items

#### A.2.9 Metrics
- KPIs the body will track and review

#### A.2.10 Records and Evidence
- Required retained records, retention expectations, and repository location

---

## Appendix B: CAB Agenda Template

### B.1 CAB Agenda (Standard)
1. **Opening and quorum confirmation**
2. **Review of previous meeting actions**
3. **Emergency changes executed since last CAB**
   - Summary, outcomes, and required follow-ups
4. **Planned changes for approval**
   - High-risk changes first
   - OT-impacting changes flagged explicitly
5. **Change calendar conflicts and freeze windows**
6. **Risk review**
   - Exceptions intersecting with planned changes
7. **Communications plan review**
8. **Post-implementation review summaries (from prior changes)**
9. **Metrics review**
   - Emergency rate, success rate trends
10. **Decisions and conditions recap**
11. **Close and action assignment**

### B.2 CAB Minutes Requirements
- Attendance (roles and names)
- Decisions made and conditions
- Action items, owners, due dates
- Links to change records and evidence locations

---

## Appendix C: Decision Log Template (Governance Decision Record)

### C.1 Decision Log Table
| Field | Required Content |
|---|---|
| Decision ID | Unique identifier |
| Date/Time | When decision was made |
| Governance Body | CAB / ARB / SSC |
| Decision Type | Approve / Reject / Defer / Approve with Conditions |
| Decision Summary | What was decided |
| Rationale | Why it was decided |
| Risk Considerations | Key risks identified and mitigations required |
| Affected Services/CIs | Specific CIs and services impacted |
| Conditions/Actions | What must occur (with due dates) |
| Owner Role | Service Owner / Platform Owner / IT Operations Manager etc. |
| Evidence Links | Links to ITSM records, ADRs, logs, reports |
| Review Date | If follow-up is required |

---

## Appendix D: Architecture Review Checklist (ARB)

### D.1 ARB Checklist (Infrastructure)
| Category | Check | Pass Criteria | Evidence |
|---|---|---|---|
| Security | Identity and access model | Least privilege; privileged access via PAM; MFA enforced | IAM design section; access model diagram |
| Security | Logging and monitoring | Central logging to SIEM; alerting defined | Logging architecture; SIEM integration plan |
| Network | Segmentation | OT/IT boundaries defined; controlled gateways | Network diagrams; firewall policy approach |
| Resilience | RTO/RPO | Targets defined per service; feasible design | Service continuity section |
| Resilience | Backup | Backup method and restore testing defined | Backup architecture and test approach |
| Operations | Support model | On-call and runbooks defined; ownership clear | Operating model; runbook list |
| Change | Deployability | Change approach supports CAB; rollback feasible | Release/change plan |
| Compliance | Control mapping | Key controls mapped to evidence | Control mapping table |
| Data protection | GDPR considerations | Personal data in logs minimized; retention justified | DPO consultation record if needed |
| Supplier | Third-party dependencies | Supplier responsibilities defined | Supplier management notes |

### D.2 ARB Decision Outcomes
- Approved
- Approved with conditions (conditions must be measurable)
- Deferred (information required specified)
- Rejected (rationale and remediation path provided)

---

## Appendix E: Exception Request Form (Policy/Standard Exception)

### E.1 Exception Request Form
| Field | Required Entry |
|---|---|
| Requestor | Name and role |
| Requesting Organization | Global IT Operations / Regional IT Operations / Supplier (if applicable) |
| Service Owner | Name and role |
| Platform Owner | Name and role |
| Affected Service(s) | Service names |
| Affected CIs | CI identifiers and descriptions |
| Requirement Being Excepted | Policy/standard clause reference |
| Business Justification | Why exception is necessary |
| Risk Assessment Summary | Confidentiality, integrity, availability, privacy, SOX impacts |
| OT Impact | Yes/No; description if yes |
| Compensating Controls | Specific controls to reduce risk |
| Duration | Start date and expiry date |
| Review Date | Mandatory review date prior to expiry |
| Approvals Required | Based on risk level (Section 13.2) |
| Implementation Plan | Steps to implement compensating controls |
| Validation Evidence Plan | What proof will be provided and when |

### E.2 Exception Approval Record
| Approver Role | Name | Decision | Date | Conditions |
|---|---|---|---:|---|
| Head of IT Infrastructure Services |  |  |  |  |
| CISO |  |  |  |  |
| CIO (High Risk Only) |  |  |  |  |

*Note: Names are recorded at time of use; the template supports attributable approvals.*

---

## Appendix F: Sample Evidence Pack Index (Audit-Ready)

### F.1 Evidence Pack Structure
| Section | Description | Example Artifacts |
|---|---|---|
| 1. Governance | Proof governance bodies operate as designed | CAB minutes, ARB ADRs, SSC minutes, decision logs |
| 2. Policy Lifecycle | Proof documents are controlled | Version history, approvals, review attestations |
| 3. Change Enablement | Proof changes are controlled | Change samples with approvals, test evidence, backout plans, validation |
| 4. Access Controls | Proof identity and PAM controls operate | MFA policy evidence, PAM reports, access reviews |
| 5. Monitoring & Incidents | Proof detection and response | SIEM ingestion, alert rules, incident tickets, PIRs |
| 6. Vulnerability Management | Proof scanning and remediation | Scan reports, remediation records, exception approvals |
| 7. Backup & Continuity | Proof recoverability | Restore test results, RTO/RPO records, continuity exercises |
| 8. CMDB/CI | Proof asset governance | CI ownership reports, dependency mappings, attestations |
| 9. Exceptions | Proof controlled deviations | Exception register, forms, compensating control validation |
| 10. Metrics & Reviews | Proof management oversight | KPI dashboards, quarterly reviews, action backlogs |

### F.2 Evidence Quality Checklist
- Evidence is within the audit period
- Approvals show approver identity and date/time
- Logs are traceable to systems and protected
- Validation artifacts show results and acceptance criteria
- Cross-references exist (change ↔ CI ↔ service ↔ decision record)

---

## Appendix G: Governance Meeting Runbook (Operational Execution)

### G.1 Pre-Meeting Checklist (CAB/ARB/SSC)
| Step | Owner Role | Completion Criteria |
|---|---|---|
| Confirm agenda and quorum | IT Governance Manager | Agenda distributed; required roles invited |
| Validate submissions completeness | ITSM Process Owner / Platform Owner | Required artifacts attached and readable |
| Identify high-risk/OT-impacting items | Security Engineer / Platform Owner | Items flagged and prioritized |
| Prepare metrics dashboard | IT Governance Manager | Updated metrics for review period |
| Validate prior action status | IT Governance Manager | Action list updated with evidence links |

### G.2 During Meeting Checklist
| Step | Owner Role | Completion Criteria |
|---|---|---|
| Record decisions in Decision Log | IT Governance Manager | Decision ID assigned; rationale captured |
| Confirm conditions are measurable | Chair (Head of IT Infrastructure Services) | Conditions have due dates and evidence requirements |
| Assign action owners | Chair | Owner roles named; due dates set |
| Escalate when required | Chair / CISO | Escalations documented with next steps |

### G.3 Post-Meeting Checklist
| Step | Owner Role | Completion Criteria |
|---|---|---|
| Publish minutes | IT Governance Manager | Minutes posted with links to artifacts |
| Update ITSM records | ITSM Process Owner | Changes/requests updated with decision references |
| Track actions | IT Governance Manager | Action register updated and monitored |
| Evidence indexing | IT Governance Manager | Evidence linked to index for audit readiness |

---

## Appendix H: Extended Control-to-Evidence Catalog (Expanded Examples)

### H.1 Example Evidence Types by Control Area
| Control Area | Example Evidence | Notes |
|---|---|---|
| Change Enablement | Approved change record; implementation transcript; configuration diff; validation test output | Must show who approved and who implemented |
| Access Control | PAM session report; privileged group membership export; access review approvals | Ensure personal data handling aligns to GDPR |
| Monitoring | SIEM rule configuration export; alert ticket; on-call runbook | Demonstrate detection-to-ticket linkage |
| Vulnerability | Scan report and remediation ticket lifecycle | Include exception approvals if delayed |
| Backup/Recovery | Restore test results including timestamps and outcomes | Evidence must show successful restore and verification |
| OT/IT | Network segmentation diagram + firewall rule approval + remote access logs | Show governance approvals and ongoing monitoring |

### H.2 Evidence Traceability Matrix (Sample Pattern)
| Governance Artifact | Must Reference | Purpose |
|---|---|---|
| Change record | Affected CIs + CAB decision reference | Trace change to assets and approvals |
| ADR | Standards requirements + security considerations | Show design alignment |
| Exception form | Requirement clause + compensating controls | Document risk acceptance path |
| Incident record | Related changes + monitoring alerts | Support post-incident analysis |
| KPI dashboard | Source reports | Demonstrate repeatability |

---

## Appendix I: Detailed Governance Process Maps (Textual)

### I.1 CAB Governance Flow (Text)
1. Change request created in ITSM and linked to affected CIs.
2. Risk assessed by Service Owner/Platform Owner; OT impact flagged.
3. Evidence attached: test plan/results, backout plan, comms plan, validation plan.
4. CAB reviews; decision recorded.
5. Change implemented by authorized engineers; implementation evidence captured.
6. Validation performed; monitoring confirmed stable.
7. CAB post-implementation review confirms outcomes; change closed with evidence link.

### I.2 ARB Governance Flow (Text)
1. Architecture proposal submitted with diagrams and operational model.
2. ARB reviews against principles, security outcomes, and supportability.
3. ADR issued; conditions must be satisfied before implementation.
4. Implementation changes follow CAB with ADR reference.
5. Operational readiness confirmed with runbooks and monitoring.

### I.3 SSC Governance Flow (Text)
1. Metrics and risk posture compiled monthly.
2. Exceptions and vulnerability trends reviewed; priorities set.
3. High-risk items escalated to CIO as needed.
4. Actions tracked to closure with evidence.

---

## Appendix J: Comprehensive Requirements Checklist (Policy Self-Assessment)

### J.1 Policy Compliance Checklist
| Requirement | Evidence Artifact | Frequency |
|---|---|---|
| CAB operates with charter and documented decisions | CAB minutes + decision logs | Weekly |
| ARB operates and issues ADRs | ADR repository + meeting records | Bi-weekly |
| SSC reviews risk and metrics | SSC minutes + dashboard | Monthly |
| All production changes recorded and approved | ITSM change reports | Continuous |
| Emergency changes reviewed post-implementation | eCAB records + retrospectives | Per event |
| CMDB critical CI ownership maintained | CMDB ownership report | Quarterly |
| Privileged access reviews completed | Access review outputs | Quarterly (or per ISMS requirement) |
| Vulnerability remediation tracked | Scan + ticket reports | Monthly |
| Restore testing evidenced | Restore test results | Per service continuity plan |
| Exceptions time-bound and reviewed | Exception register | Monthly |

---

*End of Document*