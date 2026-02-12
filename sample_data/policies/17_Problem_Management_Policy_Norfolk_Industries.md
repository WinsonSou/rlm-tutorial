# Problem Management Policy (Norfolk Industries)

## 1. Purpose
This Problem Management Policy establishes the mandatory governance, minimum control requirements, and operating expectations for identifying, analyzing, and eliminating the root causes of Incidents and recurring service degradation within Norfolk Industries. The policy aligns Problem Management with ITIL 4 practices and the Norfolk Industries Information Security Management System (ISMS), ensuring stable, secure, and resilient 24×7 operations across hybrid cloud, on-premises, and Operational Technology (OT) integrated environments.

## 2. Scope
### 2.1 In scope
This policy applies to:
- All services delivered or supported by **IT Infrastructure Services** across North America, Europe, and APAC.
- **Global IT Operations** and **Regional IT Operations** staff and processes.
- Hybrid cloud platforms (Microsoft Azure primary, AWS secondary), on-prem data centers, identity services (Active Directory and Entra ID (Azure AD) / Entra ID), endpoint management (Microsoft Intune and ConfigMgr where needed), monitoring/SIEM/EDR/vulnerability tooling, and related infrastructure platforms.
- IT/OT integration points affecting plant networks, remote access, and shared identity or monitoring, including SCADA/MES connected zones (without superseding OT safety and plant control requirements).

### 2.2 Out of scope
- Product quality investigations unrelated to IT service delivery.
- Purely business process issues not involving IT service impairment (these should be handled by the relevant business process governance).
- Safety incident investigations (handled by EHS), except where IT service failures are contributing factors; in such cases, Problem Management provides supporting technical analysis.

## 3. Policy statement
Norfolk Industries will:
1. Use a standardized Problem Management process to reduce Incident recurrence and minimize the impact of Incidents that cannot be prevented.
2. Maintain a **Known Error Database (KEDB)** within the ITIL-aligned ITSM tool to document Known Errors, workarounds, and permanent corrective actions.
3. Perform Root Cause Analysis (RCA) for qualifying Problems using consistent methods (5 Whys and fishbone cause-and-effect concepts) and maintain evidence that is time-bound, attributable, and repeatable.
4. Ensure corrective actions are risk-assessed, tested, implemented through Change Enablement governance, and validated for effectiveness.
5. Track Problem trends to proactively address systemic weaknesses and to support continual improvement.

## 4. Definitions and terminology
### 4.1 Canonical terms (mandatory)
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

### 4.2 Problem vs Incident (required distinction)
- **Incident**: An unplanned interruption to an IT service or reduction in the quality of an IT service requiring restoration as quickly as possible to meet SLOs.
- **Problem**: The underlying cause, or potential cause, of one or more Incidents, where the objective is to prevent recurrence and/or reduce impact through workaround and permanent corrective action.
- Relationship:
  - Incidents focus on **rapid restoration**.
  - Problems focus on **root cause elimination and prevention**.
  - A Problem may exist without a major Incident (e.g., a detected vulnerability or capacity trend likely to cause future service disruption).

### 4.3 Known Error and KEDB
- **Known Error**: A Problem with a documented root cause (or most probable cause) and a documented workaround and/or permanent fix plan.
- **Known Error Database (KEDB)**: The authoritative repository (within the ITSM tool) containing Known Error records linked to Incidents, Problems, Changes, CIs, and knowledge articles.

## 5. Roles and responsibilities
All roles below are mandatory and must align to the role definitions established by Norfolk Industries.

### 5.1 Key responsibilities
- **CIO**
  - Executive oversight of IT governance and outcomes related to stability and risk.
- **Head of IT Infrastructure Services**
  - Accountable for Problem Management effectiveness across IT Infrastructure Services, including resourcing and prioritization.
- **CISO**
  - Ensures Problem Management outputs support the ISMS, including security-related root causes and corrective actions.
