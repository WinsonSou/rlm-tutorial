# Encryption & Key Management Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for encryption and cryptographic key management across Norfolk Industries to:
- Protect confidentiality and integrity of information in accordance with the Information Security Management System (ISMS).
- Reduce risk of unauthorized disclosure, tampering, and service disruption.
- Provide consistent, auditable controls for encryption and key lifecycle management across hybrid cloud, on-prem data centers, endpoints, and Operational Technology (OT) environments where applicable.

## 2. Scope
This policy applies to:
- All Norfolk Industries information assets, services, and systems managed by IT Infrastructure Services, including cloud (Microsoft Azure primary, AWS secondary), on-prem data centers, endpoints, identity platforms (Active Directory and Entra ID (Azure AD), then Entra ID), and monitoring/backup platforms.
- All Configuration Items (CIs) recorded in the ITSM tool CMDB that store, process, transmit, or protect Norfolk Industries information.
- Third parties processing Norfolk Industries data where contractual and technical controls are required.
- OT environments where encryption and key management are technically feasible and do not create unacceptable operational risk; OT/IT integration must follow segmentation and remote access controls.

## 3. Policy Statement
Norfolk Industries shall:
- Encrypt data based on classification, risk, and regulatory requirements, using approved cryptographic protocols and strong key management practices.
- Manage cryptographic keys and certificates through controlled lifecycle processes, including generation, distribution, storage, rotation, revocation, and destruction.
- Use centrally governed standards and evidence-based controls aligned to ISO/IEC 27001, NIST CSF, SOC 2 Trust Services Criteria, ITIL 4, COBIT 2019, GDPR, and SOX requirements.
- Ensure encryption and key management controls are operationalized through ITIL-aligned processes (Change Enablement, Incident Management, Service Configuration Management) and governed by Global IT Operations with regional execution by Regional IT Operations.

## 4. Definitions
All definitions align to the Norfolk Industries glossary:
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

Additional policy terms (created for this document and used consistently):
- **Hardware Security Module (HSM)**: A tamper-resistant device or service designed to generate, store, and use cryptographic keys without exposing key material.
- **Key Management Service (KMS)**: A centralized service used to create, store, control access to, rotate, and audit cryptographic keys (including cloud-native key vault services).
- **Break-glass Access**: Pre-authorized emergency access method used only during incidents or outages, with enhanced monitoring and post-use review.

## 5. Roles and Responsibilities
Role responsibilities use Norfolk Industries canonical roles.

### 5.1 Responsibility Summary
| Role | Responsibilities (Encryption & Key Management) |
|---|---|
| CIO | Executive oversight of enterprise IT governance and risk posture. |
| Head of IT Infrastructure Services | Accountable for infrastructure encryption and key management outcomes across platforms and regions. |
| CISO | Accountable for ISMS oversight, cryptographic control requirements, and security risk acceptance inputs. |
| IT Governance Manager | Maintains this policy lifecycle, compliance tracking, and audit evidence coordination. |
| Service Owner | Ensures services meet encryption requirements, maintains key/certificate inventories for the service, and meets evidence obligations. |
| Platform Owner | Defines platform cryptographic standards, implementation patterns (KMS/HSM/cert services), and engineering controls. |
| IT Operations Manager | Ensures operational readiness (24×7), incident coordination for key compromise, and execution of approved procedures. |
| Security Engineer | Implements and validates cryptographic controls; integrates logs into SIEM; supports incident response for key compromise. |
| IAM Engineer | Supports certificate-based identity and access integrations and administrative access controls for key systems. |
| ITSM Process Owner | Ensures ITIL-aligned process integration (Change Enablement, Incident Management, CMDB, evidence workflows). |
| Internal Audit | Independently assesses control design and operating effectiveness. |
| Data Protection Officer (DPO) | Provides oversight for privacy requirements related to encryption for personal data and GDPR alignment. |

