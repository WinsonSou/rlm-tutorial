# Infrastructure Documentation & Knowledge Management Policy (Norfolk Industries)

## 1. Purpose
This policy defines mandatory requirements for creating, maintaining, governing, and evidencing infrastructure documentation and operational knowledge for Norfolk Industries. It ensures documentation is accurate, secure, discoverable, auditable, and usable to support 24×7 operations across North America, Europe, and APAC, aligned with the Information Security Management System (ISMS), ITIL 4, COBIT 2019, ISO/IEC 27001, ISO/IEC 22301, NIST CSF concepts, SOC 2 Trust Services Criteria, GDPR, and SOX.

## 2. Scope
### 2.1 In scope
This policy applies to all documentation used to design, operate, secure, recover, and support services owned by IT Infrastructure Services, including:
- Hybrid cloud services (Microsoft Azure primary; AWS secondary)
- On-prem data center platforms
- Identity services (Active Directory and Entra ID (Azure AD) on first mention; Entra ID thereafter)
- Endpoint management (Microsoft Intune and ConfigMgr where needed)
- Security tooling (SIEM, EDR, vulnerability scanning, PAM)
- Monitoring, logging, backup, recovery, and resilience documentation
- OT/IT integration documentation where IT Infrastructure Services enables connectivity and controlled remote access to Operational Technology (OT) environments
- ITIL-aligned service management processes and operational procedures captured in the ITSM tool knowledge base and associated repositories

### 2.2 Out of scope
- Product engineering documentation not used to operate IT infrastructure services
- Purely local team notes not relied upon for operational execution (these must not be treated as authoritative)
- OT vendor proprietary procedures that cannot be stored due to licensing restrictions (a controlled reference record must still exist with access constraints and location metadata)

## 3. Policy Statement
Norfolk Industries requires that all infrastructure services and platforms have current, accessible, and controlled documentation sufficient to:
- Operate and support services safely and consistently under normal and degraded conditions
- Execute incidents, changes, and recoveries within defined Service Level Objectives (SLO), Recovery Time Objectives (RTO), and Recovery Point Objectives (RPO)
- Demonstrate compliance and control effectiveness through time-bound, attributable, repeatable evidence
- Reduce single points of knowledge failure via standardization and review

Documentation is a controlled asset. It must be owned, reviewed on a defined cadence, protected according to sensitivity, linked to the Configuration Item (CI) inventory (CMDB), and maintained through governed procedures.

## 4. Governance and Accountability
### 4.1 Governance model
- Global IT Operations sets global documentation standards, tooling requirements, and minimum content requirements.
- Regional IT Operations executes documentation creation and upkeep for regional implementations, consistent with global standards.
- The Information Security Management System (ISMS) defines security and control obligations for documentation handling and retention.

### 4.2 Roles and responsibilities (policy-level)
The following roles (from the Norfolk Industries role catalog) are responsible as defined below.

| Area | Accountability / Responsibility |
|---|---|
| Policy ownership | IT Governance Manager (owns lifecycle, compliance tracking, audit coordination) |
| Policy approval | CIO (A), Head of IT Infrastructure Services (R) per RACI master |
| Documentation standards and templates | IT Governance Manager (R), ITSM Process Owner (C) |
| Service documentation completeness | Service Owner (R), Head of IT Infrastructure Services (A) |
| Platform documentation completeness | Platform Owner (R) |
| Operational runbooks and SOP library | IT Operations Manager (R), Service Owner (C) |
| Security content and access controls | CISO (C), Security Engineer (R for implementations) |
| Audit assessment | Internal Audit (A for evidence coordination per RACI master; performs independent assessment) |

### 4.3 RACI alignment (summary)
This policy aligns to the provided RACI master for: Policy approval, Standard approval, Procedure ownership, CAB chairing, and Audit evidence coordination. Where documentation changes require formal change, Change Enablement and the Change Advisory Board (CAB) apply per Change Management.

## 5. Definitions and Terminology
This document uses canonical Norfolk Industries terminology and the following glossary terms:
- IT Infrastructure Services
- Global IT Operations
- Regional IT Operations
- Information Security Management System (ISMS)
- Change Advisory Board (CAB)
- Configuration Item (CI)
- Operational Technology (OT) and Information Technology (IT)
- Service Level Objective (SLO)
- Recovery Point Objective (RPO)
- Recovery Time Objective (RTO)

