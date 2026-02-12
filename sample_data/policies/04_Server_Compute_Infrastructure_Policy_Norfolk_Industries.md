# Server & Compute Infrastructure Policy (Norfolk Industries)

## 1. Purpose
This policy defines the minimum requirements for designing, building, operating, securing, and retiring server and compute infrastructure at Norfolk Industries. It ensures consistent, secure, and resilient server services across hybrid cloud (Microsoft Azure primary, AWS secondary) and on-prem data centers, aligned to the Information Security Management System (ISMS), ITIL 4, COBIT 2019, NIST CSF and NIST SP 800-53 concepts, SOC 2 Trust Services Criteria, GDPR, and SOX.

## 2. Scope
### 2.1 In Scope
- All Windows and Linux server operating systems running workloads for Norfolk Industries in:
  - On-prem data centers
  - Microsoft Azure
  - AWS
- Virtualization platforms and compute orchestration layers, including VMware and Hyper-V concepts (where deployed)
- Server images and templates (gold images), configuration standards, baseline hardening
- Server administration, privileged access, service accounts, logging, monitoring, and backup/restore
- Clustered systems (compute clusters, failover clusters, hyperconverged concepts where deployed)
- Interfaces supporting Operational Technology (OT) integrations when servers are hosted in IT zones that provide OT-facing services

### 2.2 Out of Scope
- End-user endpoints (covered under endpoint standards managed through Microsoft Intune and ConfigMgr where needed)
- Network infrastructure (covered by network standards)
- Application-specific secure coding and SDLC requirements (owned by application governance), except where they affect server configuration and runtime controls

## 3. Policy Statement
Norfolk Industries will:
- Standardize server builds using approved gold images and configuration baselines.
- Enforce least privilege and privileged access controls using Privileged Access Management (PAM) (e.g., CyberArk) and centrally managed identity via Active Directory and Entra ID (Azure AD) (then “Entra ID”).
- Maintain secure and supportable compute platforms through timely patching, vulnerability remediation, monitoring, and lifecycle management.
- Ensure resilience through standardized cluster design, backups, and tested restoration procedures aligned to business requirements (RTO/RPO).
- Provide auditable evidence of control operation that is time-bound, attributable, and repeatable.

## 4. Definitions
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
### 5.1 Governance and Accountability
| Role | Responsibilities (Server & Compute) |
|---|---|
| CIO | Executive oversight for IT strategy and governance alignment. |
| Head of IT Infrastructure Services | Accountable for server/compute standards, operations, and service outcomes. |
| CISO | Ensures security requirements align to the ISMS; oversight of security risk posture. |
| IT Governance Manager | Policy lifecycle, compliance tracking, audit coordination, evidence expectations. |
| Service Owner | End-to-end service performance, risk posture, lifecycle, and compliance for a defined service (e.g., “Windows Server Hosting”). |
| Platform Owner | Defines technical standards for compute domains (virtualization, OS baselines, clustering, images). |
| IT Operations Manager | Operational execution, on-call readiness, incident coordination for compute services. |
| Systems Engineer | Builds, configures, and supports Windows/Linux servers and on-prem compute. |
| Cloud Engineer | Builds, configures, and supports Azure/AWS compute services and cloud-native controls. |
| IAM Engineer | Identity integration, access models, privileged workflows, service account governance. |
| Security Engineer | Logging, detection integrations, EDR deployment, vulnerability remediation validation. |
| ITSM Process Owner | Ensures procedures align to ITIL 4 practices and ITSM tool workflows. |
| Internal Audit | Independent assessment of control design and operating effectiveness. |

### 5.2 RACI (Policy-Applicable Activities)
Aligned to the Norfolk Industries RACI master.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy Requirements (Controls)
### 6.1 Standard Server Builds (Windows/Linux)
1. **Approved versions and supportability**
   - Servers must run vendor-supported OS versions and editions.
   - End-of-support OS deployments are prohibited unless an approved exception exists under the ISMS risk acceptance process with compensating controls and a dated retirement plan.

2. **Gold images and configuration**
   - All new server deployments must be created from an approved gold image or approved automation baseline (Infrastructure-as-Code) that enforces:
     - OS configuration baseline (security settings, logging, time sync, auditing)
     - EDR agent deployment (e.g., Microsoft Defender for Endpoint)
     - Vulnerability scanning agent registration (e.g., Tenable/Nessus)
     - Backup agent/policy assignment where applicable
     - Monitoring/telemetry integration (SIEM such as Microsoft Sentinel)
   - Gold images must be versioned, tested, and approved by the Platform Owner and Security Engineer prior to use.