### 5.2 RACI Alignment (selected activities)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval (crypto standards) | I | A | C | R | C | R | C | C | I |
| Procedure ownership (key/cert procedures) | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing (crypto-impacting change) | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy Requirements

### 6.1 Data States and Mandatory Encryption
Norfolk Industries shall apply encryption controls for the following data states:

#### 6.1.1 Data at Rest
Encryption at rest is required when any of the following apply:
- Data is stored on cloud services, databases, storage accounts/buckets, virtual machine disks, backups, or endpoint devices.
- Data includes personal data subject to GDPR, financial data subject to SOX controls, security logs, credentials, secrets, or sensitive operational data.
- The system is internet-facing, accessible by third parties, or resides in a shared services environment.

Minimum requirements:
- Use industry-standard, strong encryption (conceptually equivalent to AES-256 or better) where supported.
- Use platform-native encryption where available and centrally managed keys where required by risk.
- Keys for encryption at rest must be protected by KMS and/or HSM controls; direct human access to key material is prohibited except where explicitly approved under an exception.

#### 6.1.2 Data in Transit
Encryption in transit is required for:
- All external communications over untrusted networks (including internet and partner connections).
- All administrative access to infrastructure services.
- All service-to-service communication carrying authentication tokens, personal data, or sensitive business data.

Minimum requirements (conceptual):
- TLS 1.2 or TLS 1.3 for HTTPS and application transport security.
- Secure shell (SSH) for administrative access using strong key-based authentication.
- VPN or equivalent secure tunnel for remote access when TLS is not sufficient for the protocol.

Prohibited:
- SSL, TLS 1.0/1.1, and deprecated/weak cipher suites.
- Cleartext protocols for sensitive data (including Telnet, FTP, HTTP for sensitive paths, and unencrypted database connections).

#### 6.1.3 Data in Use
For data in use (processed in memory/compute):
- Services handling sensitive data shall use platform protections to reduce exposure (e.g., least privilege, hardened runtime, secure enclaves where appropriate, and protected secrets handling).
- Secrets and keys must not be stored in application code, scripts, or configuration files in plaintext.
- Where supported, use managed identity patterns and secret stores integrated with KMS.

### 6.2 Approved Cryptographic Approaches (Conceptual Baselines)
Norfolk Industries uses conceptual baselines to remain technology-agnostic while requiring strong cryptography:
- Symmetric encryption: AES-class algorithms (128-bit minimum; 256-bit preferred for high-risk data).
- Asymmetric encryption: RSA 2048-bit minimum or ECC-class equivalents.
- Hashing: SHA-256-class or stronger.
- Key exchange and TLS: ECDHE-class forward secrecy where available; avoid static key exchange.
- Certificates: X.509 certificates issued by approved internal or external certificate authorities.

Platform Owners shall publish and maintain implementation standards for Azure, AWS, and on-prem platforms consistent with this policy and validated by Security Engineer controls.

### 6.3 Key and Certificate Lifecycle Management
All cryptographic keys and certificates must be managed through a defined lifecycle.

#### 6.3.1 Key Generation
- Keys must be generated using approved cryptographic libraries or KMS/HSM mechanisms.
- Keys must not be generated on end-user workstations for enterprise services unless explicitly approved and risk-assessed.
- High-value keys (e.g., CA keys, HSM master keys, key encryption keys) must be generated and stored in HSM-backed solutions where feasible.

#### 6.3.2 Key Storage and Protection
- Keys must be stored in approved KMS/HSM solutions. For cloud workloads, prefer cloud-native key vault services integrated with Entra ID.
- Private keys must never be stored in source code repositories or shared file shares.
- Access to keys must be role-based and granted using least privilege with enforced multi-factor authentication for administrative operations.
- Key usage must be logged, and logs forwarded to the SIEM for monitoring and alerting.

