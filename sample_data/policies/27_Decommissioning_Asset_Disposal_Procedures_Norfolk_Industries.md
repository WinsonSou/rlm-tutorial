# Decommissioning & Asset Disposal Procedures (Norfolk Industries)

## 1. Purpose
This document defines standardized procedures for securely decommissioning Information Technology (IT) and Operational Technology (OT)–connected assets, disposing of hardware and media, and tearing down cloud resources at Norfolk Industries. It ensures confidentiality, integrity, availability, safety, compliance, and auditability through verified secure wipe, controlled chain of custody, and evidence capture aligned to the Information Security Management System (ISMS), ITIL 4, COBIT 2019, NIST CSF concepts, SOC 2 Trust Services Criteria, GDPR, and SOX.

## 2. Scope
### 2.1 In Scope
- Physical assets: servers, endpoints, network equipment, storage arrays, removable media, backup media, OT-adjacent IT assets used for plant connectivity, and any device that stores Norfolk Industries data.
- Virtual and cloud assets: Azure subscriptions/resources, AWS accounts/resources, virtual machines, managed disks, databases, object storage, container registries, key management services, and associated identities, credentials, and DNS records.
- Records and evidence: approvals, wipe verification artifacts, asset inventory updates, vendor certificates, and chain-of-custody documentation.
- Disposal and recycling workflows for assets owned, leased, or managed by Norfolk Industries.

### 2.2 Out of Scope
- Physical building facilities disposal processes not related to IT/OT (handled by Facilities and Environmental Health & Safety processes).
- Purely paper records disposal (handled by Records Management and Privacy governance processes), except where IT Infrastructure Services is the executor for media shredding vendors.

## 3. Governance, Standards, and Control Objectives
### 3.1 Governance Alignment
- **ISO/IEC 27001 (ISMS):** Secure disposal, access revocation, asset management, evidence.
- **ISO/IEC 22301 (BCMS):** Continuity considerations during decommission; avoid unplanned service impact.
- **ITIL 4:** Change Enablement, Service Configuration Management (CMDB), Information Security Management, Supplier Management, Service Continuity Management.
- **COBIT 2019:** Governance and management practices across EDM/APO/BAI/DSS/MEA.
- **NIST CSF:** Identify, Protect, Detect, Respond, Recover.
- **SOC 2:** Security, Availability, Confidentiality, Privacy; and Processing Integrity where applicable.
- **GDPR:** Data minimization, retention/disposal, privacy risk reduction.
- **SOX:** Controls for systems impacting financial reporting; traceability of decommission approvals and evidence.

### 3.2 Evidence Principles (Required)
Evidence must be **time-bound, attributable, and repeatable**, and include **approvals, logs, and validation artifacts** where applicable.

## 4. Definitions (Glossary)
| Term | Definition |
|---|---|
| IT Infrastructure Services | The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations. |
| Global IT Operations | Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure. |
| Regional IT Operations | Regional teams executing day-to-day operations, local support, and implementation aligned to global governance. |
| Information Security Management System (ISMS) | The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001. |
| Change Advisory Board (CAB) | The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management. |
| Configuration Item (CI) | Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references. |
| Operational Technology (OT) | Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks. |
| Recovery Point Objective (RPO) | Maximum tolerable amount of data loss measured in time. |
| Recovery Time Objective (RTO) | Target time to restore a service after disruption. |

## 5. Roles and Responsibilities
### 5.1 Role Definitions (Authoritative)
Roles in this procedure use the Norfolk Industries standard role set from roles.json.

### 5.2 Responsibilities by Role
| Role | Key Responsibilities in Decommissioning & Disposal |
|---|---|
| CIO | Executive oversight of governance and risk posture for decommissioning impacting enterprise IT and SOX scope. |
| Head of IT Infrastructure Services | Accountable for execution consistency, standards adoption, and service outcomes across regions and vendors. |
| CISO | Oversight of security requirements, ISMS alignment, and high-risk exceptions (e.g., non-standard wipe or incident-driven disposal). |
| IT Governance Manager | Maintains procedure lifecycle, compliance tracking, audit readiness, and evidence coordination. |
| Service Owner | Ensures service risk assessment, dependency mapping, customer communications, and acceptance of decommission readiness. |
| Platform Owner | Defines technical teardown standards (cloud, network, endpoint, compute) and approves platform-specific steps. |
| IT Operations Manager | Coordinates operational execution, schedules, on-call coverage, and ensures no unapproved service disruption. |
| ITSM Process Owner | Ensures integration with Change Enablement, Incident/Problem Management, and Service Configuration Management (CMDB). |
| Internal Audit | Independently assesses control design and operating effectiveness. |
| Data Protection Officer (DPO) | Ensures disposal actions align to privacy requirements (GDPR) where personal data may be present. |

