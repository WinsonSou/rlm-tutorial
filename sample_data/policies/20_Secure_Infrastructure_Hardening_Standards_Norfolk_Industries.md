# Secure Infrastructure Hardening Standards (Norfolk Industries)

## 1. Purpose
This standard defines mandatory secure configuration requirements (“hardening”) for infrastructure platforms operated or managed by Norfolk Industries. It establishes consistent security baselines, approval and exception handling, validation scanning, and drift remediation to reduce cyber risk and support the Information Security Management System (ISMS), service reliability, and regulatory obligations.

## 2. Scope
### 2.1 In Scope
- **Windows Server** and Windows-based infrastructure components.
- **Linux** servers (major enterprise distributions supported by Norfolk Industries).
- **Network devices** (routers, switches, firewalls, wireless controllers, load balancers, VPN concentrators).
- **Hybrid cloud** controls for **Microsoft Azure (primary)** and **AWS (secondary)**, including:
  - Subscriptions/accounts, management groups/organizations, resource governance
  - Network and identity configurations
  - Logging, monitoring, and security services
- **Identity-integrated hardening** aligned with Active Directory and **Entra ID (Azure AD)** (first mention), then **Entra ID**.
- Systems supporting **Operational Technology (OT)** environments where **Information Technology (IT)**-managed infrastructure components exist (e.g., jump hosts, remote access gateways), without changing OT vendor-certified configurations unless explicitly approved.

### 2.2 Out of Scope
- Application-level secure coding standards (covered by application security standards).
- Pure OT controllers and vendor-managed OT appliances where configuration changes may violate certification, except where Norfolk Industries controls the IT-facing components (e.g., remote access, identity, logging).

## 3. Audience
- Global IT Operations
- Regional IT Operations
- IT Infrastructure Services
- Information security engineering and monitoring teams
- Service Owners and Platform Owners for infrastructure services
- Internal Audit (for assurance and evidence review)

## 4. Definitions (Canonical)
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.

## 5. Roles and Responsibilities
### 5.1 Role Summary
| Role | Responsibilities in this Standard |
|---|---|
| CIO | Executive oversight of IT governance outcomes for Norfolk Industries. |
| Head of IT Infrastructure Services | Accountable for adoption and operationalization of hardening baselines across IT Infrastructure Services. |
| CISO | Accountable for security requirements alignment to the ISMS and risk posture. |
| IT Governance Manager | Owns standards lifecycle, compliance tracking, and audit coordination for this standard. |
| Service Owner | Accountable that services meet baseline requirements, including logging and validation evidence. |
| Platform Owner | Defines platform-specific baseline technical requirements and implementation patterns. |
| IT Operations Manager | Ensures 24×7 operational readiness for monitoring, drift remediation, and response coordination. |
| Security Engineer | Implements security tooling integrations (SIEM, EDR, vuln scanning) and validates detection/logging requirements. |
| Systems Engineer / Cloud Engineer / Network Engineer | Implements and maintains hardening controls on managed platforms. |
| ITSM Process Owner | Ensures Change Enablement and related ITIL practices support baseline enforcement and exceptions workflow. |
| Internal Audit | Independently assesses design and operating effectiveness; consumes evidence artifacts. |
| Data Protection Officer (DPO) | Consulted for privacy impacts of logging/telemetry and GDPR alignment. |

### 5.2 RACI Alignment (Selected)
RACI aligns to the Norfolk Industries master RACI for governance activities; baseline standards approval and evidence coordination follow the same accountability structure.

## 6. Standard Statements (Mandatory Requirements)
### 6.1 Baseline Requirement
1. All in-scope platforms **must implement an approved secure configuration baseline** defined by the relevant Platform Owner and approved per Section 12.
2. Baselines must be conceptually aligned to **CIS Benchmarks** (or equivalent recognized hardening guidance) and mapped to Norfolk Industries control frameworks (Section 18).
3. Baselines must address, at minimum:
   - Secure configuration settings
   - Identity and access management (least privilege, administrative controls)
   - Cryptography requirements
   - Logging and monitoring
   - Vulnerability and patch management integration
   - Remote access and management plane protection
   - Time synchronization
   - Drift detection and remediation processes

