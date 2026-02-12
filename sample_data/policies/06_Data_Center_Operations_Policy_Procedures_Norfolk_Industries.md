# Data Center Operations Policy & Procedures (Norfolk Industries)

## 1. Purpose
This document defines the policy and procedures for secure, reliable, and auditable data center operations at Norfolk Industries. It establishes standardized requirements for physical access control, environmental and infrastructure monitoring, operational routines, and repeatable execution procedures (Methods of Procedure) to support 24×7 operations under centralized governance and regional execution.

## 2. Scope
### 2.1 In scope
- All Norfolk Industries on-prem data centers, server rooms, network rooms, and co-location spaces used to operate Information Technology (IT) services.
- Physical access control, visitor handling, escorting, key/badge management, and access reviews.
- Environmental controls and monitoring (power, cooling, humidity, water leak detection, smoke/fire detection).
- Rack, cabling, labeling, and asset/Configuration Item (CI) requirements.
- Operational routines (daily checks, scheduled maintenance, vendor coordination).
- Procedures for rack installation, Move/Add/Change (MAC), break-fix, and media handling.

### 2.2 Out of scope
- Operational Technology (OT) plant floor access controls and plant network cabinet standards (covered under OT security and plant network standards), except where OT systems are hosted in an IT-managed data center space.
- Application-level operations not directly tied to data center infrastructure.
- Detailed building safety programs beyond data center operational controls (owned by Facilities/EHS processes), while this document specifies IT requirements and coordination points.

## 3. Audience
- IT Infrastructure Services personnel and contractors performing work in data centers.
- Global IT Operations and Regional IT Operations.
- Service Owners and Platform Owners for infrastructure platforms hosted in data centers.
- Information security stakeholders supporting the Information Security Management System (ISMS).
- Internal Audit for assurance and evidence validation.

## 4. Definitions (Glossary)
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

## 5. Policy Statement
Norfolk Industries shall operate data centers using standardized, secure, and auditable processes that:
- Protect facilities and hosted assets from unauthorized physical access and environmental threats.
- Maintain reliable power, cooling, and monitoring aligned to service availability requirements and defined SLOs.
- Ensure all work is controlled through ITIL-aligned change enablement and documented Methods of Procedure (MOPs) for repeatability.
- Maintain accurate CI records and evidence suitable for ISMS, SOC 2, SOX, and audit requirements.
- Coordinate vendor and third-party activity using approved access controls, escort requirements, and documented work orders.

## 6. Roles and Responsibilities
Roles are used exactly as defined in the Norfolk Industries roles catalog.

### 6.1 Responsibilities overview
| Role | Key responsibilities for data center operations |
|---|---|
| CIO | Executive oversight of IT governance expectations impacting business risk. |
| Head of IT Infrastructure Services | Accountable for overall data center operations policy adherence and outcomes. |
| CISO | Oversight of physical security requirements under the ISMS; consults on high-risk exceptions. |
| IT Governance Manager | Policy lifecycle, compliance tracking, exception governance support, audit coordination and evidence principles. |
| Service Owner | Accountable for service outcomes, RTO/RPO alignment, and approving service-affecting maintenance in coordination with change enablement. |
| Platform Owner | Technical standards for platforms hosted in the data center (network/compute/storage). |
| IT Operations Manager | Operational execution, 24×7 readiness, incident coordination, and operational routines. |
| ITSM Process Owner | Ensures ITIL-aligned Change Enablement, Incident Management, and Service Configuration Management are followed. |
| Internal Audit | Independent assessment of control design and operating effectiveness. |

### 6.2 RACI alignment (selected activities)
| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 7. Governance, Compliance, and Control Mapping
### 7.1 Governance principles
- Centralized governance: Global IT Operations defines minimum requirements; Regional IT Operations executes locally with site-specific procedures that meet or exceed this document.
- All recurring controls must produce **time-bound, attributable, repeatable** evidence and include approvals, logs, and validation artifacts where applicable.

