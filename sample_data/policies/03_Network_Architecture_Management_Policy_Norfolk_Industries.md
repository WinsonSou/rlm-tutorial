# Network Architecture & Management Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory requirements for network architecture, configuration, operation, and management across Norfolk Industries. It ensures secure, resilient, and standardized network services supporting 24×7 operations across North America, Europe, and APAC, while enabling centralized governance and regional execution.

## 2. Scope
### 2.1 In Scope
- All Norfolk Industries network environments supporting Information Technology (IT) and Operational Technology (OT), including:
  - Campus and plant networks (core, distribution, access layers)
  - Data center networks (on-prem and cloud connectivity)
  - WAN/SD-WAN and carrier services
  - Internet edge services and DMZ
  - Remote access (VPN and Zero Trust Network Access (ZTNA) where applicable)
  - Wireless networks (corporate and guest Wi-Fi)
  - Network security services (firewalls, NAC, IDS/IPS capabilities where implemented)
  - Network management services (monitoring, configuration backups, firmware lifecycle)

### 2.2 Out of Scope
- Application-layer security controls (covered by application security standards)
- Non-network physical security controls (covered by facility security policies)
- End-user device configuration standards (covered by endpoint standards; this policy references integration requirements)

## 3. Policy Statement
Norfolk Industries shall design, implement, and operate networks using a standardized, layered architecture with strong segmentation between IT and OT, least privilege access controls, validated change governance through the Change Advisory Board (CAB), and continuous monitoring. All network changes must be authorized, traceable, and aligned with the Information Security Management System (ISMS), service continuity requirements, and regulatory obligations (including GDPR and SOX where applicable).

## 4. Definitions
Terms used in this document follow the Norfolk Industries glossary:
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
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

### 5.2 Operational Responsibilities (Network Domain)
- **Head of IT Infrastructure Services**: Accountable for enterprise network architecture standards, operational outcomes, and resourcing.
- **Service Owner** (Network Services): Accountable for end-to-end network service performance (SLO), risk posture, lifecycle, and compliance evidence.
- **Platform Owner** (Network): Accountable for architecture, engineering standards, approved technologies, and reference designs.
- **IT Operations Manager**: Responsible for operational execution, on-call readiness, incident coordination, and escalation management for network services.
- **Network Engineer**: Implements and supports network infrastructure per approved standards, procedures, and change governance.
- **Security Engineer**: Ensures network security tooling integrations, log onboarding to SIEM, and validation of control operation.
- **ITSM Process Owner**: Ensures Change Enablement, Incident Management, Problem Management, and Service Configuration Management practices are followed.
- **IT Governance Manager**: Coordinates policy lifecycle, exception handling, compliance reporting, and audit readiness.

## 6. Reference Architecture (Required Patterns)
Norfolk Industries uses a layered and segmented network architecture. Deviations require documented exception approval per Section 16.

### 6.1 Campus/Plant LAN (Core–Distribution–Access)
- **Core layer**: High availability, fast convergence, minimal policy; connects distribution blocks and upstream services (data centers/WAN/Internet edge).
- **Distribution layer**: Aggregation, routing boundaries, policy enforcement (where approved), and summarization.
- **Access layer**: Endpoints, printers, IoT, and plant-adjacent IT devices; enforces VLAN membership, NAC, and port security.

**Requirements**
- Redundancy at core and distribution for critical sites (dual devices/links where feasible).
- Access switches shall be managed, authenticated, and monitored; unmanaged switching is prohibited except as approved for specific OT use cases with compensating controls.
- STP and loop prevention must be implemented and validated for access environments.

### 6.2 WAN / SD-WAN
- Standard WAN topology is hub-and-spoke with regional hubs; site breakout patterns are approved per risk and performance needs.
- SD-WAN may be used to provide application-aware routing, centralized policy, and encryption over transports.

**Textual diagram: “hub/spoke”**
- Spokes (plants/offices) connect to regional hubs (North America, Europe, APAC).
- Hubs connect to:
  - On-prem data centers
  - Microsoft Azure (primary)
  - AWS (secondary)
  - Internet edge services
