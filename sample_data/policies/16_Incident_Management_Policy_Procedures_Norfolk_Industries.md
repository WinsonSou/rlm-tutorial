# Incident Management Policy & Procedures (Norfolk Industries)

## 1. Purpose
This document defines the policy and procedures for Incident Management at Norfolk Industries to restore normal service operation as quickly as possible, minimize adverse impact to business operations (including 24×7 manufacturing), and ensure effective coordination across IT Infrastructure Services, Global IT Operations, Regional IT Operations, and the Information Security Management System (ISMS).

This document is ITIL 4-aligned (Incident Management, Monitoring and Event Management, Service Continuity Management, Information Security Management) and supports governance obligations under ISO/IEC 27001, ISO/IEC 22301, COBIT 2019, NIST CSF, SOC 2 Trust Services Criteria, GDPR, and SOX.

## 2. Scope
### 2.1 In scope
- All incidents impacting services operated or supported by IT Infrastructure Services across:
  - Microsoft Azure (primary), AWS (secondary), on-prem data centers
  - Identity services: Active Directory and Entra ID (Azure AD) on first mention, then Entra ID
  - Endpoints managed by Microsoft Intune and ConfigMgr where needed
  - Networks, monitoring, backup, vulnerability scanning, PAM, SIEM, EDR
- Incidents affecting Operational Technology (OT) connectivity where IT is a dependency (e.g., plant network uplinks, remote access paths, identity integration, shared services).
- Incidents raised via the ITIL-aligned ITSM tool, monitoring systems, or approved communication channels.

### 2.2 Out of scope
- Non-service-impacting requests and standard changes (handled by Request Fulfillment and Change Enablement).
- Product quality events unrelated to IT/OT service delivery (handled by manufacturing quality processes), except where an IT/OT service incident is a contributing factor.
- Security investigations that have no service impact and are handled purely as security events; these may still require an incident record when they affect availability, confidentiality, or integrity of services.

## 3. Governance, Principles, and Objectives
### 3.1 Governance principles
- **Single system of record:** Every incident is recorded and managed in the ITSM tool as an incident ticket; related records (problem, change, security case) are linked.
- **Safety and production first:** Any incident affecting plant safety or manufacturing continuity is treated with elevated priority and coordinated with OT stakeholders.
- **Time-bound and attributable evidence:** Evidence is retained per the evidence principles: time-bound, attributable, repeatable; includes approvals, logs, and validation artifacts where applicable.
- **Separation of duties:** Incident resolution actions that require privileged access follow PAM controls; emergency actions follow Change Advisory Board (CAB) emergency change governance.
- **Regional execution, centralized governance:** Global IT Operations sets standards and cross-region coordination; Regional IT Operations executes response per local operational needs and regulatory requirements.

### 3.2 Objectives
- Restore service within agreed Service Level Objective (SLO) targets.
- Reduce recurrence through root cause analysis and Problem Management linkage.
- Maintain clear communications and stakeholder confidence during outages.
- Ensure regulatory and audit readiness (ISO/IEC 27001, SOC 2, SOX, GDPR) through complete, accurate incident records and evidence.

## 4. Roles and Responsibilities
All roles below are authoritative and consistent with Norfolk Industries’ role definitions.

### 4.1 Core roles
| Role | Responsibilities in Incident Management |
|---|---|
| CIO | Executive oversight for major business-impact incidents; escalation endpoint for enterprise impact. |
| Head of IT Infrastructure Services | Accountable for infrastructure service restoration outcomes and resourcing; ensures adherence to policy and CAB alignment. |
| CISO | Accountable for security program oversight and ISMS alignment; engaged for security incidents and risk decisions. |
| IT Governance Manager | Owns policy lifecycle, compliance tracking, and audit coordination; ensures evidence completeness and control mapping. |
| Service Owner | Accountable for end-to-end service performance; approves customer-facing comms for their service when required; ensures PIR actions are executed. |
| Platform Owner | Technical authority for platform decisions; leads technical diagnosis and remediation patterns. |
| IT Operations Manager | Runs operational response, on-call readiness, incident coordination, and war room facilitation. |
| ITSM Process Owner | Owns Incident Management process design and continual improvement; maintains severity model and templates. |
| Service Desk Manager | Ensures correct intake, categorization, prioritization, and timely escalations; manages user communications as defined. |
| Internal Audit | Independently assesses control design and operating effectiveness; may request evidence artifacts. |
| Data Protection Officer (DPO) | Oversees privacy governance and GDPR alignment; engaged when personal data exposure is suspected/confirmed. |