## 6. Documentation Standards (Minimum Required Documentation)
### 6.1 Documentation types and minimum set
Each infrastructure service (as defined by a Service Owner) must maintain, at minimum, the following authoritative documentation set. Artifacts may be separate documents or a structured set within the knowledge base, but must meet content requirements and be version-controlled.

| Documentation Type | Minimum Required Content | Owner (Primary) | Required Linkage |
|---|---|---|---|
| Service Overview (Service Profile) | Purpose, customers, support hours, dependencies, SLOs, RTO/RPO where applicable, key contacts/rotations, escalation path | Service Owner | CMDB service CI; monitoring dashboards |
| Architecture & Design | Current-state architecture, logical and physical diagrams, network flows, trust boundaries, identity model, data flows | Platform Owner | CMDB CIs; diagram repository links |
| Operational Runbooks | Step-by-step operational procedures for common and critical tasks (start/stop, failover, restore, rotation, patching, access requests, certificate renewal) | IT Operations Manager | CMDB; change records; monitoring alerts |
| Standard Operating Procedures (SOP) Library | Repeatable SOPs for operational tasks; includes prerequisites, steps, validation, rollback | IT Operations Manager | Knowledge base category; related CIs |
| Security & Controls | Access control model, logging requirements, security monitoring, vulnerability management expectations, PAM usage, break-glass process references | CISO (C), Security Engineer (R for implementation), Service Owner (R for service adoption) | SIEM/EDR integration references; CMDB |
| Recovery & Continuity | Backup strategy, restore procedures, DR approach, RTO/RPO, recovery validation cadence, dependency recovery order | Service Owner (R) | ISO/IEC 22301 evidence; CMDB |
| Operations & Monitoring | Key metrics, alert thresholds, runbook mappings to alerts, on-call rotations, event triage | Platform Owner (R), IT Operations Manager (R) | Monitoring tool dashboards; SIEM |
| CMDB / CI Records | CI attributes, relationships, owner, lifecycle state, support group, criticality, location, environment | Platform Owner (R), Service Owner (R) | ITSM tool CMDB |
| Vendor / Supplier References (as applicable) | Support contracts, SLAs, support portals, escalation paths | Service Owner (R) | Supplier Management records |
| Known Error / Problem Records (as applicable) | Root cause, workaround, permanent fix, risk and change references | ITSM Process Owner (C), IT Operations Manager (R) | Incident/Problem records |

### 6.2 Naming conventions (mandatory)
All authoritative documents must follow a consistent naming scheme to support searchability and auditability.

**Format:**
`NI-ITS-[Domain]-[ServiceOrPlatform]-[DocType]-[Environment]-[Region]-vMajor.Minor`

**Rules:**
- `NI` = Norfolk Industries
- `ITS` = IT Infrastructure Services
- `Domain` examples: Cloud, Network, Endpoint, Identity, Security, Backup, Monitoring, Datacenter, OT-Access
- `DocType` examples: ServiceProfile, Architecture, Runbook, SOP, Recovery, Controls, DiagramPack
- `Environment` one of: Prod, NonProd, Shared
- `Region` one of: NA, EU, APAC, Global
- Versioning must use semantic major/minor increments:
  - **Major**: material process/architecture change or control impact
  - **Minor**: clarifications, non-material updates, formatting, contact updates

### 6.3 Ownership and approval standards
- Every document must have a single accountable owner (role + named individual) and an identified backup owner.
- Documents that define control requirements, access models, or recovery strategy must be reviewed by the CISO (consulted) and approved by the Service Owner.
- Documents that constitute operational procedures must be reviewed by IT Operations Manager and aligned with ITSM Process Owner guidance.

### 6.4 Review cadence (mandatory)
Minimum review intervals; teams may choose more frequent reviews based on criticality.

| Artifact | Minimum Review Cadence | Triggered Review Events |
|---|---:|---|
| Service Profile | Quarterly | Major incident, SLO change, ownership change |
| Runbooks / SOPs | Quarterly | Post-incident PIR actions, tooling change, platform upgrade |
| Architecture & Diagrams | Semi-annually | Network topology change, identity or trust boundary change |
| Recovery & Continuity | Semi-annually | DR test results, backup platform change, RTO/RPO change |
| Security & Controls | Semi-annually | Control change, audit finding, new threat intel affecting design |
| CMDB CI Attributes | Monthly validation for critical services; quarterly otherwise | CI lifecycle changes, onboarding/offboarding, migrations |

Review completion must be recorded with date, reviewer, and outcome, and retained as evidence.

