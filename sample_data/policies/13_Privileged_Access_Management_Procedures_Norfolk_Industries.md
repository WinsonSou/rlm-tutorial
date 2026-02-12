# Privileged Access Management Procedures (Norfolk Industries)

## 1. Purpose
These procedures define how Norfolk Industries manages Privileged Access Management (PAM) across Information Technology (IT) and approved Operational Technology (OT) connectivity to:
- Reduce the likelihood and impact of privileged credential misuse.
- Enforce least privilege, separation of duties, and strong authentication.
- Provide auditability through credential vaulting, session monitoring, and session recording.
- Meet governance and assurance expectations aligned to the Information Security Management System (ISMS), ISO/IEC 27001, ISO/IEC 22301, ITIL 4, COBIT 2019, NIST CSF / NIST SP 800-53 concepts, SOC 2 Trust Services Criteria, GDPR, and SOX.

## 2. Scope
### 2.1 In scope
- Privileged accounts and access paths used to administer:
  - Entra ID (Azure AD) and Active Directory
  - Microsoft Azure and AWS
  - On-prem servers, virtualization, storage, backup platforms
  - Network devices (routers, switches, firewalls, VPN concentrators)
  - Endpoint management platforms (Microsoft Intune, ConfigMgr where needed)
  - Security tooling (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus)
  - Databases, middleware, and infrastructure services
- Privileged service accounts (including non-interactive accounts) used by services, automation, scheduled tasks, and integrations.
- Break-glass privileged accounts.
- Approved OT remote administration paths where IT-managed PAM is used (subject to OT segmentation and strict remote access controls).

### 2.2 Out of scope
- Standard (non-privileged) end-user access.
- Application-layer role administration inside business applications unless those roles grant platform-level administrative control. If application roles grant platform-level control, they are treated as privileged and covered by these procedures.

## 3. Governance, Control Objectives, and Principles
### 3.1 Control objectives
- Ensure privileged access is granted only when required, approved, time-bound, and logged.
- Ensure privileged credentials are vaulted, rotated, and not shared outside controlled mechanisms.
- Ensure privileged sessions are monitored and recorded where technically feasible.
- Ensure misuse is detected and responded to promptly and consistently.
- Ensure evidence is time-bound, attributable, and repeatable.

### 3.2 Principles
- **Least privilege**: grant minimal rights for the minimal duration necessary.
- **Separation of duties**: request/approve/implement roles are separated where possible.
- **Strong authentication**: multi-factor authentication and device posture controls for privileged access.
- **Just-in-time access**: privileges are activated only when needed, for a defined duration.
- **Vault-first**: privileged credentials are stored in PAM vault(s) and retrieved only through PAM workflows.
- **Record and review**: privileged activity is logged and, where supported, session recorded and reviewed.

## 4. Roles and Responsibilities
Role responsibilities are aligned to the authoritative roles list for Norfolk Industries.

### 4.1 Responsibility summary
- **CIO**: executive governance for IT strategy and oversight.
- **Head of IT Infrastructure Services**: accountable for infrastructure operations outcomes and PAM procedure adoption within IT Infrastructure Services.
- **CISO**: accountable for the information security program and ISMS oversight, including privileged access risk posture.
- **IT Governance Manager**: owns governance processes, compliance tracking, and audit coordination for PAM evidence and adherence.
- **Service Owner**: accountable for privileged access requirements, risk decisions, and service-specific control implementation.
- **Platform Owner**: accountable for platform architecture and engineering standards, including PAM integration patterns.
- **IT Operations Manager**: responsible for operational execution, on-call readiness, and coordination of incident response for privileged misuse.
- **Security Engineer**: implements and validates PAM integrations, logging, detection, and response workflows.
- **ITSM Process Owner**: ensures ITIL-aligned workflows (Change Enablement, Incident Management, Service Configuration Management) are integrated with PAM.
- **Internal Audit**: independently assesses control design and operating effectiveness.

