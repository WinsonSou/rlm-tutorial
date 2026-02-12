# Identity & Access Management Policy (Norfolk Industries)

## 1. Purpose
This policy defines how Norfolk Industries manages identity and access to Information Technology (IT) and Operational Technology (OT) systems to reduce risk, enable secure operations, and meet regulatory and contractual obligations. It establishes mandatory requirements for joiner/mover/leaver lifecycle controls, authentication, authorization, access governance, and evidence collection under the Information Security Management System (ISMS).

## 2. Scope
### 2.1 In scope
This policy applies to:
- All Norfolk Industries workforce members (employees, contractors, interns, temporary staff) and third parties with authorized access.
- All identities (human and non-human), including:
  - User accounts in Active Directory and Entra ID (Azure AD) (first mention), then Entra ID
  - Privileged accounts managed through PAM (e.g., CyberArk)
  - Service accounts, application identities, and automation identities
- All IT and OT environments, including:
  - Hybrid cloud (Microsoft Azure primary, AWS secondary)
  - On-prem data centers
  - Corporate endpoints managed by Microsoft Intune and ConfigMgr where needed
  - OT access paths (remote access into plant networks, SCADA, MES) with strict controls
- All services managed by IT Infrastructure Services and operated by Global IT Operations and Regional IT Operations.

### 2.2 Out of scope
- Physical access controls (handled under physical security policies), except where identity integrates with facility systems.
- Product embedded identity not connected to Norfolk Industries networks.

## 3. Policy statements (mandatory requirements)
1. Norfolk Industries shall use an authoritative HR source as the system of record for workforce identity status and core attributes used for provisioning, changes, and termination actions.
2. All access shall be granted based on least privilege and role-based access control (RBAC) using approved roles, groups, and entitlement catalogs where available.
3. All access requests shall be approved, recorded in the ITIL-aligned ITSM tool, and linked to a Configuration Item (CI) and service context.
4. Strong authentication shall be enforced using multi-factor authentication (MFA) for all remote access and for privileged or sensitive actions. Conditional access controls shall be applied to enforce risk-based access decisions.
5. Segregation of duties (SoD) shall be implemented for SOX-sensitive and high-risk functions; conflicting access shall be prevented or formally approved as an exception with compensating controls.
6. Joiner/mover/leaver lifecycle controls shall ensure timely provisioning, modification, and disablement of access based on HR-driven events and validated approvals.
7. Quarterly access recertification shall be performed for in-scope systems, with elevated frequency for privileged and SOX-sensitive access where required.
8. Privileged access shall be controlled through PAM with unique accounts, session controls where feasible, and audited activity.
9. Shared accounts are prohibited unless required by a technical constraint and explicitly approved as an exception with compensating controls and monitoring.
10. Evidence of control operation shall be time-bound, attributable, and repeatable, including approvals, logs, and validation artifacts where applicable.

## 4. Definitions
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.

## 5. Roles and responsibilities
### 5.1 Role accountability
The following roles from the Norfolk Industries role catalog have responsibilities within this policy:

- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes.
- **CISO**: Accountable for information security program and ISMS oversight.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for a defined infrastructure service.
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain (e.g., network, cloud, endpoint).
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- **IAM Engineer**: Implements and supports identity and access management controls and lifecycle.
- **Security Engineer**: Implements security tooling, detection, response integrations, and control validation.
- **ITSM Process Owner**: Owns ITIL-aligned process design (Change/Incident/Problem/CMDB) and continual improvement.
- **Internal Audit**: Independently assesses control design and operating effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment.

### 5.2 RACI (policy-level)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy governance
### 6.1 Ownership
- Policy Owner: **IT Governance Manager**
- Executive Sponsor: **Head of IT Infrastructure Services**
- Security Oversight: **CISO**

### 6.2 Review cycle
- This policy shall be reviewed at least annually and after material changes to identity platforms, authentication methods, or regulatory requirements.