### 4.2 Engineering roles (execution)
- Network Engineer, Systems Engineer, Cloud Engineer, Endpoint Engineer, IAM Engineer, Security Engineer execute diagnosis, containment, remediation, and validation actions under coordination of the IT Operations Manager and aligned with the Platform Owner and Service Owner.

### 4.3 RACI alignment (selected)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| CAB chairing (for Emergency Change linkage) | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 5. Definitions
Terms are consistent with the Norfolk Industries glossary.

### 5.1 Incident
An **incident** is an unplanned interruption to an IT service or reduction in the quality of an IT service, or a failure of a Configuration Item (CI) that has not yet impacted service but is likely to do so. Incidents include user-reported issues, monitoring alerts, and failures across cloud, on-prem, identity, endpoints, and network services.

### 5.2 Security incident
A **security incident** is an incident with actual or suspected impact to the confidentiality, integrity, or availability of information or services due to malicious activity, policy violation, or exploitation of vulnerability (e.g., malware, ransomware, identity compromise, data exfiltration, unauthorized access).  
Security incidents are handled under Incident Management with mandatory engagement of the CISO-designated security response capability (typically via Security Engineer) and ISMS requirements, and may also require privacy assessment with the Data Protection Officer (DPO).

### 5.3 Major incident
A **major incident** is an incident with high business impact requiring immediate cross-functional coordination, accelerated decision-making, and frequent stakeholder communications. Major incident determination is driven by impact and urgency (severity) and typically triggers a **war room** and executive escalation.

### 5.4 Configuration Item (CI)
A **Configuration Item (CI)** is any component managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.

### 5.5 Operational Technology (OT)
**Operational Technology (OT)** includes systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.

## 6. Policy Statements
1. **Mandatory logging:** All incidents must be logged in the ITSM tool with required fields completed and accurate timestamps.
2. **Severity-driven response:** Response actions, escalation, communications cadence, and staffing follow the severity model in Section 9.
3. **Major incident governance:** Major incidents require a war room, a named Incident Commander, situation reports, and documented decisions.
4. **Security incident governance:** Security incidents require Security Engineer engagement and ISMS-aligned evidence handling; privacy evaluation is required when personal data may be involved.
5. **Change control:** Remediation that alters production configuration must follow Change Enablement. Emergency actions require emergency change controls and CAB oversight as applicable.
6. **Evidence retention:** Logs, artifacts, and decisions must be retained and linked to the incident record per Section 14.
7. **Post-Incident Review (PIR):** PIR is mandatory for all Major Incidents and for any incident with significant risk, repeated occurrence, or security impact.

## 7. Compliance and Control Alignment
### 7.1 Standards mapping (conceptual)
| Framework | Alignment summary for this document |
|---|---|
| ISO/IEC 27001 (ISMS) | Incident handling, event logging, access control for response activities, evidence retention, continual improvement. |
| ISO/IEC 22301 (BCMS) | Service continuity coordination, recovery validation, lessons learned for resilience. |
| ITIL 4 | Incident Management, Monitoring and Event Management, Change Enablement linkage, Service Configuration Management (CI linkage), Service Continuity Management. |
| COBIT 2019 | DSS (service operations), MEA (monitoring/evaluation), APO (governance and risk), BAI (change and transition) concepts. |
| NIST CSF | Detect, Respond, Recover functions in procedures and playbooks. |
| NIST SP 800-53 (concepts) | Incident response, audit logging, access control, contingency planning evidence expectations. |
| SOC 2 (TSC) | Security and Availability primarily; Confidentiality/Privacy as applicable; evidence requirements for operating effectiveness. |
| GDPR | Breach assessment support, data minimization in comms, DPO engagement, audit trail. |
| SOX | Controls around system availability impacting financial reporting systems; evidence, approvals, and change linkage. |

### 7.2 Evidence principles application
Incident artifacts must be:
- **Time-bound:** include date/time and timezone, and duration where relevant.
- **Attributable:** include who performed actions and approvals.
- **Repeatable:** include steps, commands, configuration references, and verification results.

## 8. Incident Lifecycle Overview
Norfolk Industries uses the following lifecycle stages, aligned to ITIL 4 and NIST CSF (Detect → Respond → Recover):