### 6.2 Baseline Applicability and Classification
1. Each baseline must define applicability by system classification (e.g., production vs non-production), exposure (internet-facing vs internal), and environment (IT vs IT-managed OT support).
2. Where vendor support constraints exist (especially for OT-adjacent systems), deviations must follow Section 13.

### 6.3 Control Enforcement and Automation
1. Where technically feasible, baselines must be enforced using automation:
   - Windows: Group Policy Objects (GPO), security templates, Desired State Configuration, Microsoft Intune/ConfigMgr where appropriate
   - Linux: configuration management tooling and hardened images
   - Network: standardized configuration templates and centralized management platforms
   - Cloud: policy-as-code and guardrails (e.g., Azure Policy, AWS Organizations SCPs where used), and CI/CD validation gates
2. Manual configuration is permitted only when automation is not feasible and must be validated using Section 15.

## 7. Windows Server Hardening Baseline
### 7.1 Identity, Authentication, and Authorization
- Enforce domain-based administration and tiered administrative model for privileged operations.
- Local accounts:
  - Disable or rename default local Administrator where feasible.
  - Ensure local admin password management is implemented using an enterprise-controlled method.
- Privileged access:
  - Administrative access requires strong authentication and must be logged.
  - Separate administrative accounts from standard user accounts.

### 7.2 System Configuration
- Security settings must be applied via an approved baseline (conceptually aligned to CIS Windows Server guidance), including:
  - Account lockout and password policies (where applicable to local policies)
  - Restriction of anonymous access
  - Disable legacy/insecure protocols and ciphers (e.g., disable SMBv1; restrict NTLM where feasible)
  - Disable unnecessary services and roles
  - Secure remote management configuration (WinRM constrained to management networks and approved endpoints)
- Time synchronization:
  - Systems must synchronize time with approved enterprise time sources to support forensics and SIEM correlation.

### 7.3 Host Firewall and Network Protections
- Windows Defender Firewall must be enabled with inbound default-deny policy except explicitly required ports.
- RDP:
  - Allowed only from authorized management networks or approved jump hosts.
  - Network Level Authentication enabled; session timeouts configured.

### 7.4 Endpoint Detection and Response (EDR)
- Microsoft Defender for Endpoint (or Norfolk Industries-approved EDR) must be installed, healthy, and reporting.
- Tamper protection must be enabled unless an approved exception exists.

### 7.5 Logging (Windows)
- Enable and forward security-relevant logs to the SIEM (e.g., Microsoft Sentinel):
  - Security event logs (logon/logoff, privilege use, account management)
  - System and application logs relevant to service operation
  - PowerShell logging (module/script block logging where feasible)
  - Windows Defender/EDR alerts and operational logs
- Logs must be attributable to host identity and time-synchronized (Section 7.2).

## 8. Linux Hardening Baseline
### 8.1 Identity, Authentication, and Privilege Management
- Enforce centralized authentication where feasible and approved (directory integration) with least privilege.
- Root access:
  - Direct remote root login must be disabled.
  - Use `sudo` with named accounts; privileged actions must be logged.
- Multi-factor authentication must be used for administrative access where supported by the access path (e.g., via privileged access gateways).

### 8.2 Secure Configuration
- Apply an approved baseline conceptually aligned to CIS Linux Benchmarks, including:
  - Disable unnecessary packages/services
  - Secure SSH configuration (protocol 2 only, strong ciphers/MACs, disable password auth where feasible)
  - Kernel and network hardening parameters appropriate to service function
  - File permissions and ownership standards for system and service accounts
- Time synchronization must be enabled using approved enterprise time sources.

### 8.3 Host Firewall and Network Protections
- Linux host firewall must be enabled (e.g., `nftables`/`iptables`/firewalld as applicable) with default-deny inbound unless required.
- Administrative access must be restricted to management networks and approved jump hosts.