## 6. RACI (Procedure-Level)
RACI is derived from the Norfolk Industries master matrix and applied to this procedure’s activities.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Standard approval (wipe/teardown standards) | I | A | C | R | C | R | C | C | I |
| CAB chairing for decommission changes | I | A | C | C | R | R | R | R | I |
| Policy approval (governance requirements) | A | R | C | R | C | C | C | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 7. Preconditions and Triggers
### 7.1 Triggers
- Service/application retirement approved by Service Owner and funding/portfolio governance.
- Hardware refresh, end-of-lease return, or failure requiring replacement.
- Cloud modernization or migration completion (resource teardown).
- Security incident response requiring immediate isolation, seizure, or destruction of media/equipment.
- Contract termination with supplier or managed service provider requiring asset return or account closure.

### 7.2 Preconditions (Must Be Met Before Execution)
- Approved Change record in the ITSM tool (Normal or Emergency Change) with risk assessment and implementation plan.
- Completed dependency and impact assessment (including OT/IT integration and plant network considerations).
- Verified backup/retention requirements and legal hold checks (including GDPR and SOX considerations).
- Confirmed data classification and data locations (local disks, SAN, cloud disks, object storage, backups, logs).
- Asset identified in CMDB/inventory as a Configuration Item (CI) or recorded as a new CI before decommission.

## 8. Secure Wipe and Media Sanitization Standard
Norfolk Industries uses a **risk-based sanitization approach**. The default expectation is **cryptographic erase** or **secure overwrite** with verification, and **physical destruction** where required by risk, feasibility, or contract.

### 8.1 Sanitization Methods (Approved)
| Method | When Used | Minimum Requirement | Verification Requirement |
|---|---|---|---|
| Cryptographic erase (crypto-shred) | Self-encrypting drives, cloud-managed disks, storage with strong encryption and managed keys | Keys rendered unrecoverable (destroy/rotate) using approved key management; ensure disk encryption enabled prior | Evidence of key destruction/rotation logs; post-action validation that data is inaccessible |
| Secure overwrite | HDDs and media where overwrite is feasible | Overwrite all addressable space; tool must produce logs | Tool logs + independent spot-check verification |
| Secure erase (ATA/NVMe sanitize) | SSDs where supported | Use device sanitize commands via approved tools | Sanitization report + device status confirmation |
| Physical destruction | Media cannot be reliably sanitized, incident-driven seizure/destruction, high-risk data, or damaged media | Shredding/degaussing/crushing by approved vendor or controlled internal process | Vendor certificate + chain of custody + witness attestation |

### 8.2 Minimum Standards by Asset Type
| Asset Type | Default Standard | Notes |
|---|---|---|
| Servers and storage (on-prem) | Crypto erase if encrypted with managed keys; otherwise secure overwrite or sanitize; physical destruction if not verifiable | Storage arrays require LUN/volume validation and potential vendor-assisted sanitize |
| Endpoints (laptops/desktops) | Full-disk crypto erase (key destruction) where BitLocker is enabled; otherwise secure overwrite and reimage; physical destruction for failed drives | Confirm device removed from Intune/ConfigMgr and Entra ID as applicable |
| Network gear (switch/firewall/router) | Factory reset + secure erase of configuration, logs, and stored keys/certs; remove/rotate secrets | Treat removable storage (CF/SSD) as media requiring sanitize |
| Removable media (USB, SD) | Physical destruction preferred; otherwise secure overwrite with verification | High risk due to portability |
| Backup media (tapes) | Vendor-certified destruction or secure degauss + shred | Must meet retention and legal hold checks first |
| OT-adjacent IT assets | Follow IT standard plus OT access revocation | Coordinate with OT stakeholders due to plant impact |