- Control and policy are centralized; monitoring and operations are executed regionally under global standards.

### 6.3 Internet Edge and DMZ
- Internet connectivity shall terminate at approved Internet edge sites or cloud egress points with centralized policy and inspection.
- Public-facing services must reside in a controlled **DMZ** or equivalent cloud-segmented environment with explicit inbound and outbound rules.

**Textual diagram: “DMZ”**
- Internet → Edge Firewall → DMZ subnet(s) (public services, reverse proxies) → Internal Firewall boundary → Internal networks (user/server zones).
- Management access to DMZ systems is restricted to privileged admin paths and logged.

### 6.4 Remote Access (Corporate and Third Parties)
- Remote access shall follow least privilege and strong authentication using Entra ID (Azure AD) on first mention, then Entra ID.
- Standard remote access patterns:
  - **VPN** (where required for legacy apps or specific network-level access)
  - **ZTNA approach** (preferred for application-specific access): identity- and device-aware access, minimizing network-level reach.

**Requirements**
- MFA is required for remote access.
- Privileged remote administration must use PAM controls and session logging where integrated.
- Third-party remote access must be time-bound, approved, logged, and restricted to minimum required OT/IT zones.

### 6.5 Wireless (Corporate and Guest Wi-Fi)
- Corporate Wi-Fi: authenticated (enterprise), mapped to appropriate network segments, enforced via NAC posture where available.
- Guest Wi-Fi: Internet-only, isolated from internal IT and OT networks, with bandwidth controls.

### 6.6 OT Segmentation and Plant Network Integration
OT must be segmented from IT to reduce cyber risk and maintain plant safety and reliability.

**Textual diagram: “segmented OT zones”**
- IT Zone (corporate users/services)  
  → IT/OT Boundary Firewall(s)  
  → OT DMZ (jump hosts, patch staging, historian replication gateways as approved)  
  → OT Zone (SCADA/MES supervisory systems)  
  → Cell/Area Zones (production lines)  
  → PLC/Controller Zones (critical control devices)

**Requirements**
- Direct IT-to-PLC/controller access is prohibited unless explicitly approved with compensating controls and documented exception.
- OT remote access shall use strict controls (approved jump hosts, MFA, session recording where supported).
- Plant networks must maintain deterministic performance; security controls must be designed to avoid unsafe latency or instability.

## 7. Network Standards (Mandatory Technical Requirements)
### 7.1 IP Addressing and Subnetting
- IP addressing must follow an enterprise plan managed by the Platform Owner (Network) with regional allocation controls.
- Subnet design must support:
  - Segmentation by function (users, servers, OT, guest, management)
  - Route summarization where feasible
  - Capacity planning for growth and peak usage
- Private addressing (RFC1918) is standard for internal networks; public IP usage requires Service Owner approval and documented justification.

### 7.2 DNS and DHCP
- DNS is an enterprise service and must be integrated with Active Directory and/or approved cloud DNS patterns.
- DHCP shall be centrally governed; plant/site local DHCP is permitted only when necessary for resiliency and must be monitored.
- DNS and DHCP changes must follow Change Enablement and be traceable to approved requests.

### 7.3 Routing (Conceptual)
- Routing design must favor stability, fast convergence, and operational simplicity.
- Dynamic routing is permitted where standardized and documented; routing adjacencies must be authenticated where supported.
- Route redistribution between IT and OT networks must be minimized and explicitly controlled through boundary firewalls and routing policy.

### 7.4 Firewall Policy Model (Default Deny)
- All firewalls must follow a **default deny** model:
  - Explicit allow rules only
  - Least privilege (source, destination, ports, application where supported)
  - Time-bound rules for temporary access
- Rules must be:
  - Justified by a business/technical need
  - Mapped to an owner and expiration where applicable
  - Logged according to sensitivity and performance considerations
- Inbound Internet access to internal networks is prohibited; only DMZ or approved reverse proxy patterns are permitted.

