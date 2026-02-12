# IT Service Continuity Procedures (Norfolk Industries)

## 1. Purpose
These procedures define how Norfolk Industries plans, maintains, tests, and executes IT service continuity to ensure that critical services provided by IT Infrastructure Services can be sustained or restored within approved Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets. The procedures align to the Information Security Management System (ISMS), ISO/IEC 22301 concepts for Business Continuity Management System (BCMS), and ITIL 4 Service Continuity Management practices.

## 2. Scope
### 2.1 In scope
These procedures apply to:
- IT Infrastructure Services delivered across hybrid cloud (Microsoft Azure primary; AWS secondary), on-prem data centers, and supporting services (identity, endpoint management, network, monitoring, backup).
- Global IT Operations and Regional IT Operations teams operating 24×7.
- Continuity activities for services supporting business operations, including Operational Technology (OT) integration points (remote access controls, identity, network segmentation services) where IT provides enabling infrastructure.

### 2.2 Out of scope
- Plant-level OT continuity plans owned and executed by OT operational owners. However, dependencies between IT and Operational Technology (OT) must be captured and tested where relevant.
- Business process continuity plans owned by business functions, except where IT continuity inputs are required (RTO/RPO feasibility, service restoration sequencing).

## 3. Governance and Control Alignment
### 3.1 Governance model
Norfolk Industries operates with centralized governance and regional execution:
- Global IT Operations establishes continuity standards, minimum requirements, and cross-region coordination.
- Regional IT Operations executes local continuity plans, recovery activities, and testing within the global framework.

### 3.2 Control and framework alignment table
| Area | Alignment |
|---|---|
| BCMS concepts | ISO/IEC 22301 (critical services identification, continuity strategies, exercising and testing, continual improvement) |
| Information security | ISO/IEC 27001 (availability, resilience, backup, access control, incident handling within the ISMS) |
| Service management | ITIL 4 Service Continuity Management; Incident Management; Change Enablement; Monitoring and Event Management; Supplier Management; Service Configuration Management |
| Risk and governance | COBIT 2019 (EDM, APO, BAI, DSS, MEA) |
| Cybersecurity lifecycle | NIST CSF (Identify, Protect, Detect, Respond, Recover) |
| Assurance reporting | SOC 2 Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy) |
| Regulatory | GDPR (privacy and availability controls), SOX (controls supporting financial reporting system availability) |

### 3.3 Evidence principles
All continuity evidence must be time-bound, attributable, and repeatable, and should include approvals, logs, and validation artifacts where applicable.

## 4. Definitions (Canonical)
| Term | Definition |
|---|---|
| IT Infrastructure Services | The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations. |
| Global IT Operations | Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure. |
| Regional IT Operations | Regional teams executing day-to-day operations, local support, and implementation aligned to global governance. |
| Information Security Management System (ISMS) | The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001. |
| Change Advisory Board (CAB) | The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management. |
| Configuration Item (CI) | Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references. |
| Service Level Objective (SLO) | A target level of service reliability or performance, measured by agreed metrics. |
| Recovery Time Objective (RTO) | Target time to restore a service after disruption. |
| Recovery Point Objective (RPO) | Maximum tolerable amount of data loss measured in time. |
| Operational Technology (OT) | Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks. |

## 5. Roles and Responsibilities
### 5.1 Role responsibilities
| Role | Continuity responsibilities |
|---|---|
| CIO | Executive oversight for IT continuity outcomes aligned to enterprise priorities. |
| Head of IT Infrastructure Services | Accountable for continuity readiness of IT Infrastructure Services, resourcing, and service outcomes. |
| CISO | Ensures continuity controls align with the ISMS and security risk posture. |
| IT Governance Manager | Maintains continuity procedure governance, evidence tracking, audit coordination, and compliance reporting. |
| Service Owner | Owns service continuity plan content (RTO/RPO, dependencies, restoration sequence), approves test results and improvements. |
| Platform Owner | Ensures platform-level resilience patterns, runbooks, and recoverability for the domain. |
| IT Operations Manager | Coordinates 24×7 operational readiness, incident-to-recovery execution, and major communications. |
| ITSM Process Owner | Ensures continuity integrates with ITIL practices (Incident, Change Enablement, Problem, CMDB). |
| Internal Audit | Independently assesses control design and operating effectiveness. |
| Data Protection Officer (DPO) | Ensures continuity plans and exercises address privacy and GDPR obligations where personal data is impacted. |