1. **Detect** (Monitoring/event, user report, third-party notice)
2. **Log & Categorize** (Incident ticket creation, CI/service linkage)
3. **Triage** (Initial assessment, severity assignment, routing)
4. **Contain** (Stop bleeding; limit spread/impact, especially for security)
5. **Eradicate** (Remove root cause where feasible in incident window)
6. **Recover** (Restore service, validate, monitor)
7. **Communicate** (Continuous across all stages)
8. **Close** (Confirmation, documentation completeness)
9. **Post-Incident Review (PIR)** (Required triggers; track actions)

## 9. Severity Model (Impact × Urgency)
Severity is assigned during triage and updated as new facts emerge. The IT Operations Manager (or delegate Incident Commander during a major incident) owns severity decisions.

### 9.1 Severity levels
| Severity | Definition (typical) | Response targets (operational) | War room | Stakeholder updates |
|---|---|---|---|---|
| Sev 1 (Critical) | Enterprise-wide outage, major plant impact, safety/production risk, or active widespread security incident (e.g., ransomware). | Immediate engagement; paging/on-call within 15 minutes; continuous until stabilized. | Mandatory | Every 30 minutes (or more frequent if requested) |
| Sev 2 (High) | Significant regional/site impact, major degradation, partial plant disruption, high-risk security incident contained to limited scope. | Engage within 30 minutes; sustained until service restored. | Required when cross-team work needed | Every 60 minutes |
| Sev 3 (Medium) | Limited user group impact, workaround exists, moderate degradation. | Engage within 4 hours (or per SLO); resolve in standard operational window. | Optional | Every 4 hours or per agreement |
| Sev 4 (Low) | Minor issue, minimal impact, informational, or single-user issue with straightforward resolution. | Handle in standard queue; resolve per SLO. | No | As needed |

### 9.2 Impact considerations
- **Business impact:** manufacturing downtime, OT connectivity, revenue impact, customer commitment impact.
- **Scope:** number of users, sites, regions, services.
- **Critical services:** identity, network core, ERP, email/collaboration, remote access, plant connectivity dependencies.
- **Security impact:** active compromise, data exposure risk, lateral movement potential.

### 9.3 Urgency considerations
- Time sensitivity (e.g., production shift change), external commitments, regulatory timelines, exploit activity, and availability of workaround.

## 10. War Room (Major Incident) Operating Model
### 10.1 Trigger conditions
A war room is initiated when:
- Severity is **Sev 1**, or
- Severity is **Sev 2** with cross-domain coordination needs (network + identity + cloud + security), or
- OT connectivity loss affects plant operations across a site or region, or
- Any security incident requiring coordinated containment and communications.

### 10.2 War room roles
| War room role | Assigned to | Responsibilities |
|---|---|---|
| Incident Commander | IT Operations Manager (default) or delegated senior responder | Owns cadence, decisions, tasking, and situation reporting; ensures ticket accuracy. |
| Technical Lead(s) | Platform Owner(s) or senior engineer per domain | Drives diagnosis and remediation plan; reports status and risks. |
| Communications Lead | Service Desk Manager or Service Owner delegate | Drafts and distributes internal updates; coordinates stakeholder messaging. |
| Scribe | Service Desk analyst or delegated engineer | Records timeline, decisions, actions, and evidence links in the incident ticket. |
| Security Lead (if security incident) | Security Engineer (engaged under CISO oversight) | Guides containment/eradication, evidence capture, threat assessment, and ISMS alignment. |
| OT Liaison (if OT impact) | Designated plant/OT representative coordinated via Regional IT Operations | Ensures plant constraints and safety considerations are reflected in actions. |

### 10.3 War room rules of engagement
- Use one primary collaboration channel per incident and record the link in the ticket.
- Single-threaded decision making through the Incident Commander.
- No unapproved production changes; emergency changes must be recorded and linked to CAB governance.
- Every action must have an owner and timestamp.
- Confirm restoration with objective verification (monitoring + user validation + service checks).

## 11. Communications and Stakeholder Updates
### 11.1 Communication objectives
- Provide accurate, timely, and consistent status.
- Maintain confidentiality and need-to-know for security incidents.
- Enable business decision-making (production scheduling, customer commitments).

### 11.2 Stakeholder groups
- Affected end users and site leadership
- Global IT Operations and Regional IT Operations leadership
- Service Owner(s) and Platform Owner(s)
- CISO and Security Engineer (security incidents)
- Data Protection Officer (DPO) (privacy-related)
- Internal Audit (when evidence is requested or when control relevance is high)
- Third-party providers (cloud, telecom, security vendors) as required