### 6.3 Exceptions
- Exceptions shall be documented in the ITSM tool, include risk assessment and compensating controls, and require approval consistent with exception risk level.
- High-risk exceptions require approval by **CIO** (Accountable), **Head of IT Infrastructure Services** (Responsible), and **CISO** (Responsible).

## 7. Identity lifecycle management (Joiner/Mover/Leaver)
### 7.1 Authoritative HR source and identity attributes
1. The authoritative HR source shall drive:
   - Employment status (active, leave, terminated)
   - Start date and termination date/time (where available)
   - Manager assignment
   - Region/location and cost center/department
   - Worker type (employee/contractor)
2. Identity records in Active Directory and Entra ID shall be automatically or operationally reconciled to HR status at least daily.
3. Any manual identity creation must be associated with:
   - A validated business justification
   - The Service Owner’s approval for the target system
   - Post-creation reconciliation to HR attributes within one business day

### 7.2 Joiner process (new workforce member)
Minimum requirements:
- Provision unique user identity upon verified HR onboarding event.
- Assign baseline access via approved RBAC group(s) mapped to job function and region.
- Enforce authentication controls (MFA, conditional access) before granting remote or cloud access.
- Require completion of security awareness prerequisites where enforced by ISMS controls.

Operational requirements:
- Access is granted only through ITSM-recorded requests or automated HR-driven workflows with equivalent approvals and audit trails.
- Default access shall not include administrative privileges.

### 7.3 Mover process (role/location/manager changes)
Minimum requirements:
- HR-driven changes shall trigger an access review for impacted entitlements within five business days, or sooner for sensitive roles.
- Access no longer required shall be removed promptly based on updated RBAC mapping.
- For SOX-sensitive roles and privileged access:
  - Re-approval is required upon role change.
  - SoD checks must be re-evaluated.

### 7.4 Leaver process (termination and end of contract)
Minimum requirements:
- Accounts must be disabled based on HR termination status.
- For involuntary or high-risk termination:
  - Disablement shall be performed immediately upon notification from HR and/or management using established urgent processes.
- Access revocation shall include:
  - Entra ID sessions/tokens invalidation where supported
  - VPN/remote access revocation
  - PAM privileged access revocation
  - Disablement of secondary accounts and removal from privileged groups

Post-leaver requirements:
- Mailbox/data retention and legal hold actions shall follow retention and privacy governance under the ISMS and GDPR principles.
- Reassignment of owned resources (files, collaboration spaces) shall be controlled and approved by the manager and Service Owner as applicable.

## 8. Authentication standards
### 8.1 General requirements
1. All interactive user access shall use centralized identity (Active Directory and/or Entra ID) where technically feasible.
2. Single sign-on (SSO) shall be used for SaaS and federated applications to reduce credential proliferation.
3. Authentication events must be logged and retained per security logging standards integrated into the SIEM (e.g., Microsoft Sentinel).

### 8.2 Multi-factor authentication (MFA)
MFA is required for:
- All remote access to corporate resources
- All access to cloud management planes (Azure, AWS)
- All privileged access (administrative functions, PAM sessions)
- All access to systems processing SOX-relevant financial data where supported
- All access to OT remote access pathways and jump hosts

MFA methods:
- Norfolk Industries shall use phishing-resistant MFA methods where feasible (for example, FIDO2 or certificate-based methods).
- SMS-based MFA is not permitted for privileged access and should be avoided for standard access unless risk-accepted as an exception with compensating controls.

### 8.3 Password standards and passwordless
1. Passwordless authentication shall be implemented where feasible for high-risk populations (administrators, remote access users) and progressively expanded.
2. Where passwords remain in use:
   - Passwords shall comply with platform standards for length and complexity and be protected from reuse where technically supported.
   - Passwords must never be shared or stored in plain text.
3. Service accounts shall not use interactive logon and shall be vaulted and rotated through PAM or equivalent secure mechanism where supported.

