# Infrastructure Risk Management Policy (Norfolk Industries)

## 1. Purpose
This policy defines how Norfolk Industries identifies, assesses, treats, accepts, monitors, and reports risks related to IT Infrastructure Services across hybrid cloud, on-prem data centers, endpoints, identity, networking, and supporting platforms. It ensures consistent, auditable risk management aligned to the Information Security Management System (ISMS), business continuity objectives, and regulatory requirements.

## 2. Scope
### 2.1 In scope
This policy applies to:
- IT Infrastructure Services operated by Global IT Operations and executed by Regional IT Operations.
- Hybrid cloud services (Microsoft Azure primary, AWS secondary), on-prem data centers, identity (Active Directory and Entra ID (Azure AD)), endpoint management (Microsoft Intune and ConfigMgr where needed), and supporting monitoring, backup, and logging services.
- Security tooling supporting infrastructure operations (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk).
- Third-party access to infrastructure and operations tooling (including remote access pathways).
- Operational Technology (OT) integration points affecting or dependent on IT services (remote access, identity, network segmentation, logging, patching interfaces).

### 2.2 Out of scope
- Application-only risks that do not materially affect IT Infrastructure Services (handled by application/service risk processes).
- Purely physical safety hazards unless they directly impact IT Infrastructure Services availability or security (handled by EHS processes with coordination).

## 3. Policy statement
Norfolk Industries shall operate a consistent infrastructure risk management process that:
- Uses a defined risk taxonomy, scoring methodology, and documented acceptance authorities.
- Maintains a centralized risk register for IT Infrastructure Services, with regional execution and timely updates.
- Integrates with ITIL 4 practices (Change Enablement, Incident Management, Problem Management, Monitoring and Event Management, Service Continuity Management, Service Configuration Management) and the Change Advisory Board (CAB).
- Requires risk assessment for material changes, third-party access, and OT/IT integration pathways.
- Ensures risks are treated to an acceptable residual level or formally accepted with documented rationale, time-bounded approvals, and monitoring requirements.

## 4. Definitions
Terms used in this policy align to the Norfolk Industries glossary:
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.

Additional policy-specific definitions:
- **Inherent Risk**: Risk level before considering existing controls.
- **Residual Risk**: Risk level remaining after considering existing controls and planned treatments.
- **Risk Owner**: The role accountable for managing a specific risk to an acceptable residual level (typically the Service Owner; may be delegated by domain).
- **Risk Acceptance**: Formal approval to tolerate residual risk for a defined time period with documented justification and monitoring.
- **Risk Treatment Plan**: A defined set of actions with owners and due dates to reduce likelihood and/or impact, or otherwise manage risk.

## 5. Roles and responsibilities
Norfolk Industries uses the following roles (consistent with roles.json):

| Role | Responsibilities in this policy |
|---|---|
| CIO | Executive oversight for enterprise technology risk posture; participates in high-risk exception governance as defined by acceptance authority. |
| Head of IT Infrastructure Services | Accountable for this policy’s implementation across IT Infrastructure Services; ensures resources and prioritization for risk treatment. |
| CISO | Oversees alignment to the ISMS; advises on security risk treatment and acceptance decisions; ensures integration with security monitoring and control validation. |
| IT Governance Manager | Owns governance process, policy lifecycle, compliance tracking, audit coordination; maintains infrastructure risk register structure and reporting cadence. |
| Service Owner | Risk Owner by default for risks affecting their service; ensures risk assessment completion, treatment plans, evidence retention, and periodic review. |
| Platform Owner | Defines platform standards and required controls; supports risk assessment and treatment implementation across the platform domain. |
| IT Operations Manager | Ensures operational execution (24×7), monitoring, incident coordination, and timely risk escalations based on events and operational metrics. |
| ITSM Process Owner | Ensures integration of risk activities into ITIL-aligned ITSM workflows (Change/Incident/Problem/CMDB) and continual improvement. |
| Internal Audit | Independently assesses control design and operating effectiveness; reviews evidence quality and traceability. |
| Data Protection Officer (DPO) | Ensures privacy risk considerations (GDPR) are addressed where infrastructure processing of personal data is impacted. |