3. **Windows build standards**
   - Domain-joined where appropriate, using Active Directory integrated with Entra ID where required.
   - Windows Firewall enabled with inbound rules restricted to approved ports/services.
   - PowerShell remoting restricted to administrative subnets/jump hosts and approved tooling.
   - Local Administrator account disabled or managed through enterprise credential rotation controls (see runbook).

4. **Linux build standards**
   - Use approved distributions and baseline configurations.
   - SSH configured to require strong authentication; root login disabled; sudo controlled by group membership and PAM workflows.
   - Host firewall enabled (nftables/iptables or OS equivalent) with least-allowed inbound policy.
   - SELinux/AppArmor enabled where supported unless a documented technical exception is approved.

### 6.2 Virtualization and Compute Platform Standards
1. **Virtualization platform governance**
   - VMware/Hyper-V clusters and management planes must be operated as tier-0/critical infrastructure with enhanced access controls, logging, and change governance.
   - Management interfaces must be isolated on dedicated management networks with restricted access paths.

2. **Cluster design (availability and resilience)**
   - Clusters must be designed to tolerate at least one host failure without breaching SLOs for critical services.
   - Capacity planning must reserve headroom for:
     - N+1 failover capacity (or defined equivalent)
     - Patch/reboot cycles without service impact (where applicable)
   - Storage and network redundancy must avoid single points of failure.

3. **Template and cloning controls**
   - VM templates must be derived only from approved gold images.
   - Template updates must follow Change Enablement and be tracked as CIs in the CMDB.

4. **Cloud compute standards (Azure/AWS)**
   - Use approved VM images (publisher images or managed images) hardened to Norfolk Industries baselines.
   - Enforce identity-based administration (no shared keys), network segmentation, and logging to the SIEM.
   - Disk encryption and secure boot features must be enabled where available and compatible.

### 6.3 Baseline Hardening and Configuration Management
1. **Hardening baseline**
   - Hardening must align to recognized secure configuration benchmarks (conceptually aligned to NIST SP 800-53 and industry benchmarks).
   - Hardening includes:
     - Removal/disablement of unnecessary services
     - Strong cryptography configuration (TLS configurations aligned to enterprise standards)
     - Security updates and hotfix baselines
     - Enforced time synchronization to approved time sources

2. **Configuration drift control**
   - Baseline configurations must be continuously monitored for drift using configuration management tooling or compliance reporting.
   - Unauthorized configuration changes are treated as security events and investigated via Incident Management.

3. **Configuration Items (CIs)**
   - All servers must be recorded as CIs in the ITSM tool CMDB with:
     - Owner (Service Owner)
     - Support group (Regional IT Operations / Global IT Operations)
     - Environment classification (production/non-production)
     - Data classification and criticality
     - Backup policy and RTO/RPO (where applicable)
     - Patch group/maintenance window assignment

### 6.4 Administrative Access Model (PAM Tie-In)
1. **Privileged access**
   - Administrative access to servers must use named accounts and be brokered through PAM (e.g., CyberArk) for:
     - Credential vaulting and rotation
     - Session recording (where supported)
     - Just-in-time or time-bound access approvals where feasible
   - Shared administrator accounts are prohibited except for break-glass accounts controlled under section 6.7.

2. **Separation of duties**
   - Individuals approving access must be independent from those requesting access for high-risk systems, consistent with ISMS and SOX principles.

3. **Remote administration**
   - Administrative access must occur through controlled pathways:
     - Jump hosts/bastions
     - Approved remote management tools
     - Segmented management networks
   - Direct administration from user workstations is prohibited for high-criticality environments unless explicitly approved as part of a controlled workflow.

### 6.5 Service Accounts
1. **Service account lifecycle**
   - Service accounts must be:
     - Uniquely created per application/service where feasible
     - Owned by a Service Owner
     - Documented in the CMDB or authorized inventory
   - Credentials must be stored and rotated via PAM where technically feasible.

2. **Permissions**
   - Service accounts must be granted least privilege and must not be members of domain admin or equivalent high-privilege groups unless a documented exception with compensating controls exists.

3. **Authentication controls**
   - Prefer managed identities or equivalent cloud-native identity mechanisms where available.
   - Interactive logon for service accounts must be denied unless required and approved.

