# Configuration Management Policy (Norfolk Industries)

## 1. Purpose
This Configuration Management Policy establishes the requirements for managing Configuration Items (CIs) and maintaining an accurate Configuration Management Database (CMDB) to support reliable, secure, and auditable delivery of services across Norfolk Industries. The policy ensures that IT Infrastructure Services can:
- Maintain trusted records of infrastructure and service components and their relationships.
- Enable effective Change Enablement, Incident Management, Problem Management, monitoring, vulnerability management, and service continuity activities.
- Meet governance and compliance obligations under the Information Security Management System (ISMS), SOX, GDPR, SOC 2, and aligned frameworks (ISO/IEC 27001, ISO/IEC 22301, ITIL 4, COBIT 2019, NIST CSF concepts, and NIST SP 800-53 concepts).

## 2. Scope
### 2.1 In scope
This policy applies to:
- Norfolk Industries IT services and supporting components managed by IT Infrastructure Services, Global IT Operations, and Regional IT Operations.
- Hybrid cloud environments (Microsoft Azure primary, AWS secondary), on-prem data centers, and enterprise endpoints.
- Identity platforms (Active Directory and Entra ID (Azure AD), then Entra ID).
- Security and operational tooling (SIEM, EDR, vulnerability scanning, PAM).
- Network infrastructure, compute, storage, backup, monitoring, middleware where operated by IT Infrastructure Services.
- OT/IT integration points and any IT-managed components enabling Operational Technology (OT) connectivity (without requiring detailed OT asset inventory beyond agreed integration boundaries and remote access controls).

### 2.2 Out of scope
- Pure OT asset inventories managed exclusively by plant engineering teams, except where an OT asset is a dependency of an IT-managed service or where remote access controls require CI representation for governance.
- Non-IT corporate asset registries (unless integrated as an authoritative source).

## 3. Policy statement
Norfolk Industries shall maintain a CMDB that is accurate, current, and fit for operational and compliance purposes. All in-scope services and infrastructure components must be represented as CIs with defined attributes and relationships. CMDB updates shall be controlled, traceable, and auditable, with priority given to automation via authorized discovery and integration sources. Data quality shall be measured and enforced through reconciliation rules, periodic audits, and exception management.

## 4. Objectives
- Establish a standardized CMDB data model, including CI classes, mandatory attributes, and relationship types.
- Ensure CMDB integrity through defined data quality rules, reconciliation, baselining, and audit practices.
- Support ITIL-aligned practices including Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, and Service Continuity Management.
- Provide control evidence that is time-bound, attributable, and repeatable.

## 5. Definitions
The following canonical terms apply (see Glossary):
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Operational Technology (OT)** and **Information Technology (IT)** apply as defined in the Glossary.
- **Service Level Objective (SLO)**, **Recovery Point Objective (RPO)**, **Recovery Time Objective (RTO)** apply as defined in the Glossary.

## 6. Roles and responsibilities
### 6.1 Policy governance roles
- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes.
- **CISO**: Accountable for information security program and ISMS oversight.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for a defined infrastructure service.
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain.
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- **ITSM Process Owner**: Owns ITIL-aligned process design (Change/Incident/Problem/CMDB) and continual improvement.
- **Internal Audit**: Independently assesses control design and operating effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment.

### 6.2 RACI (policy-level)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 7. CMDB governance and operating model
### 7.1 Authoritative sources and system of record
- The ITSM tool CMDB is the **system of record** for CI identification, classification, and relationship mapping used by IT processes.
- **Authoritative sources** (examples) may include:
  - Cloud control planes (Azure Resource Graph, AWS APIs).
  - Endpoint management (Microsoft Intune, ConfigMgr where needed).
  - Identity sources (Active Directory, Entra ID).
  - Vulnerability scanning platforms (Tenable/Nessus).
  - EDR inventory (Microsoft Defender for Endpoint).
  - Network management systems (for network devices and topology).
- Authoritative sources must be documented per integration, including field mappings, update frequency, and reconciliation precedence.

