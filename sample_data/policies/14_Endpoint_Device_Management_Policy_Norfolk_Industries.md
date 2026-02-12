# Endpoint & Device Management Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for managing endpoints and devices at Norfolk Industries to ensure secure, reliable, and compliant operation across North America, Europe, and APAC. It defines governance, technical controls, and operating procedures for device enrollment, configuration, compliance, encryption, endpoint detection and response (EDR), patching, software deployment, remote actions (including wipe), and lifecycle management.

This policy supports the Information Security Management System (ISMS) and aligns to ITIL 4, COBIT 2019, NIST CSF concepts, SOC 2 Trust Services Criteria, GDPR, and SOX control expectations.

## 2. Scope
### 2.1 In scope
- All corporate-owned endpoints used to access Norfolk Industries information or services:
  - Windows desktops/laptops
  - macOS laptops/desktops
  - Mobile devices (iOS/iPadOS and Android) used for corporate access
- Managed virtual endpoints where Intune policy enforcement is supported (e.g., Azure Virtual Desktop endpoints where applicable)
- Device management tooling and services, including Microsoft Intune and ConfigMgr where needed
- Device identities integrated with Active Directory and Entra ID (Azure AD) (first mention), then Entra ID
- Endpoint security tooling integrations (e.g., Microsoft Defender for Endpoint)

### 2.2 Out of scope (but related)
- Operational Technology (OT) endpoints on plant networks that cannot meet corporate endpoint standards due to vendor constraints; these are governed by OT security standards and compensating controls while maintaining strict segmentation between Operational Technology (OT) and Information Technology (IT).
- Servers and cloud workloads (covered by separate hardening and patch policies).

## 3. Policy statements (mandatory requirements)
### 3.1 Device enrollment and management
1. Corporate-owned endpoints **must be enrolled** into Microsoft Intune prior to being issued to a user or placed into production.
2. ConfigMgr may be used where needed for legacy applications, constrained networks, or specific operational requirements; when used, ConfigMgr configurations **must not** weaken required security controls and **must align** to this policy.
3. Devices accessing Norfolk Industries resources **must** be uniquely identifiable and associated with a Configuration Item (CI) record in the ITSM CMDB (device CI, owner, primary user, and location).
4. Only managed and compliant devices may access corporate services unless an approved exception is in place (see Section 12).

### 3.2 Device compliance policies
1. Intune compliance policies **must** be enforced for all enrolled endpoints and mobile devices.
2. Conditional access in Entra ID **must** require compliant device status for access to corporate resources that contain internal, confidential, regulated, or SOX-relevant data.
3. Minimum compliance requirements include:
   - Supported OS version (within vendor support)
   - Encryption enabled
   - EDR onboarding and healthy status
   - Secure boot / platform integrity where supported
   - No known critical risk posture per EDR (where supported by platform)
   - Screen lock / inactivity timeout and authentication controls
4. Non-compliant devices **must** be remediated within defined timelines (Section 10). Access restrictions may be applied automatically.

### 3.3 Encryption
1. Full disk encryption **must** be enabled:
   - Windows: BitLocker with recovery keys escrowed to Entra ID and/or Active Directory as implemented by IT Infrastructure Services.
   - macOS: FileVault with secure key escrow and recovery workflow.
   - Mobile: Device-level encryption enabled and not user-disabled.
2. Removable media encryption requirements are governed by separate data protection standards; where removable media is permitted, encryption controls must be enforced.

### 3.4 Endpoint Detection and Response (EDR)
1. All supported endpoints **must** be onboarded to the approved EDR solution (e.g., Microsoft Defender for Endpoint) and report health status to the SIEM (e.g., Microsoft Sentinel) where integrated.
2. Tamper protection (or equivalent) **must** be enabled to prevent unauthorized disabling of security controls.
3. High severity EDR alerts **must** follow Incident Management and security incident response requirements, including escalation to the CISO organization per ISMS processes.

### 3.5 Local administrator control
1. Local administrator privileges on endpoints are **prohibited by default**.
2. Administrative access, where required, must be provided using controlled methods:
   - Just-in-time elevation via approved privileged access mechanisms where available
   - Unique local admin password management (e.g., LAPS or equivalent)
3. Shared local administrator accounts are **not permitted**.
4. Requests for local admin privileges must be processed through the ITSM tool with documented business justification, duration, and approval (Section 12).