### 8.4 Conditional access (risk-based access)
Conditional access controls shall be applied to enforce:
- Device compliance signals (managed devices via Intune/ConfigMgr where needed)
- Geographic and anomalous sign-in risk policies for Entra ID-based access
- Restrictions on legacy authentication protocols where possible
- Step-up authentication for sensitive actions
- Restrictions for OT access to approved jump hosts, managed devices, and approved networks

## 9. Authorization and access control
### 9.1 RBAC and group-based authorization
1. Access shall be assigned through RBAC using:
   - Entra ID groups and roles
   - Active Directory groups
   - Application roles mapped to centralized groups where supported
2. Direct user assignments should be minimized; group-based entitlements are the default.
3. RBAC definitions shall be maintained by the Service Owner with technical implementation by the Platform Owner/IAM Engineer, and reviewed during access recertification.

### 9.2 Least privilege and privileged access
1. Administrative access must be separate from standard user access via distinct privileged accounts where feasible.
2. Privileged access must be time-bound and justified for the task where supported (for example, just-in-time access).
3. Privileged sessions shall be monitored and auditable via PAM controls.

### 9.3 Segregation of duties (SoD) and SOX-sensitive access
1. SoD shall be enforced for SOX-relevant processes, including (where applicable):
   - Ability to create vendors and initiate payments
   - Ability to create users and assign financial roles
   - Ability to post and approve journal entries
2. Conflicting access combinations shall be blocked by design or managed through:
   - Documented exception approval
   - Compensating controls (enhanced logging, management review, dual approval)
   - Increased recertification frequency
3. SOX-sensitive access requires:
   - Manager approval and Service Owner approval
   - Quarterly recertification at minimum
   - Evidence retention suitable for audit

### 9.4 Third-party access
1. Third-party access must be sponsored by a Norfolk Industries manager and approved by the Service Owner.
2. Third-party identities shall be:
   - Uniquely attributable to an individual
   - Time-bound (end date required)
   - Reviewed at least quarterly
3. Remote access for third parties into OT environments must use approved secure remote access methods, MFA, and jump hosts; direct access to plant networks is prohibited unless approved as a high-risk exception.

## 10. Access request and provisioning procedures
### 10.1 Standard access requests
All access requests must be submitted in the ITSM tool and include:
- Requestor identity
- Target system/application and CI reference
- Requested RBAC role/group/entitlement
- Business justification
- Required start date and end date (mandatory for third parties and elevated access)

Approval chain (minimum):
- Requestor’s manager
- Service Owner (or delegated approver) for the target service
- Additional approval for sensitive access (SOX/privileged/OT), as defined by the Service Owner and CISO oversight

### 10.2 Provisioning execution
1. Provisioning shall be performed by IAM Engineer/Regional IT Operations per documented procedures.
2. Provisioning actions must be logged with:
   - Who performed the change
   - What was changed (group/role membership)
   - When it occurred
   - The ITSM request reference
3. Any provisioning that requires a production change to an integrated identity system must follow Change Enablement and, where applicable, CAB review.

### 10.3 Emergency access
1. Emergency access is permitted only to restore service or respond to incidents.
2. Emergency access must be:
   - Time-bound
   - Approved by the IT Operations Manager (operational approval) and Service Owner (service approval) as soon as practicable
   - Reviewed after-the-fact through Problem Management and, where required, CAB

## 11. Access reviews and recertification
### 11.1 Quarterly recertification (minimum baseline)
1. Service Owners shall conduct quarterly access recertification for:
   - Privileged groups and roles
   - SOX-sensitive applications and roles
   - Remote access/VPN and OT access pathways
2. Recertification shall validate:
   - User still active per HR status
   - User still requires access based on role
   - Access aligns with least privilege and SoD requirements
3. Outcomes must be recorded and include:
   - Approved (no change)
   - Remove access
   - Modify access (role change)
   - Exception required (with compensating controls)

### 11.2 Additional review triggers
Access must be reviewed upon:
- Role/department changes (mover events)
- Elevated privilege requests
- Security incidents involving identity compromise
- Material changes to RBAC models or application permissions

