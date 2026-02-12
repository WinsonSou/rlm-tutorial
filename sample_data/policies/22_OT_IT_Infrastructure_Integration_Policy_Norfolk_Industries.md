# OT / IT Infrastructure Integration Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for integrating **Operational Technology (OT)** and **Information Technology (IT)** environments at Norfolk Industries to enable secure, reliable, and compliant connectivity while protecting plant safety, production continuity, confidentiality, and integrity of information and systems. The policy is governed under the **Information Security Management System (ISMS)** and supports Norfolk Industries’ 24×7 operations with centralized governance and regional execution.

## 2. Scope
### 2.1 In Scope
This policy applies to:
- All OT environments, including **SCADA**, **MES**, plant networks, PLC-supporting systems, historian systems, engineering workstations, and OT jump servers.
- All IT environments operated by **IT Infrastructure Services**, including on-prem data centers and hybrid cloud (Microsoft Azure primary, AWS secondary).
- All interconnections between OT and IT networks, including:
  - Plant-to-corporate connectivity
  - Remote access (internal and third party)
  - Data flows (telemetry, logs, historian replication, reporting)
  - Identity integrations (Active Directory and **Entra ID (Azure AD)** on first mention, then Entra ID)
- Supporting security tooling integrations: SIEM (e.g., Microsoft Sentinel), EDR (e.g., Microsoft Defender for Endpoint), vulnerability scanning (e.g., Tenable/Nessus), PAM (e.g., CyberArk).

### 2.2 Out of Scope
- Standalone OT networks with no connectivity to IT or external networks (must remain standalone and documented in the CMDB as isolated).
- Product-specific engineering standards (addressed by platform standards and procedures) unless they affect boundary security or integration.

## 3. Policy Statement
Norfolk Industries will integrate OT and IT only when there is a defined business requirement, documented risk review, approved architecture, and verified security controls. OT/IT integration must:
- Enforce **segmentation using zones and conduits** with default-deny at boundaries.
- Use **jump servers** for administrative access; prohibit direct administrative access from IT user endpoints to OT assets.
- Apply **strict remote access controls** including strong authentication, least privilege, session recording where feasible, and time-bounded access.
- Account for OT patching constraints by applying **compensating controls** and heightened boundary monitoring.
- Ensure monitoring and event management at OT/IT boundaries with timely incident response coordination.
- Be managed through ITIL 4-aligned change enablement and **Change Advisory Board (CAB)** governance.

## 4. Definitions
All terms align to the Norfolk Industries glossary:
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: Governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: Cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.

Additional policy terms (introduced for this document and used consistently):
- **OT Zone**: A logical or physical network segment grouping OT assets with similar criticality and security requirements.
- **Conduit**: A controlled network path between zones where traffic is explicitly permitted, inspected, and logged.
- **OT Demilitarized Zone (OT DMZ)**: A buffer zone between IT and OT zones hosting brokered services (e.g., historian relay, patch staging, remote access gateways) to prevent direct IT-to-OT access.

## 5. Roles and Responsibilities
Roles must use the Norfolk Industries role catalog.

### 5.1 Governance and Accountability
- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes, including OT/IT integration boundary controls.
- **CISO**: Accountable for information security program and ISMS oversight, including OT/IT risk posture.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for the relevant infrastructure service (e.g., network security, remote access).
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain (e.g., network, cloud, endpoint).
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- **ITSM Process Owner**: Owns ITIL-aligned process design and continual improvement for Change/Incident/Problem/CMDB practices.
- **Security Engineer**: Implements security tooling, detection, response integrations, and control validation.
- **Network Engineer / Systems Engineer / Cloud Engineer / Endpoint Engineer / IAM Engineer**: Implement controls and configurations under their domains.
- **Internal Audit**: Independently assesses control design and operating effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment for any personal data flows across OT/IT boundaries.

