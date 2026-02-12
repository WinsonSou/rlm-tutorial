# Third-Party & Vendor Infrastructure Access Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for third-party and vendor access to Norfolk Industries infrastructure and supporting platforms operated by **IT Infrastructure Services**. The policy ensures access is risk-based, time-bounded, monitored, auditable, and aligned to the **Information Security Management System (ISMS)**, enabling 24×7 operations while protecting Norfolk Industries information and services across North America, Europe, and APAC.

## 2. Scope
### 2.1 In Scope
This policy applies to:
- All third parties, vendors, suppliers, and service providers requiring logical access to Norfolk Industries infrastructure or administrative interfaces, including but not limited to:
  - Microsoft Azure (primary) and AWS (secondary) environments
  - On-prem data centers and enterprise networks
  - **Entra ID (Azure AD)** (first mention), Active Directory, and identity services
  - Endpoint management (Microsoft Intune and ConfigMgr where needed)
  - Security tooling (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk)
  - Monitoring, backup, and management planes
- Vendor access used for implementation, troubleshooting, maintenance, support, managed services, and incident response assistance.
- Vendor access requested by **Global IT Operations** and executed by **Regional IT Operations**.

### 2.2 Out of Scope
- Physical access to facilities (covered by physical security policies).
- Access limited to vendor-owned systems with no connectivity to Norfolk Industries networks.
- Access to business application functions (covered by application access governance); however, any infrastructure or administrative access used to support applications remains in scope.

## 3. Policy Statements (Requirements)
### 3.1 General Principles
1. Vendor access must follow least privilege, segregation of duties, and need-to-know.
2. Vendor access must be explicitly approved, time-bounded, and revoked when no longer needed.
3. All vendor access must be attributable to an individual (no shared accounts), unless a documented exception is approved under the ISMS exception process.
4. All vendor access must be logged, monitored, and reviewable for audit and security investigations.
5. Vendor access must be designed to minimize exposure to **Operational Technology (OT)** networks; OT access is permitted only through strictly controlled, segmented, and approved paths.

### 3.2 Vendor Onboarding and Due Diligence
1. Vendor onboarding must include a security due diligence review proportionate to the access level and data sensitivity, coordinated by the **IT Governance Manager** with input from the **CISO** and relevant **Service Owner**.
2. Due diligence must validate:
   - Security posture (e.g., SOC 2 reports, ISO/IEC 27001 certification, security questionnaire responses)
   - Incident notification commitments
   - Subprocessor/third-party dependency transparency
   - Data handling, retention, and secure disposal practices
   - Compliance requirements relevant to Norfolk Industries (GDPR, SOX where applicable)
3. Vendors must contractually commit to:
   - Confidentiality and permitted use
   - Security incident notification timelines and cooperation
   - Access control and MFA requirements
   - Logging and evidence support for audits
4. Vendors with elevated access (administrative, privileged, or production access) require documented approval from the **Service Owner** and **Head of IT Infrastructure Services**, and consultation with the **CISO**.

### 3.3 Access Scoping and Time-Bounded Access
1. Access must be scoped to:
   - Specific systems/services (**Configuration Items (CIs)**) and environments (production vs non-production)
   - Specific roles/permissions required
   - Specific network segments and management interfaces
2. Access must be time-bounded:
   - Default maximum duration is 30 days for operational support access.
   - Shorter durations should be used where practical (e.g., 8–72 hours for troubleshooting windows).
   - Extensions require re-approval and updated justification.
3. Standing or always-on vendor access is prohibited unless:
   - The service delivery model requires it (e.g., managed service)
   - Compensating controls are implemented (PAM, session recording, strict conditional access, continuous monitoring)
   - The **Service Owner** documents the rationale and risk acceptance under the ISMS exception process.

