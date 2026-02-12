# Physical Infrastructure & Data Center Security Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory physical security requirements for Norfolk Industries facilities hosting Information Technology (IT) and Operational Technology (OT) infrastructure, including on-prem data centers, server rooms, network rooms, communications closets, and controlled plant network spaces. The objective is to prevent unauthorized physical access, tampering, theft, or disruption of services and to ensure evidence-ready compliance under the Information Security Management System (ISMS).

## 2. Scope
### 2.1 In Scope
- Norfolk Industries-owned or leased facilities where IT Infrastructure Services platforms operate (data centers, server rooms, network rooms, backup media rooms).
- OT/IT integration locations where plant networks connect to corporate services, including SCADA/MES interface rooms and remote access termination points.
- Physical security controls supporting hybrid operations where on-prem systems integrate with Microsoft Azure and AWS.
- Personnel: employees, contractors, vendors, and visitors requiring access to controlled areas.

### 2.2 Out of Scope
- Purely cloud provider physical security (Microsoft Azure and AWS data center physical controls), which is managed under supplier assurance and shared responsibility; Norfolk Industries must retain supplier evidence where applicable.
- Non-infrastructure general office access controls except where they impact secured IT/OT spaces.

## 3. Policy Statement
Norfolk Industries shall implement layered physical security controls commensurate with risk, ensuring that:
- Access to sensitive IT/OT infrastructure is restricted to authorized individuals with documented business need.
- All access is logged, reviewed, and retained as evidence in alignment with the ISMS.
- Visitors are positively identified, escorted, and recorded; no unescorted visitor access is permitted to controlled zones.
- Physical incidents (for example tailgating, forced entry, tampering, lost badges) are managed through ITIL-aligned Incident Management with Information Security escalation and documented corrective actions.
- Media containing Norfolk Industries data is protected throughout its lifecycle using secure storage, controlled transport, chain of custody, and secure destruction.

## 4. Definitions (Glossary)
| Term | Definition |
|---|---|
| IT Infrastructure Services | The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations. |
| Global IT Operations | Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure. |
| Regional IT Operations | Regional teams executing day-to-day operations, local support, and implementation aligned to global governance. |
| Information Security Management System (ISMS) | The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001. |
| Change Advisory Board (CAB) | The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management. |
| Configuration Item (CI) | Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references. |

## 5. Roles and Responsibilities
### 5.1 Policy Governance Responsibilities
| Role | Responsibilities (Policy Context) |
|---|---|
| CIO | Executive oversight of IT governance; informed on material physical security risks impacting services. |
| Head of IT Infrastructure Services | Accountable for implementing and operating physical security controls for IT Infrastructure Services areas. |
| CISO | Provides ISMS oversight; ensures physical security controls meet information security requirements and risk posture. |
| IT Governance Manager | Maintains policy lifecycle, compliance tracking, audit evidence coordination, and exception tracking for this policy. |
| Service Owner | Ensures service-specific physical security requirements and evidence are met (including RTO/RPO dependencies where applicable). |
| Platform Owner | Defines engineering standards for physical placement, rack security, and environmental expectations for the platform domain. |
| IT Operations Manager | Operational execution of access processes, incident coordination, and 24×7 response for physical security events affecting services. |
| ITSM Process Owner | Ensures Incident Management, Change Enablement, and Service Configuration Management workflows support this policy. |
| Internal Audit | Independently evaluates design and operating effectiveness; validates evidence quality and retention. |
| Data Protection Officer (DPO) | Ensures privacy considerations (for example CCTV and visitor logs) align with GDPR and local privacy requirements. |

## 6. Physical Security Zones and Control Requirements
Norfolk Industries shall implement physical zones to provide defense in depth. Zones must be documented per facility and reviewed at least annually by Regional IT Operations with oversight from Global IT Operations.