### 3.6 OS security baselines and configuration
1. Standard OS security baselines **must** be applied via Intune (and/or ConfigMgr where needed) for Windows, macOS, and mobile platforms.
2. Baselines must include, at minimum:
   - Firewall enabled and configured
   - Secure authentication configuration (password, PIN, biometrics as appropriate)
   - Screen lock controls
   - Disabling insecure legacy protocols where feasible (e.g., SMBv1)
   - Logging settings required to support detection and auditability
3. Configuration drift must be managed through policy enforcement and monitored for exceptions.

### 3.7 Patching and update management
1. Security updates **must** be applied in a timely manner based on risk:
   - Critical security updates: expedited deployment
   - Standard security updates: deployed in regular maintenance cycles
2. Update rings / phased deployment **must** be used to reduce operational risk:
   - Pilot ring (IT)
   - Early adopter ring (representative business users)
   - Broad deployment ring
3. Devices that are persistently missing security updates must be remediated per Section 10 and may be blocked from access.

### 3.8 Software deployment and application control
1. All software deployed to endpoints must be:
   - Licensed appropriately
   - Security-reviewed where required by ISMS processes
   - Deployed via managed mechanisms (Intune, ConfigMgr, approved enterprise software catalog)
2. Unapproved software installation is prohibited. Where user self-service is offered, it must be restricted to an approved catalog.
3. High-risk software (e.g., remote access tools, password dumpers, packet capture tools) is prohibited unless explicitly authorized through exception handling and security review.
4. Application control technologies (where implemented) must support preventing execution of known malicious or unauthorized software.

### 3.9 Remote actions: lock, locate, wipe, and retire
1. Norfolk Industries may execute remote actions on corporate-owned devices including:
   - Remote lock
   - Remote wipe (factory reset) or selective wipe (corporate data removal) as applicable
   - Device retire/disable
2. Remote wipe must be performed:
   - Immediately upon confirmed theft where risk warrants
   - Upon employee separation where device is not returned promptly or cannot be verified
   - When device compromise is suspected and containment requires wipe
3. Remote actions must be logged and attributable to an authorized operator, with a related incident or request record in the ITSM tool.

### 3.10 BYOD stance
1. Personally-owned devices (BYOD) are **not permitted** to enroll for full device management.
2. BYOD may be permitted for limited access using application-level controls (e.g., managed application protection policies) where supported, provided:
   - Data remains within managed applications
   - Copy/paste and data export restrictions are enforced where required
   - Conditional access enforces MFA and risk-based policies
3. BYOD access decisions must be approved by the Head of IT Infrastructure Services in consultation with the CISO where security risk is elevated.

### 3.11 Data handling and privacy
1. Endpoint telemetry and logs collected for security and operational purposes must be limited to legitimate business needs and handled consistent with GDPR and internal privacy governance.
2. Access to device data, logs, and remote control tools must be role-based and auditable.
3. For regions with additional privacy constraints, Regional IT Operations must follow guidance from the Data Protection Officer (DPO).

## 4. Roles and responsibilities
Roles below use the Norfolk Industries standard role definitions.

### 4.1 Responsibility summary
- **CIO**: Executive owner of IT strategy and governance for endpoint management.
- **Head of IT Infrastructure Services**: Accountable for endpoint management service outcomes, standards, and operational performance.
- **CISO**: Accountable for ISMS oversight and security control requirements.
- **IT Governance Manager**: Owns policy lifecycle, compliance tracking, and audit coordination.
- **Service Owner**: Accountable for end-to-end endpoint management service performance and compliance.
- **Platform Owner**: Accountable for technical standards and engineering for endpoint platforms (Intune/ConfigMgr, endpoint security baseline).
- **IT Operations Manager**: Responsible for operational execution, on-call readiness, and incident coordination.
- **Endpoint Engineer**: Implements and supports endpoint and device management controls.
- **IAM Engineer**: Implements identity, conditional access, and device identity controls.
- **Security Engineer**: Implements EDR and security integrations, validates control health.
- **ITSM Process Owner**: Maintains ITIL-aligned process integration for Incident/Change/CMDB.
- **Service Desk Manager**: Manages intake, first-line support, and user communications.
- **Internal Audit**: Independently assesses control effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment.

## 5. RACI (aligned to raci_master.csv)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy governance
### 6.1 Ownership and maintenance
- Policy Owner: **IT Governance Manager**
- Accountable Executive: **Head of IT Infrastructure Services**
- Security Oversight: **CISO**
- Review cadence: at least annually and upon major platform or regulatory change.