### 5.2 RACI (excerpt aligned to master)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Policy approval | A/R | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| CAB chairing (when continuity requires changes) | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Critical Services Identification and Tiering (ISO 22301-aligned)
### 6.1 Service criticality method
Service Owners must identify critical services using:
- Business impact analysis inputs (from enterprise continuity governance).
- Technical impact analysis (upstream/downstream dependencies, shared services).
- Compliance impact (SOX-relevant services; services processing personal data under GDPR).
- Safety and operational impact where IT enables Operational Technology (OT) remote access, identity, or plant network segmentation services.

### 6.2 Continuity tiers
| Tier | Typical target RTO | Typical target RPO | Description |
|---|---:|---:|---|
| Tier 0 | ≤ 1 hour | ≤ 15 minutes | Essential enterprise/platform services required for broad service restoration (e.g., identity, core networking, monitoring). |
| Tier 1 | ≤ 4 hours | ≤ 1 hour | High-criticality services supporting revenue, manufacturing operations enablement, or regulatory commitments. |
| Tier 2 | ≤ 24 hours | ≤ 8 hours | Important services where short outages are tolerable with workarounds. |
| Tier 3 | ≤ 72 hours | ≤ 24 hours | Non-critical services with extended tolerance. |

### 6.3 Required artifacts per critical service
Service Owners must maintain, at minimum:
- RTO, RPO, and minimum service level during disruption.
- Service restoration priority and sequencing constraints.
- Dependency map (platform services, third parties, network paths, DNS, certificates, identity, CMDB CIs).
- Data classification and privacy considerations (in coordination with the Data Protection Officer (DPO) where applicable).

## 7. Continuity Strategy Requirements
### 7.1 Strategy principles
Continuity strategies must:
- Prioritize human safety and operational stability.
- Be measurable against RTO/RPO and Service Level Objective (SLO).
- Use defense-in-depth across design, backup, and recovery.
- Be implementable by Regional IT Operations with support from Global IT Operations.

### 7.2 Strategy patterns (hybrid environment)
| Area | Minimum strategy requirements |
|---|---|
| Microsoft Azure (primary) | Region-resilient architectures for Tier 0–1 where feasible; infrastructure-as-code for rebuild; documented recovery runbooks; backup and restore validation. |
| AWS (secondary) | Used for approved redundancy patterns or recovery where designed; documented failover/failback where applicable. |
| On-prem data centers | Redundant power/network where available; documented restoration runbooks; backup replication to approved targets; spare capacity planning for Tier 0–1. |
| Identity (AD + Entra ID (Azure AD)) | Documented recovery for Active Directory (including authoritative restore scenarios where applicable) and Entra ID dependency considerations; privileged access continuity using PAM tooling. |
| Endpoint management (Microsoft Intune + ConfigMgr) | Recovery runbooks for management plane; packaging and policy baselines stored in version control; device enrollment and compliance recovery steps. |
| Security tooling (SIEM/EDR/vulnerability scanning/PAM) | Maintain minimum monitoring and response capability during disruption; log retention and restoration methods; break-glass procedures governed and audited. |
| OT/IT integration points | Enforced segmentation; controlled remote access; continuity for jump hosts, identity, VPN, and required certificate/DNS services; coordinate OT stakeholders for testing. |
| Suppliers | Contractual recovery commitments, escalation paths, and evidence of supplier testing aligned to Tier targets. |

## 8. Continuity Plan Lifecycle Management
### 8.1 Plan ownership and structure
- Each critical service must have a service continuity plan owned by the Service Owner.
- Platform Owners must provide reusable platform runbooks and architecture standards that feed service plans.
- Plans must be stored in the ITSM tool knowledge base or controlled document repository with access control and version history.

### 8.2 Review cadence
| Plan element | Minimum review frequency | Trigger-based review |
|---|---:|---|
| Service continuity plan (per service) | Quarterly | After any Major Incident, material architecture change, supplier change, or failed exercise |
| Dependency mapping / CI accuracy | Quarterly | After new integrations, migrations, or network/identity changes |
| Contact lists and escalation paths | Monthly | After org changes, on-call rotations updates |
| Backup/restore validation results | Monthly for Tier 0–1; Quarterly for Tier 2–3 | After platform upgrades or backup policy changes |

