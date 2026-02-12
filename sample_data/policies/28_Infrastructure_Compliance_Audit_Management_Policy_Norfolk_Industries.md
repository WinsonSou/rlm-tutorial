# Infrastructure Compliance & Audit Management Policy (Norfolk Industries)

## 1. Purpose
This policy establishes the minimum requirements for managing infrastructure compliance and audits across Norfolk Industries, ensuring consistent, repeatable, and evidence-based assurance of controls for IT Infrastructure Services. It defines how Norfolk Industries plans, supports, responds to, and remediates audits and compliance assessments while aligning to the Information Security Management System (ISMS), ITIL 4, COBIT 2019, NIST CSF concepts, SOC 2 Trust Services Criteria, GDPR, and SOX obligations.

## 2. Scope
### 2.1 In Scope
This policy applies to:
- IT Infrastructure Services across hybrid cloud (Microsoft Azure primary; AWS secondary), on-prem data centers, and supporting management platforms.
- Identity systems including Active Directory and Entra ID (Azure AD) on first mention, then Entra ID.
- Endpoint management (Microsoft Intune and ConfigMgr where needed).
- Security tooling and supporting platforms (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk).
- Monitoring, backup, and recovery services.
- Interconnected Operational Technology (OT) and Information Technology (IT) environments where IT Infrastructure Services provides connectivity, identity, remote access, or monitoring capabilities.

### 2.2 Out of Scope
- Product quality audits not related to IT Infrastructure Services.
- Purely OT-only controls that are fully owned and operated outside IT Infrastructure Services governance; however, where OT/IT integration exists, shared controls and evidence must be coordinated per this policy.

## 3. Policy Statements
Norfolk Industries will:
1. Maintain an audit-ready compliance posture for IT Infrastructure Services through continuous control operation, monitoring, and evidence capture.
2. Support audits through a defined audit lifecycle: intake, planning, evidence preparation, auditor request management, findings management, and closure verification.
3. Assign accountable control ownership for each control area and ensure evidence is time-bound, attributable, and repeatable.
4. Track remediation actions for audit findings through the ITIL-aligned ITSM tool and validate closure through documented testing and independent review where required.
5. Operate a risk-based audit calendar covering internal, external, customer SOC 2, and regulatory audits, including follow-up verification.
6. Ensure audit interactions do not materially increase operational risk to 24×7 operations, including OT environments; access for auditors must follow least privilege and approved remote access controls.
7. Retain audit evidence and communications in accordance with retention requirements and legal/regulatory obligations, including GDPR and SOX considerations.

## 4. Definitions (Canonical Terms)
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

## 5. Roles and Responsibilities
### 5.1 Role Expectations
All roles must cooperate with audits, provide accurate evidence, and meet defined timeframes. Evidence must follow Norfolk Industries evidence principles:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

### 5.2 RACI Alignment (Audit & Compliance Activities)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

### 5.3 Additional Responsibility Detail (Audit Context)
- **CIO**: Executive escalation for major audit outcomes impacting enterprise risk, SOX posture, or regulatory obligations.
- **Head of IT Infrastructure Services**: Overall accountable executive for audit readiness, resource allocation, and remediation delivery within IT Infrastructure Services.
- **CISO**: Ensures alignment to the ISMS, validates security control objectives, and coordinates with security assurance functions as needed.
- **IT Governance Manager**: Owns audit coordination for IT Infrastructure Services, audit calendar management, evidence quality checks, and audit communications governance.
- **Service Owner**: Accountable for service-level control operation and evidence production, including SLOs, continuity objectives (RTO/RPO), and supplier dependencies.
- **Platform Owner**: Accountable for technical control implementation standards and evidence at the platform level.
- **IT Operations Manager**: Ensures operational logs, shift execution artifacts, incident/problem records, and monitoring outputs are available and reliable.
- **ITSM Process Owner**: Ensures audit-supporting ITIL practices (Change Enablement, Incident Management, Problem Management, Service Configuration Management) are consistently executed and reportable.
- **Internal Audit**: Provides independent assessment and may validate remediation closure or test control operating effectiveness.