### 7.5 Segmentation and Security Zones
Norfolk Industries uses zone-based segmentation with controlled conduits:
- User zone(s)
- Server zone(s)
- Management zone(s)
- DMZ
- Guest
- OT zones (OT DMZ, OT supervisory, cell/area, controller)

Inter-zone connectivity must be explicitly approved, documented, and monitored.

### 7.6 Network Access Control (NAC)
- NAC shall be used where feasible to enforce:
  - Authentication (802.1X or equivalent)
  - Device classification and authorization
  - Quarantine or restricted access for non-compliant devices
- Exceptions (for legacy OT or constrained devices) must be documented with compensating controls such as dedicated VLANs, strict ACLs, and physical port controls.

### 7.7 VPN and ZTNA Approach
- ZTNA is the preferred approach for user-to-application remote access where supported:
  - Identity-centric controls via Entra ID
  - Conditional access based on user risk and device compliance (as integrated with endpoint management)
  - Reduced network-level exposure
- VPN is permitted for:
  - Site-to-site encryption over untrusted transports
  - Legacy requirements needing network-layer access
- Split tunneling must be risk-assessed and approved; for privileged administration, full tunneling or equivalent inspection patterns are preferred.

### 7.8 Device Management and Secure Configuration
- Network devices are CIs and must be:
  - Inventoried in the CMDB (or equivalent ITSM configuration repository)
  - Hardened per approved standards (management plane protection, strong authentication, least privilege, secure protocols)
  - Accessible for administration only via approved management paths
- Management protocols must use secure encryption (e.g., SSH/HTTPS/SNMPv3 where supported).
- Default credentials are prohibited.

### 7.9 Logging, Telemetry, and SIEM Integration
- Network security logs and key operational logs must be forwarded to the SIEM (e.g., Microsoft Sentinel) per logging standards.
- Logs must be time-synchronized via approved time sources.
- Minimum logging scope includes:
  - Firewall allow/deny events (per policy)
  - Administrative access and configuration changes
  - VPN/remote access authentication events
  - NAC events (auth successes/failures, posture outcomes)

## 8. Service Management Requirements (ITIL 4 Alignment)
### 8.1 Service Catalog and Ownership
- Network services must have an identified Service Owner and SLOs where required (availability, latency targets for critical sites, incident response targets).
- Service definitions must include dependencies (carriers, cloud connectivity, identity, monitoring).

### 8.2 Service Configuration Management (CMDB)
- All network devices, circuits, key logical constructs (VRFs/VLANs where applicable), and security boundaries must be maintained as CIs.
- CI records must include:
  - Owner (Service Owner/Platform Owner)
  - Location/site
  - Support group (Regional IT Operations)
  - Firmware/software version
  - Support contract status
  - Backup and monitoring status

## 9. Operational Processes (Required)
### 9.1 Network Provisioning
- Provisioning must be performed using standardized designs and approved configurations.
- Minimum steps:
  - Validate requirements and segmentation classification (IT vs OT zone)
  - Allocate IP addressing and update DNS/DHCP as needed
  - Implement configurations using approved templates
  - Register/Update CIs and monitoring
  - Validate connectivity and security controls (NAC, firewall policies)

### 9.2 Firewall Rule Changes (Lifecycle)
- All rule changes require:
  - Documented request (see Appendix A)
  - Risk and impact assessment
  - Peer review and approval
  - CAB approval for Normal Changes; Emergency Change process only when justified and retrospectively reviewed by CAB
  - Validation evidence after implementation

### 9.3 Firmware/OS Upgrades
- Firmware upgrades must follow a risk-based lifecycle:
  - Routine updates scheduled (e.g., quarterly cadence) for standard devices
  - Accelerated updates for critical vulnerabilities based on vulnerability scanning and security advisories
- Requirements:
  - Pre-checks (compatibility, redundancy health, backups)
  - Maintenance window and communications
  - Rollback plan validated
  - Post-upgrade verification and monitoring