## 6. Risk management principles
Norfolk Industries’ infrastructure risk management shall follow these principles:
- **Centralized governance, regional execution**: Global IT Operations defines methodology; Regional IT Operations executes and maintains evidence.
- **Defense-in-depth**: Layered preventative, detective, and corrective controls.
- **Least privilege and strong identity**: Identity and access risks are treated as critical, especially for privileged access via PAM.
- **Lifecycle integration**: Risk management is embedded in Change Enablement, supplier access onboarding, incident/problem management, and service continuity planning.
- **OT-aware controls**: Where OT connectivity exists, risks must reflect segmentation, strict remote access controls, and safety/availability constraints.
- **Evidence-driven**: Evidence must be time-bound, attributable, and repeatable, including approvals, logs, and validation artifacts where applicable.

## 7. Risk taxonomy (IT Infrastructure Services)
Risks shall be categorized using this taxonomy. Each risk must include one primary category and may include secondary categories.

| Category | Description | Common examples |
|---|---|---|
| Identity and Access Management | Risks to authentication, authorization, privileged access, and identity lifecycle in Active Directory and Entra ID | Excessive privileges, weak MFA enforcement, stale accounts, PAM coverage gaps |
| Cloud and Platform Security | Risks arising from misconfiguration or insufficient controls in Azure/AWS and associated platforms | Public storage exposure, insecure network rules, lack of logging, key/secret handling weaknesses |
| Network and Connectivity | Risks to network segmentation, routing, firewalling, remote access, DNS/DHCP, and boundary protection | Flat networks, insecure VPN, inadequate OT/IT segmentation, unmanaged external exposure |
| Endpoint and Server Security | Risks to operating system hardening, patching, EDR, and configuration | Unpatched vulnerabilities, EDR exclusions, legacy protocols, insecure baseline drift |
| Monitoring, Logging, and Detection | Risks to observability, SIEM ingestion, alerting, and event response coverage | Missing logs, alert fatigue, inadequate use-case coverage, weak time synchronization |
| Vulnerability and Configuration Management | Risks to scanning coverage, remediation SLAs, and configuration compliance | Unscanned subnets, remediation backlog, unsupported OS, CMDB inaccuracies |
| Backup, Recovery, and Service Continuity | Risks impacting recovery capabilities, RPO/RTO achievement, and restoration validation | Backup failures, untested restores, immutability gaps, inadequate DR runbooks |
| Supplier and Third-Party Access | Risks introduced by vendors, MSPs, integrators, and remote support channels | Unmonitored vendor accounts, shared credentials, remote access bypassing controls |
| Operational Technology (OT) Integration | Risks created at OT/IT interfaces including identity, remote access, patching, data flows, and segmentation | Remote access into plant networks, insecure jump hosts, logging gaps for OT DMZ |
| Compliance and Auditability | Risks of failing obligations (SOX, GDPR, SOC 2) due to control gaps or poor evidence | Incomplete access reviews, missing change approvals, inadequate retention |

## 8. Risk register requirements
### 8.1 Central risk register
- A centralized infrastructure risk register shall be maintained within the ITIL-aligned ITSM tool or an approved governance repository controlled by IT Governance Manager.
- Each entry must be uniquely identified and linked where feasible to impacted services and CIs in the CMDB (Configuration Item relationships).

### 8.2 Mandatory risk record fields
Each risk record shall include:

| Field | Requirement |
|---|---|
| Risk ID | Unique identifier |
| Title | Concise statement of risk |
| Description | Condition, cause, and consequence |
| Category | Primary from taxonomy; optional secondary |
| Affected services/CIs | Service and CI references (where applicable) |
| Region(s) impacted | North America, Europe, APAC, or global |
| Risk Owner | Typically Service Owner |
| Stakeholders | Platform Owner, Security Engineer, IT Operations Manager, DPO as applicable |
| Inherent likelihood/impact | Scored per methodology |
| Existing controls | Prevent/detect/correct controls in place |
| Residual likelihood/impact | Scored per methodology |
| Residual risk rating | Derived score and band |
| Treatment decision | Treat / Tolerate (accept) / Transfer / Avoid |
| Treatment plan | Actions, owners, due dates |
| Acceptance record | Approver, date, expiry, rationale (if tolerated) |
| Monitoring | Metrics, alerting, review frequency |
| Status | Open / In treatment / Accepted / Closed |
| Evidence links | Change records, scan reports, access reviews, SIEM dashboards, backup tests, etc. |