### 11.3 Update cadence (minimums)
- Sev 1: every 30 minutes
- Sev 2: every 60 minutes
- Sev 3: every 4 hours or upon milestone changes
- Sev 4: as needed

### 11.4 Communications templates
Templates are provided in Appendix B and must be used to ensure consistency and completeness.

## 12. Procedures (Detect → Triage → Contain → Eradicate → Recover → PIR)
### 12.1 Detect
**Inputs**
- Monitoring and Event Management alerts (SIEM, EDR, infrastructure monitoring, cloud alerts)
- User reports via Service Desk
- Vendor notifications (Microsoft, AWS, ISP)
- OT monitoring escalations via Regional IT Operations

**Steps**
1. Monitoring system generates alert or user reports issue.
2. Service Desk logs incident ticket (or auto-creates from monitoring integration).
3. Correlate to existing incidents/known issues to prevent duplication.
4. If indicators suggest malicious activity, classify as potential security incident and engage Security Engineer immediately.

**Minimum data to capture**
- Detection source, timestamp, affected service/CI, symptoms, initial scope, and any error codes.

### 12.2 Triage (Log, categorize, prioritize, route)
**Steps**
1. Confirm affected service and impacted users/sites; link to relevant CI(s).
2. Assign category/subcategory (e.g., Network, Identity, Cloud, Endpoint, OT Connectivity).
3. Assign severity using Section 9; update as scope/impact changes.
4. Determine if Major Incident criteria are met; initiate war room if needed.
5. Route to appropriate resolver group (Network Engineer, IAM Engineer, Cloud Engineer, Systems Engineer, Endpoint Engineer, Security Engineer).
6. For suspected security incidents, begin evidence preservation steps (Section 14) and avoid destructive actions until Security Lead confirms.

**Decision points**
- Is this a security incident? If yes, engage Security Engineer and follow security playbook elements.
- Is OT impacted? If yes, assign OT Liaison and confirm plant operational constraints before changes.

### 12.3 Contain (limit impact)
Containment aims to stop degradation/spread quickly, even if not the final fix.

**Containment actions (examples)**
- Network: isolate affected VLAN/site, block malicious IPs/domains, disable compromised VPN accounts.
- Identity: disable suspected compromised accounts, revoke sessions, enforce password reset, increase conditional access restrictions.
- Endpoint: isolate devices via EDR, block indicators, disable removable media where applicable.
- Cloud: lock down security groups/NSGs, rotate keys, restrict access paths.
- OT connectivity: failover to approved alternate connectivity paths where available; disable non-essential remote access routes.

**Governance**
- Any containment that changes production configuration is recorded and linked to Change Enablement; emergency containment is permitted when required to reduce harm but must be documented and reviewed post-action.

### 12.4 Eradicate (remove cause)
Eradication focuses on eliminating the underlying cause and preventing immediate recurrence.

**Steps**
1. Identify root cause hypothesis (vulnerability exploit, misconfiguration, dependency outage).
2. Remove malicious artifacts (security), remediate misconfiguration, apply necessary patches, rotate credentials/keys.
3. Validate that eradication did not introduce additional risk or outages.
4. If the fix is non-trivial or risk-bearing, coordinate through CAB and implement as an emergency or expedited normal change as appropriate.

### 12.5 Recover (restore and validate)
**Steps**
1. Restore services to normal operation (restart/failover/restore configuration/restore from backup).
2. Perform validation:
   - Technical checks (health probes, synthetic tests, log stability)
   - User confirmation for critical workflows
3. Monitor for recurrence for an agreed stabilization period:
   - Sev 1: minimum 2 hours post-restoration (or longer for security)
   - Sev 2: minimum 1 hour post-restoration
4. Confirm communications: “service restored” update and next steps (PIR, any required user actions).

### 12.6 Close (document and confirm)
**Closure requirements**
- Incident record includes:
  - Accurate timeline, severity, impacted services/CIs, user impact
  - Actions taken and by whom
  - Resolution summary and validation performed
  - Linkages: related incidents, problem record, changes, security case
  - Evidence links (logs, screenshots, exports)
- Service Owner confirms closure for Major Incidents and customer-facing services where required.

### 12.7 Post-Incident Review (PIR)
**PIR triggers (mandatory)**
- All Sev 1 incidents
- Sev 2 incidents with significant impact, repeat occurrence, or control concerns
- Any security incident with confirmed compromise, data exposure risk, or widespread containment actions
- Any OT connectivity loss affecting production continuity

