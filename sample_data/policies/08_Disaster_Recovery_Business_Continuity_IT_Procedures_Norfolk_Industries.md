# Disaster Recovery & Business Continuity IT Procedures (Norfolk Industries)

## 1. Purpose
This document defines the Disaster Recovery (DR) and Business Continuity (BC) IT procedures for Norfolk Industries to:
- Restore prioritized Information Technology (IT) services and supporting platforms within approved Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets.
- Provide consistent activation, failover, failback, and recovery execution across North America, Europe, and APAC under centralized governance and regional execution.
- Align IT recovery activities with the Information Security Management System (ISMS), ISO/IEC 22301 Business Continuity Management System (BCMS) concepts, and ITIL 4 practices.

## 2. Scope
### 2.1 In scope
- IT Infrastructure Services and application recovery procedures supporting corporate and plant operations.
- Hybrid cloud services (Microsoft Azure primary; AWS secondary), on-prem data centers, and supporting connectivity.
- Identity (Active Directory + Entra ID (Azure AD)), endpoint management (Microsoft Intune + ConfigMgr where needed), monitoring and security tooling (SIEM, EDR, vulnerability scanning, PAM).
- OT/IT integration touchpoints and remote access controls used to support Operational Technology (OT) environments, including SCADA/MES access pathways.
- Service continuity procedures executed via ITIL-aligned ITSM tooling and governed through the Change Advisory Board (CAB).

### 2.2 Out of scope
- Non-IT continuity procedures (e.g., facilities evacuation, physical safety) owned by Corporate Business Continuity.
- Detailed OT system recovery steps (e.g., PLC reprogramming). OT recovery is coordinated with plant OT owners; this document covers IT dependencies and access paths enabling OT recovery.

## 3. Governance, Standards, and Control Alignment
### 3.1 Governance model
- **Global IT Operations**: defines global DR standards, minimum requirements, tiering, and evidence expectations; coordinates cross-region recovery.
- **Regional IT Operations**: executes recovery actions in-region, maintains regional runbooks consistent with this procedure, and provides operational evidence.

### 3.2 Standards alignment
This procedure aligns to:
- ISO/IEC 27001 Annex A control areas (conceptual mapping to continuity, access control, operations security, supplier, incident management).
- ISO/IEC 22301 continuity principles (strategy, plans, exercises, continual improvement).
- ITIL 4: Incident Management, Problem Management, Change Enablement, Monitoring and Event Management, Service Continuity Management, Information Security Management, Service Configuration Management.
- NIST CSF: Identify, Protect, Detect, Respond, Recover.
- SOC 2 Trust Services Criteria: Security, Availability, Confidentiality, Processing Integrity, Privacy.
- COBIT 2019: EDM, APO, BAI, DSS, MEA.
- GDPR and SOX requirements where applicable to systems processing personal data or financial reporting.

### 3.3 Evidence principles
Evidence produced under this procedure must be:
- Time-bound, attributable, and repeatable.
- Inclusive of approvals, logs, and validation artifacts where applicable.

## 4. Roles and Responsibilities
Roles used below are from the Norfolk Industries role catalogue.

### 4.1 DR/BC responsibilities
| Role | Responsibilities (DR/BC) |
|---|---|
| CIO | Executive owner of IT continuity posture; accountable for high-risk exception approval decisions and enterprise prioritization. |
| Head of IT Infrastructure Services | Accountable for DR readiness of infrastructure platforms and service outcomes; ensures resourcing and governance. |
| CISO | Ensures DR actions maintain ISMS controls; validates security implications of failover/failback; oversees risk acceptance. |
| IT Governance Manager | Maintains procedure lifecycle; coordinates audit evidence; tracks exercise completion and compliance. |
| Service Owner | Owns service DR tier assignment, dependency mapping, runbook accuracy, and recovery validation criteria. |
| Platform Owner | Ensures platform-level DR design is implemented (replication, backups, automation) and runbooks are maintained. |
| IT Operations Manager | Coordinates operational execution, shift/on-call readiness, and incident response coordination during DR events. |
| ITSM Process Owner | Ensures ITIL-aligned processes support DR (major incident, change, CMDB, PIR). |
| Internal Audit | Independently assesses control design and operating effectiveness; reviews evidence packages. |
| Data Protection Officer (DPO) | Confirms privacy obligations during recovery (data residency, breach considerations, GDPR). |