### 8.3 Review cadence
- **High and Critical residual risks**: reviewed at least monthly by Global IT Operations with Regional IT Operations input.
- **Medium residual risks**: reviewed at least quarterly.
- **Low residual risks**: reviewed at least semi-annually, or upon material change.

## 9. Risk scoring methodology
### 9.1 Scoring model
Norfolk Industries uses a 5×5 scoring approach:
- **Likelihood** (1–5)
- **Impact** (1–5)
- **Risk Score** = Likelihood × Impact (1–25)

Residual risk must be calculated after considering existing controls and any committed treatments already implemented.

### 9.2 Likelihood scale (1–5)

| Score | Likelihood definition (infrastructure context) |
|---:|---|
| 1 | Rare: highly unlikely given architecture, controls, and exposure |
| 2 | Unlikely: possible but not expected in normal operations |
| 3 | Possible: could occur; known weaknesses or intermittent control gaps exist |
| 4 | Likely: expected to occur due to active threats, exposure, or repeated events |
| 5 | Almost certain: occurring now or imminent based on evidence |

### 9.3 Impact scale (1–5)

| Score | Impact definition (consider worst credible outcome) |
|---:|---|
| 1 | Negligible: minimal service disruption; no material data impact |
| 2 | Minor: localized disruption; limited compliance impact |
| 3 | Moderate: service degradation or outage within a region/site; potential customer/internal reporting impact |
| 4 | Major: multi-site/regional outage; significant security exposure; likely regulatory/audit implications |
| 5 | Severe: widespread outage (multi-region/global) and/or material confidentiality/integrity breach; major safety/OT operational impact; likely significant legal/financial impact including SOX implications |

Impact assessment must consider:
- Availability against SLO, and recovery capability against RPO/RTO
- Confidentiality and privacy exposure (GDPR), including personal data processing dependencies
- Integrity risks affecting SOX-relevant systems and reporting
- OT operational impact due to OT/IT integration pathways

### 9.4 Risk rating bands

| Score | Rating band | Minimum handling requirement |
|---:|---|---|
| 1–4 | Low | Manage via standard controls; track and review |
| 5–9 | Medium | Treatment plan required unless clearly justified and time-bounded acceptance is approved |
| 10–16 | High | Treatment plan required; monthly review; CAB visibility for related changes |
| 17–25 | Critical | Immediate escalation; prioritize treatment; acceptance requires highest approval per Section 10 |

## 10. Residual risk and acceptance authority
### 10.1 Residual risk determination
Residual risk shall be re-scored after:
- Control implementation (e.g., MFA enforcement, network segmentation changes, logging enablement)
- Control validation (e.g., scan results, access review completion, backup restore tests)
- Significant environmental changes (cloud migrations, OT connectivity changes, vendor onboarding)

### 10.2 Risk acceptance rules
- Risk acceptance is permitted only when:
  - Risk cannot be reduced further in a reasonable timeframe, or
  - The cost/operational constraints outweigh benefit, and compensating controls exist, and
  - Monitoring and review frequency are documented, and
  - Acceptance is time-bounded with an expiry date and reassessment requirement.

Accepted risks must remain visible in the risk register and be reviewed per cadence.

### 10.3 Acceptance authority matrix
Approvals must be documented in the risk register and attributable.

| Residual rating | Acceptance authority | Required consults |
|---|---|---|
| Low | Service Owner | Platform Owner (as needed) |
| Medium | Head of IT Infrastructure Services | CISO; IT Governance Manager |
| High | Head of IT Infrastructure Services | CISO (required); CIO (informed); IT Governance Manager |
| Critical | CIO | Head of IT Infrastructure Services; CISO; IT Governance Manager; Data Protection Officer (DPO) if privacy impact |

Additional constraints:
- Any residual risk with material SOX impact requires consultation with IT Governance Manager and documentation of compensating controls and evidence expectations.
- Any residual risk with likely GDPR impact requires consultation with Data Protection Officer (DPO).

## 11. Integration with ITIL and operational processes
### 11.1 Change Enablement and CAB integration
- All Normal Changes affecting CIs that could materially change risk posture (exposure, privilege, segmentation, logging, recovery) must include a risk assessment summary and expected residual risk.
- High/Critical risks associated with a change must be explicitly highlighted for CAB review.
- Emergency Changes must include a post-implementation risk assessment within the defined emergency change review window, with any new risks recorded and treated.