### 8.4 EDR and Malware Protections
- Where supported, install Norfolk Industries-approved EDR agent and ensure reporting health.
- If EDR is not supported (e.g., constrained systems), implement compensating controls:
  - Increased network monitoring
  - Enhanced logging
  - Tightened access controls
  - Documented exception per Section 13

### 8.5 Logging (Linux)
- Forward security and operational logs to SIEM:
  - Authentication logs (e.g., `auth.log`/`secure`)
  - Syslog/journald events for system and service operation
  - Sudo logs and privileged command auditing where feasible
  - EDR alerts (if installed)
- Ensure consistent host identifiers and time synchronization.

## 9. Network Device Hardening Baseline
### 9.1 Management Plane Security
- Management access must be restricted to authorized management networks and approved administrative endpoints.
- Use strong authentication and centralized authorization where feasible.
- Disable insecure management protocols (e.g., Telnet, HTTP) and require secure alternatives (e.g., SSH, HTTPS).
- Enforce cryptographic standards for management interfaces (strong ciphers, modern TLS versions).
- Use unique credentials; shared credentials are prohibited except break-glass with controlled storage and audit.

### 9.2 Configuration Standards
- Standardize device configurations using approved templates:
  - Banner and legal notice (as required by policy)
  - Session timeout and lockout controls
  - AAA configuration
  - Disable unused interfaces and services
  - Restrict SNMP to secure versions (SNMPv3 preferred) and authorized managers only
- Configuration backups:
  - Maintain automated configuration backups in a controlled repository with access logging.
  - Protect backups as sensitive assets.

### 9.3 Network Security Controls
- Enforce segmentation and least privilege routing/ACL design consistent with IT/OT segmentation requirements.
- Remote access:
  - Must use approved secure remote access controls and be auditable.
- For internet-facing services (VPN, edge firewalls, load balancers):
  - Enforce hardened cipher suites
  - Enable DoS protections where supported
  - Ensure logging is enabled and forwarded (Section 11)

### 9.4 Logging (Network)
- Send logs to SIEM:
  - Authentication/authorization events
  - Configuration change events
  - VPN/session events
  - Threat and policy events (firewalls/IDS/IPS where applicable)
- Logs must be time-synchronized with approved enterprise time sources.

## 10. Cloud Baseline Controls (Azure and AWS)
### 10.1 Identity and Access Management
- Entra ID must be the authoritative identity provider for Azure access; federated access for AWS must follow approved identity architecture.
- Enforce least privilege using role-based access control:
  - Separate administrative roles from day-to-day roles
  - Use privileged access management controls (e.g., CyberArk) for privileged credentials where applicable
- Prohibit long-lived access keys where feasible; prefer short-lived tokens and modern authentication methods.
- Require strong authentication for privileged access, including conditional access patterns appropriate for risk.

### 10.2 Resource Governance and Policy
- Enforce guardrails via policy:
  - Restrict resource creation to approved regions aligned with Norfolk Industries data residency and business requirements.
  - Require tagging standards to support ownership, cost management, and incident response.
  - Require encryption at rest for supported services.
  - Require private connectivity options for sensitive services where feasible.
- Prevent public exposure:
  - Public IP assignment and open security group rules must be controlled and approved.
  - Storage services must block public access unless explicitly approved and risk-assessed.

### 10.3 Network Baseline
- Use segmented virtual networks/VPCs with controlled routing between tiers.
- Require centralized ingress/egress controls and logging.
- Administrative access to cloud workloads must use approved secure remote access patterns (e.g., jump hosts, bastions) with logging.

### 10.4 Cloud Logging and Monitoring
- Centralize cloud audit and activity logs to the SIEM:
  - Azure: subscription activity logs, identity sign-in/audit logs where applicable, resource diagnostics logs for critical services
  - AWS: account activity logs (e.g., CloudTrail concept), configuration and security findings where applicable