## 7. Knowledge Management Repositories and Tooling
### 7.1 Authoritative repositories
Authoritative documentation must be stored in systems approved by Global IT Operations and governed by IT Infrastructure Services. Approved repository patterns:
- ITSM tool knowledge base for operational knowledge articles and SOPs used by Service Desk and operations
- Version-controlled document repository (with access controls and audit history) for architecture, diagrams, runbooks, and controlled templates
- CMDB within the ITSM tool for CI records and relationships

Documentation must not be considered authoritative if stored only in personal storage, email, chat threads, or unmanaged file shares.

### 7.2 Discoverability requirements
- Each service must have a single “Service Profile” entry that links to all related artifacts (runbooks, diagrams, recovery, controls, CMDB entries).
- Knowledge base articles must include tags for: Domain, Service/Platform, Region, Environment, and Document Type.
- Runbooks must be directly linked from monitoring alerts where feasible (alert-to-runbook mapping).

### 7.3 Access control and segregation
Documentation access must follow least privilege and align to the ISMS:
- Operational runbooks that enable privileged actions (e.g., break-glass, firewall rule changes, PAM procedures) must be restricted to authorized operational groups and audited.
- Documentation containing sensitive technical details (e.g., network diagrams for critical sites, identity trust diagrams, privileged account workflows) must be classified and protected with appropriate access controls.
- OT remote access documentation must enforce segmentation principles and must not expose plant-specific sensitive details beyond the authorized audience.

## 8. Documentation Security, Classification, and Handling
### 8.1 Security requirements
- Documentation must not include secrets (passwords, private keys, token values). Secrets must be stored only in approved secret management/PAM solutions.
- Where credentials are referenced, documentation must point to the approved access request and privileged access workflow.
- All repositories must maintain access logs and version history.

### 8.2 Data protection and privacy
- Documentation must avoid inclusion of personal data unless strictly necessary; if included, it must align with GDPR requirements and be minimized.
- Incident and audit documentation must be handled per retention and confidentiality rules defined by the ISMS.

## 9. CMDB and Configuration Item (CI) Linkage Requirements
### 9.1 Mandatory linkages
For each service/platform:
- The Service Profile must link to the service CI in the CMDB.
- Architecture documents must reference the relevant CIs (subscriptions/accounts, networks, firewalls, endpoints, servers, identity components).
- Runbooks must reference the impacted CIs and include CI identifiers where applicable.
- Monitoring dashboards and alert rules must reference service/platform identifiers consistent with CMDB naming.

### 9.2 CMDB minimum attributes for critical infrastructure services
For CIs supporting critical services, the following attributes are mandatory and must be accurate:
- CI name and type
- Owner (Service Owner/Platform Owner)
- Support group (Regional IT Operations or Global IT Operations as applicable)
- Environment (Prod/NonProd/Shared)
- Region and location (where applicable)
- Criticality tier
- Upstream/downstream relationships (dependencies)
- Monitoring status and dashboard link
- Backup coverage and recovery classification (where applicable)

## 10. Operational SOP Library and Runbook Requirements
### 10.1 SOP library structure (mandatory)
The SOP library must be organized by:
- Domain (Cloud, Network, Endpoint, Identity, Security, Monitoring, Backup, Datacenter, OT-Access)
- Service/Platform
- Procedure type (Routine Ops, Incident Response Support, Maintenance, Recovery)
- Region, where regional variance exists

### 10.2 Runbook minimum content
Every runbook must include:
- Purpose and scope
- Preconditions and required access (including PAM workflow references)
- Step-by-step procedure with validation checkpoints
- Rollback/backout procedure
- Expected timing and operational impact
- References to monitoring alerts/events that should invoke the runbook
- Related CIs and dependencies
- Safety and OT considerations where applicable (explicit callout if OT-impacted)

### 10.3 Diagrams (mandatory requirements)
Architecture and operational diagrams must:
- Use standard notation consistently within the service domain (logical, physical, and data flow as appropriate)
- Identify trust boundaries and management planes for cloud/on-prem connectivity
- Include region and environment context
- Be reviewed on the same cadence as architecture documentation
- Be stored as source + export formats where feasible to support updates and auditability

## 11. Procedures: Document Lifecycle Management
### 11.1 Create new documentation
Documentation creation is required when:
- A new service/platform is introduced
- A material change impacts operations, security controls, monitoring, or recovery
- A recurring incident indicates missing or ineffective procedures
- Audit findings require documentation remediation

