# Backup, Retention & Recovery Policy (Norfolk Industries)

## 1. Purpose
This policy defines the minimum requirements for backup, retention, and recovery for Norfolk Industries to ensure service continuity, protect data integrity and availability, and support compliance obligations across Information Technology (IT) and Operational Technology (OT) environments. It establishes standardized Recovery Point Objective (RPO) and Recovery Time Objective (RTO) tiers, backup controls (including immutability and encryption), and testing and evidence requirements aligned to the Information Security Management System (ISMS) and business continuity objectives.

## 2. Scope
### 2.1 In scope
This policy applies to:
- All production and non-production data and systems owned or operated by Norfolk Industries, including:
  - On-prem data centers
  - Microsoft Azure (primary) and AWS (secondary)
  - End-user file services and collaboration data where Norfolk Industries is the data controller or processor
  - Identity services including Active Directory and Entra ID (Azure AD) (first mention), then Entra ID
  - OT-connected systems where backup is technically feasible and approved (e.g., MES historian databases, supporting servers)
- All personnel and third parties who administer, operate, or request backup or restore actions.

### 2.2 Out of scope
- Personal backups on unmanaged storage (not permitted for corporate data)
- Vendor-managed backups where Norfolk Industries has no administrative access; such services must meet equivalent requirements via contract and evidence.

## 3. Policy statement
Norfolk Industries will implement, monitor, and continuously improve backup, retention, and recovery controls to:
- Meet defined RPO/RTO targets for critical services
- Protect backups from unauthorized access, alteration, and destruction through immutability, encryption, and segregated administrative access
- Maintain offsite recoverability and an airgap concept suitable for ransomware and destructive events
- Regularly test restores and disaster recovery procedures with documented results and remediation actions
- Produce time-bound, attributable, repeatable evidence for audit and assurance activities.

## 4. Governance and accountability
### 4.1 Ownership
- Accountable executive ownership resides with the **Head of IT Infrastructure Services**.
- Information security oversight is provided by the **CISO** through the ISMS.
- Process design and continual improvement for ITIL-aligned practices is coordinated by the **ITSM Process Owner**.

### 4.2 Change governance
Backup configuration changes (policies, schedules, retention, keys, immutability settings, repository changes, DR runbooks) are controlled via Change Enablement and, where required, reviewed by the **Change Advisory Board (CAB)**.

### 4.3 RACI (policy-level)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval (backup standards derived from this policy) | I | A | C | R | C | R | C | C | I |
| Procedure ownership (runbooks/templates) | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 5. Definitions
The following glossary terms apply:
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

## 6. Policy requirements (controls)
### 6.1 Data classification and criticality alignment
- Every in-scope service must have documented:
  - Business criticality and dependency mapping
  - Assigned RPO/RTO tier (Section 7)
  - Backup scope (what is backed up) and restore scope (what must be restorable)
- Service Owners are responsible for ensuring application-level requirements (consistency, quiescing, log backups, and integrity checks) are defined and implemented.

### 6.2 Backup coverage and completeness
- Backups must include, as applicable:
  - System state and configuration (including infrastructure-as-code repositories where used)
  - Application data stores (databases, file shares, object stores)
  - Virtual machine images or snapshots where appropriate (not as the sole backup unless justified and approved)
  - Critical encryption keys and configuration secrets must be handled through approved secret management and documented recovery procedures; keys are never stored unencrypted inside backup sets.

### 6.3 Immutability and ransomware resilience
- Backup repositories for Tier 0–2 systems (Section 7) must implement immutability to prevent alteration or deletion during the defined immutability window.
- The airgap concept must be implemented through at least one of the following, and documented per platform:
  - Logically isolated immutable storage with separate administrative identities
  - Cross-account / cross-subscription backup vault separation
  - Offline copy procedures where feasible
- Administrative access to backup systems must be segregated, monitored, and protected with privileged access controls and strong authentication.