### 4.2 RACI alignment (procedure-specific)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAM procedure approval and lifecycle | A | R | C | R | C | C | C | C | I |
| Privileged role inventory ownership (per service) | I | A | C | R | A | R | R | C | I |
| Break-glass account creation/approval | I | R | A | C | R | R | R | C | I |
| High-risk exceptions to PAM controls | A | R | R | C | C | C | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 5. Definitions and Canonical Terminology
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.

Additional PAM-specific terms used in this document:
- **Privileged account**: Any account with administrative permissions or ability to materially impact confidentiality, integrity, or availability.
- **Privileged role**: A role (in Entra ID, Active Directory, cloud, or platform RBAC) that confers administrative capability.
- **Vaulting**: Storage and controlled retrieval of privileged credentials via a PAM vault with auditing and rotation.
- **Session recording**: Capture of privileged session activity (e.g., keystrokes, commands, screen/video) for accountability.
- **Just-in-time (JIT) access**: Time-bound elevation to a privileged role for an approved duration.
- **Break-glass access**: Emergency access mechanism used when standard identity or PAM workflows are unavailable.

## 6. Procedure Overview and Service Integration
### 6.1 PAM capabilities required for Norfolk Industries
Norfolk Industries uses a PAM platform (for example, CyberArk) implementing, at minimum:
- Credential vaulting and controlled checkout
- Automated credential rotation
- Privileged session management and session recording (where feasible)
- Approval workflows and time-bound access
- Central logging to the SIEM (for example, Microsoft Sentinel)
- Integration with Entra ID (Azure AD) and Active Directory
- Support for service account governance

### 6.2 Integration points
| Integration | Purpose | Minimum requirement |
|---|---|---|
| Entra ID | Authentication, conditional access, privileged access governance | MFA enforced for privileged activity; administrative roles governed by JIT where supported |
| Active Directory | Domain admin pathways, server admin groups | Privileged group membership time-bound and audited |
| ITSM tool (ITIL-aligned) | Request, approval, change/incident linkage | PAM requests linked to Request/Change/Incident records |
| SIEM (e.g., Microsoft Sentinel) | Centralized detection and alerting | PAM logs forwarded with time synchronization |
| EDR (e.g., Microsoft Defender for Endpoint) | Endpoint detection for admin actions | Correlate privileged sessions with endpoint telemetry |
| Vulnerability scanning (e.g., Tenable/Nessus) | Identify unmanaged admin paths | Findings drive onboarding to PAM |
| OT remote access controls | Segmented, approved access | PAM used as control point; session recording prioritized |

## 7. Privileged Roles Inventory (Inventory, Classification, and Review)
### 7.1 Inventory requirements
Each Service Owner maintains a privileged roles inventory for their service(s). The inventory must include:
- Privileged role name and platform (Entra ID, Active Directory, Azure, AWS, network device, etc.)
- Privilege level classification (see 7.2)
- Eligible user population (named individuals or role-based group)
- Access pathway (JIT role activation, vaulted credential, service account, API key/cert)
- Session recording feasibility and current status
- Rotation requirement and current rotation method
- Monitoring and alerting rules mapped to SIEM detections
- Associated CIs in the CMDB (Configuration Items)

### 7.2 Privilege level classification
| Level | Description | Examples | Mandatory controls |
|---|---|---|---|
| Tier 0 (Identity & Control Plane) | Can control identity, authentication, authorization, or create new admins | Entra ID Global Administrator; Active Directory Domain Admin | JIT required where supported; MFA; session recording for interactive sessions where feasible; strict break-glass controls |
| Tier 1 (Infrastructure Admin) | Admin of servers, cloud subscriptions, network/security devices | Azure Subscription Owner; firewall admin; vCenter admin | Vaulting and rotation; session recording where feasible; SIEM alerting |
| Tier 2 (Service/Tool Admin) | Admin of IT tools or services with high data impact | SIEM admin; EDR admin; backup admin | Vaulting/rotation; approval workflow; monitoring |
| Tier 3 (Limited Admin) | Narrow admin scope with constrained impact | Local admin via controlled tooling | JIT/time-bound; logging |