**Procedure (minimum steps):**
1. Assign owner and backup owner (Service Owner or Platform Owner depending on artifact type).
2. Select the correct template (Appendix A/B) and apply naming convention.
3. Draft content including CMDB linkage and operational impacts.
4. Peer review:
   - Operations review by IT Operations Manager (for runbooks/SOPs)
   - Security review by CISO (consulted) for control-affecting content
5. Publish to authoritative repository and link from Service Profile.
6. Record publication metadata (owner, version, date, reviewers).
7. Validate discoverability (search/tags) and alert-to-runbook mapping where applicable.

### 11.2 Update documentation
Documentation must be updated:
- Before or concurrently with implementing a change that alters the documented procedure/architecture, or immediately after where sequencing requires deployment first
- After major incidents as part of post-incident improvement actions

Updates must:
- Increment version (major/minor)
- Include a change summary
- Preserve prior versions for audit traceability
- Update CMDB relationships if impacted

### 11.3 Review cycle execution
At each review:
- Validate technical accuracy against current implementation and CMDB
- Validate monitoring links and operational steps
- Validate access control model and security control statements remain accurate
- Confirm contacts/on-call paths are correct
- Record review evidence (Appendix E)

### 11.4 Deprecate and archive documentation
Documentation must be deprecated when:
- A service/platform is retired or replaced
- A procedure is superseded by a new standard process
- The document is no longer used operationally

Deprecation requirements:
- Mark the document status as “Deprecated” and identify the replacement reference (if any)
- Update Service Profile links to point to the replacement and remove deprecated operational references
- Retain deprecated documents per retention requirements (Section 12) with access controls intact
- Ensure CMDB lifecycle states reflect retirement and relationships are updated

### 11.5 Emergency updates
Emergency updates are permitted when operational safety or service restoration requires immediate corrections (e.g., during major incident response).
- Emergency updates must be published with an “Emergency Update” label and include:
  - Incident reference
  - Approver (IT Operations Manager minimum)
  - Time of update and validation steps performed
- A follow-up review must occur within 5 business days to normalize formatting, completeness, and required approvals.
- If the emergency update reflects a change to production behavior requiring formal change, it must be retrospectively aligned to Change Enablement and, where applicable, reviewed by the Change Advisory Board (CAB).

## 12. Retention, Records Management, and Evidence
### 12.1 Retention requirements
Documentation must be retained in accordance with Norfolk Industries record retention and audit obligations. Minimum retention rules for infrastructure documentation evidence:
- Current authoritative version: retained for active lifecycle
- Prior versions and review records: retained to support auditability and control testing
- Incident-related emergency updates and recovery records: retained to support service continuity and audit needs

Retention implementation must ensure:
- Version history is preserved
- Access logs are available
- Evidence is time-bound, attributable, and repeatable per standards.json evidence principles

### 12.2 Evidence principles (mandatory)
Evidence produced from this policy must be:
- Time-bound (date/time captured)
- Attributable (who performed/reviewed/approved)
- Repeatable (process can be re-executed with consistent outcomes)
- Inclusive of approvals, logs, and validation artifacts where applicable

## 13. Compliance Monitoring and Metrics
Global IT Operations and the IT Governance Manager will monitor compliance using defined metrics and periodic sampling.

### 13.1 Required KPIs
| KPI | Definition | Target |
|---|---|---|
| Documentation coverage | % of services with complete minimum documentation set | ≥ 95% |
| Review compliance | % of documents reviewed within required cadence | ≥ 95% |
| Runbook effectiveness | % of priority incidents with a linked and usable runbook | ≥ 90% |
| CMDB linkage compliance | % of documents with valid CI references | ≥ 95% |
| Post-incident doc updates | % of major incidents resulting in doc improvements within 10 business days | ≥ 90% |

### 13.2 Corrective actions
Non-compliance triggers:
- Action plan owned by the relevant Service Owner/Platform Owner
- Tracking by IT Governance Manager
- Escalation to Head of IT Infrastructure Services for sustained non-compliance
- Audit engagement as required

## 14. Exceptions
Exceptions must be risk-assessed and formally approved.
- Low-risk exceptions: approved by Head of IT Infrastructure Services (responsible) with CISO consulted.
- High-risk exceptions: follow “Exception approval (high risk)” RACI (CIO A; Head of IT Infrastructure Services R; CISO R; IT Governance Manager C).