### 3.4 Remote Access Methods
Vendor remote access must use approved methods only:
1. **Privileged Access Management (PAM)** (e.g., CyberArk) is the preferred method for privileged sessions (server admin, network admin, cloud admin).
2. Approved remote access patterns include (as applicable):
   - Bastion/jump host with hardened configuration and restricted inbound access
   - VPN with device and identity controls, restricted to required segments
   - Just-in-time access workflows for cloud roles
   - Vendor support portals only when integrated with Norfolk Industries identity controls and logging requirements
3. Direct inbound connectivity to internal systems from the internet is prohibited unless explicitly approved and risk-assessed (e.g., tightly scoped IP allowlist, MFA, and logging).

### 3.5 Authentication and MFA Requirements
1. Multi-factor authentication (MFA) is mandatory for all vendor access.
2. Authentication must be integrated with Norfolk Industries identity controls where feasible:
   - Preferred: Entra ID guest/B2B with Conditional Access controls
   - Alternative: Federated identity from vendor with equivalent MFA assurance and documented validation
3. Privileged access must use strong authentication and be brokered by PAM where feasible.
4. Shared credentials are prohibited. If technical limitations require shared credentials, access must be:
   - Time-bounded and rotated after use
   - Stored and brokered via PAM
   - Approved as a documented exception under the ISMS exception process

### 3.6 Session Logging, Monitoring, and Alerting
1. Vendor administrative sessions must be logged and attributable to an individual user.
2. Privileged sessions must be recorded where supported (screen/command recording via PAM or equivalent).
3. Security monitoring must include:
   - Centralized log forwarding to the SIEM (e.g., Microsoft Sentinel) for cloud, identity, and critical infrastructure events
   - Alerting on anomalous vendor activity (e.g., unusual geolocation, excessive privilege use, repeated failures)
4. Logs for vendor access must be retained per Norfolk Industries log retention standards and be available for audit.

### 3.7 Data Handling and Protection
1. Vendor access must not be used to extract Norfolk Industries data unless explicitly approved and necessary for support.
2. When data access is required:
   - Scope to the minimum dataset necessary
   - Use secure transfer methods approved by Norfolk Industries
   - Apply encryption in transit and at rest
   - Prohibit storage of Norfolk Industries data on vendor endpoints unless contractually approved and protected by equivalent controls
3. Personal data processing must align with GDPR requirements and Norfolk Industries privacy governance, with consultation of the **Data Protection Officer (DPO)** where applicable.

### 3.8 OT/IT Integration and OT Remote Access
1. Vendor access to **Operational Technology (OT)** environments is restricted and must:
   - Use segmented access paths and strict remote access controls
   - Be approved by the relevant **Service Owner** and **Head of IT Infrastructure Services**, with consultation by the **CISO**
   - Be time-bounded and monitored with heightened logging and review
2. Remote access into OT networks must not bypass established segmentation, monitoring, or change governance.

### 3.9 Change and Incident Governance
1. Vendor activities that modify production infrastructure or security controls must follow Change Enablement and be governed by the **Change Advisory Board (CAB)** as applicable.
2. Vendor participation in incident response must follow Incident Management procedures and include evidence preservation and activity logging.

### 3.10 Access Reviews and Recertification
1. All vendor access must be reviewed at least quarterly by the **Service Owner** (or delegate) to confirm:
   - Access is still required
   - Scope remains appropriate
   - Accounts are active and correctly mapped to individuals
2. High-risk access (privileged, production, OT) must be reviewed monthly.
3. Immediate review is required following:
   - Vendor personnel changes impacting authorized users
   - Security incidents involving vendor accounts
   - Contract termination or scope reduction

### 3.11 Termination, Revocation, and Offboarding
1. Vendor access must be revoked:
   - At end of approved access period
   - Upon completion of work
   - Immediately upon suspected compromise or policy violation
   - Upon contract termination or loss of business need