### 5.2 RACI Summary (Policy-Level)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy Requirements
### 6.1 OT/IT Segmentation Model (Zones and Conduits)
1. **Zone-based segmentation is mandatory** for all OT networks connected to IT or external networks.
2. Norfolk Industries will implement at minimum the following zones, sized appropriately per site:
   - **Enterprise IT Zone** (corporate user and service networks)
   - **OT DMZ**
   - **OT Operations Zone** (SCADA servers, historian core, OT application services)
   - **OT Control Zone** (controllers, PLC-supporting services, control network segments)
   - **OT Engineering Zone** (engineering workstations and tooling)
   - **Remote Access Zone** (remote access gateways, bastions, session brokers)
3. **Conduits must be explicit and documented**:
   - All OT/IT traffic must traverse designated conduits enforced by firewalls or equivalent policy enforcement points.
   - **Default deny** at every OT boundary; permit rules must be minimal, specific, and time-bounded where feasible.
4. **No direct routing** from Enterprise IT Zone to OT Control Zone. Access must be brokered through the OT DMZ and approved conduits.
5. **Dual-homing is prohibited** for endpoints and servers (no simultaneous connection to both IT and OT networks), unless explicitly approved via exception under this policy and implemented with strict controls.

### 6.2 Jump Servers and Administrative Access Controls
1. Administrative access to OT assets must be performed via **OT jump servers** located in the OT DMZ or designated OT administrative zone.
2. Jump servers must enforce:
   - Strong authentication integrated with Active Directory/Entra ID where feasible and safe for OT operations.
   - Least privilege, role-based access, and removal of local administrator rights where possible.
   - Session timeouts, clipboard/file transfer restrictions aligned to risk.
   - Central logging to the SIEM (e.g., Microsoft Sentinel).
3. Direct administrative protocols (e.g., RDP/SSH) from IT user endpoints to OT assets are prohibited.
4. Privileged credentials for OT systems must be protected using PAM (e.g., CyberArk) where technically feasible; if not feasible, compensating controls must be documented and approved.

### 6.3 Remote Access Controls (Internal and Third Party)
1. Remote access into OT environments is permitted only when:
   - A business justification exists (production support, vendor support, emergency restoration).
   - The access path uses approved remote access services/gateways and jump servers.
   - The session is authenticated using strong methods and least privilege.
2. Remote access must meet the following minimum requirements:
   - **Approved entry point**: VPN/remote access gateway terminating in the Remote Access Zone or OT DMZ.
   - **Access mediation**: jump server or session broker; no direct remote access to OT endpoints.
   - **Time-bounded authorization**: access approvals must be time-limited; standing access is permitted only with documented justification and periodic review.
   - **Session accountability**: user identity, source IP, target system, and session start/stop must be logged; session recording must be enabled where supported and not disruptive to operations.
   - **Third-party access**: must use named accounts; shared accounts are prohibited unless an approved exception exists.
3. Remote access rules:
   - Vendor connectivity must not introduce uncontrolled inbound access paths into OT.
   - Split tunneling is prohibited for OT remote access connections unless explicitly risk-approved.

### 6.4 Firewalling, Traffic Control, and Secure Data Flows
1. All conduits must be enforced using managed firewall policy with:
   - Rule-level business justification.
   - Source/destination specificity (no “any/any”).
   - Explicit ports/protocols; deny all else.
   - Logging enabled for allowed and denied traffic at OT boundaries as feasible.
2. OT data flows to IT (e.g., reporting, historian replication) must use brokered services in the OT DMZ where feasible.
3. Inbound IT-to-OT application flows are prohibited unless:
   - The flow is required for operations.
   - The flow has undergone risk review.
   - Compensating controls exist (e.g., application-layer proxy, strict allowlisting, deep inspection where feasible).

### 6.5 OT Patch Constraints and Compensating Controls
1. Norfolk Industries recognizes OT patching constraints such as:
   - Vendor certification requirements
   - Maintenance window limitations
   - Safety and availability risks
   - Legacy OS/application dependencies