**PIR steps**
1. Schedule PIR within:
   - Sev 1: within 5 business days
   - Sev 2: within 10 business days
2. Produce PIR report using Appendix D template.
3. Identify corrective actions with owners and due dates; create Problem record if systemic.
4. Track actions to completion via ITSM and report status in operational reviews.

## 13. Playbooks (Minimum Required)
Playbooks supplement the lifecycle procedures with scenario-specific actions. Each playbook must still follow the incident ticketing, evidence, communications, and change governance requirements in this document.

### 13.1 Ransomware (Security Incident, typically Sev 1)
**Primary objectives**
- Protect safety and production, stop spread, preserve evidence, restore services securely.

**Immediate actions (0–30 minutes)**
1. Declare security incident; engage Security Engineer and IT Operations Manager.
2. Initiate war room; assign Incident Commander, Security Lead, and Scribe.
3. Contain:
   - Isolate affected endpoints/servers via EDR.
   - Disable suspected compromised accounts in Active Directory and Entra ID; revoke sessions.
   - Block known indicators (hashes/domains/IPs) in EDR/SIEM controls where available.
4. Preserve evidence:
   - Capture EDR incident details, affected host list, timestamps.
   - Snapshot relevant logs (SIEM queries, authentication logs, firewall logs).

**Stabilization actions**
5. Identify initial access vector (phishing, exposed service, credential compromise).
6. Confirm backup integrity and last known good restore points.
7. Segment impacted networks; confirm OT segmentation remains effective.
8. Coordinate with Service Owner(s) on restoration priority order.

**Eradication & recovery**
9. Reimage affected endpoints; rebuild servers where required (preferred over “cleaning”).
10. Rotate credentials and secrets:
   - Admin accounts, service accounts, API keys, certificates as scoped.
11. Restore from backups; validate services and monitor for re-encryption attempts.
12. Confirm containment success using SIEM/EDR (no new detections, stable authentication patterns).

**PIR focus**
- Control gaps (MFA, conditional access, least privilege, patching)
- Backup/restore readiness and RPO/RTO adherence
- Detection gaps and response time improvement

### 13.2 Network Outage (Core WAN/LAN/Internet, Sev 1 or Sev 2)
**Immediate actions**
1. Log incident; assign severity based on site/region scope and manufacturing impact.
2. Initiate war room if Sev 1/Sev 2 cross-team.
3. Validate scope:
   - Which sites, circuits, cloud connectivity, DNS, or firewall clusters are affected?
4. Contain:
   - Failover links if available.
   - Apply routing mitigations only with documented approvals; emergency changes must be recorded.

**Diagnosis**
5. Check:
   - ISP status and circuit alarms
   - Core routing/switching health
   - Firewall/SD-WAN state
   - DNS resolution and authentication dependencies
6. Confirm whether issue is internal misconfiguration, provider outage, or DDoS (if suspicious, engage Security Engineer).

**Recovery**
7. Restore connectivity:
   - Roll back known bad changes (with change record linkage)
   - Replace failed hardware, reroute traffic, restore config from known good
8. Validate:
   - Site-to-cloud connectivity
   - Identity sign-in success
   - OT connectivity paths (if applicable)

**Communications**
- Provide clear business guidance: expected user impact (VPN, email, ERP), workarounds, and estimated restoration windows based on provider ETAs.

### 13.3 Identity Compromise (Active Directory / Entra ID, typically Sev 1)
**Immediate actions**
1. Declare security incident; engage Security Engineer and IAM Engineer.
2. Initiate war room for enterprise identity impact.
3. Contain:
   - Disable suspected accounts and privileged roles.
   - Revoke sessions and tokens in Entra ID.
   - Force password resets and rotate privileged credentials.
   - Restrict sign-in with conditional access adjustments where safe.
4. Preserve evidence:
   - Authentication logs, risky sign-in reports, admin role assignment changes, PAM audit logs.

**Diagnosis**
5. Determine compromise path:
   - MFA fatigue/social engineering, token theft, legacy auth, compromised endpoint, misconfigured federation.
6. Identify blast radius:
   - Mailbox access, SharePoint/OneDrive access, cloud subscriptions, privileged group modifications.

**Eradication & recovery**
7. Remove persistence:
   - Remove rogue MFA devices, app registrations, consent grants, backdoor accounts.
8. Validate:
   - Confirm privileged roles are correct.
   - Monitor for repeated suspicious sign-ins.