2. Offboarding must include:
   - Account disablement/deletion in Entra ID/Active Directory
   - Revocation of VPN, PAM entitlements, cloud roles, and firewall allowlists
   - Collection of evidence that access has been removed
   - Confirmation that Norfolk Industries data is returned or securely destroyed per contractual terms

## 4. Roles and Responsibilities
| Role | Responsibilities (Policy Context) |
|---|---|
| CIO | Executive owner of IT strategy and governance; informed of material vendor access risks and exceptions. |
| Head of IT Infrastructure Services | Accountable for infrastructure standards and outcomes; approves high-impact vendor access models and chairs/ensures governance alignment as needed. |
| CISO | Oversees ISMS; consults/approves for high-risk vendor access decisions and control requirements; ensures monitoring and response expectations. |
| IT Governance Manager | Coordinates policy governance, due diligence tracking, evidence coordination, and audit support for vendor access controls. |
| Service Owner | Accountable for service risk posture; approves vendor access need, scope, and duration; ensures periodic reviews and revocation. |
| Platform Owner | Defines technical access patterns and standards (PAM, bastions, conditional access); ensures platform logging/monitoring capabilities. |
| IT Operations Manager | Ensures operational execution, 24×7 readiness, and incident coordination for vendor access monitoring and rapid revocation. |
| ITSM Process Owner | Ensures ITIL-aligned workflows (Change Enablement, Incident Management, CMDB) support this policy. |
| Internal Audit | Independently assesses control design and operating effectiveness, including evidence sampling. |
| Data Protection Officer (DPO) | Oversees privacy governance; consulted for vendor access involving personal data processing. |

## 5. Exceptions
1. Exceptions to this policy must be documented, risk-assessed, and approved according to the ISMS exception process.
2. High-risk exceptions (e.g., standing access, shared accounts, direct inbound access, OT production access) require approval by the **Head of IT Infrastructure Services** and the **CISO**; the **CIO** is accountable for exception approval in high-risk cases per governance.
3. Exceptions must include compensating controls, expiration date, and review cadence.

## 6. Enforcement
1. Non-compliance may result in immediate suspension of vendor access and escalation to the **Service Owner**, **Head of IT Infrastructure Services**, and **CISO**.
2. Vendors may be subject to contractual remedies for policy violations.
3. Repeated or material violations must trigger a security review and may require vendor reassessment or termination of access.

## 7. Definitions
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.

## 8. Access Control Requirements (Minimum Control Set)
### 8.1 Identity and Account Controls
- Vendor users must be uniquely identified and linked to a named individual.
- Access must be provisioned using role-based access control (RBAC).
- Joiner/mover/leaver events for vendor personnel must be communicated by the vendor promptly and acted on within operational targets defined by IT Infrastructure Services procedures.

### 8.2 Network and Connectivity Controls
- Restrict access to only required protocols, ports, and management endpoints.
- Enforce segmentation between IT and OT networks.
- Use allowlisting (source IP ranges, conditional access locations) where feasible.

### 8.3 Privileged Controls
- Privileged access must be brokered through PAM when feasible.
- Enforce just-in-time and just-enough-administration principles for privileged roles.

### 8.4 Monitoring Controls
- Ensure vendor authentication, privilege elevation, and administrative actions are logged and forwarded to the SIEM.
- Implement detections for suspicious vendor activity aligned to NIST CSF Detect/Respond objectives.

## 9. Procedure: Request Vendor Access
### 9.1 Initiation (ITSM Request)
1. Requestor (Norfolk Industries employee or approved contractor) submits a Vendor Infrastructure Access Request via the ITSM tool.
2. The request must include all required fields from Appendix A and attach supporting documentation (support case, statement of work, incident ticket reference, or change record).

### 9.2 Scope Definition
1. The **Service Owner** confirms:
   - Business justification
   - In-scope **CIs**, environment(s), and required privileges
   - Proposed start/end dates and working hours
2. The **Platform Owner** validates technical feasibility and selects the approved access method (PAM/bastion/VPN/JIT).