- **IT Governance Manager**
  - Owns policy lifecycle, compliance tracking, and audit coordination for Problem Management evidence.
- **Service Owner**
  - Accountable for Problem prioritization, risk acceptance decisions within governance, and service-level outcomes.
- **Platform Owner**
  - Accountable for technical standards and engineering decisions impacting root cause removal for their domain (network, cloud, endpoint, identity).
- **IT Operations Manager**
  - Ensures operational execution, 24×7 readiness, and that Problem work does not degrade operational stability.
- **ITSM Process Owner**
  - Owns ITIL-aligned process design for Problem Management and integration with Incident, Change Enablement, and Service Configuration Management.
- **Internal Audit**
  - Independently assesses control design and operating effectiveness.

### 5.2 RACI alignment (policy-level)
The following table is consistent with the Norfolk Industries RACI master and interprets Problem Management activities within that framework.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy requirements (normative controls)
### 6.1 Problem identification and logging
- Problems **must** be logged in the ITSM tool when any of the following apply:
  - A Major Incident occurs.
  - Recurring Incidents exceed trend thresholds (Appendix C).
  - A high-risk security defect, vulnerability, or control failure requires systemic remediation.
  - Monitoring indicates chronic degradation, capacity exhaustion trends, or repeated component failures.
- Problem records **must** be linked to:
  - Associated Incidents, service records, and impacted **Configuration Item (CI)** entries.
  - Related Changes (including Emergency Changes) where applicable.
- Problem categorization **must** align to service and platform taxonomy used in the ITSM tool to enable reporting.

### 6.2 Prioritization and risk-based triage
- Problem priority **must** consider:
  - Business impact (including OT plant impact and production downtime).
  - Likelihood of recurrence.
  - Security, compliance, and safety implications.
  - Service criticality and SLO breach risk.
- Security-related Problems that indicate active exploitation or imminent risk **must** be coordinated with the CISO organization and Security Engineering for containment and response.

### 6.3 Root Cause Analysis (RCA) standards
- RCA **must** be performed for:
  - Major Incident-driven Problems.
  - High-risk or high-impact recurring Problems.
  - Any Problem requiring cross-domain corrective action.
- RCA **must** use at least one structured method and document evidence:
  - **5 Whys**: iterative causal questioning to identify underlying systemic causes.
  - **Fishbone (Ishikawa) concepts**: cause categories such as People, Process, Technology, Environment, Suppliers/Third Parties, and Measurement/Monitoring.
- RCA deliverables **must** include:
  - Timeline of events and contributing factors.
  - Confirmed or most probable root cause(s) with supporting evidence.
  - Workaround (if applicable) and the risk of workaround usage.
  - Corrective action plan with owners, due dates, and implementation path (Change Enablement where required).
  - Validation criteria and success measures.

### 6.4 Known Error management
- A Known Error record **must** be created when:
  - Root cause is identified and a workaround exists, or
  - Root cause is strongly suspected and a reliable workaround is available to reduce impact.
- Known Error records **must** include:
  - Symptoms, affected services/CIs, impact, and detection signals.
  - Workaround steps (operationally safe, including OT access constraints).
  - Permanent resolution plan and links to approved Changes or backlog items.
  - Review date and retirement criteria.

### 6.5 Corrective actions and Change Enablement integration
- Corrective actions that modify production services **must** follow Change Enablement and be reviewed by the **Change Advisory Board (CAB)** when classified as Normal Change, or Emergency Change as applicable.
- Corrective actions **must** address:
  - Technical remediation (patch, configuration correction, architecture improvement).
  - Process remediation (runbook updates, monitoring thresholds, access control changes).
  - Control remediation (security hardening, detection improvements, segregation changes).
- Risk acceptance is not a substitute for remediation; where risk acceptance is necessary, it **must** be documented and approved through established governance aligned to the ISMS.