2. When OT patching is delayed or not feasible, compensating controls are mandatory, selected based on risk:
   - Increased boundary restrictions (tighten firewall rules, restrict conduits).
   - Application allowlisting where supported and safe.
   - Hardening (disable unused services, remove legacy protocols where feasible).
   - Network anomaly detection and enhanced logging at OT boundaries.
   - Strict privileged access controls and jump server-only administration.
   - Isolation of vulnerable assets into more restrictive OT zones.
3. Vulnerability findings affecting OT must be triaged with operational context and documented risk acceptance only through the exception process in Appendix A.

### 6.6 Boundary Monitoring and Detection
1. OT/IT boundary devices (firewalls, remote access gateways, jump servers) must send security-relevant logs to the SIEM (e.g., Microsoft Sentinel) or an approved central log platform.
2. Monitoring must include:
   - Authentication events (success/failure)
   - Privileged session initiation
   - Firewall rule hits for OT conduits
   - Alerts from EDR where feasible on jump servers and OT Windows/Linux systems that can support it
3. Alerting must be integrated into 24×7 operations with defined escalation paths coordinated by the **IT Operations Manager** in conjunction with the **CISO** function.

### 6.7 Change Enablement and CAB Governance
1. All OT/IT integration changes must follow ITIL 4 **Change Enablement** and be recorded in the ITSM tool.
2. **CAB approval is required** for:
   - New OT/IT connections
   - Changes to firewall policies affecting OT conduits
   - Remote access enablement or material configuration changes
   - Changes that impact production safety or availability
3. Emergency changes must follow emergency change procedures and be retrospectively reviewed by the CAB.

### 6.8 Asset and Configuration Management
1. All boundary devices, jump servers, and OT/IT integration components must be maintained as **Configuration Items (CIs)** in the CMDB, including:
   - Zone membership
   - Conduit definitions
   - Owner assignment (Service Owner / Platform Owner)
   - Support group (Global IT Operations and/or Regional IT Operations)
2. Network diagrams and data flow documentation must be kept current and version-controlled.

### 6.9 Data Protection and Privacy
1. Data flows across OT/IT boundaries must be classified and minimized.
2. Personal data processing (if any) must be reviewed with the **Data Protection Officer (DPO)** for GDPR alignment, including logging and retention considerations.

## 7. Procedures (Policy-Mandated)
The following procedures are mandatory and must be executed using ITSM workflows and documented evidence.

### 7.1 Procedure: Approve OT Connectivity (New or Material Change)
1. Requestor submits an OT/IT integration request in the ITSM tool including:
   - Business purpose and operational justification
   - Source and destination zones and systems (CIs)
   - Required ports/protocols and directionality
   - Data classification and any personal data considerations
   - Availability requirements and planned maintenance window
2. **Platform Owner** (Network) and **Service Owner** (Network Security/Remote Access) validate architecture alignment to zones/conduits.
3. **Security Engineer** performs security review and monitoring requirements.
4. **CISO** function review is required for high-risk connections (e.g., inbound flows into OT, third-party standing access).
5. **CAB** reviews and approves (Normal Change) or approves and retrospectively reviews (Emergency Change).
6. Upon approval, implementation is scheduled by **Regional IT Operations** with oversight from **Global IT Operations** as applicable.

### 7.2 Procedure: Implement Firewall Rules for OT Conduits
1. Validate that:
   - The conduit is defined and documented.
   - Default deny is preserved.
2. Create firewall rules with:
   - Explicit source/destination objects mapped to CIs
   - Explicit ports/protocols
   - Logging enabled
   - Expiration date for temporary rules (where feasible)
3. Peer review:
   - **Network Engineer** drafts configuration.
   - **Platform Owner** reviews for standards compliance.
   - **Security Engineer** validates security controls and logging.
