# Monitoring, Logging & Alerting Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for monitoring, logging, and alerting across Norfolk Industries to:
- Detect, respond to, and recover from security and availability events in support of 24×7 operations.
- Provide trustworthy operational and security telemetry for investigation, forensics, compliance, and continual improvement.
- Standardize monitoring and alerting practices across IT Infrastructure Services, Global IT Operations, and Regional IT Operations, including Operational Technology (OT) boundary visibility.

## 2. Scope
This policy applies to:
- All Norfolk Industries information systems, infrastructure, and services operated by or for IT Infrastructure Services, including on-prem data centers and hybrid cloud (Microsoft Azure primary, AWS secondary).
- Identity platforms (Active Directory and Entra ID (Azure AD); thereafter “Entra ID”).
- Endpoints managed by Microsoft Intune and ConfigMgr where needed.
- Security tooling, including SIEM (for example Microsoft Sentinel), EDR (for example Microsoft Defender for Endpoint), vulnerability scanning (for example Tenable/Nessus), and PAM (for example CyberArk).
- OT/IT integration points and OT boundary monitoring for segmented plant networks, remote access paths, and OT-facing services.

Out of scope:
- Purely standalone OT telemetry inside plant control systems that is not exposed at the OT/IT boundary. However, OT/IT boundary monitoring requirements in this policy still apply.

## 3. Policy Statement
Norfolk Industries shall implement monitoring, logging, and alerting controls that are:
- **Comprehensive**: cover identity, endpoints, servers, network, cloud resources, and OT/IT boundary components.
- **Centralized**: security-relevant logs must be centralized in the enterprise SIEM.
- **Trustworthy**: logs must be time-synchronized, integrity-protected, access-controlled, and retained per defined requirements.
- **Actionable**: alerts must be severity-ranked, routed to on-call roles, escalated based on service impact, and tuned to reduce noise.
- **Auditable**: controls must produce time-bound, attributable, and repeatable evidence as part of the Information Security Management System (ISMS) and ITIL 4 practices.

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

## 5. Roles and Responsibilities
Roles and responsibilities are defined in the Norfolk Industries roles catalog and applied using the RACI master.

### 5.1 RACI (policy-level)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval (logging/monitoring standards) | I | A | C | R | C | R | C | C | I |
| Procedure ownership (onboarding/tuning/response/reporting) | I | A | C | R | R | R | R | C | I |
| CAB chairing (for monitoring/alerting changes where applicable) | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

### 5.2 Role responsibilities (summary)
- **CIO**: Executive oversight for governance alignment and resourcing.
- **Head of IT Infrastructure Services**: Accountable for outcomes of monitoring, logging, and alerting services across the enterprise.
- **CISO**: Accountable for security logging requirements, detection coverage, and ISMS oversight.
- **IT Governance Manager**: Maintains policy lifecycle, compliance tracking, and audit coordination.
- **Service Owner**: Ensures monitoring, logging, and alerting for their service meet requirements and SLOs; ensures exceptions are managed.
- **Platform Owner**: Defines technical standards and reference configurations for their domain (network, cloud, endpoint, identity).
- **IT Operations Manager**: Ensures operational readiness, 24×7 coverage, incident coordination, and alert routing.
- **ITSM Process Owner**: Ensures ITIL-aligned integration for Incident Management, Monitoring and Event Management, Change Enablement, and Service Configuration Management.
- **Internal Audit**: Independently assesses control design and operating effectiveness.

## 6. Governance, Risk, and Compliance Requirements
Monitoring, logging, and alerting are governed under the ISMS and aligned to:
- ISO/IEC 27001 control intent (logging, monitoring, and event management concepts)
- NIST CSF functions: Identify, Protect, Detect, Respond, Recover
- ITIL 4 practices: Monitoring and Event Management, Incident Management, Problem Management, Change Enablement, Information Security Management, Service Configuration Management, Service Continuity Management
- COBIT 2019 domains: EDM, APO, BAI, DSS, MEA
- SOC 2 Trust Services Criteria: Security, Availability, Confidentiality, Processing Integrity, Privacy
- GDPR: minimization and lawful handling of personal data in logs
- SOX: controls supporting integrity and auditability of systems impacting financial reporting