### 6.6 Validation and closure
- A Problem **must not** be closed until:
  - Corrective actions are implemented or formally deferred with documented rationale and interim controls.
  - Effectiveness is validated against defined success criteria (Appendix A).
  - The KEDB is updated (if applicable) and linked knowledge/runbooks are updated.
- Closure **must** include:
  - Post-implementation verification evidence.
  - Updated monitoring and alerting (where relevant).
  - Communication to stakeholders per ITSM communication standards.

## 7. Procedures (policy-mandated process)
This section defines the minimum required procedures. Detailed work instructions may exist as controlled documents under the ISMS.

### 7.1 Problem detection and initiation
Problems may be initiated from:
- Major Incident review triggers.
- Recurring Incident patterns (trend analysis).
- Monitoring and event management alerts indicating chronic degradation.
- Vulnerability management findings and security control failures.
- Capacity, performance, or reliability reporting that threatens SLO attainment.
- Supplier or cloud provider advisories affecting Norfolk Industries platforms.

Minimum steps:
1. Log Problem in ITSM tool and assign Service Owner and initial resolver group.
2. Link all related Incidents and impacted CIs.
3. Record immediate containment/workaround actions and any operational constraints (including OT segmentation and remote access controls).
4. Set priority using risk-based triage criteria.

### 7.2 Root Cause Analysis (RCA) execution
Minimum steps:
1. Establish an investigation timeline with key events (alerts, tickets, changes, deployments, authentication events, network events).
2. Collect evidence: logs (SIEM/EDR), monitoring graphs, configuration snapshots, change records, vulnerability scan outputs, and relevant access logs.
3. Apply structured analysis:
   - Perform **5 Whys** to drive from symptom to systemic cause.
   - Use **fishbone categories** to ensure non-technical contributors are evaluated (process gaps, training, supplier issues).
4. Identify:
   - Direct cause(s)
   - Contributing factors
   - Control failures (preventive/detective)
5. Document RCA in the standardized template (Appendix A) and obtain review by the Service Owner and Platform Owner.

### 7.3 Corrective action planning
Minimum steps:
1. Define corrective actions across:
   - Technology (fix)
   - Process/runbook (prevent recurrence)
   - Monitoring/detection (detect earlier)
   - Access/security controls (reduce exploitability)
2. Assign owners and due dates; record dependencies (supplier, maintenance windows, CAB schedules).
3. Determine if Change Enablement is required:
   - Production-impacting changes require Change records and CAB governance.
4. Define validation criteria and metrics (e.g., incident recurrence reduction, error rate reductions, performance improvements).

### 7.4 Implementation and validation
Minimum steps:
1. Implement corrective actions via approved Change records where applicable.
2. Validate outcomes:
   - Confirm service health and SLO compliance.
   - Confirm no regression in related services.
   - Confirm monitoring/alerting now detects the condition earlier or prevents recurrence.
3. Update operational documentation:
   - Known Error record (if created)
   - Knowledge articles and runbooks
   - CI relationships if architecture changed
4. Attach validation evidence to the Problem record per evidence principles.

### 7.5 Closure and post-closure monitoring
Minimum steps:
1. Confirm closure criteria are met (Section 6.6).
2. Conduct a short closure review for high-impact Problems:
   - Lessons learned and improvement actions.
3. Monitor for recurrence for an agreed period based on criticality:
   - Minimum: one full business cycle for non-critical services
   - For critical/24×7 services: include weekend and peak production periods as applicable
4. Close Problem and schedule KEDB record review/retirement date if relevant.

## 8. Tooling, records, and data management
### 8.1 Systems of record
- ITSM tool is the system of record for:
  - Problem records, Known Error records, linkages to Incidents/Changes/CIs, approvals, and communications.
- Monitoring and logs:
  - SIEM (e.g., Microsoft Sentinel), EDR (e.g., Microsoft Defender for Endpoint), vulnerability scanning (e.g., Tenable/Nessus), cloud platform logs, network telemetry.