### 6.1 Zone Model
| Zone | Description | Examples | Minimum Controls |
|---|---|---|---|
| Zone 0 – Public | Areas open to the public | Lobby, reception | Clear signage; no infrastructure assets accessible; visitor routing controls. |
| Zone 1 – General Business | Controlled employee areas | Office floors, non-sensitive meeting rooms | Badge access as applicable; security awareness signage for restricted areas. |
| Zone 2 – Controlled IT/OT Support | Operational areas that support IT/OT but do not house core compute | NOC space, staging rooms, telecom closets with limited gear | Badge access restricted to authorized roles; access logs; locked cabinets where feasible. |
| Zone 3 – Restricted Infrastructure | Areas housing critical infrastructure | Server rooms, network rooms, backup media rooms, OT/IT integration rooms | Badge access with least privilege; CCTV coverage; visitor escort; mantrap or 2-factor physical control where risk warrants; door forced/held-open alarms. |
| Zone 4 – High Security (if designated) | Highest sensitivity, high impact | Primary data center floor, core network distribution, privileged access terminals | Two-person rule or dual authorization where required; enhanced CCTV; strict no-visitor default unless pre-approved; continuous monitoring and alarm response. |

### 6.2 Boundary and Entry Controls
- All entrances to Zone 3 and above must use electronic access control (badge system) with unique identity assignment.
- Mechanical keys (if unavoidable) must be controlled using a key management process with sign-out logs and periodic inventory; keys to Zone 3+ are treated as security-sensitive assets.
- Doors to Zone 3+ must remain closed and must not be propped open. Door-held-open events must generate alerts where supported.

### 6.3 Rack, Cabinet, and Asset-Level Physical Controls
- Racks and cabinets hosting critical network, identity, or security tooling must be locked where practicable.
- Only authorized personnel may install, move, or remove infrastructure equipment; all moves/adds/changes that impact production services must follow Change Enablement and, where applicable, CAB approval.
- All infrastructure assets must be recorded as Configuration Items (CIs) in the ITSM tool, including location (facility, room, rack).

## 7. Access Control (Badge Access) Requirements
### 7.1 Access Provisioning
Access to Zone 2 and higher must be provisioned through a documented request in the ITSM tool and must include:
- Requestor identity and sponsor (manager or Service Owner).
- Business justification and required zones.
- Role-based alignment (least privilege).
- Start date and end date (mandatory for contractors and vendors).
- Acknowledgement of relevant security and safety requirements.

Approval requirements:
- Zone 2: Manager approval and IT Operations Manager or delegated approver.
- Zone 3 and above: Manager approval plus Service Owner (or Platform Owner for platform-managed rooms) and Information Security review for high-risk access.
- Zone 4 (if designated): Explicit approval by Head of IT Infrastructure Services and CISO delegate.

### 7.2 Access Changes and Revocation
- Access must be removed immediately upon termination, contract end, role change removing need, or security incident.
- HR-triggered offboarding and identity lifecycle events must include physical access revocation as a control requirement coordinated by Regional IT Operations.

### 7.3 Prohibited Practices
- Badge sharing is prohibited.
- “Piggybacking” and tailgating are prohibited; individuals must badge in individually.

## 8. Monitoring, CCTV, and Logging
### 8.1 CCTV Coverage
- Zone 3 and above must have CCTV coverage at entry/exit points and, where risk warrants, within the room (for example coverage of rack aisles).
- Camera placement must consider privacy (avoid sensitive personal areas) and must follow regional legal requirements, with DPO oversight for GDPR considerations in Europe.

### 8.2 CCTV Retention (Concept)
- CCTV recordings for Zone 3+ should be retained for a period sufficient to support investigations, audits, and incident response, and must align with legal/regulatory and privacy requirements by region.
- Retention configuration must be documented per facility and treated as an evidence artifact under the ISMS (including who can access recordings and under what conditions).

### 8.3 Access Logs and Alerting
- Electronic access control logs for Zone 2+ must be retained and protected from tampering.
- Security-relevant events should be monitored (for example repeated denied access, door forced open, door held open).
- Access log review must support quarterly access reviews and incident investigations.

## 9. Visitor Management
### 9.1 Visitor Identification and Registration
- All visitors must be registered, present valid identification where legally permissible, and be issued a visitor badge that clearly distinguishes them from employees.
- Visitor access to Zone 3 and above requires pre-approval by the area owner (Service Owner, Platform Owner, or IT Operations Manager as applicable) and must be time-bound.

### 9.2 Escort Requirements
- Visitors must be escorted at all times in Zone 2+ and may not be left unattended in Zone 3+.
- Escort is responsible for visitor behavior, ensuring no photography/recording unless explicitly authorized, and ensuring visitor exit is recorded.