### 9.4 Configuration Backups
- All managed network devices must have automated configuration backups.
- Backups must be:
  - Encrypted in transit and at rest
  - Protected with least privilege access
  - Tested by periodic restore validation for representative device types

### 9.5 Network Monitoring and Performance Management
- Monitoring must include:
  - Availability (device/link up/down)
  - Interface errors and utilization
  - Latency/jitter/packet loss for WAN where supported
  - CPU/memory thresholds for critical devices
  - VPN/remote access health
- Alerting must integrate with the ITSM tool to create actionable incidents.
- Performance reporting must support capacity planning and SLO tracking.

### 9.6 Troubleshooting and Problem Management
- Major or recurring issues must transition from Incident Management to Problem Management with root cause analysis.
- Known errors and standard remediation steps must be documented and maintained by Regional IT Operations under global standards.

## 10. Security and Compliance Requirements
### 10.1 Identity and Privileged Access
- Administrative access to network devices must:
  - Use unique user identities integrated with centralized identity where feasible
  - Enforce MFA for remote administrative access
  - Use PAM for privileged sessions where supported and required by risk
- Shared admin accounts are prohibited except for break-glass scenarios with controlled storage, monitoring, and periodic review.

### 10.2 Vulnerability and Patch Management
- Network devices and management platforms must be included in vulnerability scanning scope where technically feasible without impacting OT safety and stability.
- For OT constraints, compensating controls must be documented and approved by the Service Owner and CISO as needed.

### 10.3 Data Protection and Privacy
- Network telemetry and logs must be handled per GDPR and internal data handling rules.
- Access to logs must be restricted and auditable.

### 10.4 SOX Considerations (Financial Controls)
- Network changes impacting financial systems connectivity or availability must be flagged and handled with enhanced change controls:
  - Evidence of approval, testing, and validation
  - Separation of duties in review/approval where applicable

## 11. Architecture Diagrams (Textual Standards)
Norfolk Industries maintains documented diagrams for each major site and service. At minimum, diagrams must include:
- **Hub/spoke WAN** depiction (regional hub, spoke sites, cloud connectivity, Internet edge)
- **DMZ** boundaries and flows (Internet, edge, DMZ services, internal networks)
- **Segmented OT zones** (IT/OT boundary, OT DMZ, OT supervisory, cell/area, controller zones)

Diagrams must be stored as controlled documents referenced by CI records and updated upon approved changes.

## 12. Procedural Requirements (Mandatory Procedures)
### 12.1 Procedure: Firewall Rule Request & Review
**Trigger:** New application connectivity, vendor access, segmentation changes, or incident-driven containment adjustments.

**Steps**
1. Requestor submits Firewall Rule Request (Appendix A) with complete source/destination/service details and business justification.
2. Network Engineer validates:
   - Correct zones and segmentation alignment
   - Minimal required ports/protocols
   - Feasibility and routing impacts
3. Security Engineer reviews:
   - Least privilege adherence
   - Logging requirements
   - OT boundary considerations (if applicable)
4. Service Owner approves functional need and confirms rule owner and expiration (if temporary).
5. CAB approval obtained for Normal Changes; Emergency Changes must be retrospectively reviewed by CAB with evidence.
6. Implementation by Network Engineer using standard naming conventions (Appendix C).
7. Post-implementation validation:
   - Connectivity test results
   - Firewall hit counters/log verification (where available)
   - Updated CI/documentation references
8. Periodic recertification:
   - Rules must be reviewed at a defined cadence (at least annually) for necessity and scope.

### 12.2 Procedure: Switch Port Activation (Access Layer)
**Trigger:** New endpoint, device move, plant equipment addition (where IT-managed switching is used).

**Steps**
1. Validate request details:
   - Device type and owner
   - Location (site/building/closet/switch/port)
   - Required VLAN/zone
2. Confirm segmentation classification (IT vs OT; guest devices prohibited on corporate access ports).
3. Apply standard port configuration:
   - Correct VLAN assignment
   - NAC enforcement (802.1X/MAB where applicable)
   - Port security and storm control where supported