### 8.3 Change control
All changes affecting continuity capabilities (architecture, backup policies, recovery scripts, IAM break-glass accounts, network segmentation) must follow Change Enablement and be reviewed by the Change Advisory Board (CAB) for Normal Changes or governed Emergency Changes during incidents.

## 9. Continuity Readiness Requirements
### 9.1 Minimum readiness controls
| Control area | Requirement | Evidence examples |
|---|---|---|
| Recovery runbooks | Step-by-step runbooks for restoration and validation exist and are current | Versioned runbook; approval record; execution log |
| Backups | Backups configured, monitored, and periodically restored | Backup reports; restore test logs; alert tickets |
| Access | Emergency privileged access available and controlled via PAM where applicable | PAM logs; break-glass access approvals; periodic access review |
| Monitoring | Key service health telemetry and alert routing resilient | Monitoring configuration export; alert tests; incident tickets |
| CMDB / CIs | Critical service dependencies represented as CIs | CMDB relationships; CI audit results |
| Communications | Templates and channels defined and tested | Communication drill record; stakeholder distribution lists |

### 9.2 Training and competency
- IT Operations Manager ensures 24×7 teams are trained on continuity execution for Tier 0–1 services.
- Service Owners and Platform Owners must conduct annual knowledge transfer sessions and document updates after exercises.

## 10. Continuity Event Classification and Invocation
### 10.1 Continuity event triggers
A continuity plan may be invoked when one or more conditions exist:
- Sustained outage exceeding 30 minutes for Tier 0–1 services with no near-term restoration path.
- Data center or cloud region impairment impacting production workloads.
- Cybersecurity incident requiring isolation or rebuild (in coordination with the CISO and Security Engineer).
- Supplier outage impacting contractual service availability.
- Loss of key dependency (identity, DNS, core network) that blocks business operations.

### 10.2 Invocation authority
- IT Operations Manager may recommend invocation based on operational impact.
- Service Owner approves invocation for their service unless urgency requires immediate action.
- Head of IT Infrastructure Services is the escalation authority for cross-service invocation and prioritization conflicts.
- The CISO must be consulted when invocation is related to a cybersecurity event or when forensic preservation affects restoration steps.

## 11. Recovery Procedures (Execute and Restore)
### 11.1 Standard recovery phases
1. **Stabilize and assess**
   - Confirm impact scope, affected regions, and dependencies.
   - Capture timestamps, symptoms, and initial actions in the ITSM incident record.
2. **Contain and protect**
   - For security-related events: coordinate with Security Engineer; preserve logs; apply containment to prevent spread.
3. **Recover service**
   - Execute the approved runbook for the selected recovery strategy (restore, rebuild, failover).
4. **Validate**
   - Confirm service health, data integrity, access controls, and monitoring.
   - Validate against SLO, RTO, and RPO targets.
5. **Communicate**
   - Provide updates per communications procedure (Section 14).
6. **Failback (if applicable)**
   - Return to steady-state architecture after stabilization, using CAB-governed change control.
7. **Post-recovery review**
   - Open Problem record if systemic issues are identified; update runbooks and controls.

### 11.2 Restoration sequencing rules
- Restore Tier 0 dependencies first (identity, core network, DNS, certificate services, monitoring, PAM).
- Restore Tier 1 services next per business priority and dependency map.
- Restoration order must be documented in the service continuity plan and validated in exercises.

### 11.3 Data restoration validation (RPO assurance)
When restoring data:
- Verify backup set integrity and point-in-time selection.
- Confirm application-level consistency checks where applicable.
- Document achieved RPO and any variance with rationale and approvals.

## 12. Backup, Replication, and Data Protection Procedures
### 12.1 Backup policy alignment to continuity
Service Owners must ensure:
- Backup frequency supports the approved RPO.
- Backup retention aligns to regulatory and operational requirements.
- Backup storage is protected via access controls and encryption consistent with the ISMS.