### 6.6 Logging, Monitoring, and Detection
1. **Centralized logging**
   - Servers must forward security-relevant logs to the SIEM (e.g., Microsoft Sentinel), including:
     - Authentication events (success/failure)
     - Privilege changes
     - Process/service creation events where supported
     - Configuration change events (where available)
   - Log sources must be time-synchronized.

2. **EDR and alerting**
   - EDR must be installed and active on all supported servers with tamper protection enabled where available.
   - Alerts of high severity must generate incidents in the ITSM tool and be triaged by Security Engineer and IT Operations Manager on a 24×7 basis consistent with operational requirements.

3. **Monitoring**
   - Monitor performance and availability metrics, at minimum:
     - CPU, memory, disk utilization/latency
     - Network throughput/errors
     - Service health checks for critical services
   - Define SLOs per service and align alert thresholds to prevent incident escalation.

### 6.7 Break-Glass Controls
1. **Break-glass accounts**
   - Break-glass administrative accounts must:
     - Be minimal in number
     - Be stored in PAM with stringent access approval and session controls
     - Be monitored with high-priority alerts on use
   - Use requires post-event review and documentation in the ITSM tool.

2. **Emergency access**
   - Emergency access must follow Emergency Change procedures where the change impacts production configuration, with CAB review after the fact as required by Change Enablement.

## 7. Procedures (Operational Requirements)
All procedures below must be executed through ITIL-aligned ITSM workflows (Incident, Request, Change) and recorded with time-bound, attributable evidence.

### 7.1 Server Provisioning Procedure
1. **Initiation**
   - Request submitted in the ITSM tool specifying:
     - Business justification, service/application, environment, region
     - Data classification and criticality
     - Required RTO/RPO, backup needs
     - Network zone (including OT/IT boundary considerations)
2. **Design validation**
   - Platform Owner validates compute sizing, network segmentation, and baseline requirements.
   - Security Engineer validates logging, EDR, scanning, and access model.
3. **Change control**
   - Production provisioning requires a Normal Change approved via CAB when it introduces new CIs or impacts production services.
4. **Build**
   - Create from approved gold image/template (or IaC baseline).
   - Join domain (as applicable), apply baseline hardening, install required agents.
5. **Access**
   - Admin access assigned via named accounts and PAM workflows.
   - Service accounts created per section 6.5.
6. **Validation**
   - Confirm monitoring, SIEM ingestion, EDR healthy, vuln scan visibility, backup policy assignment.
7. **CMDB update**
   - Register/verify CI attributes and relationships (service mapping where available).
8. **Handover**
   - Regional IT Operations assumes operational support; Service Owner confirms acceptance criteria.

### 7.2 Server Deprovisioning Procedure
1. **Authorization**
   - Service Owner approves retirement and confirms data retention requirements (GDPR and business records).
2. **Dependency assessment**
   - Systems Engineer validates no remaining dependencies (DNS, load balancers, cluster membership, scheduled jobs).
3. **Data handling**
   - Perform required backup/archive or secure wipe per data classification.
4. **Access removal**
   - Remove privileged access assignments; disable service accounts if no longer required.
5. **Decommission**
   - Remove from cluster/load balancer; shutdown; delete VM or wipe physical system according to platform.
6. **CMDB and monitoring**
   - Update CI status to retired; remove monitoring and SIEM routing only after retention needs are met.
7. **Evidence**
   - Attach approvals, wipe confirmation, and CMDB change records to the ITSM ticket.

### 7.3 Patch Windows and Routine Patching Procedure
1. **Patch grouping**
   - Servers must be assigned to a patch group with a defined maintenance window (by region and service criticality).
2. **Testing**
   - Apply patches to non-production first where feasible; validate critical services.
3. **Deployment**
   - Deploy OS and critical third-party patches using enterprise patch tooling.
4. **Reboot coordination**
   - Reboots must be planned; clustered services should fail over gracefully.
5. **Verification**
   - Confirm patch compliance, service health, and monitoring stability.
6. **Reporting**
   - Patch compliance reports must be retained as audit evidence.

### 7.4 Emergency Patching Procedure (Security-Critical)
1. **Trigger**
   - Active exploitation, critical vulnerability with high likelihood/impact, or security directive from CISO.
2. **Risk-based prioritization**
   - Security Engineer and Platform Owner identify affected servers using vuln scanning and asset inventory.