9. Communicate required user actions (password reset, re-registration) using approved template language.

**PIR focus**
- Privileged access hardening, conditional access baselines, PAM coverage, monitoring improvements.

### 13.4 OT Connectivity Loss (Plant impact, Sev 1 or Sev 2)
**Scope note**
This playbook covers IT-managed connectivity dependencies impacting OT networks and plant operations; OT system remediation follows plant OT procedures, coordinated through the OT Liaison.

**Immediate actions**
1. Log incident and determine severity based on production impact and safety considerations.
2. Engage Regional IT Operations and assign OT Liaison.
3. Initiate war room for multi-team coordination if manufacturing impact is significant.

**Containment and safety**
4. Do not make changes that could compromise plant safety systems.
5. Confirm segmentation boundaries remain enforced; avoid ad-hoc bridging of OT and IT networks.

**Diagnosis**
6. Identify failure domain:
   - Plant WAN link, firewall rules, remote access gateway, DNS, time sync, identity dependency, cloud connector.
7. Validate whether change activity occurred prior to incident; if yes, link to the relevant change record.

**Recovery**
8. Restore connectivity using approved paths:
   - Failover circuits, alternate remote access, rollback of network policy changes (with change governance)
9. Validate with OT Liaison:
   - MES/SCADA connectivity checks, critical workflows restored, stable latency where required.
10. Establish monitoring for the restored path and confirm stabilization.

**PIR focus**
- Single points of failure, monitoring coverage, documented failover procedures, and resilience improvements aligned to ISO/IEC 22301.

## 14. Evidence Handling and Recordkeeping
### 14.1 Required incident evidence (by incident type)
| Evidence type | Examples | Required for |
|---|---|---|
| ITSM ticket data | Severity, timeline, impacted services/CIs, assignments, updates | All incidents |
| Monitoring artifacts | Alert IDs, metric graphs, synthetic test results | All monitoring-detected incidents |
| Authentication logs | Entra ID sign-ins, Active Directory logs, PAM logs | Identity and security incidents |
| Network logs | Firewall events, VPN logs, router/switch logs | Network/OT connectivity incidents |
| Endpoint/EDR artifacts | Detection details, isolation actions, host timeline | Malware/ransomware/endpoint incidents |
| Change linkage | Emergency change record, approvals, rollback plan | Any configuration change performed |
| Communications record | Stakeholder updates sent, timestamps | Sev 1/Sev 2 and major incidents |
| Recovery validation | Service health checks, user validation confirmation | Sev 1/Sev 2 and critical services |
| PIR report | Completed template with actions | PIR-triggering incidents |

### 14.2 Evidence storage and access
- Store artifacts in approved repositories with access controlled by least privilege.
- Link artifact locations in the ITSM incident record.
- For security incidents, restrict access to Security Engineer, CISO-designated stakeholders, and authorized investigators.
- Retain evidence per Norfolk Industries retention policy and applicable legal/regulatory requirements (GDPR, SOX).

## 15. Tooling, Integrations, and CMDB Linkage
### 15.1 ITSM tool requirements
- Incident workflow supports severity, major incident flag, tasks, approvals, and linked records.
- Mandatory CI linkage for Sev 1–Sev 2 and for recurring Sev 3 incidents.
- Time-stamped work notes and customer-facing notes separation.

### 15.2 Monitoring and security tooling integrations
- SIEM (e.g., Microsoft Sentinel) alerts may auto-create incidents.
- EDR (e.g., Microsoft Defender for Endpoint) incidents integrate into workflows for containment actions tracking.
- Vulnerability scanner output informs eradication and PIR actions when relevant.
- PAM (e.g., CyberArk) provides privileged session audit logs for evidence.

## 16. Metrics, Reporting, and Continual Improvement
### 16.1 Operational metrics
| Metric | Description | Applies to |
|---|---|---|
| Mean Time to Acknowledge (MTTA) | Time from detection to responder engagement | Sev 1–Sev 3 |
| Mean Time to Restore (MTTR) | Time from incident start to service restoration | Sev 1–Sev 3 |
| Major incident count | Number of Sev 1/major incidents per period | Monthly/quarterly |
| Repeat incident rate | Incidents recurring within 30/60/90 days | Service Owner review |
| PIR completion rate | PIR completed within required timeline | Sev 1 and required Sev 2 |
| Change-related incident rate | Incidents linked to changes | CAB and process improvement |