### 8.3 Verification Requirements (Mandatory)
- **Two-person control** for high-risk sanitization events (systems containing regulated personal data, SOX-relevant financial systems, security tooling, identity systems, or privileged credential stores).
- **Tool-generated logs** retained as evidence (see Section 17).
- **Asset identity linkage**: serial number, CI identifier, hostname/resource ID, and media identifier must be recorded on wipe verification form.
- **Failed wipe handling**: if verification fails, escalate to Security Engineer and CISO for disposition (repeat sanitize, physical destruction, or forensic hold).

### 8.4 Chain of Custody Requirements
Chain of custody must be maintained from removal to final destruction/recycling/return:
- Sealed containers with tamper-evident labels for drives/media.
- Logged transfers at each handoff including date/time, from/to, purpose, and signatures.
- Secure staging area with controlled access managed by Regional IT Operations.

### 8.5 Vendor Certificates
For any third-party disposal/destruction:
- Vendor must be approved through Supplier Management practices.
- A **Certificate of Destruction/Disposal** must include: vendor name, date, method, asset identifiers (serial/media IDs), and responsible signatory.
- Certificates must be attached to the Change record and stored per evidence retention (Section 17).

## 9. Procedure: Decommission Server and Application Infrastructure (On-Prem and Virtual)
### 9.1 Plan and Approvals
1. **Initiate Change** in ITSM tool with scope, risk, implementation plan, rollback plan (where applicable), and communications.
2. Service Owner confirms:
   - Service retirement approval and stakeholder notification plan.
   - RPO/RTO and continuity implications (ISO/IEC 22301 alignment).
   - Downstream dependencies (integrations, APIs, file shares, OT data feeds).
3. Platform Owner confirms technical steps and sequencing.
4. CAB approval required for Normal Changes; Emergency Changes follow CAB emergency process and post-implementation review.

### 9.2 Technical Decommission Steps (On-Prem/VMware/Hyper-V as applicable)
1. **Dependency validation**:
   - Verify no active monitoring alerts suppressed artificially.
   - Confirm application traffic and job schedules stopped.
2. **Data handling**:
   - Confirm retention obligations met; export/archive required datasets.
   - Confirm legal hold status (if any) blocks disposal and requires secure preservation.
3. **Access revocation**:
   - Remove service accounts, local admins, scheduled tasks credentials.
   - Rotate shared secrets in vaults (e.g., PAM) when accounts are removed.
4. **Backup updates**:
   - Remove asset from backup schedules only after retention and archive requirements are satisfied.
   - Document last successful backup date/time and location.
5. **Disable and quarantine phase (recommended)**:
   - Power down or isolate for a defined validation window when risk warrants.
6. **CMDB updates**:
   - Update CI lifecycle status to “Retired” and relate disposal evidence.
7. **Sanitize storage/media**:
   - Execute secure wipe per Section 8; capture logs and verification.
8. **Deprovision compute**:
   - Remove from virtualization inventory; reclaim resources.
9. **Network and identity cleanup**:
   - Remove DNS records, DHCP reservations, load balancer pools, firewall rules, and monitoring targets.
   - Remove from Active Directory domain if applicable; remove certificates from PKI where relevant.
10. **Close Change** with evidence and implementation notes.

### 9.3 Special Handling: Systems in Scope for SOX
- Service Owner and IT Governance Manager confirm SOX control impacts.
- Evidence must include approval trail, asset identification, and wipe/destruction certificate.
- Decommission must not remove audit log sources prematurely; confirm log retention/export.

## 10. Procedure: Retire Network Gear (Switches, Firewalls, Routers, Wireless)
### 10.1 Plan and Approvals
- Change record required; CAB approval required for production network changes.
- Platform Owner validates topology impact and OT segmentation constraints.

### 10.2 Execution Steps
1. **Pre-checks**:
   - Confirm redundant path availability and maintenance window.
   - Export running configuration to approved secure repository if required for recordkeeping; protect as confidential.
2. **Credential and key handling**:
   - Remove device credentials from PAM.
   - Revoke certificates and keys stored on device (device identity certs, VPN certs).
3. **Traffic cutover**:
   - Move links, update routing, validate connectivity and monitoring.
4. **Sanitization**:
   - Perform factory reset and secure deletion of configs, logs, keys.
   - If device contains removable storage (SSD/CF), treat as media and sanitize/physically destroy per Section 8.