## 6. Compliance and Audit Types
Norfolk Industries supports the following audit/assessment types for IT Infrastructure Services.

### 6.1 Internal Audits
- Performed by **Internal Audit** or delegated assurance functions.
- Objective: assess design and operating effectiveness of controls against the ISMS, ITIL 4 practices, COBIT 2019 control expectations, and internal policy/standard requirements.
- Frequency: risk-based, with higher frequency for high-impact services and repeat findings.

### 6.2 External Audits
- Performed by independent audit firms (e.g., ISO/IEC 27001 surveillance/recertification support, SOC reporting support where applicable, and other third-party assurance).
- Objective: provide external assurance that control objectives are met and evidence supports claims.

### 6.3 Customer SOC 2 Support Audits (Customer-Requested Assurance)
- Customer or customer-appointed auditor requests for SOC 2 Trust Services Criteria mapping, evidence, and walkthroughs.
- Objective: demonstrate controls relevant to customer-facing services and shared infrastructure.
- Requirements:
  - Requests must be logged via the audit request intake process.
  - Evidence sharing must follow confidentiality and data minimization expectations and be reviewed for GDPR and contractual constraints.

### 6.4 Regulatory Audits and Examinations
- Includes regulatory requests relevant to Norfolk Industries operations (e.g., privacy regulators for GDPR, financial control reviews supporting SOX, and region-specific compliance reviews).
- Objective: demonstrate compliance with applicable laws/regulations and internal governance.
- Special handling:
  - Engage **Data Protection Officer (DPO)** for privacy-related audits.
  - Engage **CIO** and **CISO** for regulator communications where required.

## 7. Audit Governance and Audit Calendar
### 7.1 Audit Calendar Requirements
The **IT Governance Manager** will maintain an annual rolling 12-month audit calendar for IT Infrastructure Services that includes:
- Planned audit windows (fieldwork dates and evidence due dates)
- Scope and control domains affected (identity, cloud, network, endpoint, monitoring, backup, vulnerability management, PAM)
- Primary control owners (Service Owner and Platform Owner)
- Key dependencies (Global IT Operations and Regional IT Operations coordination)
- Follow-up validation dates for remediation closure

### 7.2 Risk-Based Prioritization
Audit planning must consider:
- Critical services supporting 24×7 operations
- OT/IT integration points and remote access pathways
- Material financial systems and SOX-relevant infrastructure dependencies
- Prior audit findings, repeat findings, and known control gaps
- Major platform changes reviewed by the Change Advisory Board (CAB)

### 7.3 Audit Engagement Governance
All audits impacting IT Infrastructure Services must have:
- A named **audit coordinator** (IT Governance Manager or delegate)
- An auditable scope statement and evidence request list
- Communications protocol (single source of truth, approved channels, meeting cadence)
- A defined evidence repository location with access control and logging

## 8. Control Ownership and Evidence Management
### 8.1 Control Ownership Model
- Every control in scope must have a **control owner** aligned to a **Service Owner** and/or **Platform Owner**.
- Operational evidence is typically produced by **Regional IT Operations** and governed by **Global IT Operations** standards.
- The **CISO** provides oversight for security control objectives under the ISMS; IT Infrastructure Services remains accountable for infrastructure control operation.

### 8.2 Evidence Collection Standards
Evidence must:
- Be time-bound (clearly indicate the period covered).
- Be attributable (owner, system, and approver identifiable).
- Be repeatable (another qualified person could reproduce the evidence following the documented procedure).
- Include approvals, logs, and validation artifacts where applicable (for example: CAB approvals, SIEM/EDR logs, vulnerability scan results, access reviews).