#### 6.3.3 Key Distribution and Use
- Keys must be distributed only via secure mechanisms (KMS APIs, secure secret stores, or certificate enrollment processes).
- Applications should use managed identities or workload identities to retrieve secrets/keys where supported, rather than embedded credentials.
- Separation of duties must be maintained: individuals who approve access should not be the same individuals who implement access without oversight in high-risk systems.

#### 6.3.4 Key Rotation
- Keys and certificates must be rotated on a scheduled basis and additionally upon personnel changes or risk events where applicable.
- Rotation schedules must be documented, tracked, and evidenced (see Appendix B).

Minimum rotation expectations:
- TLS certificates: rotate before expiry; operational target is renewal completed at least 30 days prior to expiration for externally facing services.
- High-risk secrets/keys used for encryption of sensitive data: rotate at intervals defined by Platform Owner standards and risk classification, and after suspected compromise.
- Backup encryption keys: rotate per platform capability while ensuring restorability and RPO/RTO alignment.

#### 6.3.5 Key Revocation and Destruction
- Certificate revocation must be performed promptly upon compromise, decommissioning, or invalid issuance.
- Keys must be destroyed securely when no longer required, ensuring that encrypted data retention requirements are met and decryption needs for legal hold or recovery are addressed.

### 6.4 Key Access Controls
- Administrative access to KMS/HSM platforms must be restricted to authorized roles (Platform Owner-approved groups) with privileged access management controls where applicable.
- Use just-in-time access patterns where feasible and enforce strong authentication via Entra ID.
- Break-glass Access must be:
  - Limited to a small, named group approved by the Head of IT Infrastructure Services with CISO concurrence.
  - Logged and monitored in the SIEM.
  - Reviewed post-event by IT Governance Manager and CISO.

### 6.5 Secrets Management
- Passwords, API keys, connection strings, and tokens are secrets and must be protected equivalently to cryptographic keys.
- Secrets must be stored in approved secret management solutions (KMS-integrated vaults) and retrieved securely at runtime.
- Secrets must be rotated when personnel with access leave the organization or change roles, and after any suspected exposure.

### 6.6 Logging, Monitoring, and Detection
- All key management operations (create, read/access, rotate, disable, delete, policy change, permission change) must be logged with user/service identity, timestamp, and action outcome.
- Logs must be centrally collected and retained in alignment with ISMS and legal requirements, and integrated with SIEM detection rules for anomalous key access and certificate misuse.
- Alerting must be configured for:
  - Break-glass Access usage.
  - Key deletion/disablement.
  - Permission escalations.
  - Certificate issuance anomalies for high-value namespaces/domains.

### 6.7 OT Considerations
- Encryption in OT must be implemented only where supported and validated to avoid unsafe conditions.
- Remote access into OT networks must use secure encrypted channels and strict access controls.
- Any OT encryption exceptions must be risk-assessed and approved through the exception process with CISO involvement and documented compensating controls.

### 6.8 Third-Party and Supplier Requirements
- Suppliers handling Norfolk Industries data must implement encryption in transit and at rest consistent with this policy and contractually commit to key management controls.
- Where Norfolk Industries controls encryption keys (customer-managed keys), suppliers must support segregation, access logging, and revocation processes.
- Evidence of supplier compliance must be collected and retained.

### 6.9 Exceptions
- Exceptions require documented risk assessment, compensating controls, and approvals per governance:
  - High-risk exceptions require approval by CIO (Accountable), Head of IT Infrastructure Services (Responsible), and CISO (Responsible) per RACI.
- All exceptions must have an expiration date and must be reviewed periodically.

## 7. Procedures (Operational Requirements)

### 7.1 Request a TLS Certificate (Internal or External)
1. **Initiate request in ITSM tool** as a Service Request:
   - Service name and Service Owner.
   - Fully qualified domain names (FQDNs), environment (prod/non-prod), region.
   - Intended use (public web, internal API, mutual TLS, device auth).
   - Certificate type (single, SAN, wildcard) and required validity period.