### 9.3 Due Diligence Trigger
1. The **IT Governance Manager** determines whether due diligence is required or whether existing vendor assurance remains valid based on:
   - Access sensitivity (production/privileged/OT)
   - Data exposure (personal data, regulated data)
   - Vendor risk tier and recency of assessment
2. If required, Appendix B must be completed and approved before provisioning.

## 10. Procedure: Approve Vendor Access
1. Approvals must be recorded in the ITSM tool and be attributable and time-bound.
2. Minimum approval requirements:
   - **Service Owner**: required for all vendor infrastructure access
   - **Platform Owner**: required for privileged access and for access involving platform administrative controls
   - **CISO** (consult/approve as applicable): required for high-risk access, OT access, standing access models, or exceptions
   - **Head of IT Infrastructure Services**: required for high-impact/high-risk access patterns (e.g., managed service standing access, production OT access)
3. If the work requires changes, an approved CAB-governed change record must exist prior to enabling production modification access (unless responding under Emergency Change procedures).

## 11. Procedure: Provision Vendor Access
1. **Regional IT Operations** (or designated implementer) provisions access using approved patterns:
   - Entra ID guest user with Conditional Access and MFA
   - VPN profile restricted to required segments
   - PAM onboarding with role entitlements and session recording
   - Bastion/jump host access with hardened baseline
2. Access must be configured with:
   - Start and end date enforcement where technically possible
   - Least privilege RBAC roles
   - Logging enabled (identity, platform, system logs)
3. The provisioning implementer must update:
   - The ITSM request with account identifiers, group/role assignments, and expiration date
   - Related **CIs** in the CMDB, where required by Service Configuration Management

## 12. Procedure: Monitor Vendor Access
1. **IT Operations Manager** ensures operational monitoring is in place for vendor access to critical services.
2. Monitoring must include:
   - SIEM alerting for authentication anomalies and privilege use
   - PAM session review for privileged tasks (spot checks and event-driven reviews)
   - Vulnerability and configuration monitoring impacts as appropriate
3. Security events involving vendor access must be handled via Incident Management, with coordinated actions between **Security Engineer**, **IT Operations Manager**, and the **Service Owner**.

## 13. Procedure: Revoke Vendor Access
1. Access must be revoked when:
   - End date is reached
   - Work is completed
   - Contract ends or need-to-know no longer applies
   - Suspicion of compromise arises
2. Revocation actions (as applicable):
   - Disable/delete Entra ID guest account and/or Active Directory account
   - Remove RBAC roles, group memberships, and subscriptions/projects access
   - Revoke VPN access and device certificates
   - Remove PAM entitlements and rotate any credentials used
   - Remove firewall rules/IP allowlists created for vendor access
3. Revocation must be documented in the ITSM ticket with evidence (screenshots/log extracts/change logs) per Appendix C.

## 14. Records and Evidence
1. Norfolk Industries must maintain evidence demonstrating compliance and operating effectiveness.
2. Evidence must be time-bound, attributable, and repeatable, and include approvals, logs, and validation artifacts where applicable.
3. Minimum record types:
   - ITSM access request and approvals
   - Due diligence artifacts and risk tiering
   - Provisioning details (accounts, roles, expiration)
   - Monitoring and session logs (PAM/SIEM)
   - Access reviews and recertification outcomes
   - Revocation confirmation

## 15. Metrics and Reporting
The following metrics must be tracked by **IT Governance Manager** and reported to **Head of IT Infrastructure Services** and **CISO** at an agreed cadence:
- Number of active vendor accounts by risk tier and platform
- Percentage of vendor access that is time-bounded with enforced expiration
- Quarterly access review completion rate; monthly completion rate for high-risk access
- Number of vendor access exceptions and aging
- Mean time to revoke access after end date or termination notice
- Security incidents or policy violations involving vendor access