### 8.2 Recordkeeping requirements
Problem and Known Error records must include:
- Unique identifier, timestamps, and ownership
- Service and CI linkage
- RCA artifacts and evidence references
- Corrective action plan and Change linkages
- Validation evidence and closure approval

Records must be retained according to Norfolk Industries retention and audit requirements under the ISMS and applicable regulations (including SOX and GDPR), ensuring least-privilege access and appropriate data classification.

## 9. Integration with other processes
Problem Management must integrate with:
- **Incident Management**: Incident-to-Problem triggers; shared communications; Major Incident review outputs.
- **Change Enablement**: corrective actions routed through CAB as required.
- **Service Configuration Management**: CI linkage and relationship mapping.
- **Monitoring and Event Management**: event trends and alert tuning.
- **Information Security Management**: security defect/cause remediation aligned to ISMS risk treatment.
- **Service Continuity Management**: where Problems affect RTO/RPO or resilience architecture.

## 10. Metrics and reporting
Minimum reporting requirements:
- Problem backlog by priority and age
- RCA completion timeliness for Major Incident-driven Problems
- Recurrence rate: number of repeat Incidents linked to the same root cause
- Mean time to root cause identification (MTTRc)
- Mean time to permanent fix (MTTPF)
- KEDB usage: number of Incidents resolved using Known Error workaround
- Trend drivers (top services/CIs by Problem volume)

Trend analysis metrics and thresholds are defined in Appendix C.

## 11. Risk management and exceptions
- Problems indicating unacceptable risk to confidentiality, integrity, availability, or safety must be escalated to the Head of IT Infrastructure Services and the CISO.
- Exceptions (deferrals, risk acceptance, or workaround-only approaches) must be:
  - Documented in the Problem record with rationale and interim controls
  - Reviewed by the Service Owner and Platform Owner
  - Governed in alignment with the ISMS and Change Enablement where applicable
- High-risk exceptions require governance escalation consistent with Norfolk Industries risk management practices.

## 12. Compliance and audit
- Compliance is mandatory for IT Infrastructure Services, Global IT Operations, and Regional IT Operations.
- Evidence must meet Norfolk Industries evidence principles:
  - **Time-bound, attributable, repeatable**
  - Include approvals, logs, and validation artifacts where applicable
- Internal Audit may assess:
  - Completeness and quality of RCA
  - Traceability from Incident → Problem → Known Error → Change → Validation
  - Operating effectiveness of controls and metrics

An evidence list is provided in Appendix D.

## 13. Security and privacy considerations
- RCA evidence may include sensitive information (logs, identities, IPs, endpoint telemetry). Access must follow least privilege and applicable privacy controls.
- For personal data in logs or tickets:
  - Limit collection to what is necessary
  - Follow GDPR-aligned handling and retention
  - Coordinate with the Data Protection Officer (DPO) when privacy risk is identified
- OT-related Problems must respect segmentation and strict remote access controls; investigative access must follow approved remote access procedures and PAM controls.

## 14. Training and awareness
- Roles participating in Problem Management must complete training appropriate to responsibilities, including:
  - ITIL-aligned Problem Management workflow
  - RCA methods (5 Whys, fishbone concepts)
  - Evidence standards and documentation quality
  - Change Enablement and CAB expectations for corrective actions
- ITSM Process Owner coordinates training content; IT Operations Manager ensures operational staff completion.

## 15. Third-party and supplier considerations
- Where suppliers (cloud providers, managed services, telecoms, OT vendors) contribute to Problems:
  - Evidence and timelines must capture supplier engagement and outcomes.
  - Corrective actions may include contract/SLA review, escalation paths, or architectural mitigations.
  - Supplier-related Known Errors must include dependency and escalation instructions for Service Desk and on-call teams.

## 16. Business continuity and resilience alignment
- Problems impacting resilience targets must be assessed against:
  - **Recovery Time Objective (RTO)**
  - **Recovery Point Objective (RPO)**