Minimum Change record risk content:
- Description of risk introduced/mitigated by the change
- Control validation plan (how the change will be verified)
- Rollback considerations and impact to RPO/RTO where relevant
- Link to risk register entry if created/updated

### 11.2 Incident and Problem Management integration
- Significant incidents shall be reviewed for:
  - Newly discovered risks (e.g., unknown exposure, control failure)
  - Likelihood recalibration of existing risks
- Problem records must feed risk treatment plans when root cause indicates systemic control gaps (patch compliance, monitoring gaps, configuration drift).

### 11.3 Service Configuration Management (CMDB) integration
- Risks must reference impacted services and CIs where feasible.
- Material CMDB inaccuracies are treated as a risk under Vulnerability and Configuration Management or Compliance and Auditability, depending on impact.

### 11.4 Service Continuity Management integration
- Risks affecting RPO/RTO feasibility (backup failures, DR gaps, single points of failure) must be recorded and tied to continuity plans and test evidence.
- Backup restore testing outcomes must be linked as evidence for residual risk scoring.

## 12. Supplier, remote access, and third-party risk (infrastructure)
Norfolk Industries shall manage supplier and vendor risks that impact IT Infrastructure Services by ensuring:
- Vendor access is time-bounded, least privilege, and authenticated through managed identity controls (Active Directory/Entra ID) where feasible.
- Privileged vendor access uses PAM controls (CyberArk or equivalent) for credential vaulting, session controls, and auditability.
- Remote access pathways to IT and OT environments are approved, monitored, and logged, including jump hosts and segmented access to OT.
- SIEM ingestion includes authentication logs, privileged session logs (where supported), and network/security device logs relevant to vendor access.
- Vendor access changes follow Change Enablement and are visible to the CAB when risk is High/Critical.

Minimum vendor access risk controls to consider during assessment:
- Identity proofing and account lifecycle (creation, modification, termination)
- MFA enforcement and conditional access
- Privilege scope and role-based access
- Session monitoring, command logging where applicable, and retention
- Network segmentation and allowed routes (especially to OT)
- Vulnerability and patch obligations for vendor-managed components
- Contractual obligations for incident notification and security requirements (coordinated through governance processes)

## 13. Operational Technology (OT) risk considerations
Where IT Infrastructure Services connects to or supports Operational Technology (OT), risk assessments must consider:
- **Segmentation and zoning**: plant networks segmented; strict remote access controls; OT DMZ where applicable.
- **Availability and safety constraints**: patching and changes may require coordinated windows and operational approvals; compensating controls may be required.
- **Remote access controls**: jump hosts, MFA, PAM, and session logging for remote support into OT-connected environments.
- **Monitoring/logging limitations**: where OT devices cannot support agents, apply network-based monitoring, syslog, or passive visibility; document gaps and compensating controls.
- **Incident response coordination**: OT-related incidents require coordinated response procedures aligned with ISMS and operational requirements.

OT-related risks must be categorized as **Operational Technology (OT) Integration** and linked to the relevant IT services enabling access (identity, network, remote access, logging).

## 14. Procedures (mandatory workflow)
Norfolk Industries shall follow the procedures below for infrastructure risks.

### 14.1 Identify risk
Triggers include:
- Architecture reviews and platform assessments
- Vulnerability scanning findings (Tenable/Nessus) and EDR alerts
- Cloud security posture findings (configuration assessments)
- Audit findings (Internal Audit, SOC 2, ISO/IEC 27001 surveillance)
- Significant incidents and post-incident reviews
- Changes introducing new exposure (internet-facing services, privilege changes, new vendors)
- OT connectivity changes or remote support enablement

Steps:
1. Document risk statement (condition, cause, consequence) using the risk register template.
2. Assign category and impacted services/CIs.
3. Assign Risk Owner (Service Owner by default).
4. Attach initial evidence (scan ID, alert reference, change record, audit note).

### 14.2 Assess risk
Steps:
1. Determine inherent likelihood and impact using Sections 9.2 and 9.3.
2. Document existing controls (prevent, detect, correct), including control owners.
3. Determine residual likelihood and impact considering control effectiveness and current coverage.
4. Record residual risk rating and initial treatment recommendation.