### 7.3 Inventory review cadence
- **Monthly**: Service Owner verifies all active privileged assignments and vault entries remain required.
- **Quarterly**: IT Governance Manager coordinates an access recertification campaign; results are evidenced.
- **Upon major change**: Any platform redesign, migration, or security incident triggers an out-of-cycle review.

## 8. Vaulting Standards (Credentials, Secrets, and Keys)
### 8.1 What must be vaulted
The following must be stored and managed in PAM vaults unless a documented exception is approved:
- Shared administrative accounts (where unavoidable)
- Local administrator accounts on servers and network devices where PAM supports management
- Break-glass credentials
- Service account passwords (where password-based)
- API keys and secret tokens used for administrative automation when the PAM supports secret management
- Privileged SSH keys where supported by the PAM

### 8.2 Vaulting rules
- Privileged credentials must not be stored in:
  - Personal password managers
  - Spreadsheets, documents, or tickets
  - Source code repositories or scripts
- Credential checkout must be:
  - Attributable to a named user identity
  - Time-bound with automatic expiration
  - Logged centrally and forwarded to the SIEM
- Where supported, use **credential injection** (no direct password visibility).
- Credentials are unique per system and environment wherever feasible.

### 8.3 Rotation standards
- Rotation must be automated where the PAM supports it.
- Rotation triggers:
  - After each checkout for shared privileged accounts (preferred)
  - Immediately after break-glass use
  - On suspected compromise
  - On workforce separation impacting privileged access

Minimum rotation frequencies when “rotate after use” is not possible:
| Credential type | Maximum age |
|---|---:|
| Tier 0 privileged shared accounts | 7 days |
| Tier 1 privileged shared accounts | 14 days |
| Tier 2 privileged shared accounts | 30 days |
| Service account passwords (non-interactive) | 60 days, or shorter if system supports automated rotation without outage risk |

## 9. Session Management and Session Recording
### 9.1 Session controls
- Privileged sessions must use PAM session management/proxy where feasible for:
  - RDP, SSH, web admin consoles, database admin consoles, and network device admin interfaces.
- Sessions must be bound to:
  - A unique user identity (no anonymous sessions)
  - A ticket reference (Request/Change/Incident) where applicable
  - Time synchronization (NTP) on PAM components and target systems

### 9.2 Session recording requirements
- **Required** for Tier 0 and Tier 1 interactive administrative sessions where technically feasible.
- **Strongly recommended** for Tier 2 sessions and for any OT remote administration mediated by IT systems.
- If session recording is not feasible, the Platform Owner must implement compensating controls such as:
  - Enhanced command logging
  - Immutable audit logs
  - Increased alerting thresholds
  - Peer review of changes
  - Change Advisory Board (CAB) linkage for elevated actions

### 9.3 Session review
- **Security Engineer** implements alerts for high-risk actions (see Section 16).
- **IT Operations Manager** ensures periodic review of recorded sessions for:
  - Break-glass usage
  - Policy violations
  - Repeated failed elevations
  - Access outside approved windows
- **Service Owner** performs targeted reviews after high-impact changes or incidents.

## 10. Just-in-Time (JIT) Privileged Access
### 10.1 JIT model
Norfolk Industries uses JIT access to reduce standing privileges:
- Users are **eligible** for a privileged role but not permanently active.
- Activation is time-bound, requires approval when risk dictates, and is logged.

### 10.2 JIT requirements
- JIT duration must be the minimum necessary and aligned to the task.
- JIT activation must require:
  - Strong authentication via Entra ID (MFA enforced)
  - Business justification and ticket reference where applicable
  - Approval for Tier 0, Tier 1, and high-impact Tier 2 roles unless an approved auto-approval rule exists with documented risk acceptance
- JIT expiration must remove role membership automatically.

### 10.3 Standing access prohibition
Standing privileged access is prohibited for Tier 0 roles, except break-glass accounts and explicitly approved service principals required for platform operations, governed per Section 12 and Section 11.

## 11. Break-Glass Privileged Access
### 11.1 Purpose and constraints
Break-glass access is reserved for emergencies such as:
- Entra ID outage preventing standard authentication
- PAM platform outage preventing vault checkout/session management
- Critical incident requiring immediate admin action to restore services (RTO/RPO alignment)