### 6.2 Exceptions and risk acceptance
- Exceptions must follow Section 12 (Exception Handling) and be time-bound, attributable, and approved at the appropriate risk level.

## 7. Control requirements
### 7.1 Minimum endpoint control set
| Control domain | Minimum requirement | Implementation mechanism (Norfolk Industries) | Evidence examples |
|---|---|---|---|
| Enrollment & inventory | All endpoints enrolled and represented as a CI | Intune / ConfigMgr + CMDB integration | Intune device list export; CMDB CI record; assignment logs |
| Compliance enforcement | Conditional access requires compliant device | Entra ID Conditional Access + Intune compliance | Conditional Access policy export; compliance reports |
| Encryption | Full disk encryption enabled; recovery escrow | BitLocker/FileVault + escrow | Encryption compliance report; key escrow audit |
| EDR | EDR installed, onboarded, healthy | Defender for Endpoint (or approved equivalent) | EDR device health report; onboarding status |
| Local admin | Least privilege enforced; controlled elevation | Privilege management + LAPS/equivalent | Local admin group membership reports; elevation audit |
| Patching | Timely security updates with rings | Intune update rings / ConfigMgr | Patch compliance dashboards; deployment reports |
| Software | Managed deployment; restricted installs | Company Portal / ConfigMgr | App deployment logs; software inventory |
| Remote actions | Wipe/lock actions controlled & logged | Intune remote actions + ITSM records | Remote action audit logs; incident/request records |

### 7.2 Device configuration hardening
- Baselines must be maintained by the Platform Owner and implemented by Endpoint Engineers.
- Baselines must be versioned and changes governed by the Change Advisory Board (CAB) via Change Enablement.

## 8. Operational procedures (policy-mandated)
All procedures below must be executed through ITIL-aligned practices and recorded in the ITSM tool.

### 8.1 New device provisioning (corporate-owned)
1. **Request and approval**
   - User’s manager submits request in ITSM tool with role, region, and required applications.
   - Service Desk validates entitlement and forwards to Endpoint Engineering queue.
2. **Device preparation**
   - Device assigned an asset tag and linked to a CMDB CI.
   - For Windows devices: Autopilot registration (where implemented) and profile assignment.
   - For macOS: automated enrollment profile assignment.
   - For mobile: corporate enrollment method selected and assigned.
3. **Security enforcement**
   - Intune enrollment completed before issuance.
   - Compliance policy and security baseline applied.
   - EDR onboarding validated.
   - Encryption status validated.
4. **User handoff**
   - Device issued with standard build, corporate applications, and instructions for first sign-in.
   - Service Desk confirms device appears compliant within the required window and closes the request with evidence references.

### 8.2 Lost or stolen device response
1. **Intake and triage**
   - User reports to Service Desk immediately.
   - Service Desk creates an incident and captures: device identifier, last known location/time, data classification exposure, and whether the device is powered on.
2. **Containment**
   - IT Operations Manager coordinates containment actions.
   - Endpoint Engineer performs remote lock and/or wipe based on risk assessment and device type.
   - IAM Engineer may revoke sessions and require credential reset.
3. **Security escalation**
   - Security Engineer reviews EDR telemetry for compromise indicators.
   - Escalate to CISO organization when data exposure, compromise, or regulatory concerns exist.
4. **Recovery**
   - Replacement device provisioning initiated (Section 8.1).
   - Post-incident review performed per Problem Management where patterns emerge.

### 8.3 Compliance remediation
1. **Detection**
   - Non-compliance identified via Intune compliance reports, EDR health status, or patch compliance dashboards.
2. **User notification**
   - Service Desk notifies user with required remediation steps and a completion deadline based on severity.
3. **Automated remediation**
   - Apply policy-based fixes where possible (enable encryption, re-enable EDR, enforce OS update).
4. **Access restriction**
   - If not remediated in time, conditional access enforces reduced access or block for protected resources.
5. **Closure**
   - Ticket closed only after compliance is verified and evidence is attached/linked.

### 8.4 Exception handling procedure (endpoint-related)
1. **Submission**
   - Exception request must include: device identifier(s), business justification, affected control(s), compensating controls, duration, and risk owner.
2. **Review**
   - Platform Owner and Security Engineer assess technical and security impact.
   - Service Owner confirms service impact and operational feasibility.
3. **Approval**
   - Low/medium risk: Head of IT Infrastructure Services (or delegate) approval.
   - High risk: approval per RACI “Exception approval (high risk)” involving CIO, Head of IT Infrastructure Services, and CISO as required.