Assessment must consider:
- Exposure (internet-facing, vendor access, OT routes)
- Privilege levels involved (admin, service accounts, break-glass)
- Observability (logging/alerting coverage and response capability)
- Recovery capability (backup, restore test status, RPO/RTO feasibility)
- Compliance impact (SOX/GDPR/SOC 2)

### 14.3 Treat risk
Permitted treatment options:
- **Treat (reduce)**: implement controls to reduce likelihood/impact (preferred for High/Critical).
- **Transfer**: shift risk via contractual/insurance mechanisms; does not remove accountability for oversight.
- **Avoid**: stop the activity that creates the risk (decommission exposure, disable feature).
- **Tolerate (accept)**: formally accept residual risk per Section 10.

Treatment plan requirements:
- Actions must be specific, measurable, time-bounded.
- Treatment work that changes production systems must follow Change Enablement and may require CAB review.
- Validation steps must be defined (e.g., rescan results, policy compliance reports, SIEM query outputs, PAM logs, restore test results).

### 14.4 Accept risk
Steps:
1. Document justification, compensating controls, monitoring, and acceptance expiry date.
2. Obtain approvals per acceptance authority matrix (Section 10.3).
3. Record approval evidence (approval record, meeting minutes, workflow approval).
4. Ensure review cadence is set and reminders are established.

Acceptance must not be used to defer remediation without a documented rationale and monitoring plan.

### 14.5 Monitor risk
Monitoring must be proportionate to residual risk and include:
- Vulnerability remediation and scanning coverage metrics
- Security monitoring alerts and use-case coverage status
- Privileged access and vendor session monitoring outcomes
- Backup success rates and restore test outcomes
- Configuration compliance and drift indicators

High/Critical risk monitoring requires documented alerting and operational runbooks for response.

### 14.6 Report risk
Reporting channels:
- **Operational reporting**: IT Operations Manager coordinates regular risk posture summaries for IT Infrastructure Services.
- **Governance reporting**: IT Governance Manager provides periodic summaries to Head of IT Infrastructure Services and CISO, including trends and overdue treatment plans.
- **CAB reporting**: High/Critical risks related to upcoming changes are surfaced to the Change Advisory Board (CAB).
- **Audit reporting**: Evidence and risk status provided to Internal Audit upon request, aligned to evidence principles.

Minimum reporting content:
- Count of risks by rating band and category
- Top High/Critical risks with treatment status and due dates
- Overdue treatment actions and aged accepted risks approaching expiry
- Significant changes to residual risk scores month-over-month

## 15. Compliance, exceptions, and enforcement
- Compliance with this policy is mandatory for all teams delivering IT Infrastructure Services.
- Exceptions to required controls or timelines must be documented as risks in the risk register and handled via risk acceptance per Section 10.
- Repeated failure to maintain risk records, evidence, or review cadence will be escalated to Head of IT Infrastructure Services and may trigger Internal Audit review.

## 16. Evidence and record retention
Risk management evidence must be retained in an approved system with access controls and audit trails. Evidence must be time-bound, attributable, and repeatable, and include approvals, logs, and validation artifacts where applicable.

Minimum retention expectations (aligned to auditability needs):
- Risk records and acceptance approvals: retained for the life of the risk plus at least one audit cycle.
- Validation artifacts (scan reports, access review outputs, restore tests): retained per applicable governance retention schedules and audit requirements.
- Change and CAB records referenced as evidence: retained per ITSM retention controls.

## 17. Metrics and key risk indicators
Norfolk Industries shall track the following minimum metrics for IT Infrastructure Services:

| Metric | Description | Ownership |
|---|---|---|
| High/Critical residual risk count | Number of open High/Critical risks | IT Governance Manager / Service Owner |
| Treatment plan timeliness | % of treatment actions completed by due date | Service Owner |
| Vulnerability remediation performance | % remediation within defined SLA bands by severity | Platform Owner / IT Operations Manager |
| Logging coverage | % of critical infrastructure CIs with required logs ingested to SIEM | Security Engineer / Platform Owner |
| Privileged access coverage | % of privileged accounts onboarded to PAM | IAM Engineer / Security Engineer |
| Vendor access compliance | % vendor accounts time-bounded and reviewed | Service Owner / IAM Engineer |
| Backup/restore validation | % of critical services with successful restore tests within required interval | Service Owner / IT Operations Manager |
| OT remote access posture | % OT remote access sessions routed through approved controls and logged | Platform Owner / IT Operations Manager |