### 7.2 Data stewardship
- **Service Owner** is accountable for CI completeness and relationship accuracy for their service models.
- **Platform Owner** is accountable for class standards, attribute requirements, discovery coverage, and technical correctness for platform CIs.
- **IT Operations Manager** ensures operational processes create/update CIs as part of run activities (incidents, requests, changes).
- **ITSM Process Owner** maintains CMDB process design, CI class governance, and data quality measurement approach.

### 7.3 Access control and segregation of duties
- CMDB write access shall be role-based and aligned to least privilege.
- Direct manual edits to CI records are restricted to authorized roles and must be logged with attributable user identity.
- Bulk updates and integrations require change control and validation evidence (including rollback plan where feasible).

## 8. CMDB data model standard
### 8.1 CI classes (minimum required)
Norfolk Industries shall use a standardized CI class model sufficient to represent services, infrastructure, and dependencies.

| CI Class (required) | Description | Examples |
|---|---|---|
| Business Service | Customer-facing or business-aligned service representation | “Corporate Email Service”, “ERP Hosting Service” |
| Technical Service | Enabling IT service component | “Azure Landing Zone”, “VPN Remote Access” |
| Application | Deployed application or platform layer | Web app, middleware, packaged apps |
| Cloud Resource | Cloud-native resource | Azure VM, Azure SQL, AWS EC2, S3 bucket |
| Server / Compute | On-prem or IaaS compute | Physical server, VM |
| Network Device | Managed network infrastructure | Router, switch, firewall, load balancer |
| Database | Logical database instance | SQL instance, managed DB |
| Storage | Logical storage construct | SAN volume, cloud disk |
| Endpoint | User or shared device | Windows laptop, kiosk, mobile |
| Identity Object | Managed identity component | Privileged account record, service principal (represented as CI when used for service operation) |
| Security Tooling Component | Security platform element | EDR sensor group, SIEM connector |
| Facility / Location | Logical location construct | Data center room, plant site (as needed for dependency mapping) |
| Documentation / Artifact | Controlled reference used in operations | Runbook, architecture diagram (versioned link as CI) |

### 8.2 Relationship model (required relationship types)
Relationships must be recorded using consistent semantics to enable impact analysis and control evidence.

| Relationship type | Direction | Usage |
|---|---|---|
| **Depends on** | Service/Application → Component | Primary service-to-infrastructure mapping |
| **Runs on / Hosted on** | Application → Server/Cloud Resource | Workload placement |
| **Connects to** | Component ↔ Component | Network or integration dependency |
| **Managed by** | CI → Team/Role (represented via assignment fields) | Operational accountability (not a CI-to-CI relationship) |
| **Backed up by** | CI → Backup capability CI | Backup and restore traceability |
| **Monitored by** | CI → Monitoring capability CI | Observability coverage |
| **Secured by** | CI → Security control component CI | EDR/SIEM/PAM coverage |
| **Located at** | CI → Facility/Location | Physical/logical location |

### 8.3 Mandatory CI attributes (minimum baseline)
All in-scope CIs must include the mandatory attributes below, implemented as CMDB fields.

| Attribute | Requirement |
|---|---|
| CI Name | Unique, human-readable; follows naming standard by class |
| CI Class | Must be one of the approved classes |
| Unique Identifier | System-generated CMDB identifier; external identifiers stored where applicable |
| Environment | Production / Non-Production (and approved subcategories if implemented) |
| Service Owner | Named Service Owner accountable for service outcomes |
| Platform Owner | Named Platform Owner accountable for platform standards |
| Operational Assignment Group | Team responsible for day-to-day support (Global IT Operations or Regional IT Operations group as applicable) |
| Region | North America / Europe / APAC (and site where applicable) |
| Criticality | Business impact tier aligned to service continuity needs |
| Data Classification | Classification level required for handling and control selection |
| Lifecycle Status | Planned / In Service / Deprecated / Retired |
| Last Verified Date | Date of last successful verification (discovery/reconciliation/audit) |
| Source | Discovery / Integration / Manual (with integration name where applicable) |
| Change Reference | Link to change record for material updates (where change controlled) |

### 8.4 Class-specific mandatory attributes (minimum)
In addition to baseline attributes, the following class-specific attributes are mandatory:

| CI Class | Mandatory attributes (in addition to baseline) |
|---|---|
| Business Service | SLO; RTO; RPO; primary support hours; customer/business unit |
| Technical Service | Supporting Business Service link; SLO; RTO; RPO |
| Cloud Resource | Subscription/account; resource group/project; cloud region; native resource ID; tags (owner, environment, classification) |
| Server / Compute | Hostname; OS; patch group; virtualization/hosting platform; IP address(es) |
| Network Device | Device type; management IP; firmware/OS; site; network zone |
| Endpoint | Device ID; OS; enrollment source (Intune/ConfigMgr); primary user or owning function |
| Database | Engine/type; version; hosting reference; backup policy reference |
| Identity Object | Identity type (service account, privileged account, app registration); owning service; PAM coverage indicator |
| Documentation / Artifact | Version; repository link; last review date; approver |

## 9. Data quality rules
### 9.1 Quality dimensions and thresholds
CMDB data quality shall be measured at least monthly and reviewed by the ITSM Process Owner with Global IT Operations.

| Dimension | Rule | Minimum threshold |
|---|---|---|
| Completeness | Mandatory attributes populated | ≥ 98% for Production CIs; ≥ 95% for Non-Production CIs |
| Accuracy | Values match authoritative sources after reconciliation | ≥ 97% for sampled CIs per class |
| Timeliness | Updates reflected within defined time window | Production: within 24 hours of discovery/integration cycle or approved change completion |
| Uniqueness | No duplicate CIs representing the same item | ≤ 0.5% duplicates per class |
| Relationship integrity | Required relationships exist for critical services | ≥ 95% of Production Business Services have “Depends on” mapping to key components |

### 9.2 Naming and tagging rules
- CI names must conform to class naming standards defined by Platform Owners and governed by the ITSM Process Owner.
- Cloud resources must include standardized tags aligning to mandatory CMDB attributes (owner, environment, classification, service mapping) to support automated enrichment and reconciliation.
- Inconsistencies between tags and CMDB records must be resolved using reconciliation precedence rules.

### 9.3 Data retention and lifecycle
- Retired CIs must be retained in the CMDB for auditability and traceability for a period aligned with Norfolk Industries record retention requirements and SOX needs.
- Relationship history for CIs supporting financial reporting systems shall be retained to demonstrate control operation during audit periods.

## 10. Discovery, reconciliation, audits, and baselining
### 10.1 Discovery tooling concepts
Norfolk Industries uses automated discovery and integrations to populate and validate CIs. Discovery shall:
- Run on a defined schedule appropriate to the CI class (e.g., endpoints daily, cloud resources multiple times per day, network devices daily/weekly depending on stability).
- Minimize production impact (rate limiting, approved credentials, segmented access for OT/IT boundaries).
- Use secure credential management and, where applicable, PAM-controlled credential checkout.

### 10.2 Reconciliation principles
Reconciliation is the process of matching and merging CI records from multiple sources to maintain a single trusted CI record.
- Each CI class must have defined **match keys** (for example: cloud native resource ID; server hostname + domain; endpoint device ID; network device serial + management IP).
- **Source precedence** must be defined (for example: cloud control plane > CMDB manual > vulnerability scanner derived fields for cloud resources).
- Conflicts must generate a reconciliation exception record and be assigned to the Platform Owner’s operational group for resolution within defined timelines (see Section 12).

### 10.3 Audits
- **Quarterly CMDB audits** are mandatory for Production services and their supporting CIs.
- Audit scope must include:
  - Critical services (based on business criticality tier).
  - A statistically meaningful sample of non-critical CIs per class.
  - Relationship validation for dependency chains supporting Incident and Change impact analysis.
- Audit evidence must be stored per Section 18 and follow evidence principles: time-bound, attributable, repeatable.

### 10.4 Baselining
- Baselines are required for critical Business Services and key infrastructure platforms.
- Baselines include:
  - CI inventory snapshot (CIs and mandatory attributes).
  - Relationship snapshot (dependencies).
  - Control coverage snapshot (monitored by, backed up by, secured by relationships or equivalent evidence fields).
- Baseline changes must be linked to approved change records where material service impact exists and reviewed in the Change Advisory Board (CAB) when applicable.