### 7.2 Standards alignment (control mapping)
| Control area | Primary alignment | Practical data center control topics covered |
|---|---|---|
| ISO/IEC 27001 (Annex A concept areas) | ISO27001 | Physical access control, secure areas, equipment protection, logging, supplier controls, media handling. |
| NIST CSF | Identify/Protect/Detect/Respond/Recover | Asset identification (CI), protective access controls, monitoring, incident response, recovery readiness. |
| SOC 2 Trust Services Criteria | Security/Availability/Confidentiality/Privacy | Facility security, availability safeguards, change control evidence, secure disposal and media protection. |
| ITIL 4 practices | Change Enablement, Incident Management, Service Configuration Management, Monitoring and Event Management, Supplier Management, Service Continuity Management, Information Security Management | CAB-controlled work, operational routines, event monitoring, vendor coordination, continuity requirements. |
| COBIT 2019 domains | EDM/APO/BAI/DSS/MEA | Governance oversight, planning and standards, build/change controls, operations and support, monitoring and assurance. |
| GDPR and SOX | Governance requirements | Access restriction, audit trails, change approvals, protection of systems processing personal data and financial reporting systems. |

## 8. Data Center Access Control Policy
### 8.1 Secure area classification
All data center spaces are designated **secure areas**. Entry is restricted to authorized personnel with a validated business need.

### 8.2 Approved access methods
- Primary access method: badge access integrated with enterprise identity processes (Active Directory + **Entra ID (Azure AD)** on first mention, then **Entra ID**).
- Where biometrics are present, they are additive controls and must follow privacy governance and local law requirements.

### 8.3 Access authorization requirements
Access must meet all of the following:
- Approved request with business justification and defined duration (permanent or time-bound).
- Manager approval and data center owner approval within IT Infrastructure Services.
- Completion of required security awareness and site safety requirements.
- Agreement to comply with escorting rules and prohibited activities.

### 8.4 Least privilege and time-bounded access
- Access is granted only to required areas (cage/room/rack row) and only for required time.
- Temporary access is preferred for non-routine work, vendors, and contractors.
- Emergency access is permitted only under an approved emergency process and must be reviewed after the fact (see Section 13).

### 8.5 Prohibited activities
- Piggybacking/tailgating or propping secure doors.
- Unauthorized photography/video recording.
- Connecting unauthorized devices to network, console ports, or power.
- Removing equipment or media without documented authorization and chain-of-custody.

## 9. Visitor Handling, Escort Rules, and Access Reviews
### 9.1 Visitor handling process
Visitors include vendors, contractors, auditors, and any Norfolk Industries personnel without approved access.

**Minimum visitor controls:**
1. **Pre-registration**: Visitor request submitted via ITSM ticket with visit purpose, date/time, and areas required.
2. **Identity verification**: Government-issued photo identification verified at sign-in.
3. **Visitor log**: Visitor sign-in/out recorded with time stamps, host name, and purpose.
4. **Badge issuance**: Visitor badge is distinct and time-limited; must be worn visibly.
5. **Safety briefing**: Site-specific safety instructions provided (e.g., emergency exits, alarms).
6. **Escort assignment**: Escort is assigned prior to entry; the escort remains accountable for visitor actions.
7. **Exit control**: Badge returned; sign-out completed; confirmation that no assets/media are removed unless authorized.

### 9.2 Escort rules
- Visitors must be escorted **at all times** within secure areas.
- Escorts must be authorized data center access holders (or otherwise approved by IT Operations Manager for the site).
- Escort-to-visitor ratio:
  - Normal work: 1 escort to up to 2 visitors when tasks are low-risk and remain in a single area.
  - Higher-risk work (e.g., cabling changes, power work, media handling): 1:1 escort ratio.
- Escorts must maintain line-of-sight and be present for any device interaction, including console access.

### 9.3 Vendor coordination requirements
- Vendor work must be linked to an approved Change record (Normal/Emergency as appropriate) and a MOP (Appendix B).
- Vendor credentials (remote or local) must use Norfolk Industries approved access methods. Shared vendor accounts are prohibited for administrative functions; named accounts are required where feasible.
- Vendor-provided evidence (work completion notes, test results, part serial numbers) must be attached to the ticket/change record.