### 4.2 RACI (key DR/BC activities)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 5. Definitions and Terminology
Norfolk Industries uses the following canonical terms (selected for DR/BC context):
- **IT Infrastructure Services**: infrastructure platforms and operations.
- **Global IT Operations**: centralized governance and coordination for infrastructure.
- **Regional IT Operations**: regional execution aligned to global governance.
- **Information Security Management System (ISMS)**: governance framework meeting ISO/IEC 27001.
- **Change Advisory Board (CAB)**: governance body approving Normal and Emergency Changes.
- **Configuration Item (CI)**: managed component delivering an IT service.
- **Operational Technology (OT)** and **Information Technology (IT)**: plant control systems vs corporate/enterprise systems.
- **Service Level Objective (SLO)**: target reliability/performance metric.
- **Recovery Point Objective (RPO)**: maximum tolerable data loss measured in time.
- **Recovery Time Objective (RTO)**: time to restore service after disruption.

## 6. DR Service Tiering and Recovery Objectives
### 6.1 Tier model
Norfolk Industries assigns each in-scope service a DR Tier to standardize recovery expectations.

| DR Tier | Business impact | Target RTO | Target RPO | Typical strategy |
|---|---:|---:|---:|---|
| Tier 0 | Safety/plant-wide stoppage risk; enterprise-critical | ≤ 4 hours | ≤ 15 minutes | Active-active or warm standby; automated failover where feasible; continuous replication |
| Tier 1 | High revenue/operations impact | ≤ 24 hours | ≤ 4 hours | Warm standby; scheduled replication; infrastructure-as-code rebuild + data restore |
| Tier 2 | Moderate impact; can tolerate short outage | ≤ 72 hours | ≤ 24 hours | Backup/restore; rebuild from templates; manual failover |
| Tier 3 | Low impact; deferrable restoration | ≤ 10 business days | ≤ 72 hours | Restore when capacity allows; primarily backup/restore |

### 6.2 Tier assignment rules
- Service Owner proposes tier based on business impact analysis inputs and dependencies.
- Head of IT Infrastructure Services approves tier assignment; CISO reviews where security or regulatory exposure changes.
- Tier must be recorded in the ITSM service record and linked to associated CIs.

### 6.3 RTO/RPO exceptions
- Exceptions require documented risk acceptance and approval per the “Exception approval (high risk)” RACI.
- Exceptions must include compensating controls (e.g., enhanced monitoring, alternate manual procedures, added backups).

## 7. DR Architecture Patterns and Failover Strategies
### 7.1 Approved patterns
| Pattern | Description | Use cases | Key considerations |
|---|---|---|---|
| Active-active | Service runs concurrently in two sites/regions | Tier 0 identity dependencies, critical connectivity components | Data consistency, split-brain controls, testing complexity |
| Warm standby | Pre-provisioned environment with replicated data | Tier 0–1 ERP/MES components, VPN/ZTNA | Runbook-driven activation; replication lag monitoring |
| Pilot light | Minimal core components running; scale out during DR | Tier 1–2 cloud-native workloads | Automation readiness; capacity reservation |
| Backup/restore | Restore data and rebuild services after event | Tier 2–3 | Restore time; dependencies often dominate RTO |

### 7.2 Failover types
- **Service failover**: application/service layer cutover (DNS, routing, load balancer, service endpoints).
- **Platform failover**: underlying compute/storage/network shift (Azure region, AWS region, on-prem site).
- **Identity failover**: authentication/authorization continuity (AD DS, Entra ID dependencies).
- **Network edge failover**: internet ingress/egress, DNS resolution, VPN/ZTNA gateways.

### 7.3 Technology baselines (hybrid cloud)
- **Microsoft Azure (primary)**: primary recovery location for supported workloads; region pairs used where feasible.
- **AWS (secondary)**: secondary recovery location for selected services where approved; must include security logging and access controls equivalent to primary.
- **On-prem data centers**: must maintain documented recovery capabilities (alternate site capability, restore procedures, or workload migration plan).

## 8. Dependency Mapping (Service Recovery Design Requirement)
### 8.1 Dependency categories
Service Owners must maintain dependency mapping across:
- **Identity**: Active Directory domain services, Entra ID, conditional access dependencies, PAM dependencies.
- **Network**: DNS, DHCP, IPAM, routing, WAN, SD-WAN, firewalls, proxies.
- **Security**: SIEM ingestion, EDR, vulnerability scanning reachability, PAM access paths.
- **Data**: databases, storage arrays, backups, key management, certificates.
- **ITSM and monitoring**: ticketing, alerting, on-call paging.
- **OT/IT integration**: plant network segmentation, jump hosts, remote access gateways, historian interfaces.