3. **Emergency Change**
   - Submit Emergency Change; execute per Emergency Change workflow with expedited approvals.
4. **Execution**
   - Patch and reboot as required; apply compensating controls if patching is not immediately feasible (e.g., firewall rules, service disablement).
5. **Post-implementation**
   - Validate remediation via rescans and log verification.
6. **CAB review**
   - CAB reviews the Emergency Change retrospectively and records outcomes and follow-ups.

### 7.5 Break-Fix Procedure (Hardware/Hypervisor/OS Failure)
1. **Detection and triage**
   - Incident opened by monitoring alerts or Service Desk intake.
2. **Stabilize**
   - If virtual: evacuate workloads, fail over cluster nodes, or restore from snapshot only if approved by Service Owner (snapshots are not backups).
3. **Repair**
   - Replace failed components or rebuild host/VM using gold images.
4. **Restore service**
   - Validate application/service health, authentication, and monitoring.
5. **Problem Management**
   - For recurring issues, initiate Problem record and root-cause analysis.
6. **Evidence**
   - Incident timeline, changes performed, and validation steps captured in ITSM.

### 7.6 Capacity Expansion Procedure
1. **Trigger**
   - Sustained utilization trends or forecasted growth that risks SLO breach (e.g., CPU > 75% sustained).
2. **Assessment**
   - Systems Engineer/Cloud Engineer confirms whether issue is capacity or misconfiguration (e.g., runaway process).
3. **Change control**
   - Capacity increases in production require a Normal Change with CAB approval if risk is non-trivial.
4. **Implementation**
   - Scale up (CPU/RAM), scale out (additional nodes), storage expansion, or cluster resource additions.
5. **Validation**
   - Confirm performance stabilization and updated monitoring thresholds.
6. **CMDB**
   - Update CI attributes (sizing), cluster relationships, and cost allocation tags (cloud).

## 8. Change Enablement (CAB Integration)
- All production server build template changes, cluster configuration changes, patch rollouts with material risk, and capacity expansions must follow Change Enablement.
- **Normal Changes**: Planned, risk assessed, CAB approved.
- **Emergency Changes**: Executed to remediate severe risk/outage; must be documented immediately and reviewed by the Change Advisory Board (CAB) retrospectively.
- Change records must link to impacted CIs and include implementation plan, validation steps, and rollback approach.

## 9. Security and Compliance Requirements
### 9.1 Vulnerability Management
- Servers must be scanned regularly using approved vulnerability scanning tooling.
- Critical vulnerabilities must be remediated within timeframes defined by the ISMS risk treatment approach and operational severity, with emergency patching used where required.
- Exceptions require risk acceptance and compensating controls.

### 9.2 Data Protection and Privacy (GDPR)
- Servers handling personal data must apply:
  - Access restriction based on least privilege
  - Logging appropriate for auditability
  - Data retention and secure deletion aligned to records requirements and GDPR principles
- Data Protection Officer (DPO) is consulted when infrastructure changes materially affect processing of personal data (e.g., new regions, new logging categories).

### 9.3 SOX Considerations
- Systems supporting financial reporting must enforce:
  - Segregation of duties for privileged access approvals
  - Change control evidence suitable for audit (approvals, testing, implementation validation)
  - Access reviews and logging retention aligned to SOX audit cycles

## 10. Service Continuity and Backup
- Backups must be configured for servers according to service criticality and RTO/RPO requirements.
- Backup success/failure must be monitored and alerted.
- Restore testing must be conducted on a defined cadence for critical services, with evidence retained (restore logs, validation screenshots/outputs, ticket references).
- Disaster recovery designs (including cross-region replication for cloud workloads where required) must be documented by the Service Owner and validated via exercises.

## 11. OT/IT Segmentation Requirements (Where Applicable)
- Servers that interface with Operational Technology (OT) environments must adhere to:
  - Strict network segmentation (no flat networks across OT/IT boundaries)
  - Controlled remote access pathways with strong authentication and monitoring
  - Additional logging and approval requirements for changes affecting OT connectivity
- Remote administration into OT-adjacent zones must follow the same PAM and jump-host principles, with explicit approvals and heightened monitoring.

## 12. Third-Party and Supplier Considerations
- Third-party managed server services must:
  - Meet Norfolk Industries baseline security and logging requirements
  - Provide auditable evidence of patching, access controls, and incident response
  - Integrate with Norfolk Industries monitoring and SIEM where contractually and technically feasible