### 11.3 Evidence requirements
Recertification evidence must include:
- The population list (export) with timestamp
- Reviewer identity and approval decision
- Remediation tickets for removals/modifications
- Completion attestation by the Service Owner

## 12. Account disablement, deletion, and retention
1. Disabled accounts must not be re-enabled without:
   - Verified HR active status (or documented sponsorship for non-HR identities)
   - Re-approval of access in the ITSM tool
2. Account deletion shall follow retention needs and legal requirements:
   - Avoid immediate deletion where it would break audit trails
   - Follow GDPR principles for data minimization and retention limitation, coordinated with the Data Protection Officer (DPO)
3. Orphaned accounts (accounts without an owner or valid HR status) must be investigated and remediated within defined operational timeframes based on risk (privileged first).

## 13. Non-human identities (service accounts, application identities, automation)
1. Non-human identities must have:
   - A named Service Owner and technical owner (Platform Owner or delegate)
   - Documented purpose and scope
   - Credential storage in an approved vault (PAM or equivalent) where applicable
2. Credentials must be rotated:
   - On a defined schedule appropriate to risk
   - Immediately upon suspected compromise
3. Permissions must be least-privilege and scoped to required resources.
4. Service accounts must be prevented from interactive logon unless explicitly required and approved as an exception with compensating controls.

## 14. Logging, monitoring, and detection
1. Identity events shall be monitored, including:
   - Privileged role assignments
   - Authentication anomalies
   - Excessive failed logons
   - Conditional access failures
   - Changes to MFA methods
2. Logs shall be integrated with the SIEM (e.g., Microsoft Sentinel) and correlated with EDR (e.g., Microsoft Defender for Endpoint) where applicable.
3. High-risk alerts shall trigger Incident Management and be handled under the ISMS incident response processes.

## 15. OT-specific IAM requirements
1. OT access shall be provisioned through controlled pathways:
   - Approved remote access solution and jump hosts
   - MFA and conditional access controls
   - Network segmentation enforced between IT and OT
2. OT privileged access must:
   - Use PAM-controlled credentials where feasible
   - Be time-bound and logged
   - Be reviewed at least quarterly
3. Vendor access into OT environments must:
   - Be sponsored by a Norfolk Industries manager
   - Be time-limited with explicit maintenance windows
   - Be monitored and reviewed after completion

## 16. Compliance, audit, and enforcement
1. Non-compliance may result in access removal and disciplinary actions consistent with HR processes and contractual terms.
2. Internal Audit may test control design and operating effectiveness, including sampling of access requests, approvals, recertifications, and termination disablements.
3. The IT Governance Manager coordinates audit evidence collection, ensuring evidence is time-bound, attributable, and repeatable.

## 17. Metrics and reporting
Minimum metrics reported by IT Infrastructure Services to Global IT Operations and the CISO:
- Percentage of privileged accounts covered by MFA and PAM
- Quarterly recertification completion rate by Service Owner and system
- Time to disable accounts after termination (median and 95th percentile)
- Number of orphaned accounts detected and remediated
- Conditional access policy coverage for high-risk applications
- SoD violations detected and resolved (including exceptions)

## 18. Control mappings (standards alignment)
| Policy control area | ISO/IEC 27001 (conceptual Annex A alignment) | NIST CSF function | SOC 2 Trust Services Criteria | ITIL 4 practice | COBIT 2019 domain | Required evidence examples |
|---|---|---|---|---|---|---|
| HR-authoritative JML lifecycle | Access control; Identity management; HR security | Protect | Security, Availability | Information Security Management; Service Configuration Management | APO, DSS | HR status feed, provisioning logs, termination disablement report |
| MFA/SSO/Conditional access | Authentication information; Access control | Protect | Security | Information Security Management; Monitoring and Event Management | APO, DSS | Conditional access policies, MFA enforcement reports, sign-in logs |
| Privileged access management | Privileged access rights; Logging and monitoring | Protect/Detect | Security | Information Security Management; Monitoring and Event Management | DSS, MEA | PAM vault records, privileged role assignment logs, session audit trails |
| Access requests and approvals | Access provisioning; Change control | Protect | Security, Processing Integrity | Change Enablement; Incident Management | BAI, DSS | ITSM tickets, approval records, implementation logs |
| Quarterly recertification | Access review; Governance | Identify/Protect | Security, Confidentiality | Information Security Management | MEA, APO | Recertification attestations, access listings, remediation tickets |
| SoD for SOX-sensitive access | Risk management; Access restriction | Identify/Protect | Security, Processing Integrity | Information Security Management | EDM, APO, MEA | SoD rule set, exception approvals, management review evidence |
| OT remote access controls | Segregation; Secure access | Protect | Security, Availability | Information Security Management; Service Continuity Management | DSS | OT access lists, jump host logs, vendor access approvals |