## 18. Control mappings (standards alignment)
This policy supports a unified control posture aligned to ISO/IEC 27001 Annex A concepts, NIST CSF functions, ITIL 4 practices, COBIT 2019 domains, and SOC 2 Trust Services Criteria.

### 18.1 Control mapping table

| Policy element | ISO/IEC 27001 (conceptual Annex A areas) | NIST CSF | SOC 2 TSC | ITIL 4 practices | COBIT 2019 |
|---|---|---|---|---|---|
| Risk taxonomy, register, scoring, acceptance | Information security governance; risk management; compliance | Identify | Security; Availability | Information Security Management | APO, EDM, MEA |
| Change/CAB risk integration | Change control; secure engineering | Protect | Security; Availability | Change Enablement; Service Configuration Management | BAI, DSS |
| Monitoring and detection integration | Logging and monitoring; incident readiness | Detect, Respond | Security; Availability | Monitoring and Event Management; Incident Management | DSS, MEA |
| Vulnerability and configuration risk management | Technical vulnerability management; configuration management | Identify, Protect | Security | Problem Management; Service Configuration Management | BAI, DSS |
| Backup, RPO/RTO risk linkage | ICT readiness for continuity | Recover | Availability | Service Continuity Management | DSS |
| Vendor access and PAM requirements | Supplier relationships; access control | Protect, Detect | Security; Confidentiality | Supplier Management; Information Security Management | APO, DSS |
| OT/IT integration risk requirements | Network security; access control; operational resilience | Identify, Protect, Respond, Recover | Availability; Security | Service Continuity Management; Information Security Management | APO, DSS |

### 18.2 Evidence principles application
Evidence collected under this policy must:
- Be time-bound, attributable, and repeatable.
- Include approvals, logs, and validation artifacts where applicable.

## 19. Policy governance
### 19.1 Ownership and maintenance
- Policy Owner: **IT Governance Manager**
- Accountable Executive: **Head of IT Infrastructure Services**
- Security Oversight: **CISO**

### 19.2 Review cycle
- Reviewed at least annually, and additionally upon:
  - Material changes to hybrid cloud strategy or OT/IT integration controls
  - Significant audit findings
  - Major incidents indicating control failures

### 19.3 Publication and communication
- Published in the approved Norfolk Industries policy repository and communicated to Global IT Operations and Regional IT Operations.
- Process changes impacting ITSM workflows will be coordinated by ITSM Process Owner.

---

## Appendix A: Infrastructure Risk Register Template (Markdown)
Use this template for each risk entry captured in the approved system.

| Field | Value |
|---|---|
| Risk ID |  |
| Title |  |
| Description (condition/cause/consequence) |  |
| Category (primary/secondary) |  |
| Affected services |  |
| Affected CIs (CMDB references) |  |
| Region(s) impacted | North America / Europe / APAC / Global |
| Risk Owner (Service Owner) |  |
| Stakeholders |  |
| Inherent likelihood (1–5) |  |
| Inherent impact (1–5) |  |
| Inherent score (L×I) |  |
| Existing controls (prevent/detect/correct) |  |
| Control effectiveness notes |  |
| Residual likelihood (1–5) |  |
| Residual impact (1–5) |  |
| Residual score (L×I) |  |
| Residual rating band | Low / Medium / High / Critical |
| Treatment decision | Treat / Transfer / Avoid / Tolerate (accept) |
| Treatment plan summary |  |
| Treatment actions (detailed) |  |
| Action owners |  |
| Due dates |  |
| Monitoring (metrics/alerts/review frequency) |  |
| Acceptance record (if tolerated) | Approver / Date / Expiry / Rationale |
| Related Change records |  |
| Related Incident/Problem records |  |
| Evidence links |  |
| Status | Open / In treatment / Accepted / Closed |
| Last reviewed (date/by) |  |

---

## Appendix B: Risk Assessment Worksheet (Markdown)
Use this worksheet to ensure consistent evaluation and documentation.