### 12.2 Restore testing
Minimum restore testing requirements:
| Tier | Minimum restore test frequency | Scope |
|---|---:|---|
| Tier 0 | Monthly | Full restore or equivalent recovery simulation with validation |
| Tier 1 | Quarterly | Restore validation for core datasets and configurations |
| Tier 2 | Semi-annually | Restore validation for representative components |
| Tier 3 | Annually | Restore validation or rebuild test |

## 13. Supplier and Third-Party Dependency Management
### 13.1 Supplier continuity requirements
- Identify all critical suppliers supporting each critical service (cloud providers, telecom, managed services, SaaS).
- Maintain documented escalation contacts, support levels, and contractual recovery commitments.
- Require supplier evidence where feasible (e.g., availability reports, continuity attestations, exercise outcomes).

### 13.2 Supplier outage procedure
1. Log incident in ITSM and mark as supplier-related.
2. Engage supplier escalation path and record timestamps and case numbers.
3. Activate workaround or alternate routing where designed (e.g., secondary provider, alternate region).
4. Communicate status to stakeholders (Section 14).
5. Post-incident: update supplier risk register inputs and continuity plans.

## 14. Communications and Stakeholder Notification
### 14.1 Communications objectives
- Provide timely, accurate, and role-appropriate updates.
- Maintain a single source of truth in the ITSM incident record.
- Protect confidentiality and privacy; avoid exposing sensitive security details broadly.

### 14.2 Communication channels and roles
| Audience | Owner | Channel | Minimum frequency during active recovery |
|---|---|---|---|
| Executive stakeholders | Head of IT Infrastructure Services | Executive brief via agreed channel | At invocation; then at least every 60 minutes for Tier 0–1 events |
| Technical responders | IT Operations Manager | War-room bridge/chat | Every 15–30 minutes or as operationally necessary |
| Business service owners | Service Owner | Targeted updates | At least every 60 minutes for Tier 1 impact |
| Security stakeholders | CISO / Security Engineer | Secure channel | As required, at least every 60 minutes for security-led events |
| Privacy stakeholders | Data Protection Officer (DPO) | Secure channel | Promptly if personal data availability or integrity risk exists |

### 14.3 Customer/regulatory communications
- External notifications (customers, regulators) are coordinated through Norfolk Industries corporate communications and legal/privacy governance, with inputs from the Head of IT Infrastructure Services and the Data Protection Officer (DPO) where applicable.
- For SOX-relevant systems, ensure finance controls stakeholders are informed per internal governance.

## 15. Exercising, Testing, and Validation (ISO 22301-aligned)
### 15.1 Exercise types
| Exercise type | Purpose | Typical scope |
|---|---|---|
| Tabletop exercise | Validate decision-making, communications, and runbook completeness | Tier 0–2 services; cross-team coordination |
| Technical recovery test | Validate restore/failover procedures and tooling | Tier 0–1 services; platform components |
| Full simulation | End-to-end recovery including dependencies and validation | Selected Tier 0–1 services annually |

### 15.2 Minimum exercise cadence
| Tier | Tabletop | Technical recovery test | Full simulation |
|---|---:|---:|---:|
| Tier 0 | Semi-annually | Quarterly | Annually |
| Tier 1 | Annually | Semi-annually | Every 18 months |
| Tier 2 | Annually | Annually | As risk-driven |
| Tier 3 | As risk-driven | As risk-driven | As risk-driven |

### 15.3 Exercise success criteria
Exercises must validate:
- Achieved or estimated RTO and RPO versus targets.
- Dependency accuracy and restoration sequencing.
- Communications execution and stakeholder alignment.
- Evidence capture quality (logs, approvals, timestamps).
- Required improvements with owners and due dates.

## 16. Post-Incident and Continual Improvement
### 16.1 After-action review
For any invoked continuity event or failed exercise:
- IT Operations Manager convenes an after-action review within 5 business days.
- Service Owner documents lessons learned, control gaps, and remediation actions.
- IT Governance Manager tracks remediation to closure and retains evidence.

### 16.2 Problem Management integration
Systemic causes identified must be routed into Problem Management with:
- Root cause analysis
- Permanent corrective actions
- Control improvements (runbook updates, monitoring improvements, architecture changes)