Where conflicts exist, the stricter requirement applies.

## 7. Monitoring Requirements (Domains and Coverage)
Monitoring must provide actionable visibility into availability, performance, capacity, and security events. Coverage must include, at minimum:

### 7.1 Infrastructure monitoring (compute, storage, virtualization)
Required monitoring signals:
- Host health (CPU, memory, disk, IOPS, filesystem utilization)
- Service/process health for critical services (authentication, directory services, DNS, DHCP where applicable)
- Backup job status and backup repository capacity
- Patch compliance posture (where integrated with endpoint/server management)
- Certificate expiration and key service dependencies

### 7.2 Application and service monitoring (where owned/managed by IT Infrastructure Services)
Required monitoring signals:
- Service endpoints availability (synthetic checks where applicable)
- Error rates and latency (transaction/response time)
- Dependency checks (databases, message queues, identity providers)
- Authentication/authorization failures (security-relevant trends)

### 7.3 Network monitoring
Required monitoring signals:
- Device health and interface status
- Latency, packet loss, jitter for critical paths
- VPN/remote access health, capacity, and authentication failures
- Firewall rule change detection (where supported) and configuration drift indicators
- DNS anomalies and critical routing events

### 7.4 Cloud monitoring (Azure and AWS)
Required monitoring signals:
- Control plane events (resource creation, deletion, privilege changes)
- Resource health (VMs, managed services, storage, network)
- Identity events related to cloud access (Entra ID logs, role assignments)
- Cost and consumption anomaly signals where available
- Security posture signals (cloud security service findings where deployed)

### 7.5 Endpoint monitoring
Required monitoring signals:
- EDR health, sensor status, and policy compliance
- Malware detections, suspicious behavior, exploit signals
- Disk encryption compliance (where applicable)
- Local admin usage anomalies where measurable

### 7.6 Identity monitoring (Active Directory and Entra ID)
Required monitoring signals:
- Authentication failures and lockouts (volume and anomaly)
- Privilege changes (role assignments, group membership changes)
- Conditional access outcomes (where implemented)
- Directory replication/health events (for Active Directory)

### 7.7 OT boundary monitoring
At minimum, monitoring must cover OT/IT boundary assets and controls:
- Remote access gateways/jump hosts used for OT access
- Firewall/segmentation enforcement points between OT and IT networks
- Authentication and authorization events for OT remote access workflows
- File transfer mechanisms crossing the OT boundary (if used)
- Alerts on prohibited traffic patterns across OT segmentation boundaries

OT boundary monitoring must be designed to preserve OT safety and availability; invasive scanning or high-frequency polling must not impact OT operations.

## 8. Logging Standards (What to Log, Integrity, Time Sync, Centralization)
Security and operational logging must be implemented so events can be correlated across domains and support investigations.

### 8.1 Minimum log event categories (mandatory)
All in-scope systems must generate and retain logs (where technically feasible) for:

1. **Identity and access**
   - Successful and failed authentication events
   - Privileged authentication events and elevation activity
   - Account lifecycle events (create, disable, delete)
   - Group/role membership changes (including Entra ID role assignments)

2. **Administrative activity**
   - Configuration changes to security controls (firewalls, endpoint policies, IAM policies)
   - Administrative actions on critical systems (start/stop services, configuration changes)
   - Changes to logging/monitoring configuration (enable/disable, retention changes)

3. **System and application events**
   - Service start/stop, crashes, and error conditions
   - Application security events (authorization failures, input validation failures where logged)
   - API access events for management planes (cloud and security tooling)

4. **Network and remote access**
   - VPN connections, disconnections, failures, and MFA outcomes where applicable
   - Firewall allow/deny events for critical boundaries (especially OT/IT boundaries)
   - DNS query logs where enabled for security detection use cases

5. **Security tooling**
   - EDR detections and response actions
   - SIEM ingestion and parsing errors for critical sources
   - PAM session logs and privileged session recordings metadata (where supported)

6. **Data protection and continuity**
   - Backup success/failure, restore operations, and administrative actions
   - Key management events where applicable (key rotation, access to secrets)