- Corrective actions must prioritize elimination of single points of failure, restoration automation, and monitoring improvements for critical services.
- Where appropriate, Problem outcomes must be fed into Service Continuity Management for exercise scenarios and plan updates.

## 17. Standards and control mapping
This policy is aligned to recognized frameworks used by Norfolk Industries and is governed under the ISMS.

### 17.1 Control mapping overview (conceptual)
| Framework | Area / Concept | Problem Management alignment | Typical evidence |
|---|---|---|---|
| ISO/IEC 27001 (Annex A concept) | Information security incident management; operational procedures; monitoring and logging; change control | RCA for security-impacting failures; corrective actions; controlled change implementation; evidence retention | Problem records, RCA, change approvals, SIEM/EDR logs, validation results |
| NIST CSF | Identify / Protect / Detect / Respond / Recover | Trend identification; preventive fixes; detection tuning; response learnings; recovery improvements | Trend reports, monitoring dashboards, Known Errors, post-implementation verification |
| SOC 2 TSC | Security, Availability, Confidentiality, Processing Integrity, Privacy | Availability and security improvements driven by root cause removal; privacy-aligned evidence handling | Problem/KEDB records, access controls, retention logs, validation artifacts |
| ITIL 4 | Problem Management; Change Enablement; Incident Management; Monitoring and Event Management | Standard Problem lifecycle with RCA and Known Errors integrated with change and incident workflows | Linked Incident–Problem–Change records; RCA templates; CAB decisions |
| COBIT 2019 | EDM/APO/BAI/DSS/MEA concepts | Governance, planning, build/implement fixes, service delivery stability, monitoring and assurance | Governance reporting, backlog aging, audit evidence packs |

## 18. Review cycle and maintenance
- This policy must be reviewed at least annually, and additionally upon:
  - Significant platform changes (cloud/identity/network architecture)
  - Major audit findings
  - Material changes to regulatory obligations or ISMS requirements
- The IT Governance Manager coordinates review; the Head of IT Infrastructure Services is accountable for approval workflow per governance.

## 19. Appendices (templates, checklists, runbooks)
All appendices are mandatory controlled templates for use within the ITSM tool or attached as governed artifacts.

### Appendix A: Root Cause Analysis (RCA) Template (5 Whys + fishbone concepts)
#### A.1 RCA record metadata
| Field | Required content |
|---|---|
| Problem ID | ITSM Problem identifier |
| Related Incident IDs | Linked Incidents (include Major Incident reference if applicable) |
| Service | Impacted service name |
| Impacted Configuration Item (CI) | CI(s) and relationships |
| Service Owner | Name/role per ITSM assignment |
| Platform Owner | Name/role per domain |
| IT Operations Manager | Coordinator for operational execution |
| Dates | Start date, RCA completion date, closure date |
| Severity / Priority | As per ITSM prioritization model |
| Customer/Business impact | Operational impact, downtime, OT impact if any, financial/SOX considerations |

#### A.2 Event timeline (minimum)
| Timestamp (UTC or local standard) | Event | Source evidence reference | Notes |
|---|---|---|---|
|  | Detection/alert | Monitoring/SIEM/EDR event ID |  |
|  | Incident opened | ITSM Incident ID |  |
|  | Mitigation | Command/runbook reference |  |
|  | Recovery | Validation evidence |  |
|  | Recurrence (if applicable) | Incident IDs |  |

#### A.3 Symptoms and scope
- Observable symptoms:
- Affected users/sites/regions:
- Affected OT/plant zones (if applicable):
- What was not affected (boundary):

#### A.4 5 Whys analysis (required)
| Why # | Question: “Why did this happen?” | Answer (fact-based) | Evidence reference |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

#### A.5 Fishbone categories (required coverage)
Document contributing factors under each category (use only applicable categories, but explicitly confirm review of each):