2. **Validation**:
   - Service Owner validates domain ownership/registration and business justification.
   - Platform Owner validates technical feasibility, supported ciphers/protocols, and endpoint configuration requirements.
   - Security Engineer validates compliance requirements (e.g., mutual TLS for sensitive service-to-service traffic).
3. **Approval**:
   - Normal certificate requests follow standard approval workflow.
   - High-risk requests (wildcards for sensitive zones, large SAN lists) require explicit Security Engineer review and Service Owner approval.
4. **Issuance**:
   - Use approved certificate authority (internal PKI or approved external CA).
   - Private keys must be generated and stored in KMS/HSM where supported; otherwise stored in an approved secure store with access controls.
5. **Deployment**:
   - Deploy through controlled automation or approved runbook.
   - Record certificate as a CI relationship (service ↔ certificate) in CMDB.
6. **Evidence**:
   - ITSM request record, approval trail, issuance logs, and deployment change record (if required).

### 7.2 Rotate Keys (Encryption Keys and Secrets)
1. **Plan rotation**:
   - Confirm rotation window, impacted services, rollback plan, and maintenance communications.
   - Determine if rotation is Normal Change; submit change for CAB review when customer impact is possible.
2. **Pre-rotation checks**:
   - Verify backups and recovery readiness consistent with service RPO/RTO.
   - Confirm that applications support key versioning or re-wrapping patterns.
3. **Execute rotation**:
   - Generate new key version in KMS/HSM.
   - Update applications/services to reference the new key version (prefer alias/identifier patterns to reduce code changes).
   - Re-encrypt data or re-wrap data encryption keys as applicable.
4. **Post-rotation validation**:
   - Validate service health, access patterns, and monitoring.
   - Confirm logs show expected key usage and no unauthorized access attempts.
5. **Decommission old keys**:
   - Disable old key versions after validation period, then schedule secure destruction per retention needs.
6. **Evidence**:
   - Change record (if applicable), KMS audit logs, validation results, and CMDB updates.

### 7.3 Revoke Certificates
1. **Trigger events**:
   - Suspected compromise, private key exposure, decommissioned service, incorrect issuance, or domain transfer.
2. **Initiate Incident or Service Request**:
   - Use Incident Management for compromise or urgent cases.
   - Use Change Enablement for planned decommissioning when revocation could cause service impact.
3. **Revoke**:
   - Revoke certificate in the issuing CA system; publish revocation (CRL/OCSP) per CA design.
4. **Replace**:
   - Issue a new certificate with new private key; deploy and validate.
5. **Contain**:
   - Block compromised endpoints, rotate related secrets, and invalidate sessions/tokens as needed.
6. **Evidence**:
   - Incident/change records, revocation logs, replacement issuance logs, and service validation.

### 7.4 Respond to Suspected Key Compromise
1. **Identify and classify** (Incident Management):
   - Determine scope: key type (TLS private key, KMS key, secret), affected services, and data exposure risk.
2. **Containment actions**:
   - Disable affected keys or key versions where possible.
   - Revoke impacted certificates immediately.
   - Restrict access policies (KMS IAM policy hardening) and disable suspected accounts.
3. **Eradication and recovery**:
   - Rotate keys and secrets; re-encrypt or re-wrap data encryption keys as required.
   - Redeploy certificates and enforce secure configs (TLS policies, cipher restrictions).
   - Restore service using validated configurations; confirm RPO/RTO impacts.
4. **Investigation and evidence**:
   - Collect KMS/HSM audit logs, SIEM alerts, system logs, change history, and access history from Entra ID and PAM tooling where applicable.
5. **Communication**:
   - Coordinate communications through IT Operations Manager and Security Engineer; engage Data Protection Officer (DPO) for privacy impact assessment where personal data is involved.
6. **Post-incident actions**:
   - Perform root cause analysis (Problem Management), update controls, and report to governance per ISMS requirements.