### 8.2 Log quality requirements
Logs must be:
- **Time-synchronized**: All in-scope systems must synchronize time using approved enterprise time sources. Time drift must be monitored, and significant drift must generate an alert.
- **Consistent and attributable**: Logs must capture user/service identity, source IP/host, target system, action performed, and outcome (success/failure) where applicable.
- **Sufficient for correlation**: Use consistent host naming and identifiers aligned with CI records in the CMDB (CI relationships should support event correlation).

### 8.3 Log integrity and protection
- Logs must be protected from unauthorized access, modification, and deletion using role-based access control and platform-native protections.
- Administrative access to modify logging pipelines, retention, or SIEM connectors is restricted to authorized personnel and must be recorded.
- Where supported, enable immutable or write-once retention controls for security logs within the SIEM or log archive.
- Logs containing personal data must be handled per GDPR principles, including minimization and access control.

### 8.4 Centralized SIEM requirement
- Security-relevant logs for in-scope systems must be centrally forwarded to the enterprise SIEM.
- Log ingestion must support:
  - Normalization/parsing (where feasible)
  - Correlation across identity, endpoint, network, server, and cloud events
  - Alert generation based on defined detections
- SIEM ingestion failures for critical log sources must generate an operational alert.

## 9. Log Retention and Disposal
Retention must support security investigations, operational needs, and compliance, while minimizing unnecessary retention of personal data.

### 9.1 Standard retention requirements (minimums)
| Log category | Minimum online retention (searchable) | Minimum archive retention | Notes |
|---|---:|---:|---|
| SIEM-ingested security logs (identity, EDR, network security, cloud control plane) | 90 days | 1 year | Archive must preserve integrity and support retrieval. |
| Critical infrastructure logs (core network, identity services, virtualization platforms) | 90 days | 1 year | Include administrative actions and configuration changes. |
| OT boundary logs (remote access, segmentation controls) | 180 days | 1 year | Longer online retention supports incident investigations involving OT. |
| Backup and restore logs | 90 days | 1 year | Include restore operations and administrative actions. |
| Monitoring/alerting system audit logs (rule changes, routing changes) | 180 days | 1 year | Supports auditability of alert configuration changes. |

If a regulation, contractual obligation, legal hold, or risk decision requires longer retention, the Service Owner must document the requirement and ensure implementation.

### 9.2 Secure disposal
At retention end:
- Logs must be disposed of securely using platform-approved deletion or lifecycle policies.
- Disposal actions must be auditable (system logs or change records).

## 10. Alerting Standards (Severity, Routing, Escalation, Noise Reduction)
Alerts must be actionable and mapped to operational impact and security risk.

### 10.1 Alert severity levels
Norfolk Industries uses four standardized alert severities:

| Severity | Definition | Expected response | Examples |
|---|---|---|---|
| **Sev 1 – Critical** | Imminent or ongoing major business impact, widespread outage, or confirmed high-risk security event | Immediate (24×7) response; on-call engaged; incident declared | Ransomware indicators; identity compromise; OT boundary breach attempt; core network outage |
| **Sev 2 – High** | Significant degradation or credible security threat with limited scope | Rapid response; escalate if scope increases | Repeated privileged login failures; key service performance collapse; SIEM ingestion failure for critical source |
| **Sev 3 – Medium** | Notable issue requiring timely remediation; limited impact | Address during operational hours or on-call if trending worse | Single host resource saturation; non-critical connector errors |
| **Sev 4 – Low** | Informational, non-urgent, or planned condition | Track and trend; backlog/maintenance | Routine restarts; known benign scans blocked |

### 10.2 Routing and on-call
- Sev 1 and Sev 2 alerts must route to the 24×7 on-call function managed by the IT Operations Manager.
- Alert routing must include:
  - Primary responder group (Regional IT Operations or Global IT Operations as applicable)
  - Service Owner notification for impacted services
  - Security Engineer notification for security detections and any OT boundary alerts
- Contact methods and schedules must be maintained in the ITSM tool and reviewed monthly.