4. Implement change during approved window.
5. Post-implementation validation:
   - Connectivity test (expected traffic only)
   - Confirm logs visible in SIEM
   - Update CMDB conduit documentation and diagrams
6. Attach evidence to the ITSM change record (see Appendix C).

### 7.3 Procedure: Conduct OT/IT Integration Risk Review
1. Identify assets and criticality:
   - Safety/availability impact
   - Production impact
   - Data sensitivity
2. Identify threats and constraints:
   - Remote access exposure
   - Patchability constraints and known vulnerabilities
   - Third-party dependencies
3. Determine required controls:
   - Segmentation placement and conduit rules
   - Jump server requirements and authentication
   - Monitoring/alerting coverage
   - Compensating controls for patch delays
4. Risk decision:
   - Acceptable risk proceeds to CAB for approval.
   - Unacceptable risk requires redesign or formal exception (Appendix A).
5. Record risk review outcome in ITSM and link supporting documents.

### 7.4 Procedure: Incident Response Coordination for OT/IT Events
1. Detection:
   - Alerts from SIEM/EDR/firewalls or operational reports.
2. Triage:
   - **IT Operations Manager** coordinates initial triage with **Security Engineer**.
   - Determine if OT operations may be impacted and if containment could affect production.
3. Containment:
   - Prioritize safe containment actions (boundary blocks, session termination) that minimize operational disruption.
   - Coordinate with Regional IT Operations for site execution steps.
4. Escalation:
   - Engage **CISO** function for security incident governance.
   - Engage relevant **Service Owner** and **Platform Owner** for technical remediation.
5. Recovery:
   - Restore authorized connectivity and validate system integrity.
6. Post-incident:
   - Capture lessons learned; create Problem record as appropriate.
   - Review conduits, remote access rules, and compensating controls.

## 8. Compliance and Exceptions
1. Compliance with this policy is mandatory for all Norfolk Industries sites and regions.
2. Exceptions are permitted only through the OT exception process in Appendix A and must:
   - Be time-bound
   - Include compensating controls
   - Be approved per the RACI (including high-risk approvals)
3. Non-compliance may result in access revocation, change rollback, disciplinary actions per HR policy, and increased audit scrutiny.

## 9. Control Mapping (Standards Alignment)
Control mapping is conceptual and must be supported by evidence per the standards evidence principles.

| Policy Area | ISO/IEC 27001 (Annex A concept) | NIST CSF | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Typical Evidence |
|---|---|---|---|---|---|---|
| Segmentation (zones/conduits) | Network security, access control | Protect | Security, Availability | Information Security Management | APO, DSS | Approved network diagrams, firewall configs, CMDB CIs |
| Jump servers & privileged access | Access control, privileged access | Protect | Security | Information Security Management | DSS | Jump server build standard, PAM logs, access reviews |
| Remote access controls | Access control, supplier access | Protect | Security, Availability | Supplier Management; Information Security Management | APO, DSS | Remote access approvals, session logs, vendor account inventory |
| Patch constraints & compensating controls | Vulnerability management | Protect, Detect | Security, Availability | Information Security Management | DSS, MEA | Vulnerability reports, exception records, boundary hardening evidence |
| Boundary monitoring | Logging/monitoring | Detect, Respond | Security | Monitoring and Event Management | DSS | SIEM alerts, log forwarding configs, use case runbooks |
| Change governance for OT/IT | Change management | Protect | Security, Availability | Change Enablement | BAI, DSS | CAB minutes, change records, implementation validation |

## 10. Evidence Requirements
Evidence must be **time-bound, attributable, and repeatable** and include approvals, logs, and validation artifacts where applicable.

Minimum evidence per OT/IT integration:
- Approved ITSM request and associated risk review.
- CAB approval record (Normal/Emergency).
- Firewall rule set export or configuration diff with peer review evidence.
- Jump server access logs and (where enabled) session recording references.
- SIEM log ingestion confirmation and alerting configuration references.
- Updated CMDB records for CIs, zone membership, and conduits.
- Vulnerability assessment results and patch/compensating control decision record.