Break-glass access must not be used for convenience, routine maintenance, or to bypass approvals.

### 11.2 Break-glass account design
Break-glass accounts must:
- Be dedicated and named as break-glass in the platform naming convention
- Be excluded from conditional access policies only to the minimum required extent, with compensating controls
- Use strong authentication mechanisms supported by the platform
- Have credentials stored in the PAM vault when available; if the PAM vault is unavailable by definition, credentials must be stored in a separate sealed and controlled mechanism approved by the CISO and Head of IT Infrastructure Services
- Be monitored with highest priority SIEM alerts

### 11.3 Break-glass authorization
- Authorization to use break-glass requires:
  - Approval from the **IT Operations Manager** (or on-call delegate) and notification to the **Security Engineer**
  - If time-critical life-safety or major outage conditions exist, the operator may proceed immediately and obtain retrospective approval within 4 hours
- All break-glass use must be logged using the template in Appendix B and attached to the Incident record in the ITSM tool.

### 11.4 Post-use actions
Immediately after break-glass use:
- Rotate credentials.
- Review all actions performed (session recording and audit logs).
- Open or update an Incident record and, if applicable, a Problem record.
- If unauthorized activity is suspected, initiate the incident response steps in Section 15.

## 12. Service Account Governance
### 12.1 Service account standards
Service accounts (including automation accounts and service principals) must:
- Be uniquely identified and owned by a **Service Owner**
- Have a defined purpose, scope, and system dependencies documented
- Use least privilege permissions (no broad admin roles unless explicitly required and approved)
- Avoid interactive logon where not required; deny interactive logon when feasible
- Use vaulted secrets and automated rotation where supported
- Be inventoried as CIs and linked to the dependent services

### 12.2 Creation and onboarding
- New service accounts require:
  - Documented justification
  - Approval by the Service Owner and Platform Owner
  - Security review for Tier 0/Tier 1 equivalent permissions
- All service accounts must be onboarded to PAM secret management or vaulting unless an exception is approved.

### 12.3 Credential and key management
- Password-based service accounts: rotate per Section 8.3 without causing outages; changes must be tested in non-production where possible.
- Certificate/key-based: lifecycle managed with expiry monitoring; private keys treated as privileged secrets and stored in approved secret stores integrated with PAM where supported.
- API tokens: short-lived tokens preferred; long-lived tokens must be vaulted and rotated.

## 13. PAM Onboarding Procedure (System/Platform to PAM)
This procedure onboards a target system/platform to PAM for credential vaulting and session management.

### 13.1 Preconditions
- Target system is in CMDB as a CI and has a Service Owner and Platform Owner assigned.
- Network connectivity from PAM components to target is approved and segmented appropriately (including OT constraints).
- Logging is enabled and time synchronized.

### 13.2 Steps
1. **Initiate request**
   - Requestor opens an onboarding Request in the ITSM tool and identifies the CI(s), environment (prod/non-prod), and administration protocols (RDP/SSH/web).
2. **Classify privileges**
   - Service Owner classifies the privileged roles (Tier 0–3) and confirms session recording requirements.
3. **Design onboarding approach**
   - Platform Owner selects PAM integration pattern:
     - Vaulted credential only
     - Vaulted credential + session proxy/recording
     - Secret management for service accounts/automation
4. **Implement vault objects**
   - Security Engineer (or delegated engineer) creates vault entries, access policies, rotation schedules, and safe/collection structure.
5. **Configure target**
   - Systems Engineer / Network Engineer / Cloud Engineer configures target to allow PAM-managed access (least access required, dedicated admin accounts where needed).
6. **Enable session management**
   - Configure session proxy, connectors, and recording.
   - Validate session metadata capture (user, time, target, ticket reference).
7. **Integrate monitoring**
   - Forward PAM logs and session events to the SIEM.
   - Implement baseline alerts (failed checkouts, failed logons, access outside window).
8. **Test**
   - Execute functional tests:
     - Credential checkout/injection
     - Rotation test (non-prod first where feasible)
     - Session recording playback test