- Supplier access must be time-bound, approved, and brokered through PAM or equivalent secure remote access controls.

## 13. Metrics, Monitoring, and Reporting
### 13.1 Minimum Operational Metrics
| Metric | Description | Owner |
|---|---|---|
| Patch compliance rate | Percent of in-scope servers compliant within required window | IT Operations Manager |
| Vulnerability remediation performance | Time-to-remediate by severity | Security Engineer |
| Backup success rate | Successful backup jobs vs total | IT Operations Manager |
| Restore test success | Pass/fail and time-to-restore vs RTO | Service Owner |
| Monitoring coverage | Percent of servers sending logs/metrics | Platform Owner |

### 13.2 Reporting Cadence
- Monthly operational reporting to Head of IT Infrastructure Services.
- Quarterly risk and compliance reporting aligned to the ISMS management review cycle.

## 14. Exceptions
- Exceptions must be formally requested, risk assessed, and approved per ISMS governance.
- High-risk exceptions require approval per RACI (including CISO involvement and, where applicable, CIO).
- Exceptions must include:
  - Scope (systems/CIs)
  - Business justification
  - Compensating controls
  - Expiration date and remediation plan
- Exception evidence must be retained for audit.

## 15. Enforcement
Non-compliance may result in:
- Access restriction or removal of administrative privileges
- Forced remediation activities (patching, hardening, rebuild)
- Escalation to Head of IT Infrastructure Services and CISO for risk disposition
- Audit findings and required corrective actions

## 16. Document Governance
### 16.1 Ownership
- Policy Owner: **IT Governance Manager**
- Accountable Executive: **Head of IT Infrastructure Services**
- Security Oversight: **CISO**

### 16.2 Review and Maintenance
- Review at least annually, and upon significant changes to:
  - Compute platforms (e.g., virtualization stack upgrades, cloud architecture shifts)
  - Regulatory requirements (GDPR/SOX)
  - Material security events impacting server infrastructure
- All revisions follow Change Enablement and are recorded as controlled documents under the ISMS.

## 17. Control Mapping (Standards Alignment)
### 17.1 Mapping Table (Conceptual)
| Policy Control Area | ISO/IEC 27001 (Annex A concept) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Typical Evidence |
|---|---|---|---|---|---|---|
| Standard builds & hardening | Secure configuration, change control | Protect | Security, Availability | Service Configuration Management | BAI, DSS | Gold image approval record, baseline scan reports |
| Privileged access & PAM | Access control | Protect | Security | Information Security Management | APO, DSS | PAM logs, access approvals, session records |
| Logging & monitoring | Logging and monitoring | Detect | Security, Availability | Monitoring and Event Management | DSS, MEA | SIEM ingestion proof, alert tickets |
| Patching & vulnerability mgmt | Technical vulnerability management | Protect | Security, Availability | Change Enablement | BAI, DSS | Patch reports, vuln scan deltas, change records |
| Backup & restore | Information backup, resilience | Recover | Availability | Service Continuity Management | DSS | Backup job logs, restore test tickets |
| CMDB and CI control | Asset/config management | Identify | Security | Service Configuration Management | BAI, MEA | CMDB records, CI audits |
| Incident & break-fix | Incident handling | Respond | Security, Availability | Incident Management | DSS | Incident records, RCA/problem records |

### 17.2 Evidence Principles
Evidence must be **time-bound, attributable, and repeatable**, and include approvals, logs, and validation artifacts where applicable.

## 18. References
- Norfolk Industries Information Security Management System (ISMS) policy set
- ITIL 4 practices: Change Enablement, Incident Management, Problem Management, Service Configuration Management, Monitoring and Event Management, Information Security Management, Service Continuity Management
- COBIT 2019 governance and management objectives (EDM/APO/BAI/DSS/MEA domains)
- NIST CSF (Identify, Protect, Detect, Respond, Recover)
- SOC 2 Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy)
- GDPR and SOX obligations as applicable to infrastructure and access controls