4. **Implementation**
   - Endpoint Engineer applies scoped configuration change with audit logging.
   - IAM Engineer adjusts conditional access only when required and approved.
5. **Monitoring and expiry**
   - Exceptions must be time-bound with an expiry date and periodic review.
   - Upon expiry, controls are reinstated or a renewal is processed.

## 9. Change management and CAB requirements
1. Changes to endpoint baselines, compliance policies, conditional access rules, EDR configurations, or update rings are **Normal Changes** and must be reviewed and approved through Change Enablement and the Change Advisory Board (CAB), unless classified as Emergency Change.
2. Emergency changes (e.g., active exploitation requiring immediate mitigation) must:
   - Be documented in the ITSM tool
   - Receive Emergency Change approval per Change Enablement practice
   - Be reviewed retrospectively by the CAB with evidence of effectiveness.

## 10. Service levels, monitoring, and reporting
### 10.1 Monitoring expectations
- Endpoint health and compliance must be monitored continuously using Intune dashboards, EDR console, and SIEM where applicable.
- Reporting must be available by region to support Regional IT Operations execution and Global IT Operations governance.

### 10.2 Remediation timelines (minimum)
| Control area | Non-compliance example | Required remediation time (maximum) | Enforcement action |
|---|---|---|---|
| EDR health | Sensor inactive/tampered | 24 hours | Conditional access restriction + incident escalation |
| Encryption | Not encrypted | 72 hours (or immediate if device contains confidential data) | Block access to protected resources |
| Critical patches | Missing critical security update | 7 days (expedited deployment) | Access restriction; forced update; escalation |
| Standard patches | Missing monthly security updates | 30 days | Progressive enforcement |
| Unsupported OS | OS out of vendor support | 14 days to plan replacement and mitigate; replacement executed per approved plan | Block for sensitive systems; replacement required |
| Local admin misuse | Unauthorized admin rights detected | 24 hours | Remove rights; security review |

## 11. Compliance and audit
1. Compliance is mandatory for all in-scope endpoints.
2. Internal Audit may request evidence of operating effectiveness; evidence must be time-bound, attributable, and repeatable in accordance with Norfolk Industries evidence principles.
3. Repeated or material non-compliance must be tracked via Problem Management and reported to the Head of IT Infrastructure Services and CISO.

## 12. Exceptions
- Exceptions must follow Section 8.4 and be recorded in the ITSM tool with:
  - Scope, justification, risk assessment, compensating controls
  - Approval record
  - Expiry date and review schedule
  - Verification that exception has been implemented as approved
- Exceptions impacting OT-connected endpoints must include validation that OT/IT segmentation and remote access controls remain effective.

## 13. Enforcement
- Access to corporate services may be restricted or revoked for non-compliant devices via conditional access and/or network access controls.
- Users and support teams must not bypass controls (e.g., disabling EDR, delaying patches, disabling encryption). Violations may result in disciplinary action consistent with HR policies and may trigger security incident response.

## 14. Definitions
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

## 15. Standards and control mappings
This section provides conceptual alignment to required frameworks. Control mapping evidence must follow Norfolk Industries evidence principles.

### 15.1 ISO/IEC 27001 (Annex A concept alignment)
| Endpoint control area | ISO/IEC 27001 Annex A (conceptual) | Expected evidence |
|---|---|---|
| Asset management & device inventory | Asset management and acceptable use controls | CMDB CI records; inventory exports |
| Access control & least privilege | Identity and access management controls | Local admin audits; privilege elevation logs |
| Cryptography | Encryption controls | BitLocker/FileVault compliance and escrow |
| Malware protection & monitoring | Protective technology and monitoring | EDR onboarding and health; alert handling records |
| Vulnerability and patch management | Technical vulnerability management | Patch compliance reports; change records |
| Logging & monitoring | Event logging and monitoring | SIEM forwarding status; audit logs |
| Incident response | Incident management controls | Incident tickets; response timeline evidence |

### 15.2 NIST CSF (functional alignment)
| Function | Endpoint & device management alignment |
|---|---|
| Identify | CMDB CIs, inventory, ownership, supported OS tracking |
| Protect | Encryption, least privilege, baselines, patching, conditional access |
| Detect | EDR monitoring, compliance reporting, SIEM integration |
| Respond | Lost device response, containment, remote wipe, incident workflow |
| Recover | Device replacement, re-provisioning, lessons learned and problem records |