## 17. Records Management and Audit Evidence
### 17.1 Required records
- Service continuity plans and revision history
- Exercise plans, attendance, outcomes, and remediation tracking
- Incident records for continuity invocations and recovery activities
- Backup/restore test logs and reports
- CAB records for continuity-related changes
- Supplier communications and attestations where applicable

### 17.2 Evidence retention and access
- Evidence must be stored in controlled repositories aligned to the ISMS, with least-privilege access.
- Retention must support audit cycles for ISO/IEC 27001, ISO/IEC 22301-aligned BCMS expectations, SOC 2 reporting periods, GDPR accountability, and SOX requirements for in-scope systems.

## 18. Metrics, Monitoring, and Reporting
### 18.1 Required continuity metrics
| Metric | Description | Owner | Frequency |
|---|---|---|---|
| Continuity plan coverage | % of Tier 0–2 services with current continuity plans | IT Governance Manager | Monthly |
| Exercise completion | % of required exercises completed on time | IT Operations Manager | Quarterly |
| RTO/RPO attainment | Achieved RTO/RPO vs targets in tests and events | Service Owner | Quarterly |
| Backup restore success rate | Restore tests passed / attempted | Platform Owner | Monthly |
| Remediation closure rate | Open vs closed corrective actions | IT Governance Manager | Monthly |
| Supplier continuity performance | Supplier incident metrics vs commitments | Service Owner | Quarterly |

### 18.2 Reporting
- Global IT Operations provides a quarterly continuity readiness report to the Head of IT Infrastructure Services and the CISO.
- High-risk gaps are escalated with remediation plans and timelines.

## 19. Exceptions and Non-Compliance Handling
- Any inability to meet approved RTO/RPO, exercise cadence, or minimum readiness requirements must be documented as an exception request.
- High-risk exceptions require approval per governance (CIO, Head of IT Infrastructure Services, and CISO engagement as appropriate) and must include compensating controls and an approved remediation timeline.
- Exceptions impacting Change Enablement or recovery safety must be reviewed with the Change Advisory Board (CAB) when relevant.

## Appendices

## Appendix A: IT Service Continuity Plan Template (Norfolk Industries)
### A.1 Plan metadata
| Field | Value |
|---|---|
| Service name |  |
| Service Owner |  |
| Platform Owner(s) |  |
| Tier (0–3) |  |
| Approved RTO |  |
| Approved RPO |  |
| Primary hosting location |  |
| Secondary / recovery location |  |
| Last review date |  |
| Next review date |  |
| Related CIs (CMDB references) |  |

### A.2 Service description and boundaries
- Service purpose and primary user groups
- In-scope components (applications are included only as dependencies if owned outside IT Infrastructure Services)
- Out-of-scope components and assumptions

### A.3 Criticality justification
- Business impact summary (operations, revenue, safety, compliance)
- Operational Technology (OT) dependencies or enabling services (if any)

### A.4 Dependency map
| Dependency type | Dependency | Why required | Failure impact | Recovery notes |
|---|---|---|---|---|
| Identity | Active Directory / Entra ID |  |  |  |
| Network | WAN/LAN/Firewall/VPN |  |  |  |
| Platform | Compute/Storage |  |  |  |
| Data | Databases/File shares |  |  |  |
| Security | EDR/SIEM/PAM |  |  |  |
| Supplier | ISP/SaaS/Managed service |  |  |  |

### A.5 Continuity strategy selection
| Scenario | Strategy | Preconditions | RTO/RPO feasibility | Notes |
|---|---|---|---|---|
| Single component failure | Restore/repair |  |  |  |
| Site failure (on-prem) | Restore to alternate site / rebuild |  |  |  |
| Cloud region impairment | Failover to alternate region |  |  |  |
| Cybersecurity event | Rebuild from known-good / restore |  |  |  |
| Supplier outage | Workaround / alternate supplier route |  |  |  |