## 11. Integration with ITIL practices and operational processes
### 11.1 Change Enablement
- All Normal and Emergency Changes that add, remove, or materially modify a CI must update the CMDB as part of the change implementation and validation steps.
- Change records must reference impacted CIs and relationship updates required.
- The Change Advisory Board (CAB) uses CMDB relationships for impact assessment.

### 11.2 Incident and Problem Management
- Incidents must reference affected CIs and services to support prioritization and trend analysis.
- Problems must reference root cause CIs and update known relationships or attribute corrections where CMDB inaccuracies contributed.

### 11.3 Monitoring and Event Management
- Monitoring coverage shall be represented via “Monitored by” relationships or equivalent fields so that alert routing and SLO reporting can be traced.

### 11.4 Information Security Management
- Security-relevant CIs must support linking to security tooling coverage (EDR, SIEM, vulnerability scanning, PAM) via attributes or relationships.
- CMDB outputs must be usable for control validation reporting within the ISMS.

### 11.5 Service Continuity Management
- Business Services must maintain RTO and RPO values and map to critical dependencies to support recovery planning and exercises aligned to ISO/IEC 22301.

## 12. Procedures (policy-mandated)
The procedures below are mandatory requirements; detailed work instructions may exist in the ITSM knowledge base and must not conflict with this policy.

### 12.1 CI creation procedure
1. **Trigger**: New service introduction, new infrastructure deployment, onboarding of a platform component, or discovery of previously unmanaged items.
2. **Classification**: Select correct CI class and environment.
3. **Mandatory attributes**: Populate baseline mandatory attributes and applicable class-specific attributes.
4. **Identifiers**: Record authoritative unique identifiers (cloud resource ID, serial number, device ID).
5. **Ownership assignment**: Assign Service Owner, Platform Owner, and Operational Assignment Group.
6. **Relationship mapping**:
   - For Business Services: create “Depends on” relationships to Technical Services and key components.
   - For hosted workloads: create “Runs on / Hosted on” relationships.
7. **Source recording**: Set Source to Discovery/Integration/Manual and specify integration name where applicable.
8. **Validation**: Confirm discovery coverage exists or create integration onboarding request.
9. **Change linkage**: If created due to a change, link the change record in Change Reference.
10. **Approval**: Where manual creation is performed for Production CIs, require review by the Platform Owner’s delegate per access controls.

### 12.2 CI update procedure
1. **Trigger**: Approved change completion, discovery delta, operational correction, or audit finding.
2. **Impact review**: Confirm relationships and dependent services affected.
3. **Attribute update**: Update fields; maintain audit history and Change Reference where applicable.
4. **Verification**: Validate against authoritative sources; update Last Verified Date.
5. **Notification**: For critical services, notify Service Owner when dependency changes materially alter impact paths.

### 12.3 Relationship mapping procedure (minimum)
1. Identify the Business Service and confirm Service Owner accountability.
2. Map Technical Services that enable the Business Service.
3. Map “Depends on” relationships to critical components:
   - Identity dependencies (Active Directory, Entra ID components where applicable).
   - Network and remote access components for user connectivity.
   - Compute/cloud resources hosting the application.
   - Monitoring, backup, and security coverage components.
4. Validate relationships using discovery outputs, architecture diagrams (as Documentation / Artifact CIs), and operational runbooks.
5. Record relationship verification date as part of the audit cycle.

### 12.4 Quarterly CMDB audit procedure (required)
1. **Plan**: ITSM Process Owner publishes quarterly audit schedule and sample plan by CI class and region.
2. **Extract**: Generate CMDB reports for:
   - Mandatory attribute completeness.
   - Duplicate candidates.
   - Relationship coverage for critical Business Services.
   - CI records not verified within the last quarter.
3. **Reconcile**: Compare sampled CIs to authoritative sources.
4. **Validate relationships**: Confirm dependency chains for selected critical services.
5. **Remediate**: Create tasks to correct attributes/relationships; link tasks to audit record.
6. **Certify**: Platform Owners and Service Owners attest completion for their scope.
7. **Evidence**: Store reports, attestations, and remediation logs as an evidence pack (see Appendix C).