### 8.2 Minimum dependency artifacts
- Service dependency diagram (logical).
- CI linkage in CMDB (service-to-CI relationships).
- External dependency list (telecom carriers, SaaS, managed service providers).
- Data classification and regulatory impacts (GDPR/SOX applicability).
- Recovery validation checks (what “restored” means).

### 8.3 Dependency sequencing principle
Recovery order must be driven by dependency constraints:
1. Network edge + DNS
2. Identity (AD DS / Entra ID connectivity dependencies)
3. Core security/monitoring (minimum viable logging + EDR reachability)
4. ERP and core enterprise platforms
5. MES and OT access services (remote access gateways, jump hosts)
6. Collaboration services and user productivity tooling

## 9. Crisis Communications Alignment
### 9.1 Communication objectives
- Provide accurate, timely, and security-approved updates to stakeholders.
- Prevent misinformation and reduce operational disruption.
- Maintain consistent messaging across regions.

### 9.2 Communication governance
- IT Operations Manager leads the IT communications cadence during DR events.
- Service Desk Manager coordinates user-facing messaging channels (portal banners, email notifications when available).
- CISO reviews messages when security incidents or data exposure are possible.
- Data Protection Officer (DPO) is engaged for privacy-related messaging (GDPR).

### 9.3 Communication channels (preferred order)
1. ITSM major incident communications (system of record)
2. Corporate collaboration platform message (if available)
3. Email notifications (if available)
4. SMS/voice call tree (Appendix B)
5. Executive brief (CIO / Head of IT Infrastructure Services)

### 9.4 Standard communication cadence
| Event phase | Update frequency | Audience |
|---|---:|---|
| Initial declaration / stabilization | Every 30–60 minutes | Executive stakeholders, Regional IT Operations leads, Service Owners |
| Recovery execution | Every 2–4 hours (or milestone-based) | Affected business units, plant leadership, IT leadership |
| Post-restoration monitoring | At restoration + 24 hours | Stakeholders, Internal Audit (if required), IT Governance Manager |

## 10. DR Activation Criteria and Disaster Declaration
### 10.1 Trigger conditions (examples)
A disaster declaration may be warranted when one or more conditions apply:
- Loss of a primary data center or cloud region supporting Tier 0–1 services beyond 60 minutes with no credible restoration window within RTO.
- Cybersecurity event causing loss of integrity or availability requiring environment rebuild (e.g., ransomware affecting production workloads).
- Network edge outage affecting multiple regions or all remote access pathways.
- Major identity outage preventing authentication for critical services.
- Facility event (power, fire, flooding) preventing safe operations within RTO.

### 10.2 Authority to declare
- **Primary**: Head of IT Infrastructure Services (or delegate) in coordination with IT Operations Manager.
- **Security concurrence**: CISO (or delegate) required when the event includes suspected or confirmed security compromise.
- **Executive notification**: CIO notified immediately upon declaration.

### 10.3 Declaration procedure
1. Open a Major Incident in the ITSM tool and mark as “DR Event”.
2. Assign Incident Commander (IT Operations Manager or delegate).
3. Identify impacted services and preliminary DR tiers.
4. Engage Service Owners and Platform Owners for impacted services.
5. Confirm whether the event is operational disruption only or includes security compromise.
6. Approve DR activation scope (service-by-service) and record decision log in the major incident.
7. Initiate call tree and communications cadence (Section 9).

## 11. DR Execution Procedures (Activate, Failover, Failback)
### 11.1 Activate DR (common steps)
1. **Stabilize and isolate**
   - If cybersecurity suspected: contain affected networks/hosts in coordination with Security Engineer; preserve logs.
   - Ensure OT network segmentation remains enforced; do not open plant networks without approved remote access controls.
2. **Establish command structure**
   - Incident Commander confirms roles: communications lead, technical leads per platform, scribe.
3. **Confirm recovery objectives**
   - Validate RTO/RPO targets and current replication/backup status for each service.
4. **Dependency confirmation**
   - Confirm network edge, DNS, identity readiness prior to application cutovers.
5. **Change governance**
   - DR actions are executed as Emergency Changes with CAB notification/ratification as required by Change Enablement.
6. **Execute runbooks**
   - Follow service runbooks (Section 12) and capture evidence (Appendix D).
7. **Validation**
   - Validate service functionality and security controls (authentication, logging, privileged access).
8. **Stakeholder communication**
   - Publish milestones: “Failover started”, “Service restored (limited/full)”, “Monitoring period”.

