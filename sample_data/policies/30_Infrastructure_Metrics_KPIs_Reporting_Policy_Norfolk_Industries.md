# Infrastructure Metrics, KPIs & Reporting Policy (Norfolk Industries)

## 1. Purpose
This policy defines how Norfolk Industries establishes, measures, reports, and governs Infrastructure metrics and Key Performance Indicators (KPIs) for IT Infrastructure Services. It ensures consistent, auditable reporting that supports service reliability, risk management, compliance obligations, and continual improvement across Global IT Operations and Regional IT Operations.

## 2. Scope
### 2.1 In Scope
- All services operated or governed by IT Infrastructure Services across:
  - Microsoft Azure (primary) and AWS (secondary)
  - On-prem data centers
  - Identity services (Active Directory and Entra ID (Azure AD), then Entra ID)
  - Endpoint management (Microsoft Intune and ConfigMgr where needed)
  - Security tooling (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk)
  - Monitoring, backup, and disaster recovery (DR)
- KPI reporting for 24×7 operations across North America, Europe, and APAC.
- KPI reporting that supports ITIL 4 practices, ISO/IEC 27001, ISO/IEC 22301, SOC 2, GDPR, and SOX.

### 2.2 Out of Scope
- Application business KPIs not owned by IT Infrastructure Services (unless explicitly defined as supporting metrics for an infrastructure service).
- OT production metrics owned exclusively by plant engineering; however, infrastructure KPIs that enable Operational Technology (OT) connectivity and secure remote access are in scope where provided by IT Infrastructure Services.

## 3. Policy Statement
Norfolk Industries will:
1. Define a standard KPI catalog for IT Infrastructure Services, including formulas, data sources, thresholds, owners, and cadences.
2. Collect KPI data from authoritative systems of record and monitoring tools, ensuring evidence is time-bound, attributable, and repeatable.
3. Report KPI results to operational teams, the Change Advisory Board (CAB), and executives through standardized monthly and quarterly reporting packs.
4. Perform monthly KPI reviews and enforce remediation actions when thresholds are not met.
5. Maintain KPI definitions and reporting artifacts as controlled documentation within the Information Security Management System (ISMS) and ITIL-aligned ITSM processes.

## 4. Governance, Standards, and Control Alignment
### 4.1 Governance Frameworks (Always Apply)
This policy is governed by and aligned to:
- ISO/IEC 27001 (ISMS)
- ISO/IEC 22301 (BCMS)
- ITIL 4
- COBIT 2019
- NIST CSF and NIST SP 800-53 concepts
- SOC 2 (Trust Services Criteria)
- GDPR
- SOX

### 4.2 Control-to-Evidence Principles
All KPI evidence must follow these principles:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

### 4.3 Control Mapping Summary (Conceptual)
| KPI Domain | ISO/IEC 27001 Annex A (Conceptual) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain |
|---|---|---|---|---|---|
| Availability / Performance / Capacity | Availability & resilience controls; operational procedures | Protect, Detect, Recover | Availability | Monitoring and Event Management; Service Continuity Management | DSS, BAI, MEA |
| Change Success Rate | Change control; operational change procedures | Protect | Security, Availability | Change Enablement | BAI, DSS, MEA |
| Incident MTTR | Incident handling; operational resilience | Respond, Recover | Availability, Security | Incident Management; Problem Management | DSS, MEA |
| Vulnerability SLA | Vulnerability management; technical security | Identify, Protect, Detect | Security | Information Security Management | APO, DSS, MEA |
| Backup Success | Backup and recovery controls | Recover | Availability | Service Continuity Management | DSS, MEA |
| DR Testing | Business continuity and DR validation | Recover | Availability | Service Continuity Management | DSS, MEA |
| Compliance Posture | Policy, logging, access, auditability | Identify, Protect | Security, Privacy | Information Security Management | EDM, APO, MEA |

## 5. Definitions (Glossary)
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.

## 6. Roles and Responsibilities
### 6.1 Accountability and Ownership
- KPI ownership is assigned to the **Service Owner** for each infrastructure service.
- KPI platform instrumentation and technical data integrity are owned by the **Platform Owner**.
- Operational execution and day-to-day performance against KPIs are owned by the **IT Operations Manager** (Global IT Operations and/or Regional IT Operations depending on the service model).