### 6.4 Encryption and key management
- Backups must be encrypted in transit and at rest using industry-standard cryptography.
- Encryption keys must be protected using enterprise key management controls appropriate to the platform (cloud KMS/Key Vault or equivalent).
- Access to decrypt/restore data must be limited to authorized roles and logged.

### 6.5 Retention and legal/regulatory holds
- Retention must follow the defined tiers (Section 8) and any legal, regulatory, contractual, or records management requirements.
- If legal hold applies, backup deletion schedules must be suspended for relevant datasets in coordination with Norfolk Industries governance processes.

### 6.6 Monitoring, alerting, and remediation
- Backup job success/failure, repository capacity, immutability status, and restore-point availability must be monitored.
- Failed backups for Tier 0–2 must trigger incident handling and timely remediation aligned to operational SLOs.

### 6.7 Documentation and CMDB alignment
- Backup configurations, repositories, and protected workloads must be registered as **Configuration Items (CIs)** or linked to relevant CIs in the ITSM tool.
- Restore procedures must be maintained as controlled runbooks with versioning and change history.

## 7. RPO/RTO tiers and system mapping
### 7.1 Tier definitions
RPO and RTO tiers define the maximum tolerable data loss and target restoration time. Targets are set per service and validated via testing.

| Tier | Intended use | RPO target | RTO target | Minimum restore-point frequency expectation |
|---|---|---:|---:|---|
| Tier 0 (Mission-critical identity & safety-adjacent) | Identity and access and services whose failure causes enterprise-wide outage or safety/production stoppage | ≤ 15 minutes | ≤ 4 hours | Continuous or ≤ 15-minute capture (log/replication where applicable) |
| Tier 1 (Critical business services) | Revenue/production planning, order processing, plant support services with major operational impact | ≤ 1 hour | ≤ 8 hours | Hourly (or better) for data; daily image/snapshot as applicable |
| Tier 2 (Important services) | Departmental and shared services with moderate impact | ≤ 4 hours | ≤ 24 hours | Every 4 hours or daily depending on workload |
| Tier 3 (Standard services) | Non-critical services; can tolerate longer interruption | ≤ 24 hours | ≤ 72 hours | Daily |
| Tier 4 (Non-production / best effort) | Dev/test or low-value datasets | ≤ 24 hours | ≤ 5 business days | Daily or per team agreement |

### 7.2 System mapping (minimum targets)
Service Owners may set more stringent targets; less stringent targets require an approved exception.

| System / service class | Examples | Default tier | Notes on approach |
|---|---|---:|---|
| Enterprise Resource Planning (ERP) | ERP application and databases | Tier 1 | Database-aware backups, transaction log backups; tested point-in-time restore required |
| Manufacturing Execution System (MES) | MES app servers, historians, MES databases | Tier 1 (production plants) / Tier 2 (non-critical sites) | Coordinate with OT segmentation and plant windows; prioritize database consistency and historian restore validation |
| Active Directory | Domain controllers, AD-integrated DNS | Tier 0 | System-state backups + bare-metal/VM recovery; authoritative restore runbook required |
| Entra ID | Cloud identity control plane | Tier 0 (control dependency) | Configuration and audit export backups (tenant config, conditional access changes, privileged role assignments); validate break-glass accounts and recovery procedures |
| File services | Windows file shares, NAS, cloud file storage | Tier 2 (shared) / Tier 3 (local) | Use immutable backups; enable item-level and point-in-time restore where supported |
| Cloud workloads (Azure/AWS) | VMs, PaaS databases, object storage | Tier based on service criticality | Use native backups where applicable plus centralized governance; cross-region vault where required for Tier 0–2 |