### 11.2 Failover procedure (service-level)
1. Confirm failover prerequisites:
   - Replication health within RPO.
   - Target environment accessible with PAM controls.
   - Monitoring and logging active.
2. Freeze non-essential changes for impacted services.
3. Execute failover sequence:
   - Data layer (final sync if safe).
   - Compute/platform start in DR site.
   - Update network routing/DNS/load balancer.
4. Validate:
   - Authentication/authorization.
   - Core transactions.
   - Logging to SIEM and EDR coverage.
5. Update ITSM records:
   - Major incident work notes, timestamps, approvals, and validation results.

### 11.3 Failback procedure (return to primary)
Failback is performed only after stability and integrity are confirmed.

1. Preconditions:
   - Primary site/region restored and hardened.
   - Security verification complete (where applicable): clean rebuild evidence, vulnerability scan results, credential rotation confirmation.
   - CAB-approved failback plan (Emergency or Normal Change depending on urgency).
2. Data reconciliation:
   - Confirm authoritative source of truth; perform delta sync or controlled replication reversal.
3. Cutback execution:
   - Reverse routing/DNS/load balancer changes.
   - Validate service and monitor error rates.
4. Post-failback monitoring:
   - Minimum 24–72 hours heightened monitoring depending on DR tier.
5. Close-out:
   - Ensure all evidence is attached to the major incident record.
   - Initiate Post-Incident Review (Section 13).

## 12. DR Runbooks (Core Services)
Runbooks below define the minimum required steps. Service Owners and Platform Owners may extend these runbooks, but must not reduce required controls or validation.

### 12.1 Identity Runbook (Active Directory + Entra ID)
**Tier guidance**: Typically Tier 0.

#### 12.1.1 Preconditions
- Privileged access via PAM is available for domain admin and tenant admin functions.
- Break-glass accounts are available and tested per ISMS controls (use audited access).
- DNS services available in DR environment.
- Time synchronization (NTP) is functional.

#### 12.1.2 Failover steps (Active Directory)
1. Confirm AD DS replication status and identify surviving domain controllers.
2. If primary site domain controllers are unavailable:
   - Promote pre-staged domain controllers in DR site (if applicable).
   - Ensure Global Catalog availability in DR site.
3. Validate DNS SRV records and AD-integrated DNS zones.
4. Validate authentication:
   - Test user login from representative networks (corporate and remote access).
   - Validate Kerberos and LDAP connectivity.
5. Validate critical integrations:
   - VPN/ZTNA authentication
   - Email/collaboration directory sync dependencies
   - ERP/MES authentication mechanisms
6. Confirm logging:
   - Domain controller security logs forwarded to SIEM.
   - EDR active on domain controllers.

#### 12.1.3 Failover steps (Entra ID dependencies)
1. Validate connectivity from critical services to Entra ID endpoints.
2. Validate Conditional Access policies are functioning as intended (no emergency bypass unless approved).
3. If hybrid identity sync is impacted:
   - Confirm last successful sync time and business impact.
   - Use documented emergency access procedure for required admin functions.
4. Validate privileged access:
   - PAM access to tenant admin roles.
   - Ensure alerts are flowing to SIEM.

#### 12.1.4 Recovery validation checklist
- Authentication success for representative user groups.
- Privileged access functions with MFA and PAM controls.
- SIEM receives identity logs; EDR is healthy on identity servers.
- No unauthorized policy changes detected during DR event.

---

### 12.2 Network Edge Runbook (Internet Edge, DNS, Firewall, WAN/SD-WAN)
**Tier guidance**: Typically Tier 0 (edge/DNS) to Tier 1 (regional WAN components).

#### 12.2.1 Preconditions
- Documented network diagrams and CI relationships available in ITSM/CMDB.
- Out-of-band access methods available for network devices.
- Telecom provider escalation paths available.

#### 12.2.2 Failover steps (edge services)
1. Confirm scope: region, site, or global edge impact.
2. Activate alternate egress/ingress:
   - Bring up DR site internet circuits (if not already active).
   - Activate cloud-based edge (if used) and ensure policies match baseline.
3. DNS continuity:
   - Confirm authoritative DNS availability.
   - Adjust DNS records to point to DR endpoints where required (lower TTL where pre-approved).
4. Firewall and proxy:
   - Validate policy baseline deployed in DR.
   - Confirm logging is enabled and forwarded to SIEM.
5. WAN/SD-WAN:
   - Re-route critical traffic to DR site; prioritize identity, ERP, MES, and remote access.