Evidence principles applied:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

## 19. Document control
### 19.1 Version and approval record
| Item | Value |
|---|---|
| Document title | Identity & Access Management Policy (Norfolk Industries) |
| Policy owner | IT Governance Manager |
| Executive sponsor | Head of IT Infrastructure Services |
| Security oversight | CISO |
| Approved by | CIO |
| Effective date | 2025-12-26 |
| Next review date | 2026-12-26 |

### 19.2 Distribution
This policy is published within Norfolk Industries’ controlled policy repository and is binding for IT Infrastructure Services, Global IT Operations, Regional IT Operations, and all users and third parties accessing Norfolk Industries systems.

---

## Appendix A: Access request form (ITSM data requirements)
This appendix defines the required fields and approval logic for identity and access requests submitted through the ITIL-aligned ITSM tool.

### A.1 Standard access request fields
| Field | Requirement | Notes |
|---|---|---|
| Request type | Mandatory | Joiner / Mover / Leaver / Standard access / Privileged access / Third-party / OT remote access |
| Requestor | Mandatory | Person submitting request |
| Beneficiary (user) | Mandatory | Person receiving access |
| Beneficiary worker type | Mandatory | Employee / Contractor / Vendor |
| Manager | Mandatory | From HR where applicable |
| System/application name | Mandatory | Must map to a CI where managed |
| CI reference | Mandatory | Configuration Item (CI) identifier or linked service record |
| Requested entitlement | Mandatory | RBAC group/role name; avoid free-text permissions |
| Business justification | Mandatory | Must state purpose and scope |
| Access sensitivity | Mandatory | Standard / Privileged / SOX-sensitive / OT |
| Start date/time | Mandatory | Immediate allowed only when justified |
| End date/time | Mandatory for third-party and elevated | Required for time-bound access |
| Data classification context | Mandatory where applicable | Confidentiality impact informs approvals/controls |
| Approvers | System-enforced | Manager + Service Owner minimum; additional for sensitive |
| Implementation notes | Optional | Execution steps, if needed |
| Evidence attachments | Conditional | Screenshots/exports when automation not available |

### A.2 Approval rules (minimum)
| Access type | Required approvals | Additional conditions |
|---|---|---|
| Standard access | Manager + Service Owner (or delegate) | Must map to RBAC group |
| Privileged access | Manager + Service Owner + CISO delegate (as defined by ISMS process) | Must use PAM; separate privileged identity where feasible |
| SOX-sensitive access | Manager + Service Owner | SoD check required; quarterly recertification enforced |
| Third-party access | Sponsor manager + Service Owner | End date required; quarterly review |
| OT remote access | Sponsor manager + Service Owner + Security Engineer (control validation) | MFA + jump host + monitored session required |

---

## Appendix B: Quarterly access recertification checklist (Service Owner)
### B.1 Preparation
- Confirm system scope and CI reference are current in the CMDB/service records.
- Export current access lists for:
  - Privileged roles/groups
  - SOX-sensitive roles/groups
  - Remote access and OT access groups
- Obtain latest HR active workforce status feed (or authoritative report).