5. **Inventory/CMDB**:
   - Update CI status and relationships (site, circuits, VLANs, firewall policies references).
6. **Disposal/return**:
   - Coordinate with supplier for leased gear returns with chain of custody and confirmation of receipt.

### 10.3 OT/Plant Network Considerations
- Regional IT Operations must coordinate with OT stakeholders to ensure no impact to SCADA/MES connectivity, and maintain strict remote access controls.
- Do not relax segmentation during decommission activities.

## 11. Procedure: Endpoint Decommission and Disposal
1. **Validate device ownership and user assignment** in CMDB/endpoint management.
2. **Backup/transfer user data** per policy where required and lawful.
3. **Access revocation**:
   - Retire device in Intune and ConfigMgr (where used).
   - Remove device objects from Entra ID and Active Directory as appropriate.
4. **Secure wipe**:
   - Prefer crypto erase where full-disk encryption is enabled and keys are managed; otherwise perform secure overwrite with verification.
5. **Disposition**:
   - Redeploy (internal reuse) only after wipe verification is completed and recorded.
   - Dispose/recycle via approved vendor with certificate and chain of custody.
6. **Evidence**:
   - Attach wipe verification and vendor certificate to ITSM Change or Request record.

## 12. Procedure: Cloud Resource Teardown and Account Closure (Azure and AWS)
### 12.1 Governance Requirements
- Cloud teardown must be executed as a controlled Change with CAB oversight for production services.
- Service Owner confirms business retirement approval and data retention/archival requirements.
- Platform Owner defines teardown sequence and security controls.

### 12.2 Azure Teardown (Microsoft Azure Primary)
1. **Inventory and dependency mapping**
   - Enumerate resource groups, resources, managed identities, Key Vaults, storage accounts, private endpoints, VNets, peering, and monitoring/logging.
2. **Data retention and export**
   - Export required logs (e.g., activity logs, diagnostic logs) to approved storage with defined retention.
   - Validate retention for databases, storage blobs, backups, and snapshots.
3. **Identity and access cleanup**
   - Remove RBAC assignments and Privileged Identity Management eligible roles tied to the service.
   - Disable/delete managed identities where no longer required.
   - Revoke application registrations and credentials (client secrets/certificates) used by the service.
4. **Key and secret handling**
   - Rotate or delete secrets in Key Vault tied to the service; ensure crypto erase via key destruction when applicable.
5. **Resource deletion sequence**
   - Stop workloads, deallocate compute, remove scale sets/AKS nodes as needed.
   - Delete data plane resources after retention is satisfied: disks, snapshots, storage containers, databases.
   - Remove network constructs: private DNS zones, records, load balancers, public IPs, NAT gateways, NSGs, route tables, peering.
6. **DNS cleanup**
   - Remove public and private DNS records associated with service endpoints (A/CNAME/TXT/SRV).
   - Confirm no stale records remain that could enable takeover.
7. **Monitoring and SIEM**
   - Remove or update Microsoft Sentinel connectors, alert rules, and workbooks for the service.
   - Ensure decommission does not reduce required security logging coverage for retained systems.
8. **Subscription and tenant-level closure (when applicable)**
   - If retiring a dedicated subscription: confirm no remaining resources, budgets, policies, and role assignments; then follow subscription cancellation/closure process.
9. **Verification**
   - Evidence: deployment inventory, deletion logs, access revocation proof, and final “resource not found” validation for critical components.

### 12.3 AWS Teardown (Secondary)
1. **Inventory and dependency mapping**
   - Enumerate accounts (if applicable), VPCs, subnets, security groups, IAM roles/users, KMS keys, S3 buckets, snapshots, AMIs, CloudTrail, and CloudWatch.
2. **Data retention and export**
   - Export logs and required datasets; confirm S3 retention/lifecycle policies aligned to requirements.
3. **Credential revocation**
   - Delete/disable IAM access keys, roles, and instance profiles.
   - Revoke secrets in secrets management tools; rotate shared credentials.
4. **KMS key handling**
   - Schedule deletion of KMS keys only after confirming no dependencies and retention satisfied; capture evidence.