6. Validate:
   - External reachability (synthetic checks).
   - Internal routing to key subnets.
   - OT segmentation controls remain enforced.

#### 12.2.3 Recovery validation checklist
- DNS resolution for critical services.
- Stable internet ingress/egress with correct security controls.
- SIEM ingestion of firewall/proxy logs.
- Remote access pathways function (hand-off to VPN/ZTNA runbook).

---

### 12.3 ERP Runbook (Enterprise Resource Planning)
**Tier guidance**: Typically Tier 0–1 depending on business impact and SOX relevance.

#### 12.3.1 Preconditions
- Database replication status known (time since last sync aligned to RPO).
- Application binaries/configurations version-controlled.
- Key management and certificates accessible in DR environment.
- SOX-relevant change logging is enabled.

#### 12.3.2 Failover steps
1. Confirm dependency readiness:
   - Identity (AD/Entra ID) operational.
   - Network edge stable; DNS prepared for cutover.
2. Database layer:
   - Execute controlled failover to DR database node/cluster.
   - Validate database integrity checks.
3. Application layer:
   - Start ERP application services in DR environment.
   - Validate integrations (EDI, reporting, file transfers, APIs).
4. Cutover:
   - Update DNS/load balancer to DR endpoints.
   - Validate user authentication and core transactions.
5. Security and monitoring:
   - Confirm EDR on ERP servers.
   - Confirm application and database logs flowing to SIEM.
6. Declare service restoration status:
   - “Limited” (core transactions only) vs “Full” (all integrations).

#### 12.3.3 Failback steps (summary)
- CAB-approved plan.
- Replicate DR changes back to primary; reconcile transactions.
- Controlled cutback during defined window; validate SOX control logging.

#### 12.3.4 Recovery validation checklist
- Order-to-cash and procure-to-pay representative transactions.
- Batch jobs and scheduled interfaces.
- Audit logging for privileged and financial-impact actions.
- Performance within agreed SLO thresholds for DR mode.

---

### 12.4 MES Runbook (Manufacturing Execution System) with OT/IT Controls
**Tier guidance**: Typically Tier 0–1 for plants relying on MES for production.

#### 12.4.1 Preconditions
- OT network segmentation remains enforced; no direct IT-to-OT bridging outside approved paths.
- Remote access controls and jump host patterns are available.
- Plant leadership and OT representatives are engaged.

#### 12.4.2 Failover steps
1. Confirm allowed access pathways:
   - Jump hosts / remote access gateways operational.
   - MFA and PAM enforced for administrative actions.
2. Validate integration dependencies:
   - MES database availability in DR.
   - Interfaces to ERP, historians, and reporting.
3. Bring up MES application stack in DR (if centralized) or validate local plant instance recovery.
4. Plant connectivity validation:
   - Confirm that plant networks can reach MES endpoints without violating segmentation.
5. Functional validation:
   - Work order dispatch, tracking, and confirmation flows.
   - Machine/line data ingestion where applicable.
6. Monitoring and security:
   - Confirm logs to SIEM (MES, gateways, jump hosts).
   - EDR coverage on IT-side components (jump hosts, application servers).

#### 12.4.3 Recovery validation checklist
- Plant can execute defined “minimum viable production” workflow.
- No segmentation exceptions created without CAB and security concurrence.
- Remote access sessions are recorded/audited where capability exists.

---

### 12.5 Email and Collaboration Runbook
**Tier guidance**: Typically Tier 1–2 depending on operational reliance and incident communications needs.

#### 12.5.1 Preconditions
- Identity operational (Entra ID, MFA).
- Network edge egress policies allow service endpoints.
- Alternate communications method available if email is impaired (ITSM + call tree).

#### 12.5.2 Recovery steps
1. Validate service status from vendor/admin portal and synthetic checks.
2. If hybrid components exist (connectors, relays, identity sync):
   - Restore mail relay/connectors in DR site.
   - Validate inbound/outbound mail flow.
3. Restore collaboration dependencies:
   - Meeting services, chat, and file collaboration access paths.
4. Validate compliance/security:
   - DLP and retention policies remain effective where applicable.
   - Logging to SIEM for admin actions (as available).

#### 12.5.3 Recovery validation checklist
- Send/receive internal and external email (test accounts).
- Calendar and meeting creation.
- Admin audit logs review for anomalous actions during DR.

---

### 12.6 VPN/ZTNA Runbook (Remote Access)
**Tier guidance**: Tier 0 for supporting 24×7 operations and plant support.