### 6.2 RACI (Policy-Level)
Aligned to the authoritative RACI master.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 7. KPI Domains and Requirements
Norfolk Industries maintains KPI domains that reflect service reliability, security posture, and operational excellence. Each KPI must define:
- **Formula** (including numerator/denominator and inclusions/exclusions)
- **Data source(s)** (authoritative systems)
- **Reporting cadence**
- **Owner** (Service Owner; contributing roles as needed)
- **Thresholds** (target, warning, breach)
- **Segmentation** (Global/Regional; by service; by environment: cloud/on-prem; by criticality tier)
- **Evidence artifacts** for audit readiness

Required KPI domains:
1. Availability
2. Performance
3. Capacity
4. Change success rate
5. Incident MTTR
6. Vulnerability SLA
7. Backup success
8. DR testing
9. Compliance posture

## 8. KPI Definitions, Formulas, and Thresholds
### 8.1 Availability KPI
**Metric Name:** Service Availability (%)

- **Formula:**  
  \[
  \text{Availability \%} = \left( \frac{\text{Total Minutes} - \text{Unplanned Downtime Minutes}}{\text{Total Minutes}} \right) \times 100
  \]
- **Inclusions:** Customer-impacting unplanned outages of the service (including underlying infrastructure failures when attributable).
- **Exclusions:** Pre-approved maintenance windows implemented via Change Enablement and approved by the Change Advisory Board (CAB); force majeure events may be excluded only if formally recorded as an approved exception and referenced in the monthly KPI review minutes.
- **Thresholds (default unless service-specific SLO differs):**
  - Target: ≥ 99.9%
  - Warning: 99.5% to < 99.9%
  - Breach: < 99.5%
- **Primary data sources:** Monitoring platform (infrastructure monitoring), ITSM incident records (outage start/stop validation), major incident timeline.
- **Owner:** Service Owner
- **Contributors:** Platform Owner, IT Operations Manager, ITSM Process Owner

### 8.2 Performance KPI
**Metric Name:** Service Performance SLO Attainment (%)

- **Formula:**  
  \[
  \text{SLO Attainment \%} = \left( \frac{\text{Number of Measurement Intervals Meeting SLO}}{\text{Total Measurement Intervals}} \right) \times 100
  \]
- **Example SLO types:** API response time, authentication latency (Entra ID integrated services), network latency between defined sites, storage IOPS latency, endpoint compliance check-in latency.
- **Thresholds (default):**
  - Target: ≥ 99.0%
  - Warning: 98.0% to < 99.0%
  - Breach: < 98.0%
- **Primary data sources:** Monitoring/APM metrics, Azure Monitor, AWS CloudWatch, network monitoring, synthetic transaction results.
- **Owner:** Service Owner
- **Contributors:** Platform Owner, IT Operations Manager

### 8.3 Capacity KPI
**Metric Name:** Capacity Headroom (%)

- **Formula:**  
  \[
  \text{Headroom \%} = \left( \frac{\text{Total Capacity} - \text{Peak Utilization}}{\text{Total Capacity}} \right) \times 100
  \]
- **Measurement:** Use peak (P95) utilization during the month for CPU, memory, storage, bandwidth, and key license pools where applicable.
- **Thresholds (default):**
  - Target: ≥ 20% headroom
  - Warning: 10% to < 20% headroom
  - Breach: < 10% headroom
- **Primary data sources:** Monitoring platform, cloud capacity metrics (Azure/AWS), SAN/NAS monitoring, IPAM/network telemetry, licensing portals where applicable.
- **Owner:** Service Owner
- **Contributors:** Platform Owner, Cloud Engineer, Systems Engineer, Network Engineer

### 8.4 Change Success Rate KPI
**Metric Name:** Change Success Rate (%)

- **Formula:**  
  \[
  \text{Change Success Rate \%} = \left( \frac{\text{Successful Changes}}{\text{Total Implemented Changes}} \right) \times 100
  \]