Exceptions must include:
- Scope and duration
- Compensating controls
- Residual risk statement
- Expiration date and review schedule
- Evidence of approval and communication to affected Regional IT Operations teams

## 15. Policy Violations and Enforcement
Violations include (non-exhaustive):
- Operating production services using undocumented or unapproved procedures where documentation is required
- Storing secrets in documentation repositories
- Failure to review documentation within defined cadence without an approved exception
- Publishing sensitive diagrams or privileged workflows without appropriate access controls

Enforcement actions may include access restrictions, mandatory remediation, and escalation through management channels aligned to ISMS governance and HR processes where applicable.

## 16. Related Policies, Standards, and Procedures
### 16.1 Related internal governance
- Information Security Management System (ISMS) policies and standards
- Change Enablement procedures and Change Advisory Board (CAB) governance
- Incident Management, Problem Management, Service Configuration Management (CMDB), Monitoring and Event Management, Service Continuity Management (ITIL 4 practices)
- Access management and privileged access management standards (CyberArk or equivalent)
- Vulnerability management and patching standards

### 16.2 External alignment (control mapping overview)
This policy supports:
- ISO/IEC 27001 (Annex A control areas conceptually; documentation as controlled information and operational procedures)
- ISO/IEC 22301 (service continuity documentation and recovery procedures)
- NIST CSF (Identify/Protect/Detect/Respond/Recover knowledge artifacts)
- SOC 2 (Security, Availability, Confidentiality, Processing Integrity where applicable, Privacy where documentation includes personal data)
- COBIT 2019 (EDM/APO/BAI/DSS/MEA governance and operational controls)

## 17. Audit and Assurance
### 17.1 Audit readiness
IT Governance Manager coordinates audit evidence for IT Infrastructure Services, including:
- Documentation inventories and coverage reports
- Review logs and approvals
- Version histories for critical runbooks and architecture documents
- CMDB linkage reports
- Access control evidence for restricted documentation sets

Internal Audit independently assesses design and operating effectiveness and may sample services across regions.

### 17.2 Evidence collection expectations
Evidence must include (where applicable):
- Knowledge base publication and revision history
- Peer review/approval records
- CAB references when documentation changes reflect governed changes
- Incident references for emergency updates
- CMDB screenshots/exports demonstrating CI linkage and relationships

## 18. Version Control and Change History
### 18.1 Version control requirements
- This policy and all controlled documentation must maintain version history.
- Major changes to this policy require approval per RACI master: CIO (A), Head of IT Infrastructure Services (R), CISO (C), IT Governance Manager (R).

### 18.2 Document control record
| Field | Value |
|---|---|
| Document title | Infrastructure Documentation & Knowledge Management Policy (Norfolk Industries) |
| Policy owner | IT Governance Manager |
| Executive accountable | Head of IT Infrastructure Services |
| Approved by | CIO |
| Consulted | CISO, ITSM Process Owner |
| Applies to | IT Infrastructure Services; Global IT Operations; Regional IT Operations |

## 19. Appendices (Templates, Checklists, Runbooks, Evidence)
## Appendix A: Infrastructure Document Template (Standard)
### A.1 Header metadata (required)
| Field | Required Content |
|---|---|
| Document ID | Must follow naming convention in Section 6.2 |
| Document type | ServiceProfile / Architecture / Runbook / SOP / Recovery / Controls / DiagramPack |
| Service/Platform | Name of service/platform |
| Domain | Cloud / Network / Endpoint / Identity / Security / Backup / Monitoring / Datacenter / OT-Access |
| Environment | Prod / NonProd / Shared |
| Region | NA / EU / APAC / Global |
| Owner | Role + named individual |
| Backup owner | Role + named individual |
| Review cadence | Per Section 6.4 |
| Last reviewed | Date + reviewer |
| Next review due | Date |
| Classification | Per ISMS classification scheme; include access restrictions |
| CMDB linkage | Service CI ID and related CIs |

### A.2 Standard sections (required)
- Purpose and scope
- Dependencies and upstream/downstream relationships (include CI references)
- Operational considerations (support hours, on-call, maintenance windows)
- Monitoring and event handling (dashboards, alert routing)
- Security and access (no secrets; reference PAM workflows)
- Change impacts (what changes require doc updates)
- Validation steps (how to confirm correct operation)
- References (related docs, KB articles, change records, incident records)