#### 12.6.1 Preconditions
- Identity services operational; MFA available.
- Network edge and firewall policies in DR are deployed.
- Certificates/keys for gateways are accessible with controlled access.

#### 12.6.2 Failover steps
1. Determine remote access model impacted:
   - VPN gateways (hardware or virtual)
   - ZTNA service edges
2. Activate DR gateways:
   - Start gateway instances in DR site/cloud.
   - Confirm capacity for peak connections (regional concurrency).
3. Update routing/DNS:
   - Point remote access FQDNs to DR endpoints.
   - Validate split-tunnel/full-tunnel policies as approved.
4. Validate access controls:
   - Conditional Access policies.
   - Device compliance where required (Intune).
   - PAM for administrative access.
5. Validate OT remote access controls:
   - Ensure jump host requirement remains in place.
   - Ensure session logging/recording remains enabled where implemented.

#### 12.6.3 Recovery validation checklist
- User authentication success (test users per region).
- Authorization to key apps (ERP, MES, ITSM).
- No broadened access beyond approved policies.
- Logs forwarded to SIEM; alerts functioning.

## 13. Post-Incident Review (PIR) and Continual Improvement
### 13.1 PIR timing and ownership
- IT Operations Manager initiates PIR within 5 business days of service stabilization.
- ITSM Process Owner ensures PIR workflow and documentation quality.
- IT Governance Manager ensures evidence completeness and tracks actions to closure.

### 13.2 PIR minimum contents
- Timeline with timestamps for declaration, failover start, restoration milestones, failback.
- RTO/RPO achieved vs targets; variances and root causes.
- Dependency issues encountered and remediation actions.
- Security findings (credential resets, policy changes, malware indicators).
- Communications effectiveness review.
- Action plan with owners and due dates (tracked as Problems/Changes as appropriate).

### 13.3 Change management outcomes
- Required architecture/process improvements are raised as Normal Changes for CAB review.
- Emergency changes executed during DR are reviewed for completeness and compliance.

## 14. Testing, Exercises, and Validation
### 14.1 Exercise types
| Exercise type | Description | Minimum frequency |
|---|---|---:|
| Tabletop | Scenario walkthrough; decision-making and communications | Semi-annual (Tier 0–1 services), annual (Tier 2–3) |
| Technical failover test | Execute failover steps in controlled window | Annual for Tier 0; every 18 months for Tier 1 |
| Restore verification | Backup restore tests and integrity checks | Quarterly for Tier 0–1 data sets; semi-annual for Tier 2 |
| Communications drill | Call tree and stakeholder messaging test | Quarterly |

### 14.2 Success criteria
- Recovery within tier targets (or documented variance and remediation).
- Evidence package complete per Appendix D.
- No unauthorized weakening of security controls (MFA, PAM, segmentation).
- Lessons learned recorded and actioned.

## 15. Tooling, Records, and Evidence Management
### 15.1 Systems of record
- ITSM tool: major incident record, change records (Emergency/Normal), problem record (PIR outputs), knowledge articles/runbooks.
- CMDB: service-to-CI relationships and DR tier attributes.
- SIEM: event correlation, identity and edge logging, DR period audit trail.
- EDR: endpoint/server health and threat status during recovery.
- PAM: privileged access logs for DR actions.
- Backup system: restore job logs and integrity verification results.

### 15.2 Evidence retention
- DR event evidence retained per ISMS and audit requirements applicable to the service (including SOX where in scope).
- Evidence must link to the ITSM major incident record and relevant change approvals.

## 16. Security and Compliance Requirements During DR
### 16.1 Non-negotiable controls
- Privileged actions must use PAM where implemented; all use must be logged.
- MFA remains enforced unless explicitly approved as a time-bound emergency measure with CISO concurrence and documented compensating controls.
- OT network segmentation controls remain in place; temporary connectivity exceptions require CAB governance and security review.
- Logging to SIEM is maintained for identity, network edge, and privileged operations.
- EDR must be enabled on recovered servers where supported.

### 16.2 Data protection considerations (GDPR/SOX)
- Data Protection Officer (DPO) engagement is required if:
  - Personal data processing location changes across regions.
  - There is suspected unauthorized disclosure.
- SOX-relevant systems (e.g., ERP) must preserve:
  - Change logs, access logs, and audit trails.
  - Segregation-of-duties controls (no ad-hoc role expansions without documented approval and review).