### 8.3 Evidence Repository and Access Control
- Evidence must be stored in an approved enterprise repository with access control and audit logging.
- Access must follow least privilege and be time-bound for auditors.
- Evidence containing personal data must be minimized and handled in alignment with GDPR and privacy governance. Coordinate with the **Data Protection Officer (DPO)** as required.

### 8.4 Evidence Quality Checks
The **IT Governance Manager** will perform quality checks before evidence submission to confirm:
- Completeness against request
- Correct timeframe
- Clear traceability to the control objective
- No unauthorized disclosure of sensitive data (credentials, secrets, personal data beyond necessity)

## 9. Audit Lifecycle Procedures (Mandatory)
### 9.1 Procedure: Prepare an Evidence Pack
**Objective:** Create a complete and consistent evidence pack prior to fieldwork.

**Steps:**
1. Confirm audit scope, period, and control domains with the auditor and Internal Audit (if applicable).
2. Create an evidence index using Appendix A.
3. Assign evidence items to control owners (Service Owner / Platform Owner) and evidence producers (Global IT Operations / Regional IT Operations).
4. Collect evidence artifacts for the audit period, ensuring each artifact includes:
   - System/source
   - Date/time range
   - Owner and approver where relevant
   - Linkage to control requirement
5. Validate evidence integrity:
   - Confirm logs are exported directly from authoritative tools (for example SIEM, EDR, vulnerability scanning platform, Entra ID sign-in logs, PAM reports).
   - Confirm change records include CAB approvals for Normal and Emergency Changes.
6. Store the evidence pack in the approved repository and apply access controls.
7. Conduct a pre-audit walkthrough with control owners to ensure they can explain:
   - Control intent
   - Procedure execution
   - Exceptions and how they were handled

**Minimum inclusions (as applicable to scope):**
- Change Enablement records (CAB agenda/minutes, approvals, implementation validation)
- Incident and Problem records demonstrating operational control
- Access control evidence (Entra ID access reviews, PAM session logs)
- Vulnerability scanning outputs and remediation tracking
- Backup and recovery evidence aligned to RPO/RTO where applicable
- Monitoring and alerting evidence (event rules, alert samples, response records)
- Asset and CI records from Service Configuration Management

### 9.2 Procedure: Respond to Auditor Requests (Request Management)
**Objective:** Ensure consistent, traceable responses to auditor requests with controlled communications.

**Steps:**
1. Log each auditor request in the audit request log (Appendix C form output) and link it to the audit engagement record in the ITSM tool where applicable.
2. Classify request type:
   - Evidence request
   - Walkthrough/interview
   - Sampling clarification
   - Exception inquiry
3. Assign an owner and due date. Owner must be a Service Owner or Platform Owner for control interpretation; evidence production can be delegated.
4. Validate the request for:
   - Scope alignment
   - Data sensitivity (GDPR, confidential, OT-sensitive details)
   - Least-privilege access needs
5. Provide response through approved channels, referencing the evidence index item ID and version.
6. Record what was provided, when, and by whom; retain communications as part of the evidence pack.

**Rules:**
- Do not provide direct system access to auditors unless approved by the **Head of IT Infrastructure Services** and **CISO**, and logged as a controlled access event with time-bound access.
- OT environment details must be shared on a need-to-know basis; remote access mechanisms remain subject to strict remote access controls.

### 9.3 Procedure: Manage Audit Findings (Remediation Tracking)
**Objective:** Ensure findings are triaged, owned, risk-assessed, remediated, and verified.

**Steps:**
1. Record each finding in the finding tracker (Appendix B) and in the ITSM tool as a tracked item (e.g., problem record, risk item, or remediation task), referencing the audit and finding ID.
2. Classify severity using Norfolk Industries risk governance (at minimum: Critical/High/Medium/Low) and identify impacted services and CIs.
3. Assign accountable remediation owner:
   - Service Owner for service-level control gaps
   - Platform Owner for technical implementation gaps
   - ITSM Process Owner for process gaps (Change Enablement, Incident Management, Service Configuration Management)