## 8. Backup types, schedules, and retention
### 8.1 Approved backup types
Norfolk Industries uses the following backup mechanisms as appropriate to workload:
- **Full backups**: Complete copy of selected data set.
- **Incremental backups**: Captures changes since last backup.
- **Differential backups**: Captures changes since last full backup (where used).
- **Application-aware backups**: Quiescing and consistent snapshots for databases and transactional systems.
- **Transaction log backups** (databases): Enables point-in-time recovery.
- **Snapshots**: Permitted as a recovery acceleration mechanism; not the sole protection for Tier 0–2 unless a documented design demonstrates equivalence and is approved.

### 8.2 Standard schedules (minimums by tier)
| Tier | Minimum backup schedule | Minimum retention (operational) | Minimum retention (monthly) | Minimum retention (annual) |
|---|---|---:|---:|---:|
| Tier 0 | Hourly or better for data changes; daily full; logs/replication where supported | 35 days | 12 months | 7 years (if required for system of record) |
| Tier 1 | Daily full + hourly increments/logs where supported | 35 days | 12 months | 7 years for systems of record; otherwise 3 years |
| Tier 2 | Daily (full or incremental chain) | 35 days | 6 months | 3 years where required |
| Tier 3 | Daily | 14 days | 3 months | 1 year where required |
| Tier 4 | Daily or per team agreement | 7 days | Not required | Not required |

Retention must be increased when needed for:
- Regulatory requirements (including SOX-relevant financial systems)
- Contractual obligations
- Records management and legal hold

### 8.3 Immutability window standards
- Tier 0–1: Minimum 14 days immutable restore points
- Tier 2: Minimum 7 days immutable restore points
- Tier 3–4: Immutability recommended based on risk; required if exposed to ransomware pathways

### 8.4 Offsite and cross-region requirements
- Tier 0–2 must have at least one recoverable copy stored offsite:
  - Different data center for on-prem
  - Different region or equivalent isolation for cloud where feasible and approved
- Offsite copy must be protected with immutability or equivalent deletion protection and segregated administrative access.

### 8.5 Airgap concept (ransomware and destructive events)
Norfolk Industries implements an airgap concept for Tier 0–2 by maintaining at least one backup copy that is:
- Isolated from production identity and administrative paths (separate admin roles/identities)
- Protected with immutability and/or offline retention procedures
- Regularly validated via restore testing (Section 10)

## 9. Access control and segregation of duties
- Restore and backup administration access must be restricted to authorized personnel within IT Infrastructure Services and logged.
- Privileged operations must use approved privileged access controls (e.g., PAM) and strong authentication.
- Backup operators must not have unrestricted ability to:
  - Disable security tooling
  - Delete immutable repositories
  - Modify retention without change approval
- Service Desk may initiate restore requests but does not directly execute privileged restore actions for Tier 0–2 without documented authorization.

## 10. Testing and exercises
### 10.1 Restore testing requirements
Restore testing is mandatory to validate RPO/RTO feasibility and backup integrity.

| Tier | Minimum restore test frequency | Minimum test type |
|---|---:|---|
| Tier 0 | Quarterly | Full restore to isolated environment + validation steps; include identity recovery scenario components |
| Tier 1 | Semi-annually | Application-consistent restore + point-in-time recovery validation where applicable |
| Tier 2 | Annually | File/database restore validation and integrity checks |
| Tier 3–4 | Annually (sample-based) | Spot restore tests |

Testing must include:
- Verification of data integrity (application checks, database consistency checks as applicable)
- Timing capture (start/end timestamps) to demonstrate achieved RTO
- Confirmation of achieved restore point to demonstrate achieved RPO

### 10.2 Disaster recovery (DR) exercises
DR exercises validate end-to-end recovery capability beyond backups (e.g., dependencies, networking, identity, access, communications).

| Exercise type | Frequency | Minimum participants | Required outputs |
|---|---:|---|---|
| Tabletop exercise | Quarterly | IT Operations Manager, Service Owner(s), Security Engineer, ITSM Process Owner | Scenario notes, decisions, gaps, actions |
| Technical DR exercise (partial) | Semi-annually | Platform Owner(s), Service Owner(s), Regional IT Operations | Runbook execution evidence, timings, remediation |
| Technical DR exercise (full for highest criticality) | Annually | Global IT Operations + Regional IT Operations + Security Engineer | Recovery report, RTO/RPO achievement, improvement plan |