## 11. Metrics and Reporting
Global IT Operations will coordinate reporting with Regional IT Operations.

Minimum metrics:
- Number of OT/IT conduits by site and risk rating.
- Percentage of OT boundary devices forwarding logs to SIEM.
- Count of OT remote access sessions (internal vs third party) and percent time-bounded.
- Vulnerability aging for OT assets with documented patch constraints.
- Number of active exceptions and average days to expiry.
- Change success rate for OT boundary changes (incident-free implementations).

## 12. Technology Standards (Minimum Baselines)
1. Boundary enforcement:
   - Managed firewalls with centralized policy management where feasible.
   - Unique administrative accounts and strong authentication.
2. Jump servers:
   - Hardened builds, minimal software, EDR where compatible, restricted admin access.
3. Identity:
   - Central identity integration where feasible; if OT constraints prevent it, document alternative authentication and compensating controls.
4. Logging:
   - Time synchronization for boundary devices and jump servers.
   - Log retention aligned to ISMS requirements and legal/regulatory constraints.
5. Vulnerability management:
   - OT-safe scanning approaches; avoid disruptive scanning without site approval.

## 13. Risk Management
1. OT/IT integration risk must be assessed prior to implementation and upon material change.
2. Risk decisions must consider:
   - Safety and operational continuity
   - Cybersecurity threats and vulnerability exposure
   - Regulatory and audit impacts (SOC 2, SOX, GDPR as applicable)
3. Residual risk acceptance requires documented approval and compensating controls, managed via exception process.

## 14. Training and Awareness
1. Required training for personnel with OT/IT integration responsibilities:
   - OT segmentation principles (zones/conduits)
   - Secure remote access practices and vendor access governance
   - Change Enablement and CAB expectations for OT boundary changes
   - Incident response coordination for OT environments
2. Training completion evidence must be retained for audit purposes.

## 15. Supplier and Third-Party Management
1. Third-party OT support access must be:
   - Contractually bounded (security requirements, logging, breach notification)
   - Access-controlled via named identities and time-bounded approvals
   - Terminated promptly when no longer required
2. Third-party tooling introducing connectivity (e.g., remote support appliances) is prohibited unless explicitly approved and integrated into the segmentation model with monitored conduits.

## 16. Service Continuity and Resilience
1. OT boundary components (firewalls, remote access gateways, jump servers) supporting critical operations must have resilience appropriate to operational impact.
2. **RTO** and **RPO** for OT integration services must be defined by the relevant **Service Owner** and validated with Regional IT Operations.
3. Disaster recovery and restoration activities impacting OT/IT conduits must be governed through Change Enablement and tested as part of continuity planning aligned to ISO/IEC 22301.

## 17. Policy Review and Maintenance
1. The **IT Governance Manager** coordinates review of this policy at least annually and after significant incidents, architecture changes, or audit findings.
2. The **Head of IT Infrastructure Services** is accountable for ensuring updates are implemented and communicated.
3. Changes to this policy require approval per the RACI table and must be published through the ISMS policy lifecycle.

## 18. References
- ISO/IEC 27001 (ISMS) and ISO/IEC 22301 (BCMS)
- NIST Cybersecurity Framework (NIST CSF)
- NIST SP 800-53 concepts
- ITIL 4 practices: Change Enablement, Incident Management, Monitoring and Event Management, Information Security Management, Supplier Management, Service Continuity Management, Service Configuration Management
- COBIT 2019 domains (EDM, APO, BAI, DSS, MEA)
- SOC 2 Trust Services Criteria
- GDPR and SOX requirements as applicable to data flows and controls

## 19. Appendices
### Appendix A: OT/IT Integration Exception Template (OT Exception)
Use this template for exceptions to segmentation, jump server enforcement, patch timelines, logging, or remote access requirements.