### 9.4 Access reviews
- **Quarterly access review** for permanent badge holders to confirm:
  - continued business need,
  - correct scope of access (areas),
  - role appropriateness and employment/contract status.
- **Monthly review** of any time-bound or emergency access grants completed in the prior month to ensure timely removal and post-event validation.

**Access review evidence requirements:**
- Export of access list (date/time stamped) from access control system.
- Review sign-off by IT Operations Manager and Head of IT Infrastructure Services delegate.
- Remediation log showing removals/adjustments and completion date.

## 10. Environmental Monitoring and Facility Standards
### 10.1 Monitoring requirements
Environmental conditions must be monitored continuously with alerts routed to Global IT Operations and Regional IT Operations on-call processes (24×7).

Minimum monitored signals:
- Temperature (inlet/ambient) by row/zone.
- Humidity (relative humidity).
- Water leak detection (under raised floor and near cooling equipment where applicable).
- Smoke and fire detection system status (alarm/trouble conditions).
- Power status (UPS, PDU, generator, ATS where present).
- Cooling status (CRAC/CRAH status, chilled water supply/return, alarms).
- Door status for critical entrances (open/forced).

### 10.2 Alert handling and escalation
- Alerts generate events in monitoring and/or the SIEM (e.g., Microsoft Sentinel) when security-relevant.
- Critical alerts must be acknowledged within the operational on-call response expectations defined by the IT Operations Manager.
- All critical environmental incidents require an incident ticket with timeline, actions, and outcome; post-incident review is required for major events.

### 10.3 Power and cooling redundancy concepts
Norfolk Industries designs and operates data center power/cooling with redundancy commensurate with service criticality and site capabilities.

Minimum expectations:
- UPS protection for critical IT loads where feasible.
- Dual power feeds to equipment when supported (dual PSUs) and to separate PDUs/circuits where available.
- Generator backup where available; where not available, documented runtime expectations and graceful shutdown procedures must exist for critical services.
- Cooling redundancy or capacity management sufficient to maintain safe operating temperatures during component failure or maintenance, aligned to local facility design.

### 10.4 Rack standards
- Racks must be physically secured (bolted/anchored as applicable) and grounded per facility standards.
- No rack may exceed its rated load, power, or thermal design.
- Rack elevation (U-position) documentation is required for all installed equipment.
- Blank panels must be used to maintain proper airflow in hot/cold aisle environments where implemented.
- Equipment must be mounted with vendor-approved rails; shelf mounting requires approval by the Platform Owner.

### 10.5 Cabling standards
- All cables must be labeled at both ends using a consistent format (see Appendix D checklist).
- Copper and fiber must be routed using cable management to avoid airflow obstruction and reduce strain.
- Power cables must be separated from data cables where practicable to reduce interference and improve safety.
- Patch cords must be appropriately sized; excessive slack is prohibited.
- Color conventions (where used) must be documented per site and applied consistently.
- Any cross-connects, meet-me-room links, or carrier handoffs must be documented as CIs with circuit identifiers.

## 11. Operational Routines and Maintenance
### 11.1 Daily operational checks (24×7 readiness)
Regional IT Operations performs daily checks for each active data center site. At minimum:
- Review environmental dashboard and alarms (power, cooling, water).
- Confirm critical monitoring heartbeat (monitoring system operational).
- Review open incidents/changes that could impact facility operations.
- Validate secure area integrity (no forced/open door alarms unresolved).
- Confirm any ongoing vendor work is tracked and escorted per Section 9.

Daily check evidence:
- Dated checklist (Appendix D) attached to an ITSM worklog or stored in an approved repository with attribution.

### 11.2 Weekly and monthly routines
- Weekly: verify spare parts inventory counts (site-defined), check KVM/console access readiness, validate local procedures currency.
- Monthly: test alert routing (synthetic alarm test where feasible), review environmental trend reports for capacity risk (temperature excursions, UPS load trends).