5. **Resource deletion sequence**
   - Terminate compute, delete load balancers, remove auto scaling groups.
   - Delete EBS volumes, snapshots (after retention), RDS instances (after snapshot/retention), S3 buckets (after retention).
   - Remove VPC and networking after dependent resources are removed.
6. **DNS cleanup**
   - Remove Route 53 records/hosted zones associated with the service.
7. **Account closure (when applicable)**
   - For dedicated AWS accounts: ensure billing, IAM, and security baselines are handled; then close account per AWS process with evidence.

### 12.4 Common Cloud Controls (Azure and AWS)
- **Credential revocation is mandatory** for service principals, API keys, tokens, certificates, and federation trust relationships tied to the retired service.
- **External exposure review**: confirm no public endpoints, orphaned IPs, or DNS entries remain.
- **Cost controls**: verify budgets/alerts updated; validate zero ongoing spend for retired services.
- **CMDB linkage**: update CI relationships to reflect retirement and attach teardown evidence.

## 13. Procedure: Disposal Approvals, Logistics, and Vendor Management
### 13.1 Disposal Approval Requirements
- Disposal must be linked to an ITSM record (Change or Request) and include:
  - Asset identifiers (CI ID, serial numbers, hostname/resource ID).
  - Data classification and sanitization method selected.
  - Approval by Service Owner and Platform Owner; CAB approval where required.
- High-risk exceptions (non-standard wipe, missing identifiers, incident-related media) require CISO involvement per governance.

### 13.2 Logistics and Secure Staging
- Assets awaiting disposal must be stored in a controlled-access staging location managed by Regional IT Operations.
- Media must be secured in tamper-evident containers; chain-of-custody log required.

### 13.3 Vendor Requirements
- Vendors must provide certificates of destruction/disposal and comply with contractual security obligations.
- Vendor pickups require identity verification, logged handoff, and documented transport tracking reference.
- Returned leased assets require proof of receipt and vendor confirmation of sanitization responsibilities where contractually assigned; Norfolk Industries still retains responsibility to ensure data is protected, typically through pre-return sanitization.

## 14. Exceptions and Risk Acceptance
- Exceptions are permitted only when:
  - Sanitization is not technically feasible (e.g., damaged media) or operationally unsafe.
  - A legal hold requires retention and blocks destruction.
  - Incident response requires preservation for forensics.
- All exceptions must include:
  - Risk assessment, compensating controls, and approval trail.
  - Evidence of final disposition (e.g., sealed storage for legal hold, destruction certificate when released).
- High-risk exceptions require approval by the Head of IT Infrastructure Services and the CISO, with CIO involvement where enterprise risk warrants.

## 15. Security, Privacy, and Safety Requirements
### 15.1 Security Requirements
- Least privilege during decommission: temporary access must be time-bound and removed after completion.
- All secrets must be rotated or revoked where exposure risk exists.
- SIEM/EDR coverage must be maintained until the asset is fully isolated or wiped; do not disable telemetry without approved plan.

### 15.2 Privacy (GDPR)
- Confirm whether personal data exists on the asset; if yes:
  - Ensure disposal method is appropriate to prevent re-identification.
  - Maintain evidence supporting lawful disposal and retention compliance.
- Data Protection Officer (DPO) must be engaged for disposals involving regulated personal data at scale or where cross-border transfer may occur via vendor handling.

### 15.3 Safety
- Follow safe handling for heavy equipment, batteries, and damaged devices.
- Coordinate with site safety procedures for secure destruction activities conducted on-site.

## 16. Quality Assurance and Validation
- Post-decommission validation must confirm:
  - Service is no longer reachable internally/externally.
  - DNS records removed and no dangling references remain.
  - Firewall rules and network paths removed or tightened appropriately.
  - Monitoring updated to avoid false alerts and to maintain coverage for remaining systems.
  - CMDB reflects accurate CI status, relationships, and linked evidence.
- For cloud teardown, validate:
  - No remaining resources by tag/service identifier.
  - No remaining IAM/RBAC assignments, secrets, certificates, or keys tied to the service.

## 17. Records, Evidence, and Retention
### 17.1 Evidence Artifacts (Minimum Set)
- Approved Change record (including CAB approval where applicable).
- Dependency and impact assessment summary.
- Asset inventory/CMDB updates (CI status change and identifiers).
- Secure wipe logs and verification form (Appendix B).
- Chain-of-custody logs for media and equipment.
- Vendor certificate of destruction/disposal (Appendix C) or proof of leased asset return receipt.
- Cloud teardown evidence: inventory export, deletion logs, access revocation evidence, DNS cleanup confirmation.