### 16.2 Continual improvement process
- ITSM Process Owner reviews trends monthly with Global IT Operations and Regional IT Operations.
- Service Owner and Platform Owner implement preventative actions via Problem Management and change roadmaps.
- IT Governance Manager ensures evidence and compliance improvements are tracked and audit-ready.

## 17. Exceptions and Risk Acceptance
- Exceptions to this policy (e.g., alternate communications method, modified evidence handling due to legal constraints) require documented approval by the Head of IT Infrastructure Services and consultation with the CISO for any security-related deviation.
- High-risk exceptions follow Norfolk Industries risk governance and must be time-bound with compensating controls.

## 18. Training and Awareness
- Service Desk training: intake, severity assignment, communications templates, escalation paths.
- On-call responder training: war room operations, evidence handling, emergency change documentation.
- Security incident handling: coordinated exercises led by the CISO-designated function; includes ransomware tabletop scenarios.
- OT connectivity scenarios: joint exercises with Regional IT Operations and OT stakeholders to validate escalation and failover procedures.

## 19. Document Control
### 19.1 Ownership and maintenance
- Document owner: ITSM Process Owner
- Accountable executive: Head of IT Infrastructure Services
- ISMS oversight: CISO
- Compliance coordination: IT Governance Manager

### 19.2 Review cadence
- Reviewed at least annually and after any Sev 1 incident requiring significant process change.
- Updates follow policy/standard governance and are communicated to Global IT Operations and Regional IT Operations.

---

## Appendix A: Incident Ticket Template (ITSM)
Use this structure for incident records to ensure consistent, auditable documentation.

### A.1 Required fields (all incidents)
| Field | Requirement |
|---|---|
| Caller / Reporter | Name, contact method |
| Detection source | Monitoring system, Service Desk, vendor, OT escalation |
| Date/time detected | Include timezone |
| Service impacted | Service name and Service Owner |
| CI(s) impacted | CI reference(s) |
| Category / Subcategory | Network, Identity, Cloud, Endpoint, OT Connectivity, Security, etc. |
| Symptoms | User-visible and technical symptoms |
| Business impact statement | What is impacted (production, sites, users, revenue risk) |
| Severity | Sev 1–Sev 4, with rationale |
| Assignment group | Resolver team |
| Work notes | Time-stamped actions, owners, decisions |
| Customer-facing updates | Approved stakeholder updates (sanitized) |
| Related records | Problem, change, security case, knowledge article |
| Resolution summary | What fixed it |
| Validation performed | Checks and confirmations |
| Closure code | Restored service / workaround / duplicate / canceled |
| Evidence links | Logs, screenshots, exports, comms records |

### A.2 Major incident addendum (Sev 1 and major incidents)
| Field | Requirement |
|---|---|
| Incident Commander | Named person |
| War room link | Primary collaboration link |
| Technical lead(s) | Named person(s) by domain |
| Communications lead | Named person |
| Scribe | Named person |
| Stakeholder update cadence | 30/60 minutes as applicable |
| Timeline | Start, detection, acknowledgment, containment, recovery milestones |
| Impact quantification | Sites/users affected, duration, production impact description |
| Decision log | Key decisions with timestamps and approvers |

---

## Appendix B: Communications Templates
All templates must be copied into the incident ticket and used consistently. Do not include sensitive security details in broad distribution updates.