### 11.3 Maintenance windows
- Standard maintenance windows are defined by Regional IT Operations in alignment with Global IT Operations governance and service requirements.
- All non-trivial work in the data center requires an approved Change record, risk assessment, MOP, and backout plan.
- Maintenance work must consider RTO/RPO and service dependencies; Service Owner approval is required for service-affecting changes.

### 11.4 Housekeeping and safety
- Keep aisles clear; no storage of combustible materials.
- ESD controls must be used when handling sensitive components.
- Ladders/tools must be controlled; tools must not be left unattended in secure areas.
- Any facility safety incident must be immediately reported through the established safety process and linked to an ITSM incident if IT impact exists.

## 12. Configuration Management and Asset Handling
### 12.1 CMDB / CI requirements
- All servers, network devices, storage systems, rack PDUs, UPS interfaces, and critical circuits must be represented as CIs.
- CI records must include: location (site/room/row/rack/U), serial number, owner (Service Owner/Platform Owner), support contract, and criticality.
- MAC activities must update CI records within the operational completion criteria of the change.

### 12.2 Labeling requirements
Minimum labels:
- Rack: rack ID, row/zone, contact/on-call reference.
- Device: hostname/device name and CI identifier where supported.
- Cables: both ends labeled with source and destination identifiers.

### 12.3 Asset movement controls
- No equipment may be removed from a secure area without:
  - an approved change/work order,
  - documented authorization,
  - chain-of-custody for any data-bearing device/media (see Section 16).

## 13. Change Enablement and CAB Requirements for Data Center Work
### 13.1 Change classification
- **Normal Change**: planned installs, MAC, cabling work, firmware upgrades requiring onsite activity, rack/power changes.
- **Emergency Change**: break-fix required to restore service or prevent imminent failure (e.g., failed PSU, overheating condition).

### 13.2 CAB involvement
- Normal Changes that impact production services, facility power/cooling, or shared infrastructure must be reviewed through the Change Advisory Board (CAB) per Change Enablement.
- Emergency Changes must be documented and reviewed retrospectively in CAB for control validation and improvement actions.

### 13.3 Required change artifacts (minimum)
- Approved Change record with scope and risk.
- MOP with step-by-step tasks, validation steps, and backout plan (Appendix B).
- Communication plan and maintenance window confirmation.
- Evidence of completion (photos where permitted, logs, test results, CI updates).

## 14. Incident Management Integration (Facility and Hardware)
### 14.1 When to declare an incident
Create an incident ticket immediately when:
- Environmental alarms indicate risk to IT loads (cooling failure, water leak, smoke/fire alarm, UPS failure).
- Unauthorized access attempt is suspected (forced door alarms, visitor policy breach).
- Hardware failure impacts or threatens service availability.

### 14.2 Coordination and escalation
- IT Operations Manager coordinates incident response and communications.
- Security-relevant events must be coordinated with Security Engineer processes and SIEM monitoring.
- Major incidents require a post-incident review with corrective actions and evidence retention.

## 15. Standard Procedures (Runbooks)
All procedures in this section require an ITSM ticket and, where service-affecting, an approved Change record. Procedures must use the MOP template in Appendix B.

### 15.1 Procedure: New rack installation
#### 15.1.1 Preconditions
- Approved capacity plan and location (row/rack layout approval by Platform Owner).
- Facilities confirmation of floor loading, power availability, cooling capacity.
- CI record created for the rack and associated PDUs.

#### 15.1.2 Steps
1. Confirm rack ID assignment and labeling materials.
2. Inspect delivery for damage; record shipment and serial numbers.
3. Position rack per approved floor plan; confirm clearance and airflow direction.
4. Anchor/secure and ground rack per facility requirements.
5. Install rack PDUs and verify circuit IDs; label power feeds (A/B where applicable).
6. Install cable management (vertical/horizontal); install blanking panels if needed.
7. Update rack CI with final location and attributes.
8. Validate:
   - door operation and locks,
   - PDU power readings/monitoring connectivity where applicable,
   - environmental sensor placement (if used).