### 10.3 Escalation rules
- Escalation must follow documented on-call runbooks and ITSM escalation paths.
- The Service Owner must be engaged for any Sev 1 incident affecting their service SLO.
- Security escalations that indicate potential compromise must include the CISO’s organization per established incident handling procedures.

### 10.4 Alert noise reduction and quality controls
To keep alerts actionable:
- Each alert rule must have an owner (Service Owner for service-impacting alerts; Platform Owner for platform detections).
- Alerts must include suppression/deduplication logic where appropriate (for example, grouping by host/service within a time window).
- Threshold-based alerts must be tuned using baselines and reviewed after major platform changes.
- False positives must be tracked and reduced through rule tuning and documented changes (subject to Change Enablement and CAB when required).

## 11. Tooling and Architecture Standards
### 11.1 Monitoring and event management platform
- Monitoring must support:
  - Health checks, metrics, logs, and traces where applicable
  - Integration to the ITSM tool for incident creation and routing
  - Role-based access control and audit logging for rule changes

### 11.2 SIEM integration
- The SIEM is the authoritative system for centralized security event correlation and security alerting.
- All critical log sources must have monitored ingestion health and documented parsing/normalization.

### 11.3 Separation of duties
- Individuals who can disable or modify security alerting rules must be restricted and changes must be auditable.
- Where feasible, separate administrative roles between detection engineering and platform administration.

## 12. Procedures (Mandatory Operational Procedures)
These procedures are mandatory and must be executed by the identified roles using ITIL-aligned workflows in the ITSM tool.

### 12.1 Procedure: Onboard a log source to the SIEM
**Owner**: Platform Owner (domain-specific) with support from Security Engineer  
**Approver**: Service Owner (impacted service) and IT Governance Manager for compliance alignment as needed

Steps:
1. **Initiate request**
   - Create an ITSM request/change record (as appropriate) referencing the CI(s) and service.
   - Identify data classification and presence of personal data in the logs (GDPR consideration).
2. **Define onboarding specification**
   - Identify event categories required (per Section 8.1).
   - Identify transport method (agent, API connector, syslog) and encryption requirements.
   - Define retention and access controls per Section 9.
3. **Implement collection**
   - Configure source logging (enable audit categories, admin activity logs).
   - Configure forwarding/connector to SIEM.
4. **Validate ingestion and parsing**
   - Confirm events are arriving with correct timestamps and host identifiers.
   - Validate parsing/normalization (fields for user, action, outcome, source, target).
   - Confirm ingestion health monitoring is enabled.
5. **Access control and integrity checks**
   - Restrict access to log source configuration and SIEM workspace appropriately.
   - Confirm audit logs are enabled for connector/rule changes.
6. **Operationalize**
   - Add the source to the log source inventory (Appendix A) and link to CI.
   - Update alert catalog coverage or create detections as needed (Appendix B).
7. **Evidence capture**
   - Store configuration screenshots/exports, test event samples, and approval records in the ITSM record.

### 12.2 Procedure: Tune alerts
**Owner**: Platform Owner (technical tuning) and Service Owner (business impact)  
**Approver**: Change Advisory Board (CAB) when the change is a Normal Change; Emergency Changes follow emergency change governance

Steps:
1. **Identify noise or gaps**
   - Review alert volume, false positive rate, and missed detections.
   - Correlate with incidents and known events (maintenance windows).
2. **Define tuning change**
   - Adjust thresholds, add suppression, refine filters, improve parsing, or add enrichment.
   - Ensure tuning does not reduce required detection coverage for high-risk scenarios.
3. **Risk review**
   - Security Engineer validates security impact for security detections.
   - Confirm continued alignment to logging requirements and auditability.
4. **Implement via controlled change**
   - Submit change through Change Enablement and, if required, CAB approval.
   - Implement in lower-risk windows where possible.
5. **Validate**
   - Confirm alert triggers as intended with test events.
   - Monitor post-change for at least one business cycle (including peak/shift coverage).
6. **Document**
   - Update alert catalog entries with rationale and expected behavior.
   - Link change record to updated alert rule.