### A.6 Recovery runbook (step-by-step)
| Step | Action | Owner role | Tooling | Validation output |
|---:|---|---|---|---|
| 1 | Declare recovery war-room; confirm scope | IT Operations Manager | ITSM/bridge | Incident timeline started |
| 2 | Confirm dependencies status | Service Owner | CMDB/monitoring | Dependency checklist completed |
| 3 | Execute recovery method (restore/rebuild/failover) | Platform Owner | Platform tooling | Completion logs |
| 4 | Validate service function | Service Owner | Health checks | Validation evidence attached |
| 5 | Restore monitoring and alerts | Platform Owner | Monitoring | Alert test record |
| 6 | Communications update | IT Operations Manager | Status channels | Stakeholder update recorded |
| 7 | Failback plan (if applicable) | Service Owner | Change process | CAB record / change ticket |

### A.7 Access and credentials continuity
- Emergency access path (PAM workflow; break-glass controls)
- Required role assignments and least-privilege notes
- Logging requirements for privileged actions

### A.8 Data protection and privacy
- Data types processed (including personal data)
- GDPR considerations and notification triggers (coordinate with Data Protection Officer (DPO))
- Integrity validation steps post-restore

### A.9 Communications plan
| Stakeholder group | Contact method | When to notify | Owner |
|---|---|---|---|
| Executive stakeholders |  |  | Head of IT Infrastructure Services |
| Business owners |  |  | Service Owner |
| Security stakeholders |  |  | CISO / Security Engineer |
| Regional operations |  |  | IT Operations Manager |
| Supplier |  |  | Service Owner |

### A.10 Exercise and test record
| Date | Exercise type | Scope | Achieved RTO/RPO | Issues found | Actions and owners |
|---|---|---|---|---|---|

## Appendix B: Continuity Exercise Checklist
### B.1 Pre-exercise checklist
- Confirm exercise scope (service, tier, regions involved) and obtain Service Owner approval.
- Confirm no conflict with production freeze periods and obtain Change Advisory Board (CAB) awareness if technical testing can impact production.
- Ensure participants list includes Global IT Operations and Regional IT Operations as applicable.
- Validate contact lists and escalation paths (including supplier contacts).
- Define success criteria: target RTO/RPO, validation checks, evidence requirements.
- Prepare communication drill plan (internal stakeholder updates and cadence).
- Confirm safety and Operational Technology (OT) coordination where OT dependencies exist.

### B.2 Execution checklist
- Start time recorded; incident-style timeline initiated.
- Confirm dependency status and record assumptions.
- Execute runbook steps; record commands/activities at a level that is repeatable.
- Capture evidence: screenshots/logs/exports, change tickets, approvals, monitoring output.
- Validate service function and monitoring/alerting.
- Record achieved or estimated RTO/RPO and any variance.

### B.3 Post-exercise checklist
- Conduct debrief within 2 business days.
- Document findings, corrective actions, owners, and due dates.
- Update continuity plan and runbooks to reflect improvements.
- File evidence package in the controlled repository and link to the ITSM record.
- Report summary metrics for quarterly continuity reporting.

## Appendix C: Continuity Evidence List (Audit-Ready)
### C.1 Evidence register
| Evidence item | Minimum contents | Owner | Frequency | Storage location requirement |
|---|---|---|---|---|
| Service continuity plan | Approved plan, version history, RTO/RPO, dependencies, runbooks | Service Owner | Quarterly review | Controlled repository / ITSM knowledge base |
| Exercise package | Scope, attendees, timeline, results, achieved RTO/RPO, remediation actions | IT Operations Manager | Per cadence | Controlled repository linked to ITSM |
| Backup reports | Job status, retention, encryption status, failures and remediation | Platform Owner | Monthly | Backup system reports + exported snapshots |
| Restore test logs | Steps executed, timestamps, validation outputs, issues | Platform Owner | Per cadence | Controlled repository |
| CAB records | Change tickets, approvals, risk assessment, implementation evidence | ITSM Process Owner | Per change | ITSM change module |
| Incident records | Timeline, decisions, invocation approval, communications | IT Operations Manager | Per event | ITSM incident module |
| Supplier continuity evidence | SLA/SLO reports, outage communications, attestations | Service Owner | Quarterly | Supplier management repository |
| Remediation tracking | Action list, owners, due dates, closure evidence | IT Governance Manager | Monthly | Governance tracking repository |

### C.2 Evidence quality checks
- Time-bound: includes date/time and period covered.
- Attributable: identifies owner/approver and participating roles.
- Repeatable: includes steps and artifacts sufficient to reproduce testing or validate operation.