#### 15.1.3 Completion criteria (evidence)
- Photos (where permitted) of rack label, PDU labels, and cable management readiness.
- Updated CI records (rack, PDUs, circuits).
- Facilities sign-off or work order closure note attached to the ITSM ticket.

### 15.2 Procedure: Move/Add/Change (MAC) in-rack (server/network/storage)
#### 15.2.1 Preconditions
- Approved Change record and scheduled maintenance window (if service affecting).
- MOP includes service impact, dependencies, and backout plan.
- Spare parts and tools staged; ESD protections available.
- Escort arranged if vendor/visitor involved.

#### 15.2.2 Steps
1. Verify correct device by CI/serial and rack/U location.
2. Confirm power redundancy plan (A/B feeds mapped) and current load headroom.
3. If adding:
   - mount rails and device,
   - connect power to correct PDUs (A/B),
   - connect network/storage cabling per port plan.
4. If moving:
   - document current connections (photo where permitted),
   - disconnect in sequence (data then power, unless safety requires otherwise),
   - move and reinstall with updated labeling.
5. If changing cabling:
   - validate port plan,
   - perform one connection at a time,
   - verify link status and service checks after each critical connection.
6. Validate service health (ping/management reachability, application checks as defined by Service Owner).
7. Update CI location, cabling references, and rack elevation.

#### 15.2.3 Completion criteria (evidence)
- MOP execution log with timestamps and executor name.
- Post-change validation results attached (monitoring green, service checks).
- CI updates completed and referenced in the Change record.

### 15.3 Procedure: Hardware break-fix (field replaceable units and chassis)
#### 15.3.1 Preconditions
- Incident ticket created and triage completed (hardware diagnostics, alarms).
- Determine whether Emergency Change is required (service impact or risk).
- Confirm parts availability and vendor RMA details.
- Confirm whether the device contains data-bearing components (disks/SSDs) that require media handling controls.

#### 15.3.2 Steps
1. Verify device identity and warranty/support entitlement.
2. If possible, capture diagnostics logs and current status (controller state, PSU status, fan state).
3. Implement safety controls:
   - identify correct power feed(s),
   - avoid power removal from redundant systems unless required.
4. Replace component per vendor instructions:
   - PSU/fan: replace and confirm status normal,
   - disk/SSD: follow Section 16 before removing any data-bearing media,
   - mainboard/chassis: ensure configuration backups are captured where applicable.
5. Validate:
   - hardware health normal,
   - no new critical alerts,
   - service checks pass.
6. Record removed part serial numbers and disposition (returned to vendor, retained for destruction).

#### 15.3.3 Completion criteria (evidence)
- Before/after photos where permitted or console screenshots/log extracts.
- Updated CI maintenance history and vendor case/RMA number attached.
- Incident resolution notes including validation steps.

### 15.4 Procedure: Removable media handling (backup tapes, portable drives, data-bearing parts)
#### 15.4.1 Policy requirements
- Removable media and data-bearing components are controlled assets with chain-of-custody.
- Media must be encrypted where supported by the process and tooling.
- Storage and transport must prevent unauthorized access, damage, or loss.

#### 15.4.2 Steps
1. Create or reference an ITSM ticket for the media action (creation, transport, removal, destruction, vendor return).
2. Identify media uniquely (barcode/serial) and classify by sensitivity.
3. Log chain-of-custody entry:
   - date/time,
   - handler name,
   - purpose,
   - origin and destination,
   - seal number (if tamper-evident bag used).
4. Store media in approved secure storage (locked cabinet/vault) when not in transit.
5. For vendor returns of data-bearing parts:
   - retain the part when contractually allowed (“retain disk” option),
   - if return is mandatory, ensure encryption and documented approval by Service Owner and CISO delegate process.
6. For destruction:
   - use approved destruction method (shred/degauss/incinerate per media type and vendor guidance),
   - capture destruction certificate or internal destruction witness record.
7. Update media inventory and close ticket with evidence attachments.