## 17. Supplier and Third-Party Dependencies
### 17.1 Supplier continuity expectations
- Critical suppliers (telecom, SaaS, managed services) must provide:
  - Documented DR capabilities and RTO/RPO targets.
  - Escalation contacts and 24×7 support pathways.
  - Evidence of annual DR testing (attestations or reports), where contractually required.

### 17.2 Supplier coordination procedure during DR
1. Open supplier escalation ticket and link to ITSM major incident.
2. Request incident bridge participation if needed.
3. Capture supplier-provided timestamps, actions, and outcomes as evidence.

## 18. Metrics, Reporting, and Management Review
### 18.1 Core DR metrics
| Metric | Definition | Target / expectation |
|---|---|---|
| RTO attainment rate | % of DR events/tests meeting RTO | Tier 0: ≥ 95%; Tier 1: ≥ 90% |
| RPO attainment rate | % meeting RPO | Tier 0: ≥ 95%; Tier 1: ≥ 90% |
| Exercise completion | % of scheduled exercises completed | ≥ 95% annually |
| Evidence completeness | % of events/tests with complete evidence package | ≥ 95% |
| Recurring findings | Repeat issues across PIRs | Downward trend quarter-over-quarter |

### 18.2 Management review
- Head of IT Infrastructure Services and CISO review quarterly DR readiness and test outcomes.
- IT Governance Manager provides evidence summary for audits and ISMS management review inputs.

## 19. Document Control
### 19.1 Ownership and maintenance
- Owner: IT Governance Manager (procedure lifecycle), accountable sponsor: Head of IT Infrastructure Services.
- Service Owners and Platform Owners are responsible for ensuring their runbooks remain accurate and testable.

### 19.2 Review cycle
- Formal review at least annually, and after any major DR event, significant platform change, or audit finding.

### 19.3 Distribution
- Published in the approved policy/procedure repository and linked within the ITSM knowledge base for operational accessibility.

---

## Appendix A: DR Plan Template (Norfolk Industries)
### A.1 DR plan header
| Field | Value |
|---|---|
| Service name |  |
| Service Owner |  |
| Platform Owner(s) |  |
| DR Tier |  |
| Target RTO |  |
| Target RPO |  |
| Regions in scope | North America / Europe / APAC |
| Primary location | Azure region / On-prem site |
| DR location | Azure paired region / AWS region / Alternate data center |
| Data classification |  |
| Regulatory scope | GDPR / SOX / Other applicable |

### A.2 Service description and criticality
- Business function supported:
- Operational hours (24×7 considerations):
- Peak usage periods:
- Critical transactions and “minimum viable service” definition:

### A.3 Dependency mapping
| Dependency category | Dependency | CI / reference | DR requirement | Validation method |
|---|---|---|---|---|
| Identity |  |  |  |  |
| Network |  |  |  |  |
| Security tooling |  |  |  |  |
| Data |  |  |  |  |
| ITSM/monitoring |  |  |  |  |
| OT/IT integration |  |  |  |  |
| Supplier |  |  |  |  |

### A.4 Recovery strategy and sequencing
- Pattern (active-active / warm standby / pilot light / backup-restore):
- Sequencing prerequisites:
- Cutover mechanism (DNS, routing, load balancer):
- Backout plan:

### A.5 Operational runbook links and access
- ITSM knowledge article link(s):
- PAM access requirements:
- Break-glass procedure reference:
- Key contacts (primary/secondary):

### A.6 Validation and acceptance criteria
- Functional validation steps:
- Security validation steps (logging, EDR, access):
- Performance/SLO checks:
- Stakeholder sign-off requirements:

### A.7 Testing and exercise record
| Date | Exercise type | Result | RTO/RPO met | Issues | Linked ITSM record |
|---|---|---|---|---|---|

---

## Appendix B: Call Tree Template (Crisis Communications)
### B.1 Call tree structure
| Group | Primary contact role | Backup contact role | Method order | Expected response time |
|---|---|---|---|---:|
| Executive | CIO | Head of IT Infrastructure Services | Phone → SMS → ITSM | 30 minutes |
| Security | CISO | Security Engineer | Phone → SMS → ITSM | 30 minutes |
| Command | IT Operations Manager | Regional IT Operations lead | Phone → SMS → ITSM | 15 minutes |
| Process | ITSM Process Owner | IT Governance Manager | Phone → SMS → ITSM | 60 minutes |
| Service (ERP) | Service Owner | Platform Owner | Phone → SMS → ITSM | 30 minutes |
| Service (MES) | Service Owner | Platform Owner | Phone → SMS → ITSM | 30 minutes |
| Network edge | Platform Owner | Network Engineer | Phone → SMS → ITSM | 15 minutes |
| Identity | Platform Owner | IAM Engineer | Phone → SMS → ITSM | 15 minutes |
| Remote access | Platform Owner | Network Engineer | Phone → SMS → ITSM | 15 minutes |