### 10.3 Post-test remediation
- Findings must be recorded as problems or action items in the ITSM tool with an owner and due date.
- Repeat failures or inability to meet tiers requires risk acceptance or remediation planning through governance.

## 11. Restore procedures (operational requirements)
### 11.1 Standard restore procedure (runbook summary)
Applies to routine restores (accidental deletion, corruption, minor outage).
1. **Request intake**: Restore request logged via ITSM with business justification, affected CI, and desired restore point.
2. **Authorization**: Service Owner approval required for production restores; additional approval for sensitive datasets per access controls.
3. **Validation**: Confirm backup availability, integrity, and restore method (file-level, volume-level, VM, database).
4. **Execution**: Perform restore to target (original or alternate location) using least-privilege access.
5. **Verification**: Validate restored data with requester and/or application checks.
6. **Closure and evidence**: Attach logs, timestamps, approvals, and outcome to the ITSM record.

### 11.2 Point-in-time restore procedure
Required for transactional systems (e.g., ERP databases) and ransomware rollback decisions.
1. Identify required point in time based on incident timeline and business input.
2. Confirm availability of full backup + incremental/log chain.
3. Restore to isolated staging environment when feasible for validation.
4. Apply logs to selected time; verify consistency.
5. Cutover restore to production following Change Enablement where required.
6. Capture achieved RPO/RTO metrics and attach evidence.

### 11.3 Ransomware recovery workflow (backup-led)
This workflow applies when ransomware or destructive malware is suspected/confirmed.
1. **Containment and triage**
   - Initiate incident response via ITSM and security operations workflows.
   - Isolate affected hosts/segments; preserve forensic artifacts as directed by the CISO function.
2. **Assess backup safety**
   - Confirm backup repositories are not impacted (immutability status, unusual deletions, admin log review).
   - Identify last known-good restore point (pre-encryption).
3. **Decide recovery strategy**
   - Service Owner and IT Operations Manager coordinate recovery approach and sequencing.
   - Prioritize Tier 0 services (identity), then Tier 1 business services, then Tier 2+.
4. **Clean rebuild**
   - Rebuild systems from trusted gold images or known-good templates.
   - Re-establish security tooling and monitoring before restoring data.
5. **Restore data**
   - Restore from immutable/offsite copy when possible.
   - Use isolated validation environment for high-risk systems before production cutover.
6. **Validation and monitoring**
   - Validate application functionality and data integrity.
   - Enhanced monitoring post-recovery for a defined stabilization window.
7. **Lessons learned**
   - Document timeline, achieved RPO/RTO, control gaps, and actions; route improvements through Change Enablement.

## 12. OT-specific considerations
- OT backups must respect segmentation and strict remote access controls.
- For MES and OT-adjacent systems:
  - Backup traffic must traverse approved paths; direct connectivity from corporate backup systems into restricted OT zones requires documented architecture approval.
  - Plant maintenance windows must be coordinated with Regional IT Operations and plant stakeholders.
- Where vendor support is required for OT system backups/restores, contracts must require:
  - Evidence of backup success
  - Restore test participation
  - Secure handling of credentials and access methods

## 13. Third-party and supplier requirements
- Supplier-managed services that store or process Norfolk Industries data must provide:
  - Backup and retention commitments aligned to this policy’s tier targets where applicable
  - Evidence of restore testing and security controls (encryption, immutability/deletion protection)
  - Timely breach/incident notification and support for recovery
- Supplier assurance evidence must be maintained for audit readiness.