### 9.3 Visitor Log Requirements
Visitor logs must record:
- Visitor name and organization
- Host/escort name
- Date/time in and out
- Areas visited (zone/room)
- Purpose of visit
- Badge number (if applicable)

Visitor logs are controlled records and must be stored securely with access limited to authorized personnel.

## 10. Media Storage, Transport, and Secure Destruction
### 10.1 Media Types
This section applies to all media that may contain Norfolk Industries data, including:
- Backup tapes, removable drives, external disks, and other portable storage
- Decommissioned disks/SSDs from servers, storage arrays, and endpoints
- Printed sensitive documents stored within infrastructure spaces

### 10.2 Secure Storage Requirements
- Media must be stored in a designated locked container or room within Zone 3 (or higher) with access restricted to authorized personnel.
- Inventory must be maintained for backup media and decommissioned storage awaiting destruction, including unique identifiers and location.

### 10.3 Chain of Custody
- Media movement (internal or to a destruction provider) must maintain chain of custody, including:
  - Unique media ID
  - From/to locations
  - Date/time transfer
  - Releasing and receiving individuals (names and signatures or equivalent authenticated electronic record)
- Chain of custody records are evidence artifacts and must be retained per records retention rules supporting the ISMS and audit requirements.

### 10.4 Secure Destruction
- Media must be securely destroyed using approved methods based on sensitivity and media type (for example shredding, degaussing where applicable, or physical destruction for drives).
- Destruction must be witnessed or verified using a certificate of destruction from an approved supplier.
- For highly sensitive environments (including OT/IT integration and identity/security systems), physical destruction of drives is the default unless a documented, validated sanitization method is approved by Information Security.

## 11. Environmental and Life Safety Controls (Data Center and Server Rooms)
- Critical rooms (Zone 3+) must have appropriate environmental controls (temperature, humidity) and monitoring aligned to service needs.
- Fire detection and suppression must be present according to facility standards and local codes; suppression methods must be appropriate for IT equipment.
- Water leak detection and protection should be implemented where risk warrants.
- Emergency power (UPS/generator) requirements are defined by the Service Owner and Platform Owner based on service criticality and must be reflected in service continuity planning.

## 12. Incident Handling (Physical Security Events)
Physical security events must be managed through the ITSM tool under ITIL-aligned Incident Management with Information Security involvement when security impact is suspected.

### 12.1 Tailgating / Piggybacking Response Procedure
1. **Challenge**: Politely challenge the individual and request they badge in; if uncertain, contact security or the Service Desk.
2. **Contain**: Do not allow the individual to proceed into Zone 3+ without verification and escort.
3. **Report**: Log an incident in the ITSM tool including time, location, and description.
4. **Investigate**: Regional IT Operations coordinates with physical security and Security Engineer support as needed to review access logs and CCTV.
5. **Corrective Action**: Implement coaching, access changes, or disciplinary escalation per HR process; update controls if a gap is identified.

### 12.2 Lost or Stolen Badge Response Procedure
1. **Immediate Notification**: Report to the Service Desk and facility security immediately upon discovery.
2. **Disable Access**: Regional IT Operations disables badge access without delay; if identity compromise is suspected, escalate to Information Security.
3. **Issue Replacement**: Replacement badge issued only after identity verification and approval per access provisioning rules.
4. **Investigation**: Review recent access logs for anomalous activity and document findings in the incident record.
5. **Closeout**: Confirm revocation completed and update the access roster; record evidence of disablement and replacement issuance.

### 12.3 Evidence Handling for Physical Incidents
- Access logs, CCTV clips, visitor logs, and chain of custody documents must be preserved as evidence.
- Evidence must be time-bound, attributable, and repeatable per Norfolk Industries evidence principles, and stored with restricted access.

## 13. Access Reviews and Compliance Verification
### 13.1 Quarterly Access Review
- Quarterly access reviews are mandatory for Zone 3 and above and must confirm:
  - Active badge access list matches current job responsibilities and business need
  - Contractor/vendor access is still valid and time-bound
  - Departed/transferred personnel access has been removed
  - Any exceptions are documented and approved

### 13.2 Review Ownership and Attestation
- Regional IT Operations prepares the access list and supporting logs.
- Service Owner (or Platform Owner where applicable) attests to appropriateness of access.
- IT Governance Manager tracks completion and retains evidence for audit readiness.