| Category | Findings (causes/contributors) | Evidence |
|---|---|---|
| People |  |  |
| Process |  |  |
| Technology |  |  |
| Environment |  |  |
| Suppliers/Third Parties |  |  |
| Measurement/Monitoring |  |  |

#### A.6 Root cause statement (required)
- Root cause (single sentence, testable):
- Contributing factors:
- Control gap(s) identified (preventive/detective):

#### A.7 Workaround (if applicable)
| Item | Description |
|---|---|
| Workaround summary |  |
| Preconditions and safety constraints | Include OT remote access constraints and approval requirements |
| Step-by-step actions | Reference runbooks/commands |
| Risk of workaround | Security/availability impacts |
| When to stop using workaround | Criteria |

#### A.8 Corrective action plan
| Action ID | Action type (Tech/Process/Monitoring/Security) | Description | Owner role | Change record required (Y/N) | Target date | Validation method |
|---|---|---|---|---|---|---|
| CA-1 |  |  |  |  |  |  |
| CA-2 |  |  |  |  |  |  |

#### A.9 Validation and effectiveness
| Validation check | Expected result | Evidence reference | Outcome (Pass/Fail) |
|---|---|---|---|
| Service health restored | SLO targets met | Monitoring dashboard link/reference |  |
| No recurrence | Zero linked Incidents over monitoring period | ITSM report |  |
| Detection improved | Alert triggers earlier with lower false positives | SIEM/monitoring change record |  |

#### A.10 Closure approvals
| Approval | Required approver role | Date | Evidence |
|---|---|---|---|
| RCA reviewed | Service Owner |  | ITSM approval/log |
| Corrective actions validated | Platform Owner |  | Test/validation artifacts |
| Operational readiness confirmed | IT Operations Manager |  | Runbook/monitoring updates |
| Governance evidence complete | IT Governance Manager |  | Evidence checklist (Appendix D) |

---

### Appendix B: Known Error Record Template (KEDB)
#### B.1 Known Error metadata
| Field | Required content |
|---|---|
| Known Error ID | ITSM Known Error identifier |
| Linked Problem ID | Parent Problem |
| Linked Incident IDs | Historical Incidents and any open Incidents |
| Service | Impacted service |
| Impacted Configuration Item (CI) | CI(s) and relationships |
| Status | Draft / Approved / Retired |
| Owner role | Service Owner (accountable), Platform Owner (technical) |
| Last reviewed date | Date of last verification |

#### B.2 Description
- Title (symptom-focused):
- Symptoms / error messages:
- Conditions when it occurs:
- Impact:
- Detection signals (alerts/log patterns):

#### B.3 Workaround (required for operational use)
| Step | Action | Notes / constraints |
|---:|---|---|
| 1 |  | Include approvals, PAM requirements, OT access constraints |
| 2 |  |  |

Workaround validation:
- How to confirm workaround success:
- When to escalate:
- When not to use workaround:

#### B.4 Permanent resolution
| Item | Description |
|---|---|
| Root cause summary | From RCA (link to Appendix A record) |
| Planned fix | Technical and/or process change |
| Change records | Linked Change IDs and CAB outcomes |
| Target implementation window | Maintenance window reference |
| Retirement criteria | e.g., fix deployed globally + no recurrence over monitoring period |

#### B.5 Communications
- Service Desk guidance:
- Stakeholder communications summary:
- Customer-facing notes (if applicable):

---

### Appendix C: Trend analysis metrics and thresholds
Trend analysis is required to identify systemic issues and trigger Problems proactively.