- **Successful Change definition:** A change that is implemented within the approved window and scope, and does not cause a Severity 1 or Severity 2 incident, unplanned outage, or rollback attributable to the change within 7 calendar days.
- **Thresholds (default):**
  - Target: ≥ 95%
  - Warning: 90% to < 95%
  - Breach: < 90%
- **Primary data sources:** ITSM change records (including CAB approvals), incident/problem linkage, post-implementation review outcomes.
- **Owner:** ITSM Process Owner (process integrity); Service Owner (service-level outcome)
- **Contributors:** IT Operations Manager, Platform Owner

### 8.5 Incident MTTR KPI
**Metric Name:** Mean Time to Restore (MTTR)

- **Formula:**  
  \[
  \text{MTTR} = \frac{\sum(\text{Incident Restore Time} - \text{Incident Start Time})}{\text{Number of Incidents}}
  \]
- **Scope:** Severity 1 and Severity 2 incidents impacting IT Infrastructure Services; may be segmented by service and region.
- **Thresholds (default):**
  - Target: ≤ 4 hours (Sev1), ≤ 8 hours (Sev2)
  - Warning: 4–6 hours (Sev1), 8–12 hours (Sev2)
  - Breach: > 6 hours (Sev1), > 12 hours (Sev2)
- **Primary data sources:** ITSM incident records, major incident timelines, on-call logs.
- **Owner:** IT Operations Manager
- **Contributors:** Service Desk Manager, Service Owner, Platform Owner

### 8.6 Vulnerability SLA KPI
**Metric Name:** Vulnerability Remediation SLA Compliance (%)

- **Formula:**  
  \[
  \text{SLA Compliance \%} = \left( \frac{\text{Vulnerabilities Remediated Within SLA}}{\text{Total Vulnerabilities Due Within Period}} \right) \times 100
  \]
- **Severity-based SLA (default):**
  - Critical: 14 calendar days
  - High: 30 calendar days
  - Medium: 90 calendar days
  - Low: 180 calendar days
- **Thresholds (default):**
  - Target: ≥ 95%
  - Warning: 90% to < 95%
  - Breach: < 90%
- **Primary data sources:** Vulnerability scanner (Tenable/Nessus), ticketing workflow in ITSM, EDR exposure management where applicable.
- **Owner:** Service Owner (for affected service); CISO consulted for risk posture
- **Contributors:** Security Engineer, Platform Owner, IT Operations Manager

### 8.7 Backup Success KPI
**Metric Name:** Backup Job Success Rate (%)

- **Formula:**  
  \[
  \text{Backup Success Rate \%} = \left( \frac{\text{Successful Backup Jobs}}{\text{Total Scheduled Backup Jobs}} \right) \times 100
  \]
- **Rules:** Jobs are “successful” if completed without error and meet backup policy requirements (retention, encryption, immutability where configured).
- **Thresholds (default):**
  - Target: ≥ 98%
  - Warning: 95% to < 98%
  - Breach: < 95%
- **Primary data sources:** Backup platform logs/reports, storage snapshots audit logs, ITSM incident linkage for backup failures.
- **Owner:** Service Owner
- **Contributors:** Systems Engineer, Cloud Engineer, IT Operations Manager

### 8.8 DR Testing KPI
**Metric Name:** DR Test Completion and Success (%)

- **Formula (completion):**  
  \[
  \text{DR Completion \%} = \left( \frac{\text{DR Tests Completed}}{\text{DR Tests Scheduled}} \right) \times 100
  \]
- **Formula (success):**  
  \[
  \text{DR Success \%} = \left( \frac{\text{DR Tests Meeting RTO/RPO}}{\text{DR Tests Completed}} \right) \times 100
  \]
- **Thresholds (default):**
  - Completion Target: 100% per defined schedule
  - Success Target: ≥ 95% meeting RTO/RPO
  - Warning: Success 90% to < 95%
  - Breach: Success < 90% or any missed scheduled test
- **Primary data sources:** DR test reports, recovery runbooks execution logs, change records (if DR test requires changes), evidence attachments.
- **Owner:** Service Owner
- **Contributors:** IT Operations Manager, Platform Owner, IT Governance Manager

### 8.9 Compliance Posture KPI
**Metric Name:** Infrastructure Compliance Posture (%)