### B.2 Communication message checklist
- Confirm incident identifier (ITSM major incident number).
- Current status (what is impacted, where, since when).
- Immediate user guidance (workarounds).
- Next update time and channel.
- Security guidance (phishing/ransomware cautions if applicable).
- Confirm whether OT operations are affected and any access restrictions.

---

## Appendix C: DR Exercise Schedule (Minimum Program)
### C.1 Annual schedule matrix
| Quarter | Exercise | Scope | Required participants | Evidence outputs |
|---|---|---|---|---|
| Q1 | Tabletop | Tier 0 services cross-region | Head of IT Infrastructure Services, IT Operations Manager, Service Owners, Platform Owners, CISO | Minutes, decision log, action list |
| Q2 | Technical failover test | Identity + Network edge | Platform Owners, IAM Engineer, Network Engineer, Security Engineer | Test plan, logs, validation screenshots/exports |
| Q3 | Technical failover test | ERP | Service Owner, Platform Owner, IT Operations Manager | RTO/RPO measurement, transaction proof, SIEM log proof |
| Q4 | Technical failover test | MES remote access pathway + VPN/ZTNA | Service Owner, Platform Owner, Regional IT Operations, Security Engineer | Access validation, segmentation validation, SIEM proof |
| Quarterly | Restore verification | Tier 0–1 backups | Platform Owners, Systems Engineer/Cloud Engineer | Restore job logs, integrity checks |
| Quarterly | Communications drill | Call tree | IT Operations Manager, Service Desk Manager, Regional IT Operations | Call results, response times, improvements |

---

## Appendix D: DR Evidence Checklist (Audit-Ready)
### D.1 Evidence package (per DR event or exercise)
| Evidence item | Description | Source system | Required for tiers |
|---|---|---|---|
| Major incident record | Timeline, decisions, stakeholders, status updates | ITSM | All |
| Change records | Emergency/Normal Changes including approvals and implementation notes | ITSM | All |
| Command log | Incident commander log including milestones and assignments | ITSM / approved repository | Tier 0–2 |
| Validation artifacts | Screenshots/exports of successful tests and transactions | Approved repository linked to ITSM | All |
| Replication/backup logs | RPO proof, restore job logs | Backup tooling / cloud logs | All |
| SIEM confirmation | Log ingestion proof during DR window (identity, edge, apps) | SIEM | Tier 0–1 |
| EDR health proof | Device health and threat status for recovered servers | EDR | Tier 0–1 (recommended all) |
| PAM session logs | Privileged access audit trail | PAM | Tier 0–1 (recommended all) |
| Communications archive | Copies of user and stakeholder messages | ITSM / collaboration exports | All |
| PIR report | Root cause, RTO/RPO variances, action plan | ITSM Problem record | All |

### D.2 Evidence quality checks
- Time stamps present and consistent across systems.
- Approvals attributable to named roles (per RACI).
- Steps are repeatable based on documented runbooks.
- Security controls validated (MFA/PAM/segmentation/logging) and recorded.

---

## Appendix E: DR Event Runbook (Declare → Activate → Failover → Failback)
### E.1 Declare disaster (checklist)
1. Confirm impact against DR tier targets and business criticality.
2. Open ITSM Major Incident flagged “DR Event”.
3. Assign Incident Commander and establish bridge.
4. Notify CIO, Head of IT Infrastructure Services, CISO (as applicable).
5. Activate call tree (Appendix B) and communications cadence (Section 9).

### E.2 Activate DR (checklist)
1. Confirm dependencies (network edge, DNS, identity).
2. Confirm privileged access via PAM and enforce MFA.
3. Freeze non-essential changes; implement Emergency Change governance.
4. Execute service runbooks in dependency order.
5. Validate and communicate milestones.

### E.3 Failover execution (checklist)
1. Confirm replication/backup position versus RPO.
2. Execute data and platform failover.
3. Cut over endpoints (DNS/routing/load balancer).
4. Validate transactions, access, logging, EDR health.
5. Document evidence continuously.

### E.4 Failback execution (checklist)
1. Confirm primary environment restored and security-verified.
2. CAB-approved failback plan.
3. Reconcile data and execute controlled cutback.
4. Validate and monitor 24–72 hours.
5. Close major incident; initiate PIR and track actions.