## 16. RACI (Aligned to Master)
This section applies the Norfolk Industries RACI master to this policy’s core activities.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 17. Control Mapping (ISO/IEC 27001, NIST CSF, SOC 2, ITIL 4, COBIT 2019)
### 17.1 Control Objectives Covered
This policy supports the following control themes:
- Identity and access management for third parties
- Supplier security and assurance
- Logging, monitoring, and incident response readiness
- Change governance for vendor-performed activities
- Business continuity and recovery support through controlled vendor support access

### 17.2 Standards Mapping Table
| Policy Requirement Area | ISO/IEC 27001 (Annex A concept) | NIST CSF | SOC 2 TSC | ITIL 4 Practices | COBIT 2019 Domains | Evidence Examples |
|---|---|---|---|---|---|---|
| Vendor due diligence and onboarding | Supplier relationships, information security in supplier relationships | Identify, Protect | Security, Confidentiality, Privacy | Supplier Management, Information Security Management | APO, MEA | Completed due diligence checklist, SOC 2/ISO certificates, contract security clauses |
| Least privilege, scoped access | Access control, identity management | Protect | Security | Information Security Management, Service Configuration Management | APO, BAI, DSS | RBAC assignments, PAM entitlements, CMDB CI linkage |
| Time-bounded access and recertification | Access control, compliance | Protect, Identify | Security, Availability | Service Configuration Management | DSS, MEA | Access expiry settings, quarterly review attestations |
| MFA and secure remote access | Authentication information, secure log-on | Protect | Security | Information Security Management | APO, DSS | Conditional Access policies, VPN MFA logs |
| Logging, monitoring, session recording | Logging and monitoring | Detect, Respond | Security, Availability | Monitoring and Event Management, Incident Management | DSS, MEA | SIEM alerts, PAM session recordings metadata, audit log exports |
| Change governance for vendor changes | Change management, operational procedures | Protect, Respond | Security, Availability | Change Enablement | BAI, DSS | CAB approvals, change records linked to vendor activity |
| Revocation and offboarding | Access control, asset management | Protect | Security | Service Configuration Management | DSS | Deprovision logs, ticket closure evidence, role removal confirmation |

## 18. Review and Maintenance
1. This policy is owned by the **IT Governance Manager** under **IT Infrastructure Services** governance.
2. Review cadence:
   - At least annually
   - Upon significant changes to remote access tooling (PAM/VPN/bastion), identity platform changes, or major vendor risk events
3. Updates require approval per the RACI table and must be communicated to **Global IT Operations** and **Regional IT Operations** for execution alignment.

## 19. Appendices (Templates, Checklists, Evidence)
### Appendix A: Vendor Infrastructure Access Request Form (ITSM Template)
| Field | Required | Description |
|---|---:|---|
| Requestor name and department | Yes | Norfolk Industries requestor initiating vendor access. |
| Service Owner | Yes | Accountable owner for the impacted service. |
| Vendor company name | Yes | Legal vendor name. |
| Vendor individual user(s) | Yes | Full name, business email, and phone for each vendor user. |
| Vendor user identity type | Yes | Entra ID guest, federated identity, or other approved method. |
| Business justification | Yes | Support case reference, project milestone, incident reference, or maintenance need. |
| In-scope Configuration Items (CIs) | Yes | Systems, subscriptions, servers, network devices, tools; include CI identifiers where available. |
| Environment | Yes | Production, non-production, OT, or mixed (must specify). |
| Access level | Yes | Read-only, operator, administrator/privileged; include specific RBAC roles/groups requested. |
| Remote access method | Yes | PAM, bastion/jump host, VPN, JIT cloud role, other approved method. |
| Access window (start/end) | Yes | Date/time range and time zone; include working hours restrictions if applicable. |
| Data exposure | Yes | None, Norfolk Industries confidential, personal data, regulated/financial reporting relevant to SOX. |
| Monitoring requirements | Yes | SIEM logging sources, PAM session recording requirement, alerting needs. |
| Change record reference | Conditional | Required if vendor will implement production changes. |
| Incident record reference | Conditional | Required if access supports incident response activities. |
| Approvers | Yes | Service Owner; Platform Owner where applicable; CISO/Head of IT Infrastructure Services for high-risk cases. |
| Revocation plan | Yes | How and when access will be removed; owner responsible for confirming revocation. |