### B.2 Review steps
1. **Population integrity check**
   - Validate no duplicate identities.
   - Identify accounts without HR match (potential orphaned accounts).
2. **Least privilege validation**
   - Confirm each user’s role aligns to job function.
   - Remove unused elevated roles and redundant group memberships.
3. **SoD validation (SOX-sensitive)**
   - Check for conflicting roles.
   - If conflict exists: remove access or process approved exception with compensating controls.
4. **Third-party validation**
   - Confirm sponsor, end date, and current business need.
   - Remove access if sponsor no longer valid or end date passed.
5. **OT access validation**
   - Confirm access only via approved pathways (jump host/remote access).
   - Confirm access window and continued need.
6. **Action tracking**
   - Create remediation tickets for removals/changes.
   - Link remediation tickets to the recertification record.

### B.3 Completion and attestation
- Record final decision per user/role line item (approve/remove/modify/exception).
- Attach exports and decision logs to the recertification record in the ITSM tool.
- Provide completion attestation with name, role (Service Owner), and date.

---

## Appendix C: Operational procedures (minimum runbook requirements)
This appendix defines the minimum procedural steps required for consistent execution by IAM Engineer and Regional IT Operations.

### C.1 Account provisioning (joiner)
1. Validate HR onboarding event and start date.
2. Create/enable identity in Active Directory/Entra ID via approved workflow.
3. Assign baseline RBAC groups by job function and region.
4. Enforce MFA enrollment and conditional access readiness before granting remote/cloud access.
5. Validate mailbox/collaboration provisioning where applicable.
6. Record provisioning completion in ITSM ticket with timestamps and group/role assignments.

### C.2 Access modification (mover)
1. Validate HR change event (manager/department/location).
2. Identify entitlements impacted by RBAC mapping.
3. Remove no-longer-required groups/roles before adding new privileges where feasible.
4. Re-run SoD checks for SOX-sensitive access.
5. Document all changes in ITSM ticket and attach exports/log references.

### C.3 Account disablement (leaver)
1. Validate HR termination event (or urgent management request for high-risk cases).
2. Disable account in Active Directory and Entra ID; revoke sessions where supported.
3. Remove from privileged and remote access groups; revoke PAM entitlements.
4. Disable or rotate associated service credentials owned by the departing user (where applicable).
5. Document actions and completion time in ITSM ticket; notify Service Owner if any access cannot be removed due to technical dependency (initiate exception if required).

---

## Appendix D: Evidence list (audit-ready)
This appendix enumerates standard evidence artifacts Norfolk Industries maintains to demonstrate compliance.

| Control area | Evidence artifact | Evidence owner role | System/source |
|---|---|---|---|
| HR-authoritative lifecycle | HR status report/export; daily reconciliation job logs | IT Governance Manager (coordination), IAM Engineer (technical) | HR system export; identity platform logs |
| Joiner provisioning | ITSM request; approvals; group assignment log | IAM Engineer | ITSM tool; Entra ID/AD audit logs |
| Mover updates | ITSM request; change history of group/role membership | IAM Engineer | ITSM tool; Entra ID/AD logs |
| Leaver disablement | Termination ticket; disablement timestamps; remote access revocation | IT Operations Manager (operational), IAM Engineer (execution) | ITSM tool; Entra ID/AD logs; VPN logs; PAM logs |
| MFA enforcement | MFA registration status; conditional access policy reports; sign-in logs | Security Engineer | Entra ID; SIEM |
| Privileged access | PAM vault inventory; session logs; privileged role assignment changes | Security Engineer | PAM platform; SIEM |
| SoD controls (SOX) | SoD rule set; exception approvals; compensating control evidence | Service Owner (business), IT Governance Manager (coordination) | ITSM tool; access governance reports |
| Quarterly recertification | Access listings; decisions; remediation tickets; attestation | Service Owner | ITSM tool; system access exports |
| OT access governance | OT access list; jump host logs; vendor approvals and time windows | Service Owner (OT service), Security Engineer (monitoring) | Remote access/jump host logs; SIEM |