- Logging must be:
  - Enabled by default for production subscriptions/accounts
  - Protected from tampering using access controls and retention policies
- Monitoring and alerting:
  - Security-relevant alerts must integrate into Global IT Operations monitoring and incident workflows.

### 10.5 Cloud Configuration Drift and Posture Management
- Implement continuous evaluation of cloud configurations using approved posture management and policy evaluation tools.
- Non-compliant resources must be remediated within defined timelines (Section 16).

## 11. Enterprise Logging and SIEM Requirements (All Platforms)
### 11.1 Minimum Logging Requirements
All in-scope systems must generate and forward logs that enable:
- Authentication and authorization tracking
- Privileged activity auditing
- Security control status (EDR health, policy violations)
- Configuration changes
- Network access and session tracking where applicable
- Service health and availability signals needed for incident response

### 11.2 Log Transport, Integrity, and Access
- Log forwarding must use secure transport and authenticated collectors where supported.
- Access to logs is restricted to authorized operational and security personnel; access must be logged.
- Logs must be time-synchronized and attributable to a specific CI.

### 11.3 Retention and Evidence
Retention must satisfy the ISMS, SOC 2 expectations, legal/regulatory requirements (including GDPR proportionality), and operational needs for investigations. The IT Governance Manager coordinates retention evidence with Service Owners and the CISO.

## 12. Baseline Lifecycle and Approval Procedure
### 12.1 Baseline Development
1. Platform Owner drafts baseline requirements and associated checklists (Appendix A).
2. Security Engineer reviews for logging/EDR/SIEM integration requirements and detection coverage.
3. Service Owners validate service impact and operational feasibility (24×7 considerations).

### 12.2 Baseline Approval
1. IT Governance Manager coordinates baseline review.
2. Head of IT Infrastructure Services approves the baseline standard update.
3. CISO is consulted for security risk acceptance alignment and ISMS consistency.
4. For changes that materially affect production operations, CAB review is required under Change Enablement.

### 12.3 Baseline Publication and Communication
- Approved baselines must be published in the ITSM knowledge repository and referenced in CI records where applicable.
- Regional IT Operations must be notified of adoption timelines and implementation instructions.

## 13. Deviation and Exception Management
### 13.1 When Exceptions Are Allowed
Exceptions may be requested when:
- Vendor support restrictions exist (common in OT-adjacent systems)
- Technical limitations prevent compliance
- Compliance would cause unacceptable service disruption and no feasible mitigation exists within required timelines

### 13.2 Exception Requirements
- Exceptions must be documented using the Exception Register template (Appendix B) and include:
  - Specific baseline control(s) not met
  - Business justification and risk description
  - Compensating controls
  - Scope (systems/CIs), duration, and expiry date
  - Monitoring and review cadence
- High-risk exceptions require approval per governance: Head of IT Infrastructure Services and CISO involvement, and escalation for executive visibility when required by risk level.

### 13.3 Exception Review and Closure
- Exceptions must be reviewed at least quarterly or upon material change.
- Exceptions must be closed when remediation is implemented or the system is retired.

## 14. Build and Deployment Standards
### 14.1 Golden Images and Standard Builds
- Windows and Linux builds must use approved hardened images or build pipelines.
- Network device deployments must use approved configuration templates.
- Cloud resources must use approved landing zones/guardrails and hardened reference architectures.

### 14.2 Configuration Item (CI) Requirements
- Each system must be represented as a CI with:
  - Owner (Service Owner) and technical contacts
  - Environment classification (prod/non-prod)
  - Data sensitivity classification (as applicable)
  - Baseline version applied
  - Logging integration status

## 15. Validation Scanning and Compliance Verification
### 15.1 Vulnerability Scanning
- All in-scope systems must be scanned using the approved vulnerability scanning platform (e.g., Tenable/Nessus) with frequency appropriate to criticality and exposure.
- Authenticated scanning is required where feasible to validate configuration and patch posture.