## Appendix B: Runbook Template (Operational)
### B.1 Runbook metadata (required)
| Field | Required Content |
|---|---|
| Runbook ID | Must follow naming convention in Section 6.2 |
| Trigger | Alerts/events/incidents that initiate this runbook |
| Impacted services/CIs | CMDB CI IDs and names |
| Required access | Role-based access; PAM workflow references |
| Estimated duration | Typical time to complete |
| Risk level | Low / Medium / High (per operational assessment) |

### B.2 Runbook body (required)
#### B.2.1 Objective
- Clear outcome (e.g., “Restore authentication for Entra ID-integrated application access”)

#### B.2.2 Preconditions and safety checks
- Confirm incident/change ticket reference
- Confirm maintenance window if required
- Confirm OT impact assessment if network path touches OT segments

#### B.2.3 Step-by-step procedure (with validation)
| Step | Action | Validation / Expected Result | Evidence to Capture |
|---:|---|---|---|
| 1 | Identify impacted CI(s) and region | CI matches CMDB; correct environment | Ticket link; CI reference |
| 2 | Execute action | System responds as expected | Command/log excerpt or screenshot reference |
| 3 | Validate service health | Monitoring returns to green; error rates drop | Dashboard link/screenshot |
| 4 | Communicate status | Updates in ITSM tool | Timestamped comms |

#### B.2.4 Rollback/backout
- Explicit reversal steps
- Conditions that require rollback
- Escalation path if rollback fails

#### B.2.5 Post-action tasks
- Confirm alerts cleared
- Update incident/change record with actions and timestamps
- Record any follow-up documentation changes needed

## Appendix C: Diagram Standards Checklist
### C.1 Diagram minimum requirements
- Includes title, document ID, version, date, owner
- Identifies environment (Prod/NonProd/Shared) and region (NA/EU/APAC/Global)
- Shows trust boundaries and management plane separation where applicable
- Shows critical dependencies and connectivity paths (including on-prem to cloud)
- Includes OT segmentation boundaries for OT-Access diagrams
- Stored with source file and export (e.g., editable + PDF/PNG)
- Linked from Service Profile and associated CMDB CIs

### C.2 Diagram quality gates (reviewer checklist)
| Check | Pass Criteria |
|---|---|
| Accuracy | Matches implemented topology and CMDB relationships |
| Completeness | Includes key components, flows, and dependencies |
| Security | Trust boundaries shown; no secrets embedded |
| Readability | Legible labels, consistent notation, clear scope |
| Currency | Last reviewed within required cadence |

## Appendix D: Documentation Review Checklist (Quarterly/Semi-annual)
| Item | Review Action | Evidence |
|---|---|---|
| Ownership | Owner and backup owner still valid | Document header + org roster reference |
| CMDB linkage | CI IDs valid; relationships current | CMDB export/screenshot |
| Operational accuracy | Steps align to current tooling and access model | Peer review notes |
| Monitoring mapping | Alerts link to correct runbooks; dashboards correct | Dashboard links; alert configuration excerpt |
| Security handling | No secrets; access restrictions correct | Repository ACL report; spot check |
| Recovery alignment | RTO/RPO accurate; restore steps tested/validated | DR/restore test record |
| Regional variance | NA/EU/APAC differences documented where applicable | Section notes; region review sign-off |
| Versioning | Major/minor increment appropriate; change summary present | Version history |

## Appendix E: Evidence List (Audit-Ready)
### E.1 Required evidence artifacts
| Evidence Category | Examples | Evidence Principles Alignment |
|---|---|---|
| Document inventory | Export/list of Service Profiles and linked artifacts | Time-bound (dated report) |
| Review records | Reviewer names, dates, outcomes, tracked actions | Attributable, time-bound |
| Version history | Repository commit history or document revision log | Repeatable, attributable |
| Approvals | Workflow approvals for controlled docs; CAB references where required | Attributable, includes approvals |
| CMDB linkage | CI exports/screenshots showing relationships and owners | Repeatable (re-runnable report) |
| Access control | Repository permission reports; access logs for restricted docs | Attributable; security evidence |
| Incident linkage | Emergency update records tied to incident tickets | Time-bound; attributable |
| Recovery validation | Restore test results, DR exercise records, lessons learned and updates | Time-bound; repeatable |

### E.2 Evidence collection cadence
- Monthly: CMDB linkage and critical CI attribute validation extracts
- Quarterly: Documentation review completion reports and runbook effectiveness sampling
- Semi-annually: Architecture/diagram and recovery documentation review attestations
- On-demand: Audit sampling packages prepared by IT Governance Manager in coordination with Service Owners and Platform Owners