### 12.3 Procedure: Respond to a Sev 1 (Critical) alert
**Owner**: IT Operations Manager (coordination), Security Engineer (security events), Regional IT Operations (local execution)  
**Approver**: Service Owner for service-impact decisions; escalation per incident governance

Steps:
1. **Acknowledge and triage (immediate)**
   - On-call acknowledges the alert in the alerting system.
   - Validate whether the alert is true positive using correlated evidence in the SIEM and monitoring platform.
2. **Declare incident**
   - If impact is confirmed or likely, open an Incident record in the ITSM tool and mark as Sev 1.
   - Establish incident communications and stakeholder notifications per incident process.
3. **Contain and stabilize**
   - For security: isolate affected endpoints/identities where feasible; enforce conditional access or credential resets as needed.
   - For availability: failover, restart, scale, or isolate faulty components following service runbooks.
   - For OT boundary alerts: prioritize safety and segmentation; restrict remote access paths per approved controls.
4. **Engage required roles**
   - Notify Service Owner and Platform Owner for impacted services.
   - Engage Security Engineer for security validation and containment actions.
5. **Preserve evidence**
   - Ensure relevant logs are retained and exported if needed; do not disable logging.
   - Record timeline and actions in the incident record.
6. **Eradicate and recover**
   - Execute remediation and recovery steps aligned to service continuity requirements.
7. **Post-incident actions**
   - Create Problem record for root cause analysis if warranted.
   - Tune alerts and improve monitoring coverage based on lessons learned.

### 12.4 Procedure: Monthly monitoring and logging reporting
**Owner**: IT Operations Manager (operational metrics), Security Engineer (security metrics), IT Governance Manager (compliance metrics)  
**Audience**: Head of IT Infrastructure Services, CISO, Service Owners

Monthly report must include:
- Monitoring coverage: % of critical services with defined monitors and SLO-aligned alerting
- Log source coverage: critical sources onboarded to SIEM and ingestion health status
- Alert performance: alert volume by severity, top noisy alerts, false positive rate trends
- Incident linkage: Sev 1/Sev 2 incidents triggered by alerts and mean time to acknowledge/resolve
- Compliance evidence status: retention confirmations and access review status for SIEM/monitoring admin roles
- OT boundary summary: counts of notable blocked attempts and remote access anomalies (without exposing sensitive operational details beyond need-to-know)

Reports must be stored in a controlled repository with access limited to authorized roles.

## 13. Change Management and CAB Requirements
- Changes to monitoring/alerting rules, SIEM connectors, retention settings, and log pipeline configurations are controlled changes under Change Enablement.
- The Change Advisory Board (CAB) must review and approve Normal Changes that materially affect:
  - Detection coverage for high-risk scenarios
  - Retention periods
  - Alert routing/escalation paths
  - OT boundary monitoring configurations
- Emergency Changes are permitted to restore security or availability but must be documented and reviewed retrospectively per Change Enablement.

## 14. Exceptions
- Exceptions must be risk-assessed, documented, time-bound, and approved according to governance.
- High-risk exceptions (for example, inability to forward security logs for a critical system) require approval per the exception approval RACI and must include compensating controls (such as increased local retention, restricted admin access, or alternative telemetry sources).
- Exceptions must be recorded in the ITSM tool and reviewed at least quarterly by the Service Owner and IT Governance Manager.

## 15. Compliance Measurement and Audit Evidence
Compliance is measured by:
- Percentage of in-scope critical systems forwarding required log categories to the SIEM
- Retention compliance against Section 9
- Time synchronization compliance and drift alerting
- Alert routing and on-call response compliance for Sev 1 and Sev 2
- Change record linkage for alert rule and connector modifications

Evidence must follow the standards.json evidence principles:
- **Time-bound, attributable, repeatable**
- Include approvals, logs, and validation artifacts

Internal Audit may request evidence samples for specific periods and systems, including proof of ingestion, retention, access controls, and alert response actions.

## 16. Data Protection and Privacy
- Logs may include personal data (usernames, IP addresses, device identifiers). Collection must be limited to what is necessary for security and operational purposes.
- Access to logs must follow least privilege and be restricted to authorized roles.
- Exporting logs outside approved systems requires documented justification and secure handling.
- Where logs are used for investigations involving personal data, handling must align with GDPR requirements and internal privacy governance overseen by the Data Protection Officer (DPO).