9. **Document**
   - Update CMDB CI record with:
     - PAM onboarding status
     - Vault object references
     - Rotation policy
     - Session recording status
10. **Operational handover**
   - IT Operations Manager ensures runbooks and on-call readiness exist for common failures (connector down, rotation failure).
11. **Close request**
   - Service Owner attests onboarding completion and signs off in the ITSM record.

## 14. Privileged Access Request, Approval, and Elevation Procedures
### 14.1 Request elevation (user procedure)
1. Open an access Request in the ITSM tool.
2. Select the target privileged role or vaulted system access.
3. Provide:
   - Business justification
   - Target system(s) / CI(s)
   - Duration needed
   - Ticket reference to a Change or Incident when applicable
4. Confirm acknowledgement of monitoring and session recording.

### 14.2 Approval workflow
Approval requirements by tier:
| Privilege tier | Approval required | Approvers |
|---|---|---|
| Tier 0 | Always | Service Owner (R) and CISO (C) for high-risk scopes; Platform Owner (R) |
| Tier 1 | Yes | Service Owner (R), Platform Owner (R) |
| Tier 2 | Conditional | Service Owner (R); Platform Owner (R) when admin scope is broad |
| Tier 3 | Conditional | Service Owner (R) or delegated approver per service model |

Additional rules:
- Approver must not be the same person as the requestor for Tier 0 and Tier 1.
- Approvals must be captured in the ITSM tool and linked to PAM activation logs.

### 14.3 Elevation execution
- For JIT roles:
  1. User activates the eligible role in the approved mechanism.
  2. User selects the time window (bounded to approval).
  3. Activation generates an audit event forwarded to the SIEM.
- For vaulted credentials:
  1. User checks out/injects credentials via PAM.
  2. If session management is enabled, user connects via PAM proxy.
  3. Upon checkout expiration, PAM rotates the credential per policy.

### 14.4 Revocation
- Access is revoked by:
  - JIT expiration
  - Manual revocation by Service Owner or Platform Owner
  - Automatic revocation upon detection of misuse or policy breach
- Immediate revocation is mandatory when:
  - Workforce separation occurs
  - Compromise is suspected
  - Break-glass misuse is detected

## 15. Monitoring, Incident Response, and Misuse Handling
### 15.1 Monitoring requirements
- PAM platform must generate and forward to the SIEM:
  - Credential checkout events
  - Failed checkouts
  - Privileged session start/stop events
  - Session recording availability failures
  - Rotation success/failure events
  - Policy changes in PAM

### 15.2 Indicators of misuse
- Access to Tier 0 roles without matching ticket/justification
- Excessive failed login attempts during privileged sessions
- Privileged activity outside approved maintenance windows
- Attempts to disable logging, EDR, SIEM forwarding, or PAM connectors
- Bulk changes to accounts, roles, firewall rules, or audit settings

### 15.3 Incident response procedure (privileged misuse)
1. **Triage**
   - IT Operations Manager coordinates initial triage; Security Engineer validates alerts and correlates telemetry (PAM + SIEM + EDR).
2. **Containment**
   - Immediately revoke elevated access and disable affected privileged accounts where appropriate.
   - Rotate suspected compromised credentials and invalidate tokens/keys.
3. **Preserve evidence**
   - Preserve session recordings, PAM logs, target system logs, and SIEM correlation outputs.
   - Ensure evidence is time-bound, attributable, and repeatable.
4. **Eradication and recovery**
   - Remove unauthorized changes, restore secure configuration, and re-establish monitoring.
   - Validate control operation (rotation, session recording, approvals).
5. **Post-incident actions**
   - Create or update Problem record.
   - Service Owner and Platform Owner review least privilege gaps and implement corrective actions.
   - IT Governance Manager coordinates evidence package for audit and ISMS reporting.

### 15.4 Regulatory and privacy considerations
- Session recordings are security records and must be access-controlled.
- Access to recordings is limited to Security Engineer, IT Operations Manager, and authorized investigators, with approvals and logging.
- Privacy handling must align to GDPR and Norfolk Industries privacy governance under the Data Protection Officer (DPO) where applicable.