#### 15.4.3 Completion criteria (evidence)
- Chain-of-custody log (Appendix E).
- Storage log entry or vault access record.
- Destruction certificate or witnessed destruction record.
- Ticket references linking incident/change/work order to media handling record.

## 16. Data Retention, Logs, and Evidence Management
### 16.1 Evidence retention principles
Evidence must be time-bound, attributable, and repeatable, and include approvals, logs, and validation artifacts where applicable.

### 16.2 Required records
| Record type | Minimum content | Minimum retention approach |
|---|---|---|
| Access requests and approvals | request, justification, approvers, duration, areas | Retained per ISMS and audit needs in ITSM/document repository |
| Visitor logs | identity verification, host/escort, times, purpose | Stored securely with access restriction |
| Access reviews | access export, reviewer sign-off, remediation list | Stored with review period clearly indicated |
| Change/MOP packages | approval, risk, steps, validation/backout, evidence | Attached to Change record |
| Environmental incident records | alerts, timeline, actions, outcomes | Incident ticket with attachments |
| Media chain-of-custody | serial/barcode, handlers, dates, disposition | Controlled repository or ITSM attachments |

## 17. Training and Competency
- Personnel performing data center work must be trained on:
  - physical access and visitor handling,
  - ESD and safe equipment handling,
  - change enablement and MOP execution standards,
  - media handling and chain-of-custody.
- Regional IT Operations maintains training completion records; Internal Audit may validate training evidence as part of assurance activities.

## 18. Exceptions and Risk Acceptance
- Exceptions to this policy require documented risk assessment, compensating controls, and approval in line with Norfolk Industries governance.
- High-risk exceptions require involvement of the CISO and accountability by the Head of IT Infrastructure Services.
- All exceptions must have:
  - defined scope and duration,
  - compensating controls,
  - review date and closure criteria,
  - stored evidence of approval and periodic re-validation.

## 19. Document Control and Review
- Owner: Head of IT Infrastructure Services  
- Governance: IT Governance Manager coordinates reviews and audit readiness.
- Review cadence: at least annually and upon material changes to data center footprint, access control systems, or monitoring capabilities.
- Changes to this document follow Change Enablement with appropriate approvals and version control in the approved document repository.

## Appendices

### Appendix A: Data Center Access Request Form (Template)
| Field | Required input |
|---|---|
| Requestor name | Full name |
| Requestor role | Norfolk Industries role (or contractor/vendor designation) |
| Requestor organization | Norfolk Industries / vendor company |
| Manager/Engagement owner | Name and contact |
| Site(s) and areas requested | Building, data center room, cage/row/rack zones |
| Access type | Permanent / Time-bound / Emergency |
| Start date/time | Timestamp |
| End date/time (if time-bound) | Timestamp |
| Business justification | Clear rationale tied to service/support |
| Work reference | ITSM ticket/Change record number |
| Escort required | Yes/No (Yes mandatory for visitors) |
| Safety/training confirmation | Completed / Not completed |
| Approvals | Manager approval; IT Operations Manager approval for site; CISO consult if high risk |
| Access review category | Quarterly permanent review / Monthly temporary review |
| Deprovision confirmation (closure) | Date/time removed; remover name; evidence link |

### Appendix B: Method of Procedure (MOP) Template (Data Center Work)
#### B.1 MOP header
| Field | Content |
|---|---|
| MOP title | Clear action statement |
| Site / room / rack | Location details |
| Related ITSM ticket | Incident/Request number |
| Related Change record | Normal/Emergency Change identifier |
| Service Owner | Name |
| Platform Owner | Name |
| Executors | Names/roles (including vendor names if applicable) |
| Start/End window | Approved maintenance window |
| Risk level | Low/Medium/High with brief rationale |

#### B.2 Preconditions checklist
- Access approved and scheduled; visitor escort arranged if needed.
- Tools/parts available; ESD controls ready.
- Backups/config exports completed if applicable.
- Monitoring and alerting prepared (suppression plan if needed, with approval).
- Communication plan sent to stakeholders.