## 8. Change Management and CAB
- Any change that modifies encryption settings, key policies, certificate configurations, trust stores, KMS/HSM access controls, or could impact availability must follow Change Enablement.
- Changes with material risk, customer impact, or cross-region implications must be reviewed by the Change Advisory Board (CAB).
- Emergency Changes are permitted for suspected key compromise or active exploitation; they must be reviewed retrospectively by CAB with documented evidence.

## 9. Compliance, Measurement, and Reporting
### 9.1 Compliance Requirements
- Services must demonstrate encryption at rest and in transit compliance through configuration baselines and evidence artifacts.
- Key inventories must be current for in-scope services and maintained as part of Service Configuration Management.

### 9.2 Metrics (minimum)
| Metric | Description | Owner |
|---|---|---|
| Certificate expiry risk | Count of certificates expiring within 30 days | Service Owner |
| Key rotation compliance | Percentage of keys rotated within defined interval | Platform Owner |
| Unauthorized key access alerts | Number and severity of SIEM alerts for KMS/HSM access anomalies | Security Engineer |
| Break-glass Access usage | Count and outcomes of break-glass events with post-review completion | IT Operations Manager |
| CMDB key/cert coverage | Percentage of critical services with mapped key/cert CIs | ITSM Process Owner |

## 10. Audit and Evidence Retention
- Evidence must follow Norfolk Industries evidence principles: time-bound, attributable, repeatable; include approvals, logs, and validation artifacts.
- Audit evidence must be retained in accordance with ISMS requirements and legal/regulatory retention obligations (including GDPR and SOX considerations).
- Internal Audit may request samples demonstrating control operation across regions and platforms.

## 11. Risk Management and Exception Handling
- Encryption and key management risks must be captured in risk registers where applicable and tracked through ISMS governance.
- Exceptions must include:
  - Business justification
  - Risk assessment and compensating controls
  - Defined expiration date
  - Approval records aligned to the RACI requirements
  - Verification plan for remediation or reassessment

## 12. Data Protection and Privacy (GDPR)
- Encryption is a primary technical measure to reduce privacy risk and support confidentiality of personal data.
- Encryption does not replace the need for data minimization, access control, and lawful processing.
- Suspected compromise involving personal data requires coordination with the Data Protection Officer (DPO) for privacy impact and notification obligations.

## 13. Business Continuity and Disaster Recovery (ISO/IEC 22301 Alignment)
- Key management solutions (KMS/HSM, certificate authorities, secret stores) are critical dependencies and must be included in service continuity plans.
- Backup and recovery procedures must ensure:
  - Availability of keys required to restore encrypted backups.
  - Controlled access to recovery keys.
  - Restoration testing demonstrating RTO and RPO objectives can be met without exposing key material.

## 14. Training and Awareness
- Personnel with responsibilities for encryption and key management must complete role-appropriate training, including:
  - Secure key handling and secrets management
  - Certificate lifecycle processes
  - Incident response for suspected key compromise
  - Change Enablement and evidence expectations

## 15. Policy Enforcement
Non-compliance may result in:
- Required remediation actions with defined deadlines.
- Increased monitoring and restricted access.
- Formal risk acceptance only through approved exception process.
- Disciplinary measures as permitted by Norfolk Industries governance and applicable law.

## 16. References (Governing Frameworks and Internal Alignment)
This policy aligns with:
- ISO/IEC 27001 (Annex A control areas, conceptually)
- NIST CSF (Identify, Protect, Detect, Respond, Recover)
- NIST SP 800-53 concepts (cryptographic protection, key management, audit/logging)
- SOC 2 Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy)
- ITIL 4 practices (Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, Service Continuity Management, Supplier Management)
- COBIT 2019 domains (EDM, APO, BAI, DSS, MEA)
- GDPR
- SOX (financial systems encryption and control evidence requirements)