## 17. Third-Party and Supplier Requirements
- Suppliers providing managed services or platforms that generate or handle Norfolk Industries logs must:
  - Support required logging and retention
  - Provide access to logs and audit records necessary for investigations and SOC 2/ISO evidence
  - Support time synchronization and integrity controls
- Supplier access paths (including remote access) must be logged and monitored, and logs must be forwarded to the SIEM where feasible.

## 18. Policy Review and Maintenance
- Review cadence: at least annually, and additionally after material incidents, major platform changes, or audit findings.
- **Owner**: IT Governance Manager  
- **Accountable**: Head of IT Infrastructure Services  
- **Consulted**: CISO, ITSM Process Owner, Service Owners, Platform Owners, IT Operations Manager  
- Updates that affect operational procedures must include training/communications and controlled rollout across regions.

## 19. Control Mappings (ISO/IEC 27001, NIST CSF, ITIL 4, COBIT 2019, SOC 2)
This section provides conceptual mappings to recognized frameworks to support the ISMS and audits.

### 19.1 Control mapping table
| Policy requirement area | ISO/IEC 27001 (conceptual) | NIST CSF | ITIL 4 practices | COBIT 2019 domains | SOC 2 TSC |
|---|---|---|---|---|---|
| Centralized security logging and correlation | Logging and monitoring control intent | Detect | Monitoring and Event Management; Information Security Management | DSS; MEA | Security; Availability |
| Time synchronization and log quality | Event logging and system integrity control intent | Protect; Detect | Monitoring and Event Management | DSS | Security |
| Log integrity, access control, and retention | Access control; logging; records retention control intent | Protect | Information Security Management; Service Configuration Management | APO; DSS; MEA | Security; Confidentiality; Privacy |
| Alert severity, routing, on-call, escalation | Incident and event response control intent | Respond | Incident Management; Monitoring and Event Management | DSS | Security; Availability |
| OT boundary monitoring | Network security monitoring control intent | Detect; Respond | Monitoring and Event Management; Information Security Management | DSS | Security; Availability |
| Controlled changes to monitoring/alerting | Change control intent | Protect | Change Enablement | BAI | Security; Availability |
| Reporting and continual improvement | Monitoring, measurement, and improvement control intent | Identify; Recover | Problem Management; Continual improvement (via ITIL governance) | MEA | Security; Availability |

### 19.2 Evidence examples (aligned to evidence principles)
- SIEM connector configuration exports with timestamps and approver identity
- Sample log events demonstrating required fields and time synchronization
- Retention policy configuration screenshots/exports and lifecycle rules
- Monthly monitoring/logging report and distribution list
- Incident records linked to alerts (Sev 1/Sev 2), including response timelines
- Change records for alert tuning and routing changes with CAB approvals where required
- Access review evidence for SIEM and monitoring administrators

---

## Appendix A: Log Source Onboarding Template (SIEM)
Use this template to standardize onboarding and ensure audit-ready evidence.

### A.1 Log source onboarding record
| Field | Entry |
|---|---|
| Log Source Name | |
| Related Service | |
| Related CI(s) (Configuration Item) | |
| Environment | On-prem / Azure / AWS |
| Region | North America / Europe / APAC |
| Log Source Type | Identity / Endpoint / Server / Network / Cloud / OT Boundary / Application |
| Data Classification | Public / Internal / Confidential / Restricted |
| Contains Personal Data | Yes / No |
| Owner (Platform Owner) | |
| Service Owner | |
| Implementation Engineer | Network Engineer / Systems Engineer / Cloud Engineer / Endpoint Engineer / IAM Engineer / Security Engineer |
| Collection Method | Agent / API Connector / Syslog / Native Integration |
| Transport Security | TLS / Private Link / VPN / Other controlled transport |
| Time Sync Verified | Yes (method documented) |
| Required Categories Enabled (per Section 8.1) | Identity & Access / Admin Activity / System & App / Network & Remote Access / Security Tooling / Backup & Restore |
| SIEM Workspace / Tenant | |
| Parsing/Normalization Status | Complete / Partial (document gaps) |
| Ingestion Health Monitor Enabled | Yes / No |
| Alert Coverage Updated | Yes / No (reference Alert Catalog IDs) |
| Retention Applied | Online: ___ days; Archive: ___ months |
| Access Controls Applied | Roles/groups; approval reference |
| Validation Evidence | Test events, screenshots, query results |
| Change/Request Record Reference | |
| Approval Record Reference | |