### 15.3 SOC 2 Trust Services Criteria (conceptual)
| SOC 2 criterion | Endpoint control contribution |
|---|---|
| Security | EDR, encryption, least privilege, secure baselines |
| Availability | Patch discipline, standard builds, monitoring and event management |
| Confidentiality | Encryption, conditional access, BYOD restrictions |
| Processing Integrity | Standardized software deployment and configuration management |
| Privacy | Telemetry minimization, role-based access to device data, GDPR alignment |

### 15.4 ITIL 4 practice alignment
| ITIL 4 practice | How this policy supports it |
|---|---|
| Change Enablement | Baseline and policy changes governed by CAB |
| Incident Management | Lost/stolen and compromise response procedures |
| Problem Management | Repeat non-compliance trends addressed systematically |
| Service Configuration Management | Device CIs and lifecycle records in CMDB |
| Monitoring and Event Management | EDR and compliance monitoring |
| Information Security Management | ISMS-aligned security requirements |
| Supplier Management | Endpoint suppliers and licensing governance |
| Service Continuity Management | Replacement and recovery readiness for endpoint disruptions |

### 15.5 COBIT 2019 (domain alignment)
| COBIT domain | Endpoint & device management alignment |
|---|---|
| EDM | Governance of endpoint risk and compliance reporting |
| APO | Policy, standards, and lifecycle planning |
| BAI | Controlled rollout of baselines, tools, and updates |
| DSS | Operations, monitoring, incident handling |
| MEA | Compliance measurement and internal audit support |

## 16. Records management and evidence retention
1. Records must be stored in approved systems (ITSM tool, Intune/ConfigMgr reporting, EDR console, SIEM) and linked to the relevant ticket/change/CI where applicable.
2. Evidence must be:
   - **Time-bound** (date/time captured, relevant period)
   - **Attributable** (who performed/approved)
   - **Repeatable** (method to reproduce)
3. Retention must follow Norfolk Industries records retention requirements and regulatory obligations (including SOX and GDPR principles).

## 17. Training and awareness
1. Endpoint Engineers, Service Desk staff, and Regional IT Operations must be trained on:
   - Enrollment and provisioning workflow
   - Lost/stolen device procedures
   - Compliance remediation steps and user communications
   - Exception handling and approval requirements
2. End users must receive guidance on:
   - Acceptable use, secure handling, reporting lost devices immediately
   - Prohibition on disabling encryption/EDR and installing unapproved software

## 18. Policy review and continual improvement
1. Global IT Operations and IT Infrastructure Services will review:
   - Compliance metrics and trends by region
   - Incident and problem trends (e.g., repeated non-compliance, malware outbreaks)
   - Audit findings and remediation status
2. Improvements will be prioritized via Change Enablement and validated post-implementation for effectiveness.

## 19. Appendices (templates, checklists, runbooks)
### Appendix A: Endpoint baseline checklist (minimum)
Use this checklist for validating a new baseline release and for spot-check audits.

| Category | Check | Pass criteria | Validation method | Evidence artifact |
|---|---|---|---|---|
| Enrollment | Device enrolled in Intune | Device visible and managed | Intune device record | Screenshot/export with device ID and timestamp |
| Identity | Device registered in Entra ID | Device shows registered/joined state | Entra ID device record | Export/policy report |
| CMDB | CI exists and linked to user/asset tag | CI complete with owner/location | CMDB CI record | CI record link/ID |
| Encryption (Windows) | BitLocker enabled | 100% volume encrypted | Intune compliance + device status | Compliance report + escrow verification |
| Encryption (macOS) | FileVault enabled | FileVault on; recovery escrow works | Intune/macOS report | FileVault status report |
| EDR | EDR onboarded and healthy | Active, no tamper | EDR console health | Device health report export |
| Firewall | Host firewall enabled | On; required profiles enforced | Policy report | Baseline policy export |
| Screen lock | Lock after inactivity | Meets regional minimum standard | Policy report | Compliance policy export |
| Local admin | No unauthorized local admins | Only approved groups | Scripted audit / Intune report | Local group membership report |
| Patching | Update rings assigned | Correct ring & deadlines | Intune update ring assignment | Policy assignment export |
| Software | Required apps installed | Apps present and current | Intune/ConfigMgr app status | Deployment status report |
| Logging | Required audit/logging enabled | Meets baseline settings | Policy report | Baseline configuration export |