## 17. Control Mappings (Standards Alignment and Evidence)
### 17.1 Control Mapping Summary
| Policy Control Area | ISO/IEC 27001 (conceptual) | NIST CSF | SOC 2 TSC | ITIL 4 Practices | COBIT 2019 Domains | Typical Evidence |
|---|---|---|---|---|---|---|
| Encryption at rest/in transit requirements | Cryptographic controls, data protection | Protect | Security, Confidentiality | Information Security Management | APO, DSS | Config baselines, architecture standards, scan results |
| Key lifecycle (gen/store/rotate/destroy) | Key management, cryptography governance | Protect | Security, Availability | Change Enablement, Service Configuration Management | BAI, DSS | KMS audit logs, rotation records, CMDB key inventory |
| Certificate management and revocation | Cryptographic controls | Protect, Respond | Security, Availability | Change Enablement, Incident Management | DSS | CA issuance/revocation logs, ITSM tickets |
| Monitoring and alerting on key access | Logging and monitoring | Detect, Respond | Security, Availability | Monitoring and Event Management | DSS, MEA | SIEM alerts, audit logs, incident records |
| Break-glass Access governance | Access control governance | Protect, Respond | Security | Incident Management, Change Enablement | EDM, DSS | Break-glass runbook, usage logs, approvals, post-review |
| Supplier encryption requirements | Supplier relationships | Identify, Protect | Security, Confidentiality | Supplier Management | APO, MEA | Contract clauses, supplier attestations, reviews |

### 17.2 Evidence Principles Application
| Evidence Requirement | Implementation in This Policy |
|---|---|
| Time-bound | Rotation records include timestamps; tickets and approvals date-stamped; logs retained with defined windows. |
| Attributable | Actions performed by named identities (Entra ID accounts, service principals); ITSM approvals tied to roles. |
| Repeatable | Standard procedures (Sections 7.1–7.4) and templates (Appendices) define consistent execution. |
| Include approvals/logs/validation | CAB approvals, CA/KMS logs, SIEM alerts, service validation checks included for key events. |

## 18. Document Governance
### 18.1 Ownership and Maintenance
- Policy Owner: **IT Governance Manager**
- Accountable Executive: **Head of IT Infrastructure Services**
- Security Oversight: **CISO**
- This policy is reviewed at least annually and upon significant changes to cryptographic standards, platform capabilities, regulatory requirements, or material incidents.

### 18.2 Version Control and Publication
- Published in the Norfolk Industries controlled document repository under the ISMS.
- Superseded versions are retained per record retention requirements and audit needs.

## 19. Appendices (Templates, Checklists, Runbooks)

### Appendix A: Key Inventory Template (Markdown Table)
Maintain one inventory per service and platform, and link records to the CMDB CI(s).

| Field | Required | Description |
|---|---:|---|
| Service Name | Yes | Name of the service/application the key protects. |
| Service Owner | Yes | Named Service Owner responsible for compliance and lifecycle. |
| Platform | Yes | Azure / AWS / On-prem / Endpoint / OT (if applicable). |
| Region | Yes | North America / Europe / APAC (or specific data center/cloud region). |
| Key/Certificate Identifier | Yes | KMS key ID / vault name + key name/version / certificate serial / thumbprint. |
| Key Type | Yes | Symmetric / Asymmetric / Certificate private key / Secret. |
| Intended Use | Yes | Encryption at rest, TLS, signing, token encryption, backup encryption, etc. |
| Data Classification | Yes | Classification category used by the service’s data handling standard. |
| Storage Location | Yes | KMS/HSM name; vault path; CA location (no private key material stored in inventory). |
| Access Control Groups | Yes | Entra ID groups/roles allowed to administer/use the key. |
| Break-glass Access Applicable | Yes | Yes/No; if yes, reference break-glass procedure record. |
| Rotation Interval | Yes | Interval (days/months) per platform standard and risk. |
| Last Rotated Date | Yes | Date of last successful rotation. |
| Next Rotation Due | Yes | Date calculated from interval; align to Appendix B calendar. |
| Certificate Expiry (if applicable) | Conditional | Not required for non-certificate keys. |
| Dependencies | Yes | Services/components relying on the key; include CI references. |
| Monitoring Enabled | Yes | Confirmation SIEM monitoring is enabled for key events. |
| Evidence Links | Yes | Links to ITSM tickets, change records, logs, and validation artifacts. |
| Exception Reference | No | Link to approved exception record if any. |