- **Formula:**  
  \[
  \text{Compliance \%} = \left( \frac{\text{Compliant CIs}}{\text{Total In-Scope CIs Assessed}} \right) \times 100
  \]
- **Compliance dimensions (examples):** patch compliance, baseline configuration compliance, logging enabled, MFA/conditional access enforced, encryption at rest, EDR onboarding, privileged access controls, backup policy applied.
- **Thresholds (default):**
  - Target: ≥ 97%
  - Warning: 95% to < 97%
  - Breach: < 95%
- **Primary data sources:** Endpoint management (Intune/ConfigMgr), cloud policy compliance (Azure Policy; AWS Config where applicable), EDR coverage, IAM logs, CMDB CI inventory.
- **Owner:** IT Governance Manager (program reporting integrity); Service Owner (service-level compliance)
- **Contributors:** Platform Owner, IAM Engineer, Endpoint Engineer, Security Engineer, Internal Audit (independent assessment)

## 9. Data Sources, Tooling, and System of Record
### 9.1 Authoritative Systems
| Data Type | Authoritative Source | Notes |
|---|---|---|
| Incidents, Changes, Problems, CMDB CIs | ITIL-aligned ITSM tool (e.g., ServiceNow) | Source of record for workflow, approvals, linkage, and audit trail |
| Monitoring and uptime | Enterprise monitoring platform; cloud-native telemetry (Azure Monitor, AWS CloudWatch) | Monitoring must support time synchronization and retention per logging standards |
| Security detections and log analytics | SIEM (e.g., Microsoft Sentinel) | Used for correlation and evidence of detection/response where required |
| Endpoint posture | Microsoft Intune and ConfigMgr where needed | Used for compliance and coverage KPIs |
| Vulnerabilities | Tenable/Nessus (or approved equivalent) | Scanner findings must be tied to remediation tickets |
| Privileged access events | PAM (e.g., CyberArk) | Supports compliance posture evidence where applicable |
| Identity signals | Active Directory and Entra ID | Supports identity-related performance and compliance metrics |
| Backup/restore | Enterprise backup platform and immutable storage logs | Must provide job history and restore test evidence |

### 9.2 Data Quality Requirements
- KPI computations must use consistent time zones (UTC recommended for global rollups) with regional views available.
- KPI datasets must be traceable back to raw records (tickets, logs, reports).
- Any manual data adjustments require documented justification and approval by the IT Governance Manager.

## 10. Reporting Cadence and Audience
### 10.1 Cadence
| Report | Cadence | Audience | Owner |
|---|---|---|---|
| Operational KPI Review | Weekly (optional per service), Monthly (mandatory) | Global IT Operations, Regional IT Operations, Service Owners | IT Operations Manager |
| CAB KPI Snapshot | Monthly and before major release windows | Change Advisory Board (CAB) | ITSM Process Owner |
| Executive KPI Pack | Monthly | CIO, Head of IT Infrastructure Services, CISO | Head of IT Infrastructure Services (accountable), IT Governance Manager (coordination) |
| Quarterly Risk and Compliance KPI Review | Quarterly | CIO, CISO, Internal Audit (as needed), Service Owners | IT Governance Manager |
| DR Testing Summary | After each DR test + quarterly rollup | Service Owners, IT Operations Manager, IT Governance Manager | Service Owner |

### 10.2 Segmentation Standards
Reports must include:
- Global rollup plus regional breakdown (North America, Europe, APAC) where service delivery differs.
- Critical service tier tagging (business-critical vs standard).
- Cloud vs on-prem where materially relevant.
- OT-connected services must be tagged as “OT-Connected” for visibility while respecting OT governance boundaries.

## 11. Threshold Management and Exceptions
### 11.1 Standard Thresholds
Default thresholds in Section 8 apply unless a service has an approved SLO/threshold variance.

### 11.2 Threshold Exceptions
- Exceptions require a documented risk rationale and compensating controls.
- Approval:
  - High-risk exceptions: **CIO (A)**, **Head of IT Infrastructure Services (R)**, **CISO (R)**, **IT Governance Manager (C)** consistent with enterprise exception governance.