| Field | Required Content |
|---|---|
| Exception Title | Clear description (e.g., “Legacy HMI cannot support EDR; compensating controls applied”) |
| Requestor | Name, role, region/site |
| Affected CIs | CI identifiers for systems, firewalls, jump servers, conduits |
| Exception Type | Segmentation / Remote Access / Patching / Logging / Identity / Other |
| Business Justification | Operational requirement and why compliance is not feasible |
| OT Impact Assessment | Safety impact, production impact, maintenance window constraints |
| Risk Summary | Threats introduced, likelihood, impact |
| Compensating Controls | Specific controls (boundary restrictions, allowlisting, monitoring, isolation, privileged access restrictions) |
| Monitoring Plan | Logs collected, alerts configured, review frequency, responsible role |
| Time Bound | Start date, end date (expiry), renewal criteria |
| Approvals | Service Owner; Platform Owner; Security review; high-risk approval per RACI (CIO/Head of IT Infrastructure Services/CISO as applicable) |
| Validation Evidence | Artifacts proving compensating controls are in place |
| Renewal/Closure Notes | Closure criteria and evidence required |

### Appendix B: OT/IT Boundary Monitoring Checklist
Use this checklist for go-live and periodic validation of OT boundary monitoring.

| Check | Verification Steps | Evidence Artifact |
|---|---|---|
| Firewall log forwarding | Confirm boundary firewall sends allow/deny logs to SIEM | SIEM ingestion screenshot/export; firewall syslog config |
| Remote access gateway logs | Confirm authentication and session logs are centrally collected | SIEM query results; gateway audit log export |
| Jump server authentication logs | Confirm successful/failed logons captured | Windows/Linux auth log forwarding proof; SIEM queries |
| Privileged access traceability | Confirm privileged sessions map to named identities | PAM logs or jump server session logs |
| Time synchronization | Confirm NTP/time sync on boundary devices and jump servers | Device time status outputs; monitoring checks |
| Alert use cases enabled | Verify key alerts (e.g., repeated failures, new conduit traffic spike) | SIEM analytic rule list; test alert record |
| On-call routing | Confirm alerts route to 24×7 operations | ITSM alert integration record; on-call schedule reference |
| Noise tuning | Validate allowlisted expected traffic and thresholds | Change record documenting tuning; SIEM rule revision history |
| Periodic review | Confirm scheduled review of boundary alerts/logs | Recurring task record; review notes |

### Appendix C: Evidence List for OT/IT Integration (Audit-Ready)
Evidence must follow Norfolk Industries evidence principles: time-bound, attributable, repeatable; include approvals, logs, and validation artifacts.

| Control Area | Evidence Item | Source System / Owner |
|---|---|---|
| Connectivity approval | ITSM request with business justification and scope | ITSM tool / ITSM Process Owner |
| Risk review | Completed OT/IT integration risk review record | ITSM tool / Security Engineer |
| CAB approval | CAB decision record linked to change | ITSM tool / Head of IT Infrastructure Services (CAB chairing accountability) |
| Firewall implementation | Rule request, peer review evidence, config export/diff | Firewall manager / Network Engineer |
| Conduit documentation | Updated zone/conduit diagrams and CMDB CI relationships | CMDB / Platform Owner |
| Remote access governance | Time-bounded approvals, named accounts, session logs | Remote access platform / Service Owner |
| Jump server control | Build baseline, access logs, hardening validation | Systems platform / Systems Engineer |
| Monitoring | SIEM log ingestion confirmation; alert configuration; sample events | SIEM / Security Engineer |
| Vulnerability and patch constraints | Vulnerability report; patch plan or exception; compensating controls | Vulnerability scanner + ITSM / Service Owner |
| Incident coordination | Incident records, timelines, containment actions, post-incident review | ITSM tool / IT Operations Manager |
| Exception management | Approved exception record with expiry and renewal/closure evidence | ITSM tool / IT Governance Manager |