## 14. Exceptions
- Exceptions require documented risk acceptance and compensating controls.
- High-risk exceptions (for example, unlogged access, inability to enforce escorting, or inadequate secure storage for media) require approval per the governance model and may require CISO involvement.
- Exceptions must include an expiry date and a review schedule.

## 15. Training and Awareness
- Personnel with Zone 3+ access must complete security awareness and physical security briefing upon initial provisioning and at least annually.
- Visitor escort responsibilities must be communicated to all authorized escorts (including expectations for supervision and incident reporting).

## 16. Records Retention and Evidence Requirements
Records must be retained in accordance with Norfolk Industries records management expectations, legal/regulatory requirements, and the ISMS evidence principles. Minimum record categories include:
- Badge access provisioning and revocation tickets
- Quarterly access review artifacts and attestations
- Visitor logs
- Access control logs and relevant alerts
- CCTV retention configuration documentation and access records to CCTV exports
- Media inventories, chain of custody logs, certificates of destruction
- Incident records for physical security events and outcomes

## 17. Compliance Mapping (Controls-to-Standards)
### 17.1 Control Mapping Table
| Policy Control Area | ISO/IEC 27001 (Annex A concept) | NIST CSF Function | SOC 2 TSC | COBIT 2019 Domain | ITIL 4 Practice | Typical Evidence |
|---|---|---|---|---|---|---|
| Physical zones and restricted areas | Physical and environmental security | Protect | Security, Availability | APO, DSS | Information Security Management | Zone diagrams, access control configurations, room inventories |
| Badge access provisioning and least privilege | Access control; physical access management | Protect | Security | APO, DSS | Change Enablement; Information Security Management | ITSM requests/approvals, access group lists, badge issuance logs |
| CCTV and monitoring | Physical security monitoring | Detect | Security, Availability | DSS, MEA | Monitoring and Event Management | Camera coverage list, retention settings, footage access logs |
| Visitor management and escorting | Physical entry controls | Protect | Security | DSS | Information Security Management | Visitor logs, escort acknowledgements, facility procedures |
| Media storage, chain of custody, destruction | Media handling; secure disposal | Protect | Confidentiality, Security | DSS | Service Configuration Management | Media inventory, chain of custody forms, certificates of destruction |
| Incident handling for physical events | Incident response and management | Respond | Security, Availability | DSS | Incident Management | Incident tickets, investigation notes, access/CCTV extracts |
| Quarterly access reviews | Access review and monitoring | Identify / Protect | Security | MEA | Information Security Management | Review checklist, signed attestation, remediation tickets |

### 17.2 Evidence Principles (Mandatory)
| Principle | Application |
|---|---|
| Evidence must be time-bound, attributable, and repeatable. | All access reviews, incident records, and approvals must show dates, approver identity, and reproducible logs. |
| Evidence must include approvals, logs, and validation artifacts where applicable. | Maintain ITSM tickets, access logs, CCTV export logs, chain of custody, and verification outcomes. |

## 18. Related Documents and References
- Information Security Management System (ISMS) policy framework and control library
- ITIL-aligned ITSM processes: Change Enablement, Incident Management, Service Configuration Management
- Supplier Management process for third-party data center or destruction services
- Business continuity and disaster recovery documentation aligned to ISO/IEC 22301
- Applicable privacy notices and CCTV signage standards overseen by the Data Protection Officer (DPO)

## 19. Version Control and Ownership
### 19.1 Document Ownership
| Item | Value |
|---|---|
| Policy Owner | IT Governance Manager |
| Accountable Executive | Head of IT Infrastructure Services |
| Security Oversight | CISO |
| Applicability | All Norfolk Industries regions and facilities hosting IT/OT infrastructure |
| Review Cadence | At least annually and upon material facility/security changes |

### 19.2 Change Control
Updates to this policy follow Change Enablement governance. Material changes affecting controls or audit posture should be reviewed with the Change Advisory Board (CAB) and Information Security Management System (ISMS) stakeholders.

---

## Appendix A: Visitor Log Template (Controlled Areas)
### A.1 Instructions
- Complete one entry per visitor per day.
- Store completed logs in a secured repository with restricted access.
- Ensure sign-in and sign-out times are captured.