### 12.5 Exception handling procedure
1. **Identify**: Record exception type (missing CI, incomplete attributes, conflicting sources, inability to discover due to segmentation).
2. **Risk assessment**: Service Owner and Platform Owner assess operational and security impact; involve CISO where security exposure exists.
3. **Approval**:
   - High-risk exceptions follow the “Exception approval (high risk)” RACI and are routed via the IT Governance Manager for approval by CIO (A), with Head of IT Infrastructure Services and CISO (R).
4. **Compensating controls**: Define interim controls (manual verification cadence, restricted changes, additional monitoring).
5. **Expiry**: All exceptions must have an expiry date and review cadence.
6. **Closure**: Close exception upon remediation; store evidence of remediation and verification.

## 13. Control requirements
### 13.1 Minimum control set
- CMDB shall support traceability of critical service dependencies and enable impact assessment for changes and incidents.
- Discovery/integration accounts must be secured, monitored, and governed (least privilege; credential protection).
- CMDB modifications must be logged and attributable.
- Data quality metrics must be tracked and reviewed, with corrective action for sustained threshold breaches.

### 13.2 OT/IT integration controls
- Plant networks remain segmented; discovery into OT environments must follow strict remote access controls and approved methods.
- Where OT/IT integration components exist (jump hosts, remote access gateways, firewalls), these must be represented as CIs with relationship mapping to dependent services and security controls.

## 14. Compliance, monitoring, and reporting
### 14.1 Compliance monitoring
The ITSM Process Owner and IT Governance Manager shall monitor:
- Attribute completeness and relationship integrity metrics.
- Audit completion rates and remediation aging.
- Reconciliation exception volumes and resolution times.
- Percentage of changes with correct CI linkage.

### 14.2 Reporting
Minimum reports (at least quarterly; more frequently for critical services):
- CMDB data quality dashboard by region and CI class.
- Critical service dependency coverage report.
- CI verification aging report (Last Verified Date).
- Reconciliation exception report with trend analysis.

## 15. Policy exceptions
- Exceptions must follow Section 12.5 and be recorded in an exception register managed by the IT Governance Manager.
- Exceptions impacting regulated systems, financial reporting scope, or personal data processing require review by the CISO and Data Protection Officer (DPO) as applicable.
- Exceptions must include compensating controls, expiry dates, and documented acceptance authority.

## 16. Enforcement
Non-compliance with this policy may result in:
- Mandatory remediation plans managed by the Head of IT Infrastructure Services.
- Restriction of change execution privileges for teams or integrations that repeatedly bypass CMDB requirements.
- Escalation to CIO for persistent or high-risk non-compliance.
- Increased audit scrutiny and control testing.

## 17. Review and maintenance
- The IT Governance Manager is responsible for policy lifecycle management.
- This policy shall be reviewed at least annually, and additionally upon:
  - Major ITSM tool or CMDB architecture changes.
  - Significant audit findings.
  - Material changes to regulatory or ISMS requirements.
- Revisions require approval per the RACI in Section 6.2.

## 18. Evidence and auditability
Evidence must be time-bound, attributable, and repeatable. Minimum evidence retained:
- CMDB data quality reports and dashboards (dated).
- Discovery run logs and integration schedules.
- Reconciliation rules (match keys, precedence) and exception logs.
- Quarterly audit packs (sampling, results, attestations, remediation).
- Change records demonstrating CI linkage and CMDB updates for material changes.
- Access control logs for CMDB write permissions and admin activities.

## 19. Standards and control mappings
### 19.1 Control mapping summary
| Framework | Mapping (conceptual) | CMDB/Configuration Management alignment |
|---|---|---|
| ISO/IEC 27001 | Annex A control areas (conceptual) | Asset/configuration governance, change control support, logging and accountability, supplier/integration oversight |
| ISO/IEC 22301 | BCMS concepts | Dependency mapping supports BIA assumptions, recovery planning, RTO/RPO traceability |
| ITIL 4 | Service Configuration Management; Change Enablement; Incident Management; Problem Management; Monitoring and Event Management; Information Security Management; Service Continuity Management | CMDB provides trusted service/component model for operational practices |
| COBIT 2019 | EDM/APO/BAI/DSS/MEA domains | Governance, build/implement controls, operational delivery, monitoring and assurance |
| NIST CSF | Identify/Protect/Detect/Respond/Recover | Asset inventory and dependency mapping as enabling capability across functions |
| SOC 2 | Security, Availability, Confidentiality, Processing Integrity, Privacy | Evidence of controlled operations, availability dependency management, and privacy-relevant asset traceability |
| GDPR | Privacy governance | Identifies systems processing personal data and supports accountability via ownership and classification |
| SOX | Financial controls | Supports completeness/accuracy of system inventories and controlled change traceability for in-scope systems |