### Appendix B: Rotation Calendar Template
Use this calendar to plan rotations, ensure CAB coverage, and prevent expiry incidents.

| Month | Service | Key/Cert Identifier | Rotation Type | Planned Window | Change Record Required | CAB Required | Owner | Pre-check Completed | Post-validation Completed |
|---|---|---|---|---|---:|---:|---|---:|---:|
| January |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| February |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| March |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| April |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| May |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| June |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| July |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| August |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| September |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| October |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| November |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |
| December |  |  | Key rotation / Cert renewal / Secret rotation |  | Yes/No | Yes/No | Service Owner | Yes/No | Yes/No |

### Appendix C: Evidence List (Audit-Ready Artifacts)
The following evidence artifacts must be maintained and produced upon request. Evidence must be time-bound, attributable, and repeatable, including approvals, logs, and validation artifacts.

| Control Area | Evidence Item | Source System | Owner |
|---|---|---|---|
| Encryption at rest | Storage/database/disk encryption configuration export or policy assignment | Cloud platform / config management | Platform Owner |
| Encryption in transit | TLS configuration reports (protocol versions, cipher policy), endpoint configuration | Application gateway/load balancer configs / server configs | Service Owner |
| Certificate issuance | Certificate request ticket, approval trail, issuance log | ITSM tool + CA | Service Owner |
| Certificate deployment | Change record (if applicable), deployment pipeline logs, validation screenshots/output | ITSM tool + CI/CD logs | IT Operations Manager |
| Certificate revocation | Revocation record, CRL/OCSP publication proof, replacement cert details | CA | Security Engineer |
| Key inventory | Completed key inventory template linked to CMDB CIs | CMDB + repository | Service Owner |
| Key rotation | Rotation plan, CAB approval (when required), KMS audit logs, post-validation results | ITSM tool + KMS logs | Platform Owner |
| Key access control | Role assignments, Entra ID group membership evidence, PAM controls where applicable | Entra ID / PAM | IAM Engineer |
| Monitoring | SIEM rules enabled, alert history, log forwarding configuration | SIEM | Security Engineer |
| Break-glass Access | Approval record, usage logs, post-event review and corrective actions | ITSM tool + SIEM | IT Operations Manager |
| Incident response (key compromise) | Incident timeline, containment actions, eradication steps, lessons learned | ITSM tool | IT Operations Manager |
| Supplier controls | Contract clauses, supplier attestation reports, review records | Supplier management repository | IT Governance Manager |

### Appendix D: Break-glass Access Runbook (Key Systems)
#### D.1 Preconditions
- Break-glass Access may be used only when standard administrative access is unavailable or time-prohibitive during active service-impacting incidents or security events.
- Use must be approved by the IT Operations Manager during the event, with notification to the Security Engineer.

#### D.2 Steps
1. Open an Incident record in the ITSM tool and document justification, affected service, and timeframe.
2. Use break-glass credentials or emergency access mechanism per platform standard (PAM where applicable).
3. Perform only required actions to restore secure operations (e.g., rotate key, revert policy, restore access).
4. Capture command outputs/log references and document all actions in the Incident record.
5. Immediately disable/rotate any break-glass credentials used if the mechanism requires rotation after use.
6. Within one business day, IT Governance Manager coordinates post-event review with CISO and Head of IT Infrastructure Services.

#### D.3 Post-Event Review Checklist
- Confirm SIEM logs captured all actions.
- Confirm least privilege restored (temporary permissions removed).
- Confirm impacted keys/certs rotated/revoked if required.
- Confirm Problem Management record created if root cause requires control improvements.