- Exceptions must include:
  - Scope (service/CIs)
  - Duration (start and end date)
  - Compensating controls
  - Residual risk acceptance statement
  - Evidence of approval and review cadence

## 12. Procedures
### 12.1 Monthly KPI Review Procedure (Mandatory)
**Objective:** Validate KPI results, identify breaches/trends, and commit remediation actions.

**Steps:**
1. **Data compilation (Day 1–3):** Platform Owner and IT Operations Manager validate source datasets (monitoring, ITSM, vulnerability, backup, compliance).
2. **KPI calculation (Day 3–5):** Service Owner generates KPI results using approved formulas; IT Governance Manager validates policy adherence for enterprise rollups.
3. **Review meeting (By Day 7):** IT Operations Manager chairs the monthly KPI review with Service Owners and Platform Owners.
4. **Breach analysis:** For each warning/breach:
   - Confirm correctness of data and classification.
   - Identify likely contributors (change-related, capacity, third-party, configuration drift).
   - Determine whether a Problem record is required.
5. **Remediation plan creation:** Create ITSM tasks/Problem records with:
   - Owner, due date, milestones
   - Risk rating and customer impact summary
   - Required changes routed through Change Enablement and CAB as appropriate
6. **Communications:** Service Desk Manager ensures stakeholder communications for material customer impact and major trends.
7. **Evidence capture:** Attach KPI pack, minutes, and remediation tickets to the monthly KPI review record repository under ISMS evidence conventions.

**Required outputs:**
- Monthly KPI review minutes with attendance, decisions, and action register
- Updated KPI dashboard exports
- Linked ITSM records (incidents, problems, changes) for breaches

### 12.2 Executive Reporting Pack Procedure (Monthly)
**Objective:** Provide consistent executive-level visibility into reliability, security hygiene, and operational health.

**Content requirements:**
- One-page summary per KPI domain with trend (current month, prior month, 3-month rolling).
- Material incidents (Sev1/Sev2) summary with MTTR and recurring causes.
- Change performance summary with top contributors to failed changes.
- Vulnerability SLA heatmap (Critical/High/Medium/Low) and overdue aging.
- Backup and DR test status with RTO/RPO success.
- Compliance posture and top non-compliant control categories.
- “Top 5 risks” and “Top 5 remediation commitments” with due dates.

**Steps:**
1. IT Governance Manager compiles enterprise rollups and confirms evidence traceability.
2. Head of IT Infrastructure Services reviews for completeness and risk alignment.
3. CISO reviews security-related KPIs (vulnerability SLA and compliance posture) for risk statements.
4. Distribute to CIO, Head of IT Infrastructure Services, and CISO; archive versioned pack in controlled repository.

### 12.3 Remediation Actions Procedure (When Thresholds Are Not Met)
**Triggers:**
- Any KPI breach, repeated warnings over 2 consecutive months, or a single critical control failure (e.g., missed DR test, systemic backup failures).

**Required actions:**
1. **Immediate containment:** IT Operations Manager initiates operational mitigation (monitoring increases, failover readiness, change freeze if needed).
2. **Record creation:** Create or update a Problem record for systemic issues; link incidents/changes.
3. **Root cause analysis:** Platform Owner leads technical RCA; Service Owner approves remediation approach.
4. **Remediation implementation:** All remediation changes follow Change Enablement and CAB governance.
5. **Validation:** Post-change validation evidence must include metrics improvement or control verification.
6. **Closure criteria:** Breach is closed when KPI returns to target for one full reporting cycle or an approved exception is granted.

## 13. Documentation, Evidence, and Record Retention
### 13.1 Required Records
- KPI catalog (controlled document)
- Monthly KPI review packs and minutes
- Executive KPI packs (versioned)
- Source exports and queries used for KPI calculations (or references to dashboards with immutable timestamps)
- ITSM records linking incidents, problems, changes to KPI breaches
- DR test reports and runbook execution logs
- Vulnerability SLA reports with ticket linkage
- Backup job reports and restore test evidence

### 13.2 Retention and Access
- Records are retained in accordance with Norfolk Industries ISMS and audit requirements and must support SOX auditability for in-scope systems.
- Access is restricted based on least privilege, with executive packs available to authorized leadership and audit stakeholders.