4. Update CI relationships (device-to-port mapping where tracked).
5. Validate:
   - Link up and expected network access
   - NAC authentication result
6. Close request with evidence (change or request record, validation outcome).

### 12.3 Procedure: Site Turn-Up (New Site or Major Expansion)
**Trigger:** New plant/office, significant network refresh, WAN/SD-WAN onboarding.

**Steps**
1. Planning and design:
   - Confirm business requirements, criticality, and SLO targets
   - Create site topology aligned to reference architecture
   - Define IP plan, DNS/DHCP needs, and segmentation zones
2. Carrier and circuit readiness:
   - Validate demarc, testing, and redundancy needs
3. Security controls:
   - Define Internet edge pattern, DMZ needs, remote access requirements
   - Validate OT segmentation model if plant/OT is present
4. Build and staging:
   - Apply standard configurations
   - Validate firmware baselines and backups
5. Implementation under Change Enablement with CAB approval
6. Validation:
   - WAN performance tests (latency/jitter/packet loss where available)
   - Security validation (firewall rules, NAC, logging to SIEM)
   - Monitoring and alerting verification
7. Handover to Regional IT Operations:
   - Updated CMDB/CI records
   - As-built diagrams and documentation
   - On-call runbook updates

### 12.4 Procedure: Incident Triage Runbook (Network)
**Trigger:** Monitoring alert, user/site outage, security event, OT connectivity degradation.

**Triage Steps**
1. **Safety and OT impact check (if OT involved):**
   - Confirm whether OT processes are impacted
   - Engage OT stakeholders per site procedures; prioritize safe operation
2. **Scope determination:**
   - Single user/device vs VLAN/segment vs site vs region
   - Identify affected services (WAN, Internet edge, wireless, NAC, firewall)
3. **Stabilize:**
   - If active security threat suspected, coordinate with Security Engineer for containment actions (block rules, segmentation tightening) using Emergency Change if required
4. **Data collection:**
   - Monitoring alerts, interface status/errors, device health
   - Firewall logs and rule hit data
   - VPN/remote access auth logs
   - Recent changes from ITSM (last 24–72 hours) and CAB records
5. **Isolation and hypothesis testing:**
   - Layered checks: physical/link → L2/VLAN/NAC → routing → DNS/DHCP → firewall policy → application reachability
6. **Escalation:**
   - Engage carrier, cloud provider operations, or vendor support as required
   - Engage Global IT Operations for cross-region coordination
7. **Restore and validate:**
   - Confirm service restoration and stability
   - Communicate status via Service Desk Manager channels
8. **Post-incident:**
   - Document incident timeline and actions
   - Initiate Problem Management for recurring/root cause
   - Capture evidence for compliance and continuous improvement

## 13. Change Enablement and CAB Requirements
- Network changes are controlled changes and must follow ITIL 4 Change Enablement.
- Change categories:
  - **Standard Changes**: Pre-approved, low-risk, repeatable (e.g., approved port activations using standard configurations).
  - **Normal Changes**: Require CAB review/approval (e.g., new firewall rules, WAN routing changes, site cutovers).
  - **Emergency Changes**: Permitted only to restore service or contain active threats; must be documented with retrospective CAB review.
- All changes must include:
  - Implementation plan, validation steps, rollback plan
  - Impact assessment (including OT impact where applicable)
  - Evidence captured and linked to the change record

## 14. Documentation and Recordkeeping
- Network documentation must be maintained as controlled artifacts:
  - Reference architectures and as-built diagrams
  - IP plan allocations and DNS naming standards
  - Firewall rule base documentation and recertification records
  - Configuration backup status
  - Monitoring coverage and alert definitions
- Records must be time-bound, attributable, and repeatable in line with evidence principles.

## 15. Metrics, Monitoring, and Reporting
Minimum required metrics:
- Network availability by site/region and critical service components
- WAN performance metrics (latency/jitter/packet loss) where supported
- Change success rate and change-related incident rate
- Firewall rule recertification completion rate
- Configuration backup success rate
- Mean time to detect (MTTD) and mean time to restore (MTTR) for network incidents
- Logging coverage to SIEM for required network devices