## 19. Appendices (Templates, Checklists, Runbooks)
### Appendix A: Server Build Checklist (Windows/Linux)
| Step | Requirement | Windows | Linux | Evidence to Attach (ITSM Ticket) |
|---|---|---:|---:|---|
| 1 | Approved request with criticality, data classification, RTO/RPO | ✔ | ✔ | Approved request record |
| 2 | Built from approved gold image/template or IaC baseline | ✔ | ✔ | Image version ID / pipeline run ID |
| 3 | CMDB CI created/updated with owner, environment, patch group | ✔ | ✔ | CMDB CI link or export |
| 4 | Identity integration (domain join where applicable) | ✔ | ✔ | Join confirmation / config output |
| 5 | Baseline hardening applied (firewall, services, crypto) | ✔ | ✔ | Baseline compliance report |
| 6 | EDR installed and healthy | ✔ | ✔ | EDR console screenshot/export |
| 7 | Vulnerability scanner onboarded | ✔ | ✔ | Scan visibility proof |
| 8 | Central logging to SIEM enabled | ✔ | ✔ | SIEM ingestion sample event |
| 9 | Backup policy assigned (if required) | ✔ | ✔ | Backup job success log |
| 10 | Admin access via PAM; no shared admin accounts | ✔ | ✔ | PAM access policy link |
| 11 | Service accounts created, least privilege, documented | ✔ | ✔ | Service account record |
| 12 | Monitoring and alert thresholds configured | ✔ | ✔ | Monitoring dashboard link/export |
| 13 | Acceptance validation completed | ✔ | ✔ | Validation checklist signed by Service Owner |

### Appendix B: Standard Ports and Services Guidance
This guidance defines the minimum approach to port exposure. Actual implementation must follow least privilege and network segmentation standards.

#### B.1 Principles
- Deny by default; explicitly allow only required ports from approved sources.
- Separate **management traffic** from **application traffic** via network segmentation.
- Restrict admin protocols to jump hosts/management subnets.
- For OT-adjacent services, apply stricter segmentation and explicit approvals.

#### B.2 Common Ports (Guidance)
| Service Category | Protocol/Port | Typical Use | Minimum Requirement |
|---|---|---|---|
| Windows management | RDP 3389/TCP | Admin access | Only via jump host; never internet-exposed; log all sessions |
| Windows management | WinRM 5985/5986 TCP | Remote mgmt | Restrict to management subnet; prefer TLS (5986) |
| Linux management | SSH 22/TCP | Admin access | Only via jump host; key-based auth preferred; no root login |
| Directory services | LDAP/LDAPS 389/636 TCP | Auth directory | Prefer LDAPS; restrict to app subnets |
| File services | SMB 445/TCP | Windows file sharing | Restrict to needed subnets; harden SMB settings |
| Web services | HTTP/HTTPS 80/443 TCP | Application endpoints | Prefer HTTPS; enforce modern TLS; WAF/reverse proxy where applicable |
| Monitoring | Agent-specific | Telemetry | Allow only to monitoring collectors; document flows |
| Backup | Agent-specific | Backup operations | Allow only to backup infrastructure; document flows |
| Database | Vendor-specific | App DB connectivity | Allow only app-to-DB paths; no broad access |

### Appendix C: Runbook — Restore Server from Backup
#### C.1 Preconditions
- Incident or request ticket exists in the ITSM tool with Service Owner approval for restore.
- Identify server CI, environment, and required restore point (timestamp) aligned to RPO.
- Confirm whether restore is for:
  - Full server restore (system + data)
  - Volume/file-level restore
  - Bare-metal/VM restore

#### C.2 Steps
1. **Confirm scope and impact**
   - Validate affected services, dependencies, and whether a point-in-time restore could cause data inconsistency.
2. **Select restore point**
   - Choose the most recent clean restore point meeting business needs.
3. **Prepare target**
   - Decide restore destination:
     - In-place restore (overwrite)
     - Restore to alternate VM (recommended for validation where feasible)
4. **Execute restore**
   - Use approved backup tooling to initiate restore job.
5. **Post-restore validation**
   - Validate:
     - OS boots and services start
     - Network connectivity and DNS as required
     - Application functionality (Service Owner confirms)
     - EDR healthy; logging to SIEM resumed
6. **Security checks**
   - Confirm no indicators of compromise prompted the restore; if suspected, coordinate with Security Engineer for containment and forensic steps.
7. **Closeout**
   - Attach restore job logs, timestamps, and validation results to the ticket.
   - Update CMDB CI notes if configuration changed.

#### C.3 Escalation
- If restore fails or exceeds RTO risk: escalate to IT Operations Manager and Service Owner; consider alternate recovery options (rebuild from gold image + data restore).

### Appendix D: Runbook — Rotate Local Admin Credentials
#### D.1 Objective
Reduce credential compromise risk by rotating local administrator credentials on servers and ensuring privileged access remains brokered through PAM.