### Appendix B: Vendor Due Diligence Checklist (Infrastructure Access)
| Control Area | Check | Evidence Required | Pass Criteria |
|---|---|---|---|
| Vendor security posture | Confirm vendor maintains a security program aligned to recognized standards | SOC 2 report and bridge letter (if applicable) and/or ISO/IEC 27001 certificate; security questionnaire | Artifacts current within accepted period and no critical unresolved findings impacting access |
| Identity and MFA | Confirm vendor can support MFA and individual accountability | MFA description, identity federation details, user list and lifecycle process | MFA enforced; individual users identified; leaver handling defined |
| Privileged access management | Confirm privileged activities can be brokered/recorded | PAM integration approach or equivalent session control | Privileged sessions controlled and auditable |
| Logging and monitoring cooperation | Confirm vendor supports audit logging and investigation cooperation | Log source list, retention statement, support SLAs for investigations | Logs available and attributable; cooperation timeframes defined |
| Incident notification | Confirm vendor incident notification obligations | Contract clause for notification and cooperation | Notification timelines and contacts defined |
| Data handling | Confirm secure handling, encryption, retention, and disposal | Data handling policy excerpt, encryption statement | Meets Norfolk Industries requirements for in-transit/at-rest protections and disposal |
| Subprocessors | Identify any subcontractors involved in access | Subprocessor list and locations | Visibility provided; risks assessed |
| Privacy (GDPR) | Confirm lawful processing and protections for personal data | DPA terms, privacy controls summary | DPA in place where required; privacy controls adequate |
| Financial controls (SOX relevance) | If access impacts financial reporting systems, confirm control support | Audit support statement, access governance description | Access and change evidence can be produced for audits |
| OT access controls (if applicable) | Validate segmentation and strict remote access controls | Network segmentation diagram, remote access workflow | Access path controlled, time-bounded, monitored |
| Reassessment cadence | Confirm reassessment interval based on risk | Documented review date and owner | Reassessment scheduled and tracked |

### Appendix C: Minimum Evidence List (Audit-Ready)
| Evidence Item | Source | Minimum Content | Retention/Notes |
|---|---|---|---|
| Vendor access request record | ITSM tool | Request form fields completed; CI scope; start/end dates | Must be attributable and time-bound |
| Approval evidence | ITSM tool | Approver identities, timestamps, conditions | Include CISO/Head of IT Infrastructure Services approvals for high-risk access |
| Due diligence package | Governance repository | Checklist results, SOC 2/ISO artifacts, risk notes | Ensure current and linked to vendor record |
| Provisioning evidence | Identity/PAM/VPN/cloud logs | Account created, roles assigned, conditional access applied, expiry configured | Include screenshots/log extracts where appropriate |
| Session logs/recording metadata | PAM/SIEM | Session start/end, commands or recording reference, user identity | Recordings protected and access-controlled |
| SIEM monitoring proof | SIEM | Alerts/dashboards showing vendor activity monitoring | Demonstrate detections and escalation path |
| Access review evidence | Review record | Quarterly review results; monthly for high-risk | Include list of accounts reviewed and outcomes |
| Revocation evidence | Identity/PAM/VPN/cloud logs + ITSM | Disablement/removal timestamps; ticket closure notes | Must show access removed across all relevant systems |
| Change/CAB linkage | ITSM Change records | CAB approvals and implemented changes tied to vendor work | Required for production changes |
| Incident linkage (if used) | Incident records | Vendor involvement, actions taken, timeline | Include containment actions and access suspension if needed |