### 15.2 Configuration Compliance Validation
- Validate baseline compliance via:
  - Configuration compliance tooling (where available)
  - CIS-aligned benchmark assessment approaches (conceptual alignment)
  - Cloud policy compliance reports
  - Network configuration compliance checks
- Evidence must be time-bound, attributable, and repeatable per standards.json evidence principles.

### 15.3 Remediation Validation
- After remediation, re-scan or re-validate must be performed to confirm closure.
- Results must be attached to the relevant ITSM records (incident/problem/change as applicable) and linked to the CI.

## 16. Drift Remediation and Enforcement
### 16.1 Drift Detection
- Drift is any deviation from the approved baseline after initial implementation.
- Drift detection must be continuous where feasible (policy evaluation, configuration monitoring) and at minimum aligned to vulnerability scanning cycles.

### 16.2 Remediation Timelines (Risk-Based)
| Severity / Risk Indicator | Example Indicators | Target Remediation Timeline |
|---|---|---|
| Critical | Internet-facing weakness, privileged access exposure, active exploitation evidence | Immediate (expedite change; CAB process as applicable) |
| High | Significant baseline deviation increasing compromise likelihood | As soon as operationally feasible; prioritize within standard patch cycle |
| Medium | Non-critical deviation with limited exposure | Plan and remediate in scheduled maintenance window |
| Low | Minor hardening gaps with minimal risk | Address through continual improvement and standard build updates |

### 16.3 Emergency Changes
- If drift introduces imminent risk, remediation may require Emergency Change handling with CAB visibility per Change Enablement practice.

## 17. Metrics, Reporting, and Continual Improvement
### 17.1 Required Metrics
Service Owners and Platform Owners must report, at minimum:
- Percentage of in-scope CIs meeting baseline compliance
- Number of open exceptions and average age to closure
- Vulnerability findings related to configuration weaknesses (trend)
- Logging coverage (percentage of CIs forwarding required logs)
- EDR coverage and health reporting rates

### 17.2 Governance Reviews
- Global IT Operations reviews metrics with Regional IT Operations regularly to drive remediation and standard improvements.
- The IT Governance Manager coordinates audit readiness and evidence completeness.

## 18. Control Mapping (Framework Alignment)
This standard supports Norfolk Industries governance and assurance obligations and maps conceptually to the following:

### 18.1 ISO/IEC 27001 (Annex A Conceptual Areas)
| Baseline Topic | ISO/IEC 27001 Annex A Conceptual Alignment | Typical Evidence |
|---|---|---|
| Secure configuration baselines | Secure configuration management / technical controls | Approved baseline documents; CAB records for material changes |
| Access control hardening | Identity and access management controls | Role assignments; PAM logs; admin access audit logs |
| Logging and monitoring | Logging, monitoring, and event management | SIEM ingestion dashboards; alerting rules; log retention settings |
| Vulnerability and patch integration | Vulnerability management | Scan reports; remediation tickets; re-scan evidence |
| Network device hardening | Network security controls | Standard templates; config backup logs; device audit logs |
| Cloud guardrails | Cloud security governance | Policy compliance reports; landing zone controls; audit logs |

### 18.2 NIST CSF Mapping
| NIST CSF Function | How This Standard Supports |
|---|---|
| Identify | CI baseline versioning; asset coverage and ownership |
| Protect | Hardening settings, least privilege, encryption requirements |
| Detect | Centralized logging, EDR integration, SIEM alerting inputs |
| Respond | Evidence-ready logs and change governance for urgent remediation |
| Recover | Standard builds and drift remediation supporting restore to known-good |

### 18.3 SOC 2 Trust Services Criteria Mapping
| SOC 2 Criterion | Alignment Examples |
|---|---|
| Security | Baselines, access restrictions, secure management protocols |
| Availability | Drift remediation, controlled change, monitoring requirements |
| Confidentiality | Encryption requirements, access controls, logging protections |
| Processing Integrity | Configuration control and validation scanning reduce misconfiguration risk |
| Privacy | Logging governance and DPO consultation for proportionality and access control |