#### C.1 Minimum trend metrics
| Metric | Definition | Measurement source | Minimum review cadence | Primary owner role |
|---|---|---|---|---|
| Repeat Incident rate | Count of Incidents with same symptom/CI/service over period | ITSM reporting | Weekly | IT Operations Manager |
| Top recurring services | Services with highest repeat incidents | ITSM reporting | Weekly | Service Owner |
| Major Incident drivers | Top root cause categories for Major Incidents | ITSM + RCA summaries | Monthly | ITSM Process Owner |
| Time to RCA completion | Days from Problem open to RCA completed | ITSM timestamps | Monthly | IT Governance Manager |
| Time to permanent fix | Days from RCA completed to fix validated | ITSM + Change records | Monthly | Platform Owner |
| KEDB utilization | Incidents resolved using Known Error workaround | ITSM linkage | Monthly | Service Desk Manager (where applicable) / IT Operations Manager |
| Monitoring gaps | Incidents detected by users vs monitoring | ITSM incident source fields | Monthly | Platform Owner |
| Vulnerability-linked Problems | Problems created from vuln/control findings | Vulnerability tool + ITSM | Monthly | Security Engineer |

#### C.2 Trigger thresholds (minimum)
A Problem record must be created when any threshold is met:
| Trigger | Threshold |
|---|---|
| Recurring Incidents | ≥ 3 similar Incidents impacting the same service/CI within 14 calendar days |
| High-impact repeat | ≥ 2 Incidents causing production downtime, OT disruption, or SLO breach within 30 calendar days |
| Monitoring deficiency | Any Major Incident where detection originated from end-user report rather than monitoring/alerting |
| Security control failure | Any repeat security alert pattern indicating control weakness, or any vulnerability repeatedly re-detected after remediation window |
| Capacity risk | Sustained resource utilization trend that projects exhaustion within 60 days for critical services |

---

### Appendix D: Audit-ready evidence list (Problem Management)
This checklist defines the minimum evidence artifacts that must be available for audit and assurance activities.

#### D.1 Evidence principles (mandatory)
Evidence must be **time-bound, attributable, and repeatable**, and include approvals, logs, and validation artifacts where applicable.

#### D.2 Evidence checklist
| Evidence item | Description | Source system | Required for |
|---|---|---|---|
| Problem record | Complete Problem fields, ownership, priority, timestamps | ITSM tool | All Problems |
| Incident linkage | Associated Incident IDs and timelines | ITSM tool | All Problems triggered by Incidents |
| CI linkage | Impacted Configuration Item (CI) references and relationships | ITSM/CMDB | All Problems |
| RCA document | Completed Appendix A template (or equivalent controlled format) | ITSM attachment/knowledge | Major/high-impact Problems |
| Log extracts | SIEM/EDR/network/cloud logs supporting cause | SIEM/EDR platforms | Evidence-backed RCA |
| Monitoring graphs | Performance/availability charts showing degradation and recovery | Monitoring platform | Availability-related Problems |
| Vulnerability scan evidence | Findings, re-scan results, remediation proof | Tenable/Nessus (or equivalent) | Security-related Problems |
| Corrective action tracking | Actions, owners, due dates, completion proof | ITSM tasking | All Problems with actions |
| Change records | Approved Change(s) and CAB outcomes | ITSM Change module | Production-impacting fixes |
| Test/validation results | Post-change verification, regression checks, success criteria | ITSM attachments / monitoring | Closure criteria |
| KEDB record | Known Error entry with workaround and resolution plan | ITSM KEDB | Problems with workaround/known error |
| Communications | Stakeholder notifications, service desk briefings (as applicable) | ITSM comms/logs | Major/high-impact Problems |
| Closure approval | Closure review/approval evidence | ITSM approvals | All closed Problems |
| Trend reports | Weekly/monthly trend metrics and actions | ITSM reporting | Process effectiveness |

#### D.3 Minimal closure checklist (runbook-style)
1. Problem has linked Incidents and impacted CIs.
2. RCA completed using 5 Whys and fishbone category review (or justified alternative) with evidence.
3. Corrective actions implemented via Change Enablement where required and validated.
4. Monitoring/alerting updated if detection gap identified.
5. KEDB updated/created if workaround exists or recurring pattern is likely.
6. Evidence artifacts attached and approvals captured in ITSM tool.
7. Post-closure monitoring period defined and completed (or documented ongoing monitoring plan).