Reports are owned by the Service Owner and reviewed with Global IT Operations and the Head of IT Infrastructure Services on an agreed cadence.

## 16. Exceptions
- Exceptions must be documented, risk-assessed, and approved according to governance requirements.
- High-risk exceptions require approval aligned to the “Exception approval (high risk)” RACI and must include compensating controls and expiry/review date.
- Exceptions involving OT segmentation or remote access require Security Engineer review and CISO oversight as needed.

## 17. Enforcement
Non-compliance may result in:
- Removal of unauthorized connectivity
- Increased monitoring and compensating controls
- Mandatory remediation plans with deadlines
- Escalation to the Head of IT Infrastructure Services and CISO for repeated or material violations

## 18. Control Mappings and Evidence Requirements
### 18.1 Control Mapping (Conceptual)
| Policy Area | ISO/IEC 27001 (Annex A concept) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Required Evidence Examples |
|---|---|---|---|---|---|---|
| Network segmentation & zoning | Access control; network security management | Protect | Security, Availability | Information Security Management | APO, DSS | Network diagrams; firewall zone matrix; approved rule sets; OT boundary validation |
| Change governance (CAB) | Change management; operational procedures | Protect, Respond | Security, Availability | Change Enablement | BAI, DSS | CAB minutes/approvals; change records; implementation/validation logs |
| Monitoring & logging to SIEM | Logging and monitoring | Detect, Respond | Security | Monitoring and Event Management | DSS, MEA | SIEM ingestion proof; alert rules; sample logs; time sync configuration |
| Remote access controls | Access control | Protect | Security, Confidentiality | Information Security Management | APO, DSS | Entra ID access policies; VPN/remote access logs; PAM session records |
| OT/IT boundary controls | Network security management | Protect, Detect | Security, Availability | Information Security Management; Service Continuity Management | APO, DSS | OT segmentation diagrams; boundary firewall rules; vendor access approvals; review attestations |
| Backup of device configs | Information backup | Recover | Availability | Service Continuity Management | DSS | Backup job logs; restore test records; access controls on backups |

### 18.2 Evidence Principles
Evidence must meet these requirements:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

## 19. Review Cycle
- This policy shall be reviewed at least annually by the IT Governance Manager, Service Owner, Platform Owner, Security Engineer, and approved per the RACI.
- Reviews must consider:
  - Material incidents and problem trends
  - Audit findings and compliance requirements
  - Changes in OT/IT integration scope
  - Technology lifecycle and vendor advisories

## Appendices

## Appendix A: Firewall Rule Request Template (Mandatory)
| Field | Required Content |
|---|---|
| Requestor name / department | Named individual and department |
| Business justification | Why the rule is required; impact if not implemented |
| Application/service name | Business service and technical component |
| Environment | Production / Non-production |
| Source zone / subnet(s) | Zone name and CIDR(s) |
| Source host(s) | Hostnames/IPs (avoid “any”) |
| Destination zone / subnet(s) | Zone name and CIDR(s) |
| Destination host(s) | Hostnames/IPs (avoid “any”) |
| Protocol/port | TCP/UDP/ICMP and specific ports; application-ID if supported |
| Direction | Inbound / Outbound / Inter-zone |
| NAT requirement | None / SNAT / DNAT with details |
| Authentication dependency | Entra ID, certificates, service accounts (if applicable) |
| Logging requirement | Log allow/deny as required; rationale if log suppression requested |
| Data sensitivity | Confidentiality considerations; GDPR relevance if applicable |
| OT impact assessment | Yes/No; if yes, identify OT zone(s) and stakeholder confirmation |
| Requested implementation window | Date/time; business constraints |
| Expiration date (if temporary) | Mandatory for temporary access |
| Testing/validation plan | How connectivity and security will be validated |
| Rollback plan | How to revert safely |
| Approvals | Service Owner approval; Security Engineer review; CAB approval reference |
| Rule owner | Individual/team responsible for ongoing ownership and recertification |