### 18.4 ITIL 4 and COBIT 2019 Alignment
| Reference | Alignment |
|---|---|
| ITIL 4 Practices | Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, Supplier Management, Service Continuity Management |
| COBIT 2019 Domains | EDM (governance oversight), APO (standards and risk), BAI (build/change), DSS (operations), MEA (monitoring and assurance) |

## 19. Document Governance
### 19.1 Ownership and Maintenance
- **Owner:** IT Governance Manager (governance lifecycle), with technical ownership shared by Platform Owners under Head of IT Infrastructure Services.
- **Security oversight:** CISO (ISMS alignment).
- **Review cadence:** At least annually, and additionally upon major platform changes, audit findings, or material incidents.

### 19.2 Compliance and Enforcement
- Compliance is mandatory for all in-scope CIs operated by IT Infrastructure Services.
- Non-compliance must be addressed via remediation (Section 16) or documented exception (Section 13).
- Evidence must meet principles: time-bound, attributable, and repeatable.

---

## Appendix A: Platform Baseline Checklists (Minimum Required Controls)

### A.1 Windows Server Baseline Checklist
| Control Area | Minimum Requirement | Validation Method | Evidence Artifact |
|---|---|---|---|
| Accounts and admin model | Separate admin accounts; restrict local admin membership | AD/GPO review; local group audit | Admin group membership export; baseline policy link |
| Local admin credential control | Local admin password managed; no shared uncontrolled credentials | Tool configuration review; audit logs | PAM/LAPS-equivalent reports; access logs |
| Insecure protocols | SMBv1 disabled; legacy protocols restricted where feasible | Config review; vuln scan | Registry/policy export; scan finding closure |
| Firewall | Enabled; inbound default deny; explicit rules only | Host firewall policy check | Firewall policy report; config snapshot |
| Remote access | RDP restricted to management paths; NLA enabled | Policy check; network ACL verification | GPO settings; firewall rules evidence |
| EDR | EDR installed, healthy, tamper protection enabled | EDR console health | EDR device inventory and health export |
| Logging | Security logs + PowerShell logs forwarded to SIEM | SIEM ingestion check; event sample | SIEM dashboard screenshot/export; log forwarding config |
| Time sync | Enterprise time source configured | Config check | Time service configuration output |

### A.2 Linux Baseline Checklist
| Control Area | Minimum Requirement | Validation Method | Evidence Artifact |
|---|---|---|---|
| Root access | Remote root login disabled; sudo used | SSHD config check; auth log review | `sshd_config` excerpt; sample sudo log events |
| SSH hardening | Strong ciphers/MACs; disable password auth where feasible | Config check; scan | SSH configuration output; scan report |
| Services | Unnecessary services removed/disabled | Service audit | Service list and enabled-state report |
| Firewall | Enabled; inbound default deny except required | Firewall rules review | Firewall rules export |
| EDR | Installed and reporting where supported | EDR console health | EDR inventory export or exception record |
| Logging | Auth/system/sudo logs forwarded to SIEM | SIEM ingestion check | Forwarder config; SIEM log samples |
| Time sync | Enterprise time source configured | NTP/chrony status | Time sync status output |

### A.3 Network Device Baseline Checklist
| Control Area | Minimum Requirement | Validation Method | Evidence Artifact |
|---|---|---|---|
| Secure management | SSH/HTTPS only; restrict mgmt access | Config review | Config excerpt showing mgmt ACLs and protocols |
| AAA | Centralized auth where feasible; unique credentials | AAA config review | AAA configuration export; access logs |
| Session control | Timeout, lockout, audit banner where required | Config review | Config excerpt |
| SNMP | SNMPv3 preferred; restrict managers | Config review | SNMP config excerpt |
| Config changes | Config change logging enabled | SIEM log review | SIEM event samples for config changes |
| Backups | Automated config backups secured | Backup system logs | Backup job logs; repository access logs |
| Time sync | NTP configured | Device status | NTP status output |