## 16. Privileged Credential Rotation and Failure Handling
### 16.1 Rotation failure response
When automated rotation fails:
1. PAM generates an alert to SIEM and notifies IT Operations Manager and Security Engineer.
2. Platform Owner assesses service impact and determines remediation path.
3. Systems Engineer / Network Engineer / Cloud Engineer performs controlled remediation:
   - Fix connector/permissions
   - Retry rotation
   - If manual rotation is required, perform it as an emergency controlled activity and immediately restore automated rotation
4. Document actions and attach evidence to the ITSM record.

### 16.2 Emergency credential reset
- Emergency resets must:
  - Be initiated through an Incident record
  - Be time-stamped and attributable
  - Trigger review of related privileged sessions and access logs

## 17. Exceptions and Risk Acceptance
- Any deviation from these procedures requires a documented exception approved per risk:
  - High-risk exceptions: approved by **CIO (A)**, with **Head of IT Infrastructure Services (R)** and **CISO (R)** involved; documented and time-bound.
- Exceptions must define:
  - Scope (systems, roles, duration)
  - Compensating controls
  - Evidence to demonstrate compensating control operation
  - Expiration date and review cadence

## 18. Records, Evidence, and Audit Requirements
### 18.1 Record retention and access
- PAM logs and session recordings are retained per Norfolk Industries record retention requirements and legal/regulatory needs (GDPR and SOX considerations).
- Access to PAM records is restricted and logged.

### 18.2 Minimum evidence set (principles applied)
Evidence must be time-bound, attributable, and repeatable and include approvals, logs, and validation artifacts where applicable. Minimum evidence includes:
- Privileged roles inventory and quarterly recertification outputs
- PAM onboarding records linked to CIs
- JIT activation logs and ITSM approvals
- Vault checkout logs and rotation logs
- Session recordings or compensating control logs
- Break-glass use logs and post-use rotation confirmation
- Incident records and investigation artifacts for misuse

## 19. Control Mappings (ISO/IEC 27001, NIST CSF, SOC 2, ITIL 4, COBIT 2019)
### 19.1 Control mapping summary
| Procedure area | ISO/IEC 27001 (conceptual) | NIST CSF | SOC 2 TSC | ITIL 4 practice | COBIT 2019 domain |
|---|---|---|---|---|---|
| Privileged access governance, least privilege | Annex A access control concepts | Protect | Security | Information Security Management | APO, DSS |
| Vaulting and rotation | Annex A cryptography & access control concepts | Protect | Security, Confidentiality | Information Security Management | APO, DSS |
| Session monitoring and recording | Annex A logging/monitoring concepts | Detect, Respond | Security, Availability | Monitoring and Event Management | DSS, MEA |
| Break-glass controls | Annex A continuity & access control concepts | Respond, Recover | Availability, Security | Service Continuity Management | DSS, EDM |
| Incident response for misuse | Annex A incident management concepts | Respond | Security | Incident Management | DSS |
| Evidence and auditability | Annex A compliance concepts | Identify | Security, Availability | Service Configuration Management | MEA |

### 19.2 Evidence-to-control alignment statement
Norfolk Industries demonstrates control operation through:
- ITSM approvals linked to PAM events
- SIEM-ingested PAM logs and alert records
- Session recordings and review attestations
- CMDB CI linkages proving consistent governance across platforms

---

## Appendices

## Appendix A: PAM Onboarding Checklist (Template)
### A.1 System identification
| Item | Value |
|---|---|
| CI name (CMDB) |  |
| Environment (Prod/Non-prod) |  |
| Service Owner |  |
| Platform Owner |  |
| Administration protocols (RDP/SSH/Web/API) |  |
| Tier classification (0–3) |  |
| OT involvement (Yes/No; details) |  |

### A.2 Prerequisites validation
- [ ] CI exists in CMDB and is current (owner, environment, dependencies)
- [ ] Network connectivity from PAM to target approved and segmented appropriately
- [ ] Target system time synchronization enabled
- [ ] Logging enabled on target system for administrative actions
- [ ] Administrative pathways documented (accounts, groups, roles)