### Appendix B: Device lifecycle SOP (standard operating procedure)
#### B.1 Intake and request
1. Request logged in ITSM tool with user, cost center, region, and required software.
2. Verify user identity and entitlement (manager approval where required).
3. Confirm device type aligns to role requirements and security constraints.

#### B.2 Provisioning and enrollment
1. Assign asset tag and create/update CI in CMDB.
2. Register device for automated provisioning (e.g., Autopilot for Windows where implemented).
3. Enroll into Intune and ensure:
   - Compliance policy assigned
   - Baseline configuration assigned
   - EDR onboarding initiated
4. Validate encryption and EDR health before issuing device.

#### B.3 Operate (steady-state)
1. Monitor compliance, patch status, and EDR health.
2. Deliver software via approved catalog and managed deployments.
3. Process incidents and service requests via Service Desk.
4. Track recurring issues via Problem Management.

#### B.4 Change and maintenance
1. Baseline updates follow Change Enablement and CAB approval.
2. Patch rings updated as needed with risk-based scheduling.
3. Validate impact via pilot ring and defined success criteria.

#### B.5 Transfer, refresh, and return
1. For device reassignment:
   - Retire from prior user
   - Wipe and re-provision
   - Update CI ownership and assignment records
2. For lifecycle refresh:
   - Migrate user data using approved tools
   - Re-provision new device and confirm compliance
3. For returns:
   - Confirm device check-in
   - Wipe/retire in Intune and update CI status

#### B.6 Decommission and disposal
1. Wipe device using approved secure method.
2. Remove corporate profiles, certificates, and tokens.
3. Update CMDB CI to decommissioned/disposed state with date and method.
4. Dispose via approved supplier channels and retain disposal evidence.

### Appendix C: Lost device response runbook (operational)
1. **Open Incident** in ITSM tool; capture device ID/asset tag, user, time, location, circumstances.
2. **Validate device status** in Intune and EDR (last check-in, risk signals).
3. **Containment decision**
   - If high risk (confidential data, suspicious activity, unknown location): remote wipe and session revocation.
   - If moderate risk: remote lock, force sign-out, increased monitoring; wipe if not recovered within defined window.
4. **Execute remote action** (lock/wipe/retire) in Intune; capture action log.
5. **Credential actions**: force password reset and revoke sessions via IAM workflow as directed.
6. **Security review**: check EDR alerts, unusual sign-ins, and data access patterns; escalate as needed.
7. **Replacement**: initiate new provisioning; confirm user access restored securely.
8. **Closure**: document actions taken, evidence links, and post-incident improvements.

### Appendix D: Compliance remediation runbook (operational)
1. Identify non-compliance category (encryption/EDR/patch/OS version/local admin).
2. Attempt automated remediation (policy re-sync, restart security services, push update).
3. Contact user with a remediation appointment window (Regional IT Operations time zone appropriate).
4. If unresolved:
   - Escalate to Endpoint Engineer queue
   - Apply access restriction via conditional access (where required and approved)
5. Validate compliance status restored; record evidence and close ticket.

### Appendix E: Audit evidence list (endpoint & device management)
Evidence must be time-bound, attributable, and repeatable.

| Evidence area | System of record | Evidence artifact | Frequency |
|---|---|---|---|
| Enrollment coverage | Intune / ConfigMgr | Device inventory export with managed status | Monthly |
| CI completeness | CMDB | CI report showing owner/location/status | Quarterly |
| Compliance enforcement | Entra ID + Intune | Conditional Access policy export + compliance report | Quarterly and upon change |
| Encryption compliance | Intune | Encryption compliance dashboard export | Monthly |
| Key escrow validation | Entra ID / AD | Sample recovery key escrow verification logs | Quarterly |
| EDR onboarding & health | EDR console | Onboarding status and health reports | Monthly |
| Local admin control | Endpoint reporting | Local admin membership audit report | Monthly |
| Patch compliance | Intune/ConfigMgr | Patch compliance dashboard and deployment logs | Monthly |
| Software deployment | Intune/ConfigMgr | App deployment status reports | Monthly |
| Remote wipe/lock actions | Intune + ITSM | Remote action audit log linked to incident | Per event |
| Exception register | ITSM tool | Exception records with approvals and expiry tracking | Monthly review |
| CAB approvals for baseline changes | ITSM tool | Change records + CAB approval evidence | Per change |
| Incident handling | ITSM tool | Incident records for lost/stolen and compromise cases | Per event; quarterly sampling |