4. Define corrective action plan:
   - Root cause statement
   - Remediation steps
   - Compensating controls (if needed)
   - Milestones and target dates
5. Assess whether remediation requires a change:
   - If yes, follow Change Enablement and obtain CAB approval where required.
6. Provide status updates at agreed cadence (weekly for Critical/High; biweekly for Medium; monthly for Low unless otherwise required).

**Rules:**
- Repeat findings trigger an escalated review by the **Head of IT Infrastructure Services** and **IT Governance Manager** to address systemic issues.
- If a finding affects ISMS control objectives, coordinate with the **CISO** for risk acceptance or control redesign.

### 9.4 Procedure: Verify Closure (Closure and Validation)
**Objective:** Confirm remediation is implemented and operating effectively, with evidence.

**Steps:**
1. Define validation method (test of design, test of operating effectiveness, or both).
2. Collect closure evidence that demonstrates:
   - Remediation implemented (configuration screenshots/exports, policy/procedure updates, system logs)
   - Control operates over a defined period where applicable (for example: access review completion, vulnerability remediation cycle)
   - Approvals and change records (CAB evidence where relevant)
3. Obtain validation sign-off:
   - Remediation owner confirms implementation.
   - IT Governance Manager confirms evidence adequacy.
   - Internal Audit validates if required by audit terms or severity.
4. Update the finding tracker and ITSM record to “Closed” only after validation sign-off and evidence archival.
5. Schedule follow-up testing if the auditor requires a sustained period of operation.

## 10. Remediation, Exceptions, and Risk Acceptance
### 10.1 Remediation Requirements
- All findings must have an owner, due date, and measurable corrective action.
- Critical and High findings must include interim risk reduction steps where remediation cannot be immediate.

### 10.2 Exceptions
When immediate compliance cannot be achieved:
- Document an exception with scope, justification, duration, compensating controls, and risk assessment.
- High-risk exceptions require approval aligned to the RACI for **Exception approval (high risk)** (CIO accountable; Head of IT Infrastructure Services and CISO responsible).
- Exceptions must be time-bound and reviewed at least monthly until closure.

### 10.3 Risk Acceptance
Risk acceptance for audit-related control gaps must:
- Be documented with rationale and business impact.
- Include approving authority consistent with enterprise risk governance.
- Be retained as auditable evidence.

## 11. Data Protection, Confidentiality, and Legal Considerations
- Evidence sharing must adhere to confidentiality obligations and GDPR principles (data minimization, purpose limitation).
- Personal data must be redacted or minimized unless explicitly required by audit criteria.
- SOX-relevant evidence must be handled with heightened integrity controls and retention discipline.
- Requests involving customer data or contractual terms must be reviewed for confidentiality and approved sharing mechanisms.

## 12. OT/IT Considerations
- Audits involving OT-connected infrastructure must ensure no disruption to plant operations and must maintain network segmentation requirements.
- Evidence derived from OT environments must be collected via approved methods and reviewed to avoid exposing sensitive plant network details.
- Remote access evidence and controls (authentication, session recording where applicable, least privilege) must be included when OT access pathways are in scope.

## 13. Integration with ITIL 4 Practices and ITSM
Audit readiness and evidence will leverage ITIL-aligned records in the ITSM tool, including:
- **Change Enablement**: CAB records, change approvals, implementation validation, emergency change review.
- **Incident Management**: incident records, timelines, communications, post-incident reviews where applicable.
- **Problem Management**: root cause analysis, corrective actions, trend analysis.
- **Service Configuration Management**: CI inventories, relationships, and change traceability.
- **Monitoring and Event Management**: alert definitions, event logs, response evidence.
- **Service Continuity Management**: backup, restoration testing evidence, RTO/RPO alignment.