## 14. Exceptions
- Exceptions must be risk-assessed, time-bound, and approved according to governance requirements.
- High-risk exceptions (e.g., inability to meet Tier 0–1 targets, no immutability, no offsite copy) require approval by the Head of IT Infrastructure Services and the CISO, with CIO accountability where applicable.
- Approved exceptions must include compensating controls and a remediation plan.

## 15. Compliance monitoring and reporting
- Global IT Operations and Regional IT Operations will track:
  - Backup success rates by tier and platform
  - Restore-point availability (RPO adherence)
  - Restore test completion and outcomes
  - Repository capacity and immutability health
- Monthly operational reporting must be produced for Tier 0–2 coverage and escalations.
- Evidence must be **time-bound, attributable, and repeatable**, including approvals, logs, and validation artifacts where applicable.

## 16. Audit and evidence requirements
Norfolk Industries will maintain evidence sufficient to demonstrate control design and operating effectiveness, including:
- Backup policy and standards (approved versions)
- Configuration exports/screenshots/logs showing schedules, retention, encryption, immutability
- Restore test reports with timestamps and results
- DR exercise outputs and remediation tracking
- ITSM records for restores, incidents, changes, and approvals
- Access logs for privileged backup administration activities

## 17. Roles and responsibilities
### 17.1 Role responsibilities (summary)
| Role | Responsibilities under this policy |
|---|---|
| Head of IT Infrastructure Services | Accountable for backup strategy, resourcing, and outcomes; ensures tiering is implemented and tested |
| CISO | Oversees ISMS alignment; ensures ransomware resilience and security requirements (immutability, access controls, monitoring) |
| IT Governance Manager | Coordinates policy lifecycle, compliance tracking, and audit evidence coordination |
| Service Owner | Defines service criticality, RPO/RTO tier, and application recovery requirements; approves production restores; ensures testing |
| Platform Owner | Designs and implements backup architecture and standards for platforms; ensures encryption/immutability/offsite requirements |
| IT Operations Manager | Ensures operational execution, monitoring, and incident coordination; ensures runbooks are used and maintained |
| ITSM Process Owner | Ensures ITIL-aligned Change Enablement, Incident Management, Problem Management, and evidence capture are effective |
| Internal Audit | Independently assesses control design and operating effectiveness |

## 18. Control mappings (standards alignment)
### 18.1 ISO/IEC 27001 (Annex A concept)
| Policy requirement area | ISO/IEC 27001 Annex A (conceptual alignment) | Expected evidence |
|---|---|---|
| Backup, retention, restore capability | Information security controls for backup and resilience | Backup policy configs, job logs, retention settings, restore test reports |
| Access control for backup administration | Identity and access management controls | Role assignments, PAM logs, admin activity logs |
| Encryption in transit/at rest | Cryptography controls | Key management configuration, encryption settings, platform attestations |
| Logging and monitoring | Monitoring and event management | SIEM alerts, backup monitoring dashboards, incident records |
| Supplier controls | Supplier relationship controls | Contracts, SOC reports, supplier evidence, due diligence records |
| Business continuity and recovery | Resilience and continuity controls | DR exercise reports, runbooks, RTO/RPO evidence |

### 18.2 NIST CSF mapping
| NIST CSF function | How this policy supports it |
|---|---|
| Identify | Criticality tiering, CI mapping, dependency documentation |
| Protect | Encryption, immutability, access segregation, retention controls |
| Detect | Monitoring of backup failures, repository anomalies, admin activity logging |
| Respond | Ransomware recovery workflow, incident coordination via ITSM |
| Recover | Restore runbooks, DR exercises, validated RPO/RTO targets |

### 18.3 ITIL 4 practices mapping
| ITIL 4 practice | Application in this policy |
|---|---|
| Change Enablement | CAB review/approval for material backup configuration changes |
| Incident Management | Restore requests and recovery incidents managed through ITSM |
| Problem Management | Repeated backup failures and test gaps tracked to root cause and remediation |
| Service Configuration Management | Backup components and protected workloads tracked as CIs |
| Monitoring and Event Management | Backup job monitoring, alerting, capacity/health management |
| Information Security Management | ISMS-aligned controls for encryption, access, and ransomware resilience |
| Supplier Management | Third-party backup assurance and evidence requirements |
| Service Continuity Management | DR exercises, tiering, and recoverability validation |