### A.2 Onboarding validation checklist
- Time synchronization verified and drift monitored
- User/action/outcome fields present for security-relevant events
- Host identifiers match CMDB naming/CI references
- Ingestion error alerting enabled for the connector
- Retention and archive configured and tested (retrieval verification)
- Access controls and audit logging enabled for connector configuration

## Appendix B: Alert Catalog Template
Use this template to maintain a controlled, reviewable catalog of operational and security alerts.

### B.1 Alert catalog entry
| Field | Entry |
|---|---|
| Alert ID | |
| Alert Name | |
| Severity (Sev 1–4) | |
| Category | Availability / Performance / Capacity / Security / OT Boundary |
| Description | |
| Data Sources | SIEM / Monitoring platform; specific log sources |
| Detection Logic Summary | Correlation/threshold description |
| Trigger Conditions | Metric thresholds, time windows, event patterns |
| Suppression/Deduplication | Grouping key and suppression window |
| Expected Impact | Business/service impact statement |
| Primary Responder Group | Global IT Operations / Regional IT Operations |
| Secondary/Escalation | Service Owner; Security Engineer; IT Operations Manager |
| On-call Routing Enabled | Yes / No |
| Runbook Link | Incident response steps and validation queries |
| Known False Positives | Patterns and exclusions |
| Maintenance Window Handling | Schedule or tag-based suppression method |
| Change Control Required for Updates | Yes (Normal Change/CAB) / No |
| Last Reviewed Date | |
| Owner | Platform Owner / Service Owner |

### B.2 Alert review checklist (monthly)
- Top 10 alerts by volume reviewed for noise reduction
- Sev 1/Sev 2 alerts validated for correct routing and on-call notification
- Detection logic verified against recent incidents and changes
- Suppression rules validated to avoid masking real incidents
- Alert-to-incident linkage sampled in ITSM for traceability

## Appendix C: Audit Evidence List (Monitoring, Logging & Alerting)
This appendix defines the standard evidence set to demonstrate compliance and operating effectiveness.

### C.1 Evidence register
| Evidence item | Owner | Frequency | System of record | Minimum content |
|---|---|---|---|---|
| SIEM log source inventory (export) | Security Engineer | Monthly | SIEM + controlled repository | Sources, status, last ingest time, region |
| Log source onboarding records | Platform Owner | Per onboarding/change | ITSM tool | Template fields, approvals, validation artifacts |
| Retention configuration evidence | Platform Owner | Quarterly | SIEM/log archive platform | Retention policies, archive lifecycle rules |
| SIEM access review | IT Operations Manager | Quarterly | IAM system + ITSM tool | Reviewer, date, group memberships, remediation |
| Monitoring/alert rule change records | ITSM Process Owner | Per change | ITSM tool | Change approvals, CAB minutes where applicable |
| Alert catalog (current) | IT Operations Manager | Monthly | Controlled repository | Catalog entries with last review date |
| Incident records linked to alerts | IT Operations Manager | Monthly sampling | ITSM tool | Timeline, actions taken, resolution, post-incident notes |
| Time sync compliance evidence | Platform Owner | Monthly | Monitoring platform | Drift reports, alerts, remediation |
| OT boundary monitoring coverage report | Security Engineer | Monthly | SIEM/monitoring platform | Logged gateways/firewalls, notable events summary |

### C.2 Evidence quality checklist
- Evidence is time-bound (includes dates/time ranges)
- Evidence is attributable (shows who approved/executed)
- Evidence is repeatable (documented steps/queries)
- Evidence includes approvals, logs, and validation artifacts where applicable