## 14. Metrics and Reporting
### 14.1 Required Metrics
The IT Governance Manager will report at least quarterly to the Head of IT Infrastructure Services on:
- Audit requests completed on time (%)
- Evidence rework rate (requests returned for clarification or insufficiency)
- Open findings by severity and age
- Mean time to remediate findings (by severity)
- Repeat finding count and root cause themes
- Coverage of planned audits vs executed (audit calendar adherence)

### 14.2 Operational Reviews
- Critical and High findings require executive visibility and regular review until closure.
- Metrics should be segmented by service/platform and region to support Regional IT Operations execution and accountability.

## 15. Training and Awareness
- Control owners (Service Owner, Platform Owner) must complete audit readiness and evidence handling training at least annually.
- Regional IT Operations personnel involved in evidence production must be trained on:
  - Evidence quality standards
  - Data handling and confidentiality
  - Auditor interaction protocol
- The ITSM Process Owner will ensure process documentation is maintained and accessible for audit walkthroughs.

## 16. Record Retention and Evidence Preservation
- Audit evidence, communications, and finding remediation artifacts must be retained in accordance with Norfolk Industries retention requirements and legal/regulatory obligations.
- Evidence must be immutable where feasible (versioned exports, signed approvals, system-generated logs).
- Evidence must be protected from unauthorized modification and must remain retrievable for re-performance.

## 17. Policy Exceptions and Enforcement
- Non-compliance with this policy may result in audit scope expansion, adverse audit outcomes, increased regulatory exposure, and disciplinary action consistent with Norfolk Industries governance.
- Exceptions must follow Section 10.2 and be approved at the required level.
- Repeated failure to produce adequate evidence or remediate findings will trigger escalation to the Head of IT Infrastructure Services and may require additional oversight from Internal Audit.

## 18. Standards and Control Mapping
This policy is governed by and maps conceptually to the following frameworks:
- **ISO/IEC 27001**: ISMS-aligned control areas; evidence supports control operation and auditability.
- **NIST CSF**: Identify, Protect, Detect, Respond, Recover functions supported through audit-ready control evidence.
- **SOC 2 Trust Services Criteria**: Security, Availability, Confidentiality, Processing Integrity, Privacy—evidence supports applicable criteria for customer assurance.
- **ITIL 4**: Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, Supplier Management, Service Continuity Management.
- **COBIT 2019**: EDM, APO, BAI, DSS, MEA domains, emphasizing governance, build/acquire/implement, delivery/support, and monitoring/assessment.
- **GDPR and SOX**: Data protection and financial control evidence handling, integrity, and retention.

### 18.1 Control-to-Evidence Mapping (Minimum Set)
| Control Domain | Example Evidence (Minimum) | Primary Owner Roles | Typical Systems/Sources |
|---|---|---|---|
| Identity & access management | Entra ID access review exports; privileged access approvals; PAM session logs | Service Owner, Platform Owner, IAM Engineer | Entra ID, Active Directory, CyberArk |
| Change Enablement | Change records with CAB approval; implementation validation; emergency change retrospective | ITSM Process Owner, IT Operations Manager, Service Owner | ITSM tool, CAB minutes |
| Vulnerability management | Scan reports; remediation tickets; exception approvals with compensating controls | Platform Owner, Security Engineer, Service Owner | Tenable/Nessus, ITSM tool |
| Security monitoring & detection | SIEM alert samples; use-case configuration; incident linkage | Security Engineer, IT Operations Manager | Microsoft Sentinel, EDR platform |
| Endpoint management | Compliance reports; patch deployment reports; configuration baselines | Platform Owner, Endpoint Engineer | Intune, ConfigMgr |
| Backup & recovery / continuity | Backup job reports; restoration test evidence; RTO/RPO alignment evidence | Service Owner, Systems Engineer, IT Operations Manager | Backup platform, ITSM tool |
| Configuration management | CI inventory exports; relationship mapping; reconciliation results | ITSM Process Owner, Platform Owner | CMDB, discovery tools |
| OT/IT remote access controls | Approved remote access records; authentication logs; session monitoring evidence | Service Owner, Platform Owner, Security Engineer | Remote access platform, PAM, SIEM |