### 18.4 SOC 2 Trust Services Criteria mapping
| SOC 2 criterion | Policy alignment |
|---|---|
| Security | Access control, logging, encryption, immutability, segregation of duties |
| Availability | RPO/RTO targets, monitoring, restore testing, DR exercises |
| Confidentiality | Encryption and controlled restore access |
| Processing Integrity | Application-aware and point-in-time restore validation |
| Privacy | Retention controls, legal hold handling, controlled restore access for personal data |

### 18.5 COBIT 2019 mapping (domain-level)
| COBIT domain | Policy alignment |
|---|---|
| EDM | Governance of resilience and risk acceptance for exceptions |
| APO | Backup strategy, standards, supplier requirements |
| BAI | Controlled implementation via Change Enablement and platform engineering |
| DSS | Operational execution, monitoring, incident and recovery handling |
| MEA | Compliance monitoring, metrics, audit evidence, continuous improvement |

## 19. Document control
### 19.1 Review cycle
- Reviewed at least annually by IT Governance Manager in coordination with the Head of IT Infrastructure Services and the CISO.
- Reviewed after major incidents, ransomware events, significant platform changes, or audit findings.

### 19.2 Publication and communication
- Published in the controlled policy repository and communicated to IT Infrastructure Services, Global IT Operations, Regional IT Operations, and Service Owners.
- Runbooks and templates are maintained in the ITSM knowledge base under change control.

---

## Appendices

### Appendix A: Backup matrix (minimum standard)
This matrix defines minimum expectations by workload class. Service Owners may set stricter requirements.

| Workload | Tier (default) | Backup method | Schedule (minimum) | Retention (minimum) | Immutability | Offsite/cross-region | Restore validation |
|---|---:|---|---|---|---|---|---|
| ERP database | 1 | App-aware full + transaction logs | Daily full + ≤ 1 hour logs | 35 days + monthly 12 months | Yes (≥ 14 days) | Yes | Semi-annual point-in-time restore |
| ERP app servers | 1 | VM/image + config backup | Daily | 35 days | Yes (≥ 14 days) | Yes | Semi-annual restore |
| MES database/historian | 1/2 | App-aware database backups | Daily full + increments/logs as supported | 35 days + monthly 6–12 months | Yes (Tier-based) | Yes (Tier 1–2) | Annual (Tier 2) / Semi-annual (Tier 1) restore |
| Active Directory domain controllers | 0 | System state + VM/bare-metal recovery | Daily + additional per platform | 35 days + monthly 12 months | Yes (≥ 14 days) | Yes | Quarterly restore validation (authoritative scenario component) |
| Entra ID configuration | 0 | Config exports + audit log retention strategy | Daily export (or change-driven) | 12 months minimum; longer where required | Protected storage + deletion protection | Yes | Quarterly recovery validation of identity controls and break-glass |
| File services (enterprise shares) | 2 | File-level + volume backup | Daily | 35 days + monthly 6 months | Yes (≥ 7 days) | Yes | Annual restore test (sample) |
| File services (local shares) | 3 | File-level | Daily | 14 days | Recommended | Recommended | Annual sample restore |
| Azure IaaS VM | Per service | VM backup + config/IaC | Daily; more frequent if tier requires | Tier-based | Tier 0–2 required | Tier 0–2 required | Tier-based |
| Azure PaaS database | Per service | Native PITR + exports where needed | Continuous PITR where supported | Tier-based | Use platform protections + vault | Cross-region where required | Tier-based PITR test |
| AWS workloads | Per service | Native backups + centralized policy | Tier-based | Tier-based | Tier 0–2 required | Cross-account/region as required | Tier-based |