## 14. Communications and Training
- Service Owners and Platform Owners must be trained on KPI definitions, formulas, and evidence requirements annually.
- ITSM Process Owner ensures Change Enablement and Incident Management teams understand KPI linkages and ticket hygiene requirements (e.g., accurate timestamps, linkage fields).

## 15. Compliance and Audit
- Internal Audit may independently assess KPI design and operating effectiveness, including traceability from executive reporting back to raw records.
- The IT Governance Manager coordinates evidence collection and ensures consistent application of the evidence principles.

## 16. Security and Privacy Considerations
- KPI datasets may include operational logs and user identifiers; processing must align to GDPR and internal data handling rules.
- KPI reporting must avoid unnecessary personal data; use aggregation where possible.
- Security-related KPIs (vulnerability and compliance posture) must be handled as sensitive operational security information and shared on a need-to-know basis.

## 17. Policy Exceptions
- Exceptions are documented, risk-assessed, time-bound, and approved per Section 11.2.
- Exceptions must be reviewed at least monthly during KPI review until closed.

## 18. Enforcement
Non-compliance with this policy may result in:
- Mandatory corrective action plans
- Increased audit scrutiny and reporting to the CIO, Head of IT Infrastructure Services, and CISO
- Restrictions on change velocity (e.g., additional CAB scrutiny) until KPI reporting integrity and performance are restored

## 19. Review and Maintenance
- This policy is reviewed at least annually by the IT Governance Manager and approved per governance requirements.
- KPI definitions are reviewed quarterly to ensure alignment with service architecture changes, tooling changes, and emerging risks.

## Appendix A: KPI Catalog (Standard)
The following catalog defines the standard KPI set for IT Infrastructure Services. Service-specific KPIs may be added by Service Owners provided they include formula, data source, threshold, cadence, and evidence.

| KPI Domain | KPI Name | Formula (Summary) | Primary Data Sources | Cadence | Owner | Target / Warning / Breach |
|---|---|---|---|---|---|---|
| Availability | Service Availability (%) | ((Total minutes − unplanned downtime) / total minutes) × 100 | Monitoring platform; ITSM incidents | Monthly | Service Owner | ≥99.9 / 99.5–<99.9 / <99.5 |
| Performance | Performance SLO Attainment (%) | (Intervals meeting SLO / total intervals) × 100 | Monitoring; Azure Monitor; CloudWatch; network telemetry | Monthly | Service Owner | ≥99.0 / 98.0–<99.0 / <98.0 |
| Capacity | Capacity Headroom (%) | (Total capacity − P95 peak utilization) / total capacity × 100 | Monitoring; cloud metrics; storage/network telemetry | Monthly | Service Owner | ≥20 / 10–<20 / <10 |
| Change | Change Success Rate (%) | Successful implemented changes / total implemented changes × 100 | ITSM changes; incident linkage; PIRs | Monthly | ITSM Process Owner (process), Service Owner (outcome) | ≥95 / 90–<95 / <90 |
| Incident | MTTR (Sev1/Sev2) | Avg(restore time − start time) | ITSM incidents; major incident timeline | Monthly | IT Operations Manager | Sev1 ≤4h (warn 4–6, breach >6); Sev2 ≤8h (warn 8–12, breach >12) |
| Vulnerability | Vulnerability SLA Compliance (%) | Remediated within SLA / due within period × 100 | Tenable/Nessus; ITSM remediation tickets | Monthly | Service Owner | ≥95 / 90–<95 / <90 |
| Backup | Backup Job Success Rate (%) | Successful jobs / scheduled jobs × 100 | Backup platform reports; logs | Monthly | Service Owner | ≥98 / 95–<98 / <95 |
| DR | DR Completion (%) | Completed tests / scheduled tests × 100 | DR test plans/reports; runbooks | Quarterly + per test | Service Owner | 100% required; any miss is breach |
| DR | DR Success (%) | Tests meeting RTO/RPO / completed tests × 100 | DR reports; restore logs | Quarterly + per test | Service Owner | ≥95 / 90–<95 / <90 |
| Compliance | Compliance Posture (%) | Compliant CIs / assessed CIs × 100 | Intune/ConfigMgr; Azure Policy; AWS Config; EDR; CMDB | Monthly | IT Governance Manager (integrity), Service Owner (outcome) | ≥97 / 95–<97 / <95 |