### 19.2 Evidence principles (mandatory)
Norfolk Industries applies these evidence principles:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

---

## Appendix A: CI Field Dictionary (minimum baseline)
This dictionary defines required CMDB fields and validation rules for Norfolk Industries.

### A.1 Baseline fields (all CI classes)
| Field | Type | Required | Validation / rule |
|---|---:|---:|---|
| CI Name | Text | Yes | Unique within CI class and environment; naming standard enforced where supported |
| CI Class | Choice | Yes | Must match approved CI class list (Section 8.1) |
| CMDB Unique Identifier | System | Yes | System-generated; immutable |
| External Unique Identifier | Text | Conditional | Required when authoritative source provides stable ID (cloud native ID, serial, device ID) |
| Environment | Choice | Yes | Production or Non-Production (per approved values) |
| Region | Choice | Yes | North America, Europe, APAC; site allowed as child value where implemented |
| Service Owner | Reference | Yes | Must reference a named Service Owner role assignment |
| Platform Owner | Reference | Yes | Must reference a named Platform Owner role assignment |
| Operational Assignment Group | Reference | Yes | Must align to Global IT Operations or Regional IT Operations support groups |
| Criticality | Choice | Yes | Tiered impact rating; must be populated for Production |
| Data Classification | Choice | Yes | Must align to Norfolk Industries classification scheme used by ISMS |
| Lifecycle Status | Choice | Yes | Planned / In Service / Deprecated / Retired |
| Source | Choice | Yes | Discovery / Integration / Manual; integration name captured when not Manual |
| Last Verified Date | Date | Yes | Updated upon reconciliation, audit validation, or verified discovery |
| Change Reference | Reference | Conditional | Required for material production changes performed under Change Enablement |
| Description | Text | No | Must not contain secrets or credentials |

### A.2 Class-specific fields (minimum)
| CI Class | Fields | Required | Validation / rule |
|---|---|---:|---|
| Business Service | SLO; RTO; RPO; customer/business unit; primary support hours | Yes | RTO/RPO must be defined; SLO must be measurable |
| Technical Service | Supporting Business Service; SLO; RTO; RPO | Yes | Must link to at least one Business Service |
| Cloud Resource | Subscription/account; cloud region; native resource ID; tags (owner/env/classification/service) | Yes | Native resource ID required; tags must align to mandatory attributes |
| Server / Compute | Hostname; OS; IP(s); hosting platform | Yes | Hostname must match DNS naming conventions |
| Network Device | Device type; management IP; firmware/OS; network zone; site | Yes | Management IP must be valid IP format |
| Endpoint | Device ID; OS; enrollment source; primary user/owning function | Yes | Device ID must match endpoint management identifier |
| Database | Engine/type; version; hosting reference; backup policy reference | Yes | Must link to hosting CI and backup capability (relationship or field) |
| Identity Object | Identity type; owning service; PAM coverage indicator | Yes | Privileged identities must reflect PAM coverage and ownership |
| Documentation / Artifact | Version; repository link; last review date; approver | Yes | Repository link must be a controlled enterprise location; last review date within review cycle |

---

## Appendix B: Reconciliation Checklist (operational)
Use this checklist for onboarding and recurring validation of discovery/integration sources.

### B.1 Source onboarding checklist
- Confirm business justification and CI classes impacted.
- Identify authoritative source system and data owner.
- Define match keys per CI class (examples):
  - Cloud Resource: native resource ID.
  - Server / Compute: hostname + domain; serial when available.
  - Endpoint: device ID.
  - Network Device: serial + management IP.