## 19. Review, Approval, and Maintenance
- This policy is reviewed at least annually by the **IT Governance Manager** in coordination with the **Head of IT Infrastructure Services** and **CISO**.
- Material updates require approval per the RACI (Policy approval).
- Updates must be communicated to Global IT Operations and Regional IT Operations, and supporting procedures/templates must be version-controlled.
- Internal Audit feedback and post-audit lessons learned must be incorporated into continual improvement.

---

## Appendix A: Evidence Index Template (Evidence Pack)
### A.1 Evidence Index Table
| Evidence ID | Control Domain | Control Objective Summary | Evidence Description | System of Record | Period Covered (Start–End) | Owner Role | Approver Role (if applicable) | File/Link Reference | Sensitivity (Public/Internal/Confidential) | Provided to Auditor (Date) | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

### A.2 Evidence Packaging Checklist
- Evidence index completed and reviewed by IT Governance Manager
- Each artifact includes date/time or period covered
- Source system exports are authoritative (system-generated where possible)
- CAB approvals included for sampled changes (Normal/Emergency as applicable)
- Personal data minimized/redacted where not required (GDPR)
- Confidential data is access-controlled and shared via approved mechanism
- Evidence items mapped to audit request numbers and control objectives
- Walkthrough participants identified (Service Owner/Platform Owner present)

---

## Appendix B: Finding Tracker Template (Remediation Management)
### B.1 Finding Tracker Table
| Finding ID | Audit Type (Internal/External/Customer SOC 2/Regulatory) | Audit Name | Control Domain | Finding Description | Severity (Critical/High/Medium/Low) | Root Cause Category (People/Process/Technology/Supplier) | Business Impact Summary | Compensating Controls (if any) | Remediation Owner Role | Target Date | Milestones | Status (Open/In Progress/Ready for Validation/Closed) | Closure Evidence Reference | Validation Method | Validated By (Role) | Validation Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### B.2 Closure Verification Checklist
- Remediation implemented and linked to relevant CIs
- Required changes completed with CAB approval evidence (if applicable)
- Operating effectiveness demonstrated for an appropriate period (where applicable)
- Evidence is time-bound, attributable, repeatable
- Independent validation completed (Internal Audit if required)
- Auditor follow-up requirements satisfied (if applicable)

---

## Appendix C: Audit Request Intake Form (Auditor Request Management)
### C.1 Intake Form (to be logged per request)
| Field | Value |
|---|---|
| Audit Engagement Name |  |
| Audit Type (Internal/External/Customer SOC 2/Regulatory) |  |
| Request ID |  |
| Request Date |  |
| Requested By (Auditor/Organization) |  |
| Request Category (Evidence/Walkthrough/Sampling/Clarification/Exception Inquiry) |  |
| Scope Area (Identity/Cloud/Network/Endpoint/Monitoring/Backup/OT/Other) |  |
| Description of Request |  |
| Required Period / Date Range |  |
| Sensitivity Considerations (GDPR/Confidential/OT) |  |
| Assigned Owner Role |  |
| Evidence Producer Role(s) |  |
| Due Date |  |
| Delivery Method (Approved Channel) |  |
| Evidence Index ID(s) Linked |  |
| Response Date |  |
| Response Summary |  |
| Reviewed By (IT Governance Manager Role) |  |
| Notes / Constraints |  |

### C.2 Request Handling Checklist
- Request logged and assigned with due date
- Scope confirmed; out-of-scope requests escalated to IT Governance Manager
- Data sensitivity reviewed; DPO engaged for privacy concerns
- Evidence mapped to index and stored in repository
- Response delivered through approved channel; communications retained
- Request closed only after confirmation of auditor acceptance or documented follow-up plan