### Appendix B: Restore request template (ITSM)
| Field | Required | Guidance |
|---|---:|---|
| Requestor name and contact | Yes | Business and technical contact details |
| Service / application | Yes | Name of service and Service Owner |
| Affected CI(s) | Yes | CI identifiers for servers, databases, shares, cloud resources |
| Data type | Yes | Files, database, VM, configuration, identity-related |
| Environment | Yes | Production / non-production |
| Restore type | Yes | Standard restore / point-in-time restore / alternate location restore |
| Desired restore point | Yes | Date/time and time zone; include rationale |
| Impact description | Yes | Business impact, users affected, plant impact (if applicable) |
| Authorization | Yes | Service Owner approval for production; additional approvals for sensitive data |
| Validation method | Yes | How success will be confirmed (checksum, app login, report reconciliation) |
| Urgency | Yes | Map to incident priority if outage/security event |
| Security considerations | Conditional | Suspected malware/ransomware? If yes, trigger ransomware workflow and isolate restore |
| Attachments | Optional | Screenshots, file lists, database names, logs |

### Appendix C: Restore test report template
| Section | Content requirements |
|---|---|
| Test identifier | Unique ID, date, participants, roles |
| Scope | Services/CIs tested, tier, dependencies |
| Objectives | RPO/RTO target, success criteria |
| Pre-conditions | Backup job IDs, repository, immutability window status |
| Steps executed | Runbook version, commands/actions summary |
| Timings | Start/end per phase; achieved RTO |
| Restore point used | Timestamp; achieved RPO |
| Validation results | Integrity checks, application validation, user acceptance evidence |
| Issues and risks | Failures, near-misses, security findings |
| Remediation actions | Owner, due date, linkage to ITSM problem/change |
| Evidence attachments | Logs, screenshots, tickets, approvals |

### Appendix D: Evidence pack checklist (audit-ready)
Evidence must be time-bound, attributable, and repeatable.

| Evidence item | Frequency | Owner role | Source |
|---|---:|---|---|
| Approved policy version and review record | Annual | IT Governance Manager | Controlled policy repository |
| Backup configuration export (schedules/retention) | Quarterly | Platform Owner | Backup platform / cloud policy export |
| Immutability settings proof (vault/object lock) | Quarterly | Platform Owner | Platform configuration screens/logs |
| Encryption settings proof | Quarterly | Platform Owner | KMS/Key Vault settings and backup tool config |
| Backup job success reports (Tier 0–2) | Monthly | IT Operations Manager | Monitoring dashboards and job logs |
| Failed backup incident records and remediation | Monthly | IT Operations Manager | ITSM incidents/problems |
| Restore test reports by tier | Per Section 10 | Service Owner | Test report template + attachments |
| DR exercise reports (tabletop/technical) | Per Section 10 | ITSM Process Owner | Exercise notes, runbooks, outcomes |
| Access control review for backup admins | Semi-annually | CISO | IAM/PAM logs, role assignment exports |
| Change records for backup configuration | Ongoing | ITSM Process Owner | ITSM change tickets and CAB approvals |
| Supplier backup assurance evidence | Annual | IT Governance Manager | Contracts, SOC reports, attestations |

### Appendix E: RPO/RTO tier assignment checklist
| Check | Requirement |
|---|---|
| Business criticality documented | Service impact, dependencies, users/sites affected |
| Tier selected and justified | Tier 0–4 with rationale |
| Backup method supports tier | App-aware/logs for transactional; immutability for Tier 0–2 |
| Offsite/cross-region enabled | Required for Tier 0–2 |
| Restore procedures documented | Standard + point-in-time (if applicable) + ransomware workflow applicability |
| Test schedule planned | Meets Section 10 minimums |
| CMDB alignment complete | CIs linked to backup coverage and repositories |
| Monitoring and alerting configured | Failures generate actionable alerts and ITSM integration where applicable |