#### B.3 Step-by-step procedure table
| Step # | Action | Expected result | Validation evidence |
|---:|---|---|---|
| 1 | Identify target CI and location | Correct device confirmed | CI/serial match recorded |
| 2 | Execute change step | Step completes safely | Notes, screenshots, photos (if allowed) |
| 3 | Validate service/platform | Health checks pass | Monitoring green, test results attached |

#### B.4 Backout plan
| Trigger | Backout action | Validation |
|---|---|---|
| Service degradation | Restore prior cabling/config/hardware | Health checks return to baseline |
| Hardware instability | Reinstall previous component or failover | Vendor diagnostics normal |

#### B.5 Completion and approvals
- Completion time recorded
- Evidence attached to Change record
- Service Owner confirms service validation (if service-affecting)

### Appendix C: Visitor Handling Checklist (Operational)
| Check | Requirement | Performed by | Evidence |
|---|---|---|---|
| Pre-registration | ITSM ticket exists and approved | Escort/host | Ticket reference |
| ID verification | Government ID checked | Security/host | Visitor log entry |
| Badge issued | Visitor badge worn visibly | Security/host | Badge number recorded |
| Escorting | Escort present at all times | Escort | Worklog notes |
| Area limitation | Visitor stays in approved areas only | Escort | Worklog notes |
| Exit sign-out | Badge returned, sign-out time recorded | Security/host | Visitor log |

### Appendix D: Daily Data Center Operational Check (Checklist)
| Area | Check | Pass/Fail | Notes/Evidence link |
|---|---|---|---|
| Environmental | No critical temperature/humidity alarms |  |  |
| Environmental | Water leak sensors normal |  |  |
| Power | UPS/PDU/generator alarms normal (where applicable) |  |  |
| Cooling | CRAC/CRAH alarms normal (where applicable) |  |  |
| Security | No forced/open door alarms unresolved |  |  |
| Monitoring | Monitoring platform receiving telemetry |  |  |
| Work control | Active changes/vendors tracked and escorted |  |  |
| Housekeeping | Aisles clear; no unsafe storage |  |  |

Completion requirements:
- Checklist dated and attributed to the operator.
- Stored with the day’s operations record (ITSM worklog or approved repository).

### Appendix E: Media Chain-of-Custody Log (Template)
| Date/time | Media ID (barcode/serial) | Media type | Action (issue/transfer/store/destroy/return) | From (name/location) | To (name/location) | Handler signature/name | Seal # (if used) | Ticket/Change ref | Notes |
|---|---|---|---|---|---|---|---|---|---|

### Appendix F: Evidence Pack Guide (Audit-Ready)
This evidence pack defines what Norfolk Industries retains to demonstrate compliance with this policy and to support ISMS, SOC 2, and SOX controls.

#### F.1 Evidence pack contents (minimum)
| Control topic | Evidence artifact | Source system | Quality criteria |
|---|---|---|---|
| Physical access authorization | Approved access requests, approver identity, duration | ITSM + access control exports | Time-bound, attributable |
| Visitor handling | Visitor logs, escort assignment, visit tickets | Visitor log system/records + ITSM | Complete sign-in/out |
| Access reviews | Quarterly and monthly review packages | Access control exports + review sign-off | Includes remediation evidence |
| Change control | Change record, CAB approval where required, MOP, validation | ITSM | Repeatable and complete |
| Environmental monitoring | Alert logs, incident tickets, trend reports (monthly) | Monitoring tools + ITSM | Shows detection and response |
| Hardware break-fix | Vendor case/RMA, part serials, validation steps | ITSM + vendor portal artifacts | Traceable to CI |
| Media handling | Chain-of-custody logs, destruction certificates | Controlled repository/ITSM | Clear disposition trail |
| CI accuracy | CI updates for installs/MAC | CMDB | Location and ownership current |

#### F.2 Evidence handling rules
- Evidence must be stored in approved repositories with access limited to need-to-know.
- Evidence links must be referenced in the corresponding ITSM record (incident/change/request).
- Any missing evidence requires a corrective action ticket and documented remediation timeline.