### B.1 Risk statement
| Item | Response |
|---|---|
| What is happening or could happen? (condition) |  |
| Why could it happen? (cause) |  |
| What happens if it occurs? (consequence) |  |
| Which category applies? |  |
| Which services/CIs are impacted? |  |
| Which regions/sites are impacted? |  |
| Is OT impacted or involved? Describe pathways. |  |
| Is vendor/third-party access involved? Describe. |  |
| Are personal data processing or GDPR obligations impacted? |  |
| Are SOX-relevant systems or reporting impacted? |  |

### B.2 Inherent risk scoring
| Dimension | Score (1–5) | Justification |
|---|---:|---|
| Likelihood |  |  |
| Impact |  |  |
| Inherent score (L×I) |  |  |

### B.3 Existing controls assessment
| Control type | Controls in place | Evidence source | Effectiveness (Strong/Moderate/Weak) | Gaps |
|---|---|---|---|---|
| Prevent |  |  |  |  |
| Detect |  |  |  |  |
| Correct |  |  |  |  |

### B.4 Residual risk scoring
| Dimension | Score (1–5) | Justification (based on controls and evidence) |
|---|---:|---|
| Likelihood |  |  |
| Impact |  |  |
| Residual score (L×I) |  |  |
| Rating band |  |  |

### B.5 Treatment planning
| Item | Response |
|---|---|
| Treatment decision (Treat/Transfer/Avoid/Tolerate) |  |
| Target residual rating band |  |
| Planned control improvements |  |
| Dependencies (Change/CAB, vendor coordination, OT windows) |  |
| Validation plan (how will reduction be proven?) |  |
| Monitoring plan (metrics/alerts and frequency) |  |

### B.6 Risk acceptance (if applicable)
| Item | Response |
|---|---|
| Acceptance rationale |  |
| Compensating controls |  |
| Acceptance authority required (per Section 10.3) |  |
| Acceptance expiry date |  |
| Review frequency while accepted |  |
| Required evidence of monitoring |  |

---

## Appendix C: Evidence List (Minimum Evidence by Risk Type)
This appendix defines acceptable evidence artifacts to support assessment, treatment, and residual scoring. Evidence must be time-bound, attributable, and repeatable.

### C.1 Evidence by category

| Risk category | Minimum acceptable evidence examples |
|---|---|
| Identity and Access Management | Entra ID sign-in/audit logs; MFA/Conditional Access policy exports; privileged account inventory; PAM onboarding reports; access review outputs; change records for policy updates |
| Cloud and Platform Security | Azure Policy/initiative compliance reports; cloud configuration assessment outputs; resource diagnostic settings showing logging enabled; key/secret rotation evidence; change records and deployment pipelines logs |
| Network and Connectivity | Firewall rule review records; network diagrams showing segmentation; VPN/remote access configuration baselines; network device logs forwarded to SIEM; CAB approvals for boundary changes |
| Endpoint and Server Security | EDR onboarding/compliance dashboards; patch compliance reports; secure baseline compliance results; vulnerability scan evidence mapped to assets; exception approvals recorded as accepted risks |
| Monitoring, Logging, and Detection | SIEM data connector status; log source inventory; alert rule change history; incident tickets linked to alerts; time synchronization configuration evidence |
| Vulnerability and Configuration Management | Tenable/Nessus scan configurations and coverage reports; remediation tracking with due dates; rescans showing closure; CMDB reconciliation evidence; standard/baseline documents |
| Backup, Recovery, and Service Continuity | Backup job success reports; immutable backup configuration evidence where applicable; documented restore test results; DR exercise reports; achieved RPO/RTO test outputs |
| Supplier and Third-Party Access | Vendor onboarding approvals; identity records showing time-bounded access; PAM session recordings/log summaries; remote access logs; periodic vendor access reviews; contract/security requirement attestations retained by governance processes |
| Operational Technology (OT) Integration | Network segmentation diagrams (OT DMZ); jump host configuration and logs; remote session logs; firewall allow-list evidence; OT logging/monitoring coverage documentation; coordinated change windows evidence |
| Compliance and Auditability | CAB minutes/approvals; SOX control evidence packs for access/change controls; GDPR-related assessments where applicable; Internal Audit reports and remediation evidence |

### C.2 Evidence-to-risk register linkage checklist
- Evidence includes date/time and system source.
- Evidence includes approver identity where approval is required.
- Evidence is linked to the specific Risk ID and, where applicable, to Change/Incident/Problem records.
- Evidence demonstrates both implementation and validation (for control improvements).