- Define source precedence for conflicting fields (documented and approved by Platform Owner and ITSM Process Owner).
- Confirm update frequency and scheduling (include blackout considerations for plant connectivity and 24×7 operations).
- Validate credential storage and access method (least privilege; PAM controls where applicable).
- Define reconciliation actions: merge, update, flag exception, ignore (with rule justification).
- Test in non-production CMDB scope where feasible; capture test evidence.
- Obtain required approvals under Change Enablement for production integration.

### B.2 Recurring reconciliation run checklist (per cycle)
- Verify discovery job success and completion timestamp.
- Confirm record counts by CI class and compare to prior run (variance analysis).
- Run duplicate detection and match-key collision report.
- Review conflict report (field-level discrepancies):
  - Apply precedence rules automatically where safe.
  - Generate exceptions for manual review where required.
- Confirm updates applied include Change Reference where change-driven.
- Update Last Verified Date for successfully verified CIs.
- Produce reconciliation summary report and store per evidence requirements.

### B.3 Exception review checklist
- Validate whether exception is due to:
  - Missing tags/identifiers
  - Network segmentation/access restrictions (including OT boundaries)
  - Credential failure
  - Source data quality issue
  - CMDB class misclassification
- Assign to correct Platform Owner operational group.
- Set remediation due date based on criticality:
  - Production critical services: 10 business days
  - Other production: 20 business days
  - Non-production: 30 business days
- Escalate overdue exceptions to IT Operations Manager and ITSM Process Owner; high-risk to IT Governance Manager and CISO.

---

## Appendix C: Evidence Pack (CMDB and Configuration Management)
This appendix defines the minimum evidence pack contents to demonstrate policy compliance for audits (ISO/IEC 27001, SOC 2, SOX, GDPR accountability where applicable).

### C.1 Evidence pack contents (minimum)
| Evidence artifact | Description | Owner | Frequency |
|---|---|---|---|
| CMDB Data Quality Dashboard | Completeness, accuracy sample results, timeliness, duplicates, relationship integrity | ITSM Process Owner | Monthly; retained for audit period |
| Discovery Run Logs | Job execution logs and success/failure summaries | IT Operations Manager | Per run; summarized monthly |
| Reconciliation Rules Document | Match keys, precedence, merge rules, exception workflow | Platform Owner + ITSM Process Owner | Reviewed quarterly and upon changes |
| Reconciliation Exception Log | Exceptions with assignment, remediation actions, closure evidence | Platform Owner | Ongoing; reviewed monthly |
| Quarterly CMDB Audit Report | Scope, sample, findings, remediation plan, closure attestations | IT Governance Manager | Quarterly |
| Service Dependency Baselines | Snapshot of critical service CIs and relationships | Service Owner | Quarterly and after material changes |
| Change Records with CI Linkage | Evidence that changes referenced impacted CIs and CMDB updates completed | IT Operations Manager | Per change; sampled quarterly |
| Access Control Review | CMDB write/admin access review evidence | IT Governance Manager | Quarterly |
| Attestations | Service Owner and Platform Owner certification statements for their scope | Service Owner / Platform Owner | Quarterly |

### C.2 Evidence quality requirements (mandatory)
- Each artifact must include:
  - Date/time range covered
  - Owner/approver identity
  - System-generated reports or signed attestations where applicable
  - Traceability (links to CMDB records, change records, or reconciliation outputs)
- Evidence must be stored in approved enterprise repositories with access controls appropriate to the data classification.

### C.3 Quarterly attestation template (to be used as-is)
| Attestation item | Service Owner attests (Yes/No) | Platform Owner attests (Yes/No) | Notes / reference |
|---|---|---|---|
| Business Service records are complete and accurate |  |  | Link to audit report section |
| RTO and RPO values are present and reviewed |  |  | Link to continuity evidence |
| Dependency relationships are current for critical paths |  |  | Link to baseline snapshot |
| Discovery/reconciliation coverage is operating |  |  | Link to run logs |
| Exceptions are documented with compensating controls |  |  | Link to exception register |
| Remediation actions from prior quarter are closed or tracked |  |  | Link to remediation log |