## Appendix B: Executive Dashboard Mock (Textual)
### B.1 Monthly Executive Summary (One Page Layout)
**Norfolk Industries — IT Infrastructure Services KPI Dashboard (Month YYYY-MM)**

**Overall status**
- Availability: **Green / Amber / Red** (global rollup, with regional variances)
- Performance: **Green / Amber / Red**
- Capacity: **Green / Amber / Red**
- Change success: **Green / Amber / Red**
- Incident MTTR: **Green / Amber / Red**
- Vulnerability SLA: **Green / Amber / Red**
- Backup success: **Green / Amber / Red**
- DR testing: **Green / Amber / Red**
- Compliance posture: **Green / Amber / Red**

**Trends (3-month rolling)**
- Availability: Month-2 → Month-1 → Month
- MTTR Sev1: Month-2 → Month-1 → Month
- Vulnerability overdue (Critical/High counts): Month-2 → Month-1 → Month
- Backup failures: Month-2 → Month-1 → Month
- Compliance posture: Month-2 → Month-1 → Month

**Top operational events**
- Sev1 count: X (Top causes: Change-related, capacity exhaustion, provider incident, configuration drift)
- Sev2 count: Y

**Key risks (Top 5)**
1. Risk statement + impacted services + mitigation date
2. Risk statement + impacted services + mitigation date
3. Risk statement + impacted services + mitigation date
4. Risk statement + impacted services + mitigation date
5. Risk statement + impacted services + mitigation date

**Commitments (Top 5 remediation actions)**
| Commitment | Owner | Due Date | Expected KPI Impact |
|---|---|---|---|
| Problem/Initiative name | Service Owner | Date | KPI(s) improved |
| Problem/Initiative name | Platform Owner | Date | KPI(s) improved |
| Problem/Initiative name | IT Operations Manager | Date | KPI(s) improved |
| Problem/Initiative name | Service Owner | Date | KPI(s) improved |
| Problem/Initiative name | ITSM Process Owner | Date | KPI(s) improved |

## Appendix C: Evidence List (Audit-Ready)
### C.1 Standard Evidence Artifacts by KPI Domain
| KPI Domain | Evidence Artifact | Evidence Attributes Required | System of Record |
|---|---|---|---|
| Availability | Monthly uptime report export + outage timeline | Timestamped export; outage IDs; linkage to ITSM incidents | Monitoring platform; ITSM |
| Performance | SLO attainment dashboard export | Time window; SLO definition; measurement intervals | Monitoring/APM; cloud telemetry |
| Capacity | Capacity utilization report with P95 peaks | Time window; resource scope; computed headroom | Monitoring; cloud metrics |
| Change | Change success report + failed change PIRs | CAB approvals; implementation timestamps; rollback records | ITSM |
| Incident MTTR | Incident report by severity with timestamps | Start/restore fields; severity; regional/service tagging | ITSM |
| Vulnerability SLA | SLA compliance report + remediation ticket linkage | Finding IDs; due dates; closure dates; exception approvals | Tenable/Nessus; ITSM |
| Backup | Backup job success report + restore test results | Job IDs; schedules; failures; restore validation | Backup platform |
| DR testing | DR test plan, execution log, RTO/RPO results | Test date; scope; success criteria; sign-off | DR repository; ITSM changes if used |
| Compliance posture | Compliance dashboard export + CI inventory snapshot | CI count; compliance rules; timestamps; exceptions | Intune/ConfigMgr; Azure Policy; AWS Config; CMDB |

### C.2 Evidence Packaging Rules
- Each monthly reporting cycle must have a single evidence folder/package containing:
  - Executive KPI pack (final)
  - Monthly KPI review minutes and action register
  - Source exports (or immutable dashboard links) used for KPI calculations
  - Exceptions and approvals (if any)
- Evidence must be attributable to an owner (Service Owner or IT Governance Manager) and reproducible from systems of record.