#### D.2 Preconditions
- Approved change/request ticket exists (Normal Change for production rotations impacting access workflows).
- Identify target servers/CIs and verify they are reachable and managed.

#### D.3 Steps
1. **Confirm current access pathways**
   - Ensure PAM is operational and authorized administrators have alternate access paths before rotation.
2. **Rotate credentials**
   - For Windows:
     - Rotate local Administrator password using enterprise credential rotation tooling integrated with PAM.
     - Disable local Administrator where technically feasible; otherwise keep managed and rotated.
   - For Linux:
     - Remove or lock direct local admin accounts; enforce sudo via named accounts.
     - If a local privileged account exists, rotate via PAM and restrict interactive logon as appropriate.
3. **Validate**
   - Confirm:
     - Admins can access via PAM workflow
     - Service accounts are unaffected
     - No scheduled tasks/services depend on the rotated local credentials
4. **Record evidence**
   - Attach rotation logs/confirmation from PAM and validation notes to the ticket.

#### D.4 Monitoring and Alerts
- Generate an alert and incident if:
  - Break-glass account used outside of approved workflow
  - Multiple failed admin logons occur after rotation (possible lockout or attack)

### Appendix E: Runbook — Respond to CPU Saturation
#### E.1 Trigger Conditions
- Sustained CPU utilization above defined threshold (typically > 85% for 15 minutes) or repeated performance alerts impacting SLO.

#### E.2 Steps
1. **Open/confirm incident**
   - Ensure an Incident record exists with affected CI(s), time window, and impact.
2. **Stabilize service**
   - If immediate user impact:
     - Reduce load (restart failed worker service only if approved and safe)
     - Fail over to another node if clustered and safe
3. **Diagnose**
   - Identify top CPU consumers:
     - Windows: Task Manager/PerfMon/EDR telemetry
     - Linux: top/htop, systemd service status, application metrics
   - Check for:
     - Runaway processes
     - Scheduled jobs (AV scans, backups, batch jobs)
     - Recent changes (patches, configuration changes) via Change records
4. **Contain**
   - If malicious activity suspected (crypto-miner, suspicious processes):
     - Isolate host per Security Engineer guidance and EDR procedures
     - Preserve logs and start security incident workflow
5. **Remediate**
   - Options (choose based on findings and change governance):
     - Tune application/service configuration
     - Adjust job schedules (backup/scan windows)
     - Add vCPU/scale up instance size
     - Scale out (add nodes) and load balance
6. **Validate**
   - Confirm CPU returns to normal operating range and application response times recover.
7. **Problem Management**
   - If recurring, create a Problem record with root cause, trend data, and preventive actions.
8. **Evidence**
   - Attach performance graphs, process identification, actions taken, and validation results to the Incident/Change.

### Appendix F: Evidence Pack (Audit-Ready Artifacts)
The following artifacts constitute the minimum evidence set for this policy’s operating effectiveness.

| Control Area | Evidence Artifact | Source | Frequency | Evidence Quality Notes |
|---|---|---|---|---|
| Gold image governance | Image version history, approval record, test results | Image pipeline repository + ITSM change | Per image release | Time-bound approvals; link to CI/template |
| Server provisioning | Build ticket, CI record, baseline compliance | ITSM + CMDB + compliance tooling | Per server | Must show attributable implementer and approvals |
| Privileged access | PAM access approvals, session logs/recordings | PAM | Ongoing | Tie access to named user and ticket/change |
| Patching | Patch deployment reports, maintenance window records | Patch tooling + ITSM | Monthly (or cycle-based) | Include scope, success rate, exceptions |
| Vulnerability mgmt | Scan reports and remediation verification | Vulnerability scanner | Regular cadence | Provide before/after evidence for critical items |
| Logging/SIEM | Log ingestion confirmation, alert-to-incident linkage | SIEM + ITSM | Ongoing | Demonstrate repeatability (sample events) |
| Backup/restore | Backup job logs, restore test evidence, RTO/RPO validation | Backup tooling + ITSM | Per schedule | Include restore timestamps and validation outputs |
| Change control | CAB approvals, implementation & validation notes | ITSM | Per change | Link change to impacted CIs |
| Deprovisioning | Retirement approval, wipe/retention confirmation, CMDB retired status | ITSM + CMDB | Per server | Show data handling compliance (GDPR/records) |