### A.4 Azure Baseline Checklist
| Control Area | Minimum Requirement | Validation Method | Evidence Artifact |
|---|---|---|---|
| Identity | Entra ID RBAC least privilege; privileged access controlled | Role assignment review | RBAC export; privileged access logs |
| Policy guardrails | Policy enforcing tags, encryption, restricted public exposure | Policy compliance review | Azure Policy compliance report export |
| Logging | Activity logs + resource diagnostics to SIEM | SIEM ingestion and settings review | Log settings export; SIEM dashboard |
| Network | Segmented VNets; controlled ingress/egress | Architecture and config review | Network diagram; NSG/route exports |
| Public access control | Restrict public storage and public IP usage | Policy and resource review | Policy evidence; resource compliance report |

### A.5 AWS Baseline Checklist
| Control Area | Minimum Requirement | Validation Method | Evidence Artifact |
|---|---|---|---|
| Identity | Federated access and least privilege roles; minimize long-lived keys | IAM review | IAM credential reports; role policies export |
| Guardrails | Organization/account controls to prevent risky configurations where used | Config/policy review | Compliance reports; guardrail configuration export |
| Logging | Account activity logs centralized to SIEM | Log pipeline validation | Log delivery configuration; SIEM dashboard |
| Network | Segmented VPCs; restricted security groups | Config review | Security group rules export; architecture diagram |
| Public exposure | Control public S3 access and open inbound rules | Compliance review | Public access block settings; SG compliance report |

---

## Appendix B: Exception Register Template (Hardening Baseline)
| Field | Required Content |
|---|---|
| Exception ID | Unique identifier from ITSM record |
| Date Raised | Date exception was submitted |
| Requestor | Name/role and team (Regional IT Operations or Global IT Operations) |
| Service Owner | Accountable Service Owner |
| Platform Owner | Accountable Platform Owner |
| CI(s) / Scope | CI identifiers, hostnames, device IDs, subscription/account IDs |
| Environment | Production / Non-production / OT support |
| Baseline Control(s) Not Met | Specific checklist items and expected configuration |
| Business Justification | Why compliance is not feasible now |
| Risk Description | Security and operational risk impact |
| Compensating Controls | Controls implemented to reduce risk (monitoring, segmentation, access restrictions) |
| Approval | Approvers and dates (Head of IT Infrastructure Services; CISO for security risk alignment as applicable) |
| Effective Date | Start date |
| Expiry Date | Mandatory end date for the exception |
| Review Cadence | At least quarterly; record review dates |
| Closure Criteria | What must be implemented to close |
| Evidence Links | Links/attachments to scans, configs, approvals |

---

## Appendix C: Evidence List (Audit-Ready Artifacts)
| Evidence Category | Minimum Evidence | Source System / Owner |
|---|---|---|
| Baseline approval | Approved baseline document version; approval record | ITSM knowledge repository / IT Governance Manager |
| CAB governance | CAB records for material baseline changes and emergency remediations | ITSM Change records / ITSM Process Owner |
| CI linkage | CI list with baseline version and ownership | CMDB / Service Owner |
| Vulnerability scanning | Scan schedules, authenticated scan results, remediation and re-scan proof | Vulnerability scanning platform / Service Owner |
| Configuration compliance | Policy compliance reports (cloud), configuration assessments (OS/network) | Cloud governance tools; platform tooling / Platform Owner |
| Logging to SIEM | SIEM ingestion evidence and sample events per platform | SIEM (e.g., Microsoft Sentinel) / Security Engineer |
| EDR coverage | Endpoint/server inventory and health reporting | EDR console / Security Engineer |
| Exception management | Exception register with approvals, compensating controls, and expiry tracking | ITSM / IT Governance Manager |
| Drift remediation | Tickets, change records, and post-remediation validation | ITSM / IT Operations Manager |
| Access control | RBAC exports, privileged access logs, administrative group membership | Directory/IAM tools / IAM Engineer |