## Appendix B: Network Change Checklist (CAB-Ready)
### B.1 Pre-Change
- Confirm change record created in ITSM tool and correctly categorized (Standard/Normal/Emergency).
- Identify impacted CIs and services; validate CMDB entries.
- Confirm risk assessment completed, including OT impact (if applicable).
- Confirm maintenance window approved and communications prepared (Service Desk Manager coordination where required).
- Confirm backup status:
  - Device configuration backup completed within defined window
  - Current firmware version recorded
- Confirm implementation plan and rollback plan are documented and peer reviewed.
- Confirm monitoring plan (what alerts/metrics will be watched during change).

### B.2 During Change
- Record actual start time and key actions.
- Validate each step against plan; document deviations and rationale.
- Capture implementation evidence (command outputs, configuration diffs, screenshots where appropriate).
- Perform validation tests per plan and record results.

### B.3 Post-Change
- Record actual end time and outcome (success/with issues/rolled back).
- Verify:
  - Connectivity and performance
  - Firewall/NAC behavior as applicable
  - Log forwarding to SIEM remains functional
  - Monitoring alerts are normal
- Update documentation:
  - As-built diagrams if topology/flows changed
  - CI attributes (firmware version, relationships)
- Close change with evidence attachments and stakeholder confirmation.

## Appendix C: Standard Naming Conventions (Network)
### C.1 Device Naming Standard
Device names must be unique, readable, and location-aware.

**Format (recommended):**  
`NI-<REGION>-<SITE>-<ROLE>-<SEQ>`

**Components**
- `NI`: Norfolk Industries identifier
- `<REGION>`: NA / EU / APAC
- `<SITE>`: Approved site code
- `<ROLE>`: CORE, DIST, ACC, FW, WLC, AP, RTR, SDWAN, VPN
- `<SEQ>`: 01, 02, etc.

**Examples**
- `NI-NA-DET-CORE-01`
- `NI-EU-MAN-FW-01`
- `NI-APAC-SIN-SDWAN-01`

### C.2 Interface and Circuit Labels
- Circuits must include carrier and circuit ID in the CI record.
- Interface descriptions must include:
  - Remote device name
  - Remote interface (if known)
  - Circuit ID or link purpose (e.g., “OT Boundary Uplink”)

### C.3 Firewall Rule Naming
**Format (recommended):**  
`<SRCZONE>-to-<DSTZONE>-<APP>-<PORT>-<TICKET>`

**Example**
- `USER-to-SERVER-ERP-443-CHG0123456`

## Appendix D: Evidence Pack List (Audit-Ready)
The following evidence must be maintained and retrievable for network controls and audits:
- Approved network architecture standards and site as-built diagrams (hub/spoke, DMZ, segmented OT zones)
- CMDB extracts for network CIs (ownership, versions, locations, relationships)
- CAB artifacts:
  - CAB meeting minutes/approvals
  - Change records with implementation and validation evidence
- Firewall governance:
  - Firewall rule request tickets (Appendix A fields completed)
  - Rulebase exports/snapshots (as permitted)
  - Annual rule recertification attestations and action logs
- Monitoring and logging:
  - Proof of log ingestion to SIEM for in-scope devices
  - Sample alerts/incidents generated from monitoring
  - Time synchronization configuration evidence
- Configuration backups:
  - Backup job schedules and success logs
  - Restore test evidence for representative devices
- Firmware and vulnerability management:
  - Firmware lifecycle plans and maintenance records
  - Vulnerability scan summaries and remediation tracking (or documented compensating controls for OT constraints)
- Remote access and privileged access:
  - Entra ID access policy evidence for remote access where applicable
  - VPN/remote access logs (authentication and session metadata)
  - PAM session records for privileged network administration where implemented
- Incident and problem records:
  - Incident timelines, troubleshooting artifacts, and resolution notes
  - Problem Management root cause analyses for recurring network issues