### 17.2 Evidence Quality Requirements
Evidence must be time-bound, attributable, and repeatable; include approvals, logs, and validation artifacts.

### 17.3 Retention and Access
- Evidence must be stored in approved repositories with access controlled by role and need-to-know.
- Retention must satisfy ISMS, audit (SOC 2 / SOX where applicable), and privacy obligations. Where records include personal data, minimize content and restrict access.

## 18. Control Mapping (Standards Alignment)
This mapping is conceptual and is maintained to support audit readiness and consistent control intent.

| Procedure Control Area | ISO/IEC 27001 (Annex A concept) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Typical Evidence |
|---|---|---|---|---|---|---|
| Asset lifecycle and disposal governance | Asset management; secure disposal | Identify, Protect | Security, Confidentiality | Service Configuration Management | APO, BAI, DSS | CMDB updates, approvals |
| Secure wipe and media sanitization | Media handling; cryptography | Protect | Security, Confidentiality | Information Security Management | DSS, MEA | Wipe logs, verification, certificates |
| Chain of custody | Physical security; media handling | Protect | Security | Supplier Management | APO, DSS | Chain-of-custody log, vendor handoff |
| Cloud resource teardown and access revocation | Access control; operations security | Protect, Recover | Security, Availability | Change Enablement; Monitoring and Event Management | BAI, DSS | IAM/RBAC removal logs, deletion logs |
| Change governance (CAB) | Change control | Protect, Respond | Security, Availability | Change Enablement | BAI, DSS | CAB approvals, change record |
| Audit readiness and evidence management | Compliance | Identify | Security | Information Security Management | MEA | Evidence register, audit trail |

## 19. Appendices (Templates, Checklists, Runbooks)

### Appendix A: Decommission Checklist (Standard)
| Step | Category | Action | Owner Role | Evidence Required | Completed (Y/N) |
|---|---|---|---|---|---|
| 1 | Governance | Create ITSM Change/Request and link affected CIs | IT Operations Manager | ITSM record ID |  |
| 2 | Governance | Confirm CAB approval (Normal) or Emergency process completed | ITSM Process Owner | CAB approval record |  |
| 3 | Risk | Complete dependency and impact assessment (OT/IT included as applicable) | Service Owner | Assessment summary attached |  |
| 4 | Data | Confirm retention requirements and legal hold status | IT Governance Manager | Retention/hold confirmation note |  |
| 5 | Backup | Confirm last successful backup and archive/export if required | Systems Engineer / Cloud Engineer | Backup job/log proof |  |
| 6 | Identity | Revoke service accounts, API keys, certificates, secrets; rotate shared secrets | IAM Engineer / Security Engineer | Access revocation logs, vault records |  |
| 7 | Monitoring | Update monitoring and SIEM rules/connectors | Security Engineer | Change log/screenshots/export |  |
| 8 | Network | Remove firewall rules, VIPs, routes, VPN profiles, and related access | Network Engineer | Change evidence, config diffs |  |
| 9 | DNS | Remove public/private DNS records; validate no stale records remain | Platform Owner | DNS change logs |  |
| 10 | Sanitization | Execute secure wipe/crypto erase/sanitize per standard | Systems Engineer / Endpoint Engineer | Wipe logs |  |
| 11 | Verification | Complete wipe verification (two-person control when required) | IT Operations Manager | Signed verification form |  |
| 12 | Cloud | Delete resources in correct sequence; validate zero remaining resources | Cloud Engineer | Inventory + deletion logs |  |
| 13 | CMDB | Update CI status to Retired; attach evidence references | IT Operations Manager | CMDB change record |  |
| 14 | Disposal | Package and label media; maintain chain of custody | Regional IT Operations | Chain-of-custody log |  |
| 15 | Vendor | Obtain disposal/destruction certificate or return receipt | IT Governance Manager | Certificate/receipt |  |
| 16 | Closure | Close Change with implementation notes and evidence | IT Operations Manager | Closed Change record |  |