### B.1 Initial notification (Sev 1/Sev 2)
**Subject:** \[Incident\] \[Severity\] – \[Service\] Impact – \[Region/Site\] – \[Time\]  
**Message:**
- Summary: An incident is impacting **\[service\]**.
- Impact: **\[who/what is affected; include sites/regions; production/OT impact if applicable\]**
- Start time: **\[timestamp/timezone\]**
- Current status: **Investigating / Containment in progress / Recovery in progress**
- Workaround: **\[if any\]**
- Next update: **\[timestamp/timezone\]**
- Reference: **ITSM Incident \[#\]**

### B.2 Status update (ongoing)
**Subject:** \[Update\] \[Severity\] – \[Service\] – ITSM Incident \[#\]  
**Message:**
- Current status: **\[what changed since last update\]**
- Impact: **\[current scope\]**
- Actions underway: **\[high-level actions; no sensitive details\]**
- Risks/constraints: **\[if relevant\]**
- ETA: **\[best estimate; if unknown, state next milestone\]**
- Next update: **\[timestamp/timezone\]**

### B.3 Service restored
**Subject:** \[Resolved\] \[Severity\] – \[Service\] – ITSM Incident \[#\]  
**Message:**
- Resolution: Service restored as of **\[timestamp/timezone\]**
- Validation: **\[monitoring stable; user confirmation; key checks\]**
- Residual risk: **\[if any user actions required\]**
- Next steps: Post-Incident Review will be conducted by **\[date\]** (if applicable)
- Reference: **ITSM Incident \[#\]**

### B.4 Security incident stakeholder note (restricted distribution)
**Subject:** \[Restricted\] Security Incident – \[Severity\] – ITSM Incident \[#\]  
**Message:**
- Summary (restricted): **\[high-level; avoid speculation\]**
- Current containment: **\[what is contained and how\]**
- Impact assessment: **\[systems/accounts; whether personal data is suspected\]**
- Evidence captured: **\[log sources and timestamps\]**
- Required approvals/decisions: **\[e.g., password reset scope, access restriction\]**
- Next update: **\[timestamp/timezone\]**

---

## Appendix C: Incident Evidence Checklist (Minimum)
Use this checklist to ensure evidence completeness and audit readiness.

### C.1 Checklist
- Incident ticket created with accurate detection timestamp and source
- Severity assigned with rationale and updated when scope changed
- Impacted service and CI(s) linked
- Timeline captured (key milestones)
- Actions recorded with owner and timestamp
- Monitoring artifacts attached/linked (graphs, alert IDs)
- Relevant logs preserved and linked:
  - Authentication logs (if identity involved)
  - Network logs (if network/OT connectivity involved)
  - EDR artifacts (if endpoint/security involved)
  - Cloud logs (if cloud involved)
- Communications logged (initial + updates + restoration)
- Change linkage created for remediation changes; emergency change noted where applicable
- Recovery validation documented
- PIR scheduled and completed when triggered
- Problem record created when recurrence risk exists

---

## Appendix D: Post-Incident Review (PIR) Template
### D.1 PIR header
| Field | Content |
|---|---|
| ITSM Incident # |  |
| Severity |  |
| Service(s) impacted |  |
| Service Owner |  |
| Platform Owner(s) |  |
| Incident Commander |  |
| Date/time of incident |  |
| Duration |  |
| Regions/sites impacted |  |
| OT impact (yes/no) |  |
| Security incident (yes/no) |  |
| Participants |  |

### D.2 Executive summary
- What happened (brief, factual)
- Business impact (including production impact if applicable)
- Current risk posture (any residual risk)

### D.3 Detailed timeline (time-bound)
| Timestamp (timezone) | Event | Owner |
|---|---|---|
|  | Detection |  |
|  | Triage/severity assigned |  |
|  | Containment actions |  |
|  | Recovery started |  |
|  | Service restored |  |
|  | Stabilization complete |  |

### D.4 Root cause and contributing factors
- Root cause (technical)
- Contributing factors (process/tooling/monitoring/change)
- What prevented faster detection or recovery

### D.5 What went well / what did not go well
- Went well
- Did not go well

### D.6 Corrective and preventive actions (tracked)
| Action | Owner (role/name) | Due date | Linked record (Problem/Change) | Status |
|---|---|---|---|---|
|  |  |  |  |  |

### D.7 Control and compliance considerations
- ISMS considerations and evidence sufficiency
- SOC 2 Availability/Security considerations
- GDPR assessment outcome (if applicable) and DPO involvement
- SOX impact assessment (if financial systems impacted)

### D.8 Communications review
- Stakeholders notified and cadence met
- Any gaps or miscommunications and remediations

### D.9 Closure criteria
- All actions logged, owners assigned, and follow-ups scheduled
- Service Owner approval for closure (required for major incidents)

---

## Appendix E: Required Evidence List by Scenario (Quick Reference)
| Scenario | Must-have evidence |
|---|---|
| Ransomware | EDR detections + host list; SIEM correlation queries; containment actions; account disablement logs; backup restore logs; key decision approvals; comms record; recovery validation checks. |
| Network outage | Provider ticket/ETA; device logs; monitoring graphs; routing/firewall change records; rollback documentation; restoration validation (sites, identity dependencies). |
| Identity compromise | Entra ID sign-in/risky events; role assignment change logs; session revocation evidence; PAM logs; affected account list; containment decisions; user comms. |
| OT connectivity loss | Network path diagnostics; circuit status; firewall policy logs; change linkage; validation by OT Liaison; monitoring evidence for stability post-recovery. |