### A.2 Visitor Log (Template)
| Date | Site/Facility | Visitor Full Name | Visitor Organization | Government ID Verified (Y/N where legally permissible) | Visitor Badge # | Host/Escort Name | Purpose of Visit | Zones/Rooms Visited | Time In | Time Out | Notes/Incidents |
|---|---|---|---|---|---|---|---|---|---|---|---|

---

## Appendix B: Quarterly Access Review Checklist (Zone 3+)
### B.1 Access Review Checklist
| Check | Description | Evidence Artifact | Pass/Fail | Notes/Remediation Ticket |
|---|---|---|---|---|
| Access roster extraction | Export current badge access list for Zone 3+ areas | Access control system export; date/time stamp |  |  |
| Role and business need validation | Validate each person’s need-to-access (least privilege) | Attestation by Service Owner or Platform Owner |  |  |
| Contractor/vendor validity | Confirm end dates, sponsor, and active engagement | ITSM requests; contract end dates |  |  |
| Offboarding verification | Confirm terminated/transferred personnel removed | HR offboarding list (where permitted) + access removal logs |  |  |
| Access anomalies | Review denied access spikes, after-hours patterns, door alarms | Access logs; alert reports |  |  |
| Visitor log sampling | Sample visitor logs for completeness and escort compliance | Visitor logs; escort list |  |  |
| Media room access validation (if applicable) | Validate access to media storage/destruction staging | Access list + media inventory access records |  |  |
| Remediation completion | Verify prior quarter findings closed | Tickets; closure evidence |  |  |
| Record retention confirmation | Confirm evidence stored securely and retrievable | Repository path/access controls; index |  |  |

### B.2 Attestation Statement
| Item | Entry |
|---|---|
| Facility / Rooms Reviewed |  |
| Review Period (Quarter) |  |
| Reviewer (Regional IT Operations) |  |
| Attestor (Service Owner / Platform Owner) |  |
| Attestation | “I confirm that access to the listed Zone 3+ areas is authorized based on current business need, and that remediation actions have been initiated for any exceptions identified.” |
| Date |  |

---

## Appendix C: Evidence List (Audit-Ready)
### C.1 Evidence Inventory
| Control Area | Evidence Item | Source System/Location | Owner Role | Frequency | Retention Concept |
|---|---|---|---|---|---|
| Zone definitions | Facility zone map and controlled area list | Facility security repository / ITSM knowledge | IT Operations Manager | Annual / change-driven | Retain current + prior versions for audit traceability |
| Access provisioning | Approved access requests with justification | ITSM tool | Regional IT Operations | Per request | Retain per ISMS evidence and audit needs |
| Access revocation | Offboarding/role-change revocation records | ITSM tool + access control logs | Regional IT Operations | Per event | Retain per ISMS evidence and audit needs |
| Quarterly access reviews | Completed checklist and attestation | ITSM tool / governance repository | IT Governance Manager | Quarterly | Retain per ISMS evidence and audit needs |
| Access control logs | Entry/exit logs for Zone 2+ | Access control system | IT Operations Manager | Continuous | Retain aligned to investigation and audit requirements |
| CCTV configuration | Retention settings and camera coverage register | CCTV/security system config export | IT Operations Manager | Annual / change-driven | Retain current + prior settings evidence |
| CCTV access | Log of CCTV exports/access for investigations | CCTV/security system audit log | IT Operations Manager | Per incident | Retain per ISMS evidence and legal requirements |
| Visitor management | Completed visitor logs and approvals | Facility log repository | Service Desk Manager (where used) / IT Operations Manager | Daily | Retain aligned to privacy and audit requirements |
| Media inventory | Inventory of stored media and decommissioned drives | ITSM / asset repository | Service Owner | Ongoing | Retain per ISMS evidence and audit needs |
| Chain of custody | Transfer logs for media movements | Controlled log repository | IT Operations Manager | Per transfer | Retain per ISMS evidence and audit needs |
| Destruction proof | Certificates of destruction / witness records | Supplier portal / repository | IT Governance Manager | Per batch | Retain per ISMS evidence and SOX/SOC 2 needs |
| Physical incidents | Incident tickets with investigation artifacts | ITSM tool | IT Operations Manager | Per incident | Retain per ISMS evidence and legal requirements |

---