### A.3 Vaulting configuration
- [ ] Vault container/safe created with least-privilege access policies
- [ ] Privileged accounts created/dedicated (no shared personal accounts)
- [ ] Credential injection enabled where supported
- [ ] Rotation schedule configured per Section 8.3
- [ ] Rotation tested successfully (non-prod first where feasible)

### A.4 Session management / recording
- [ ] Session proxy configured (if supported for protocol)
- [ ] Session recording enabled for Tier 0/Tier 1 (where feasible)
- [ ] Session metadata captured (user, target, start/stop time, ticket reference)
- [ ] Recording playback validated and access restricted

### A.5 Monitoring and SIEM integration
- [ ] PAM audit logs forwarded to SIEM
- [ ] Alerts configured (failed checkouts, rotation failures, unusual activity)
- [ ] Correlation with EDR enabled for privileged endpoints (where applicable)

### A.6 Operational readiness
- [ ] Runbook exists for connector failures and rotation failures
- [ ] On-call routing configured for PAM alerts
- [ ] Service Owner sign-off recorded in ITSM request
- [ ] CMDB updated with PAM onboarding status and references

## Appendix B: Break-Glass Log Template (Template)
### B.1 Break-glass usage record
| Field | Entry |
|---|---|
| Incident record reference (ITSM) |  |
| Date/time initiated (UTC) |  |
| Date/time ended (UTC) |  |
| Break-glass account identifier |  |
| Requestor (named user) |  |
| Approver (IT Operations Manager or delegate) |  |
| Notified Security Engineer (name/time) |  |
| Business justification (emergency condition) |  |
| Systems/CIs accessed |  |
| Actions performed (high level) |  |
| Session recording reference (if available) |  |
| Logs collected (PAM/SIEM/target) |  |
| Credential rotation completed (time/evidence reference) |  |
| Post-use review completed by (name/time) |  |
| Follow-up actions (Problem record, control improvements) |  |

### B.2 Break-glass post-use checklist
- [ ] Incident record updated with full timeline and approvals
- [ ] Credential rotated immediately after use
- [ ] Session recordings reviewed (or compensating logs reviewed)
- [ ] SIEM alerts reviewed and cleared with rationale
- [ ] Any unauthorized change reversed and validated
- [ ] Lessons learned captured and assigned

## Appendix C: PAM Evidence List (Audit-Ready)
### C.1 Evidence catalog
| Evidence item | Source system | Owner | Frequency | Meets evidence principles (time-bound, attributable, repeatable) |
|---|---|---|---|---|
| Privileged roles inventory per service | CMDB + service documentation | Service Owner | Monthly/Quarterly | Yes |
| Quarterly privileged access recertification results | ITSM reporting | IT Governance Manager | Quarterly | Yes |
| JIT activation logs for Tier 0/Tier 1 | Entra ID + PAM | Security Engineer | Ongoing | Yes |
| Vault checkout logs and user attribution | PAM vault | Security Engineer | Ongoing | Yes |
| Credential rotation success/failure logs | PAM vault | Platform Owner | Ongoing | Yes |
| Session recordings and access logs | PAM session management | IT Operations Manager | Ongoing | Yes |
| SIEM alert records for PAM events | SIEM (e.g., Microsoft Sentinel) | Security Engineer | Ongoing | Yes |
| Break-glass usage logs (Appendix B) | ITSM + PAM | IT Operations Manager | Per event | Yes |
| Onboarding completion records per CI | ITSM + CMDB | Platform Owner | Per onboarding | Yes |
| Incident records for misuse and remediation | ITSM + SIEM | IT Operations Manager | Per incident | Yes |

### C.2 Evidence linkage requirements
- Every privileged access event must link to at least one of:
  - Approved Request record
  - Change record (CAB-approved when required)
  - Incident record (including break-glass and emergency actions)
- Session recordings must be linkable to:
  - User identity
  - Target CI
  - Time window
  - Corresponding ticket reference (where applicable)