### Appendix B: Wipe Verification Form (Standard)
#### B.1 Asset Identification
| Field | Value |
|---|---|
| ITSM Record ID | |
| CI Identifier | |
| Asset Type | |
| Manufacturer / Model | |
| Serial Number | |
| Hostname / Resource ID | |
| Location (Site/Region) | |
| Data Classification (highest known) | |
| Encryption Status (e.g., BitLocker/SED/KMS) | |

#### B.2 Sanitization Details
| Field | Value |
|---|---|
| Sanitization Method Used (crypto erase / overwrite / sanitize / destruction) | |
| Tool/Command Used | |
| Tool Version | |
| Start Date/Time (UTC) | |
| End Date/Time (UTC) | |
| Operator (Name/Role) | |
| Second Verifier (Name/Role, if required) | |

#### B.3 Verification Results
| Verification Item | Result (Pass/Fail) | Notes |
|---|---|---|
| Tool-generated report captured and attached |  |  |
| Serial number/media ID matches report |  |  |
| Spot-check validation performed (if overwrite) |  |  |
| Crypto key destruction/rotation evidence captured (if crypto erase) |  |  |
| Device boots to blank/uninitialized state (where applicable) |  |  |
| Exceptions encountered (describe) |  |  |

#### B.4 Sign-Off
| Sign-Off | Name | Role | Date/Time (UTC) | Signature/Attestation |
|---|---|---|---|---|
| Performed By |  |  |  |  |
| Verified By |  |  |  |  |
| Approved for Disposal/Return |  |  |  |  |

### Appendix C: Disposal / Destruction Certificate Template (Vendor or Internal)
| Field | Value |
|---|---|
| Certificate ID | |
| Disposal Vendor Name | |
| Vendor Contact (Name/Phone/Email) | |
| Disposal Method (shred/degauss/crush/recycle/return) | |
| Disposal Location (Facility Address) | |
| Date/Time of Destruction/Disposal (UTC) | |
| Transport Tracking Reference (if applicable) | |
| Norfolk Industries ITSM Record ID | |
| Norfolk Industries Custodian (Name/Role) | |
| Vendor Authorized Signatory (Name/Title) | |
| Statement of Assurance | “The assets/media listed below were disposed of/destroyed using the method stated, rendering data unrecoverable.” |

#### C.1 Asset/Media Listing
| CI ID | Asset Type | Serial/Media ID | Quantity | Sanitization Method (if performed prior) | Notes |
|---|---|---|---|---|---|

### Appendix D: Chain of Custody Log (Standard)
| Date/Time (UTC) | Item (CI/Serial/Media ID) | Action (Collected/Stored/Transferred/Destroyed/Returned) | From (Name/Role) | To (Name/Role/Vendor) | Location | Tamper Seal ID | Signature/Attestation |
|---|---|---|---|---|---|---|---|

### Appendix E: Evidence List (Minimum) for Audit Readiness
| Evidence Item | Description | Source System / Location | Owner Role |
|---|---|---|---|
| ITSM Change/Request record | Scope, approvals, CAB decision, implementation notes | ITSM tool | IT Operations Manager |
| CAB approval record | Approval trail for Normal/Emergency Changes | ITSM tool | ITSM Process Owner |
| CMDB CI update | CI retired status and relationships updated | ITSM tool (CMDB) | IT Operations Manager |
| Dependency/impact assessment | Documented technical and business dependencies | Change attachments | Service Owner |
| Wipe tool report/log | Time-stamped sanitize output mapped to asset ID | Secure repository / Change attachments | Systems Engineer / Endpoint Engineer |
| Wipe verification form | Completed verification and sign-off | Change attachments | IT Operations Manager |
| Key destruction/rotation logs | Evidence for crypto erase and secret revocation | Key management / PAM logs | IAM Engineer / Security Engineer |
| DNS cleanup evidence | Records removed; validation results | DNS management logs | Platform Owner |
| Cloud deletion evidence | Inventory export + deletion logs; final state validation | Azure/AWS logs; Change attachments | Cloud Engineer |
| Vendor disposal certificate | Certificate with method and asset IDs | Vendor doc + secure repository | IT Governance Manager |
| Chain-of-custody log | Handoffs and secure storage tracking | Secure repository | Regional IT Operations |
| Return receipt (leased assets) | Proof of delivery/receipt by lessor | Vendor portal/email archived | IT Governance Manager |