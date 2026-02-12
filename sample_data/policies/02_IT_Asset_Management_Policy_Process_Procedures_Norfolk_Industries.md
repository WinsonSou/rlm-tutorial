# IT Asset Management Policy, Process & Procedures (Norfolk Industries)

## 1. Purpose
Norfolk Industries establishes this IT Asset Management Policy, Process & Procedures document to ensure that Information Technology (IT) and Operational Technology (OT) assets are managed consistently and securely across their full lifecycle: **request → procure → receive → tag → inventory → deploy → maintain → transfer → retire → dispose**.

This document supports:
- Protection of Norfolk Industries information and services through accurate control and accountability of assets.
- Reliable operations for **24×7** manufacturing and services environments.
- Financial stewardship (including capitalization, depreciation, and SOX-aligned traceability).
- Security and compliance alignment with the **Information Security Management System (ISMS)**, privacy obligations, and audit requirements.

## 2. Scope
### 2.1 In Scope
This document applies to all Norfolk Industries regions (North America, Europe, APAC) and covers the asset lifecycle for:

- **Hardware assets**
  - End-user computing (laptops, desktops, tablets, mobile devices)
  - Servers and compute (on-prem and cloud-managed appliances where applicable)
  - Network devices (switches, routers, firewalls, wireless controllers, access points)
  - Data center infrastructure components that are Configuration Items (CIs) (e.g., storage arrays where managed as CIs)
  - Peripherals (docks, monitors, specialty devices where tracked)
- **Software assets**
  - Commercial off-the-shelf software (COTS)
  - SaaS subscriptions
  - On-prem and cloud-hosted applications where managed by IT Infrastructure Services
  - Security tooling and agents
- **Cloud resources**
  - Azure subscriptions and resources (primary cloud)
  - AWS accounts and resources (secondary cloud)
  - Identity and access objects used to deliver services (e.g., managed identities/service principals where tracked as CIs)
- **Operational Technology (OT) assets** (where applicable and approved)
  - SCADA components, MES-connected endpoints, OT network devices, and plant network assets that interface with IT governance and remote access controls

### 2.2 Out of Scope (unless explicitly brought into scope by a Service Owner)
- Personal devices not enrolled or authorized under Norfolk Industries policy.
- Assets managed entirely by third parties without Norfolk Industries operational control (however, contract and assurance evidence remain required via Supplier Management practices).
- Consumables with no tracking requirements (e.g., standard cables) unless regionally mandated.

### 2.3 Applicability and Precedence
- This policy applies to **IT Infrastructure Services**, **Global IT Operations**, and **Regional IT Operations**.
- Where OT requirements differ, OT security and plant governance may impose stricter controls; stricter control prevails.
- In the event of conflict, Norfolk Industries ISMS-aligned security policies and approved standards take precedence.

## 3. Definitions and Canonical Terminology
The following terms are used as defined in the Norfolk Industries glossary:

- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.  
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.  
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.  
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.  
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.  
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.  
- **Operational Technology (OT)**: Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks.  
- **Service Level Objective (SLO)**, **Recovery Point Objective (RPO)**, **Recovery Time Objective (RTO)**: Used where asset management interacts with service continuity, backup, and disaster recovery.

Additional terms used in this document:
- **Asset**: A financial or operational resource owned, leased, or otherwise controlled by Norfolk Industries, including IT and OT assets.
- **Asset record**: The authoritative entry representing an asset or CI in the CMDB or other authoritative inventory source.
- **Chain of custody**: Documented control and accountability for an asset as it moves between people, locations, and statuses.
- **True-up**: A periodic process to reconcile software licenses/subscriptions with actual usage and installations.
- **Shadow IT**: IT resources procured, deployed, or used without governance, visibility, or approval through Norfolk Industries processes.
- **Stockroom**: Controlled storage location for assets pending deployment, repair, redeployment, or disposal.

## 4. Policy Statement
Norfolk Industries will maintain complete and accurate control of IT and in-scope OT assets across their lifecycle to protect confidentiality, integrity, and availability; manage cost and risk; and ensure compliance with regulatory and contractual requirements.

Norfolk Industries will:
1. Maintain an authoritative inventory of assets and CIs, including ownership, location, lifecycle status, and security classification.
2. Ensure procurement, deployment, and changes to assets follow ITIL-aligned governance and the Change Advisory Board (CAB) where applicable.
3. Implement controls to prevent, detect, and remediate shadow IT.
4. Maintain software license compliance, including entitlement records, deployment evidence, and periodic true-up.
5. Ensure secure retirement and disposal processes, including data sanitization, disposal certification, and audit trails.
6. Define clear roles and accountability for asset management activities across Global IT Operations and Regional IT Operations.

Non-compliance may result in access restrictions, removal of unauthorized assets, escalation to management, and formal disciplinary processes consistent with Norfolk Industries governance.

## 5. Governance, Roles, and RACI
### 5.1 Governance Model
Norfolk Industries operates under centralized governance with regional execution:
- **Global IT Operations** defines global policy, minimum standards, tooling strategy, and reporting.
- **Regional IT Operations** executes asset lifecycle processes, maintains local stockrooms, and ensures timely updates in authoritative inventories.
- The **Information Security Management System (ISMS)** provides oversight to ensure asset management reduces security risk.
- The **Change Advisory Board (CAB)** governs asset-impacting changes that affect production services, security posture, or availability.

### 5.2 Roles and Responsibilities (consistent with roles.json)
- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes.
- **CISO**: Accountable for information security program and ISMS oversight.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for a defined infrastructure service.
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain (e.g., network, cloud, endpoint).
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- **ITSM Process Owner**: Owns ITIL-aligned process design (Change/Incident/Problem/CMDB) and continual improvement.
- **Internal Audit**: Independently assesses control design and operating effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment.

### 5.3 RACI for Asset Management (aligned to raci_master.csv patterns)
The following table extends Norfolk Industries’ governance RACI to asset management activities.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Asset Management Policy approval | A | R | C | R | C | C | C | C | I |
| Asset Management Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership (asset lifecycle) | I | A | C | R | R | R | R | C | I |
| Authoritative inventory model (CMDB and tooling) | I | A | C | R | R | R | R | A | I |
| Quarterly asset reconciliation governance | I | R | C | A | R | R | R | C | I |
| License compliance and true-up governance | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Asset Management Principles
Norfolk Industries manages assets using the following principles:

1. **Single source of truth by asset type**: Each asset category must have an authoritative inventory source, with defined reconciliation to the CMDB.
2. **Lifecycle-driven status management**: Asset status must reflect real-world state transitions with time-bound updates.
3. **Least privilege and security by design**: Asset deployment must enforce identity, endpoint, and network security baselines.
4. **Traceability and chain of custody**: Transfers, loans, and disposals require documented approvals and evidence.
5. **Segregation of duties**: Procurement approval, receipt, and disposal evidence must be separable where feasible to support SOX-aligned controls.
6. **Operational resilience**: Asset records must support incident response, vulnerability response, and service continuity (RTO/RPO dependencies where applicable).
7. **OT safety and availability**: OT asset activities must not introduce unacceptable risk to plant safety, quality, or availability; remote access is strictly controlled.

## 7. Asset Classification and Ownership
### 7.1 Asset Ownership Requirements
Every managed asset must have:
- **Asset owner** (business accountability; typically aligned to Service Owner or designated business function)
- **Custodian** (operational accountability; typically Regional IT Operations for endpoints, Platform Owner domain teams for infrastructure)
- **Support group** aligned to IT Infrastructure Services operating model
- **Location** (region, site, building/room/rack or plant area where applicable)

Ownership requirements apply to IT and in-scope OT assets and must be recorded in the authoritative inventory source and/or CMDB CI record.

### 7.2 Asset Classification Approach
Asset classification must align to the sensitivity and criticality of information processed and the operational impact of the asset.

Minimum classification dimensions:
- **Data sensitivity** (e.g., Public, Internal, Confidential, Restricted) as required by Norfolk Industries ISMS practices
- **Service criticality** (e.g., Non-critical, Important, Critical, Mission-critical)
- **Regulatory relevance** (GDPR personal data handling, SOX relevance for financial systems)
- **OT impact category** (OT-only: Safety/Availability impact)

The **Asset Classification Matrix** is provided in Appendix A and must be used consistently.

## 8. Authoritative Inventory Sources and CMDB Model
### 8.1 Authoritative Inventory Sources
Norfolk Industries maintains authoritative sources by asset type:

| Asset Type | Authoritative Inventory Source | Purpose | Reconciliation Target |
|---|---|---|---|
| End-user devices (Windows/macOS/mobile) | Microsoft Intune (and ConfigMgr where needed) | Device compliance, configuration, deployment, and reporting | CMDB CI and Asset records |
| On-prem servers | ConfigMgr where needed and/or platform monitoring systems plus CMDB | Operational management and patching visibility | CMDB CI records |
| Cloud resources (Azure) | Azure Resource Graph / Azure Policy inventory exports and CMDB integration | Subscription/resource inventory, tagging compliance | CMDB CI records |
| Cloud resources (AWS) | AWS Config / inventory exports and CMDB integration | Account/resource inventory, tagging compliance | CMDB CI records |
| Identity (Entra ID (Azure AD) objects, critical accounts) | Entra ID | Identity objects, privileged access control | CMDB for select CIs where required |
| Network devices | Network management system inventory and CMDB | Network operational inventory | CMDB CI records |
| Software installations | Intune/ConfigMgr software inventory + EDR telemetry | Install footprint | Software Asset records and CMDB relationships |
| Vulnerability visibility | Vulnerability scanning (e.g., Tenable/Nessus) | Discovery validation | Reconciliation and exception detection |
| Security endpoint visibility | EDR (e.g., Microsoft Defender for Endpoint) | Active endpoint confirmation and risk | Reconciliation and exception detection |
| Procurement and financial records | Procurement system and finance fixed asset register | Entitlement and financial asset truth | CMDB/Asset mapping and audits |
| OT assets (in scope) | OT asset inventory system and plant network inventory exports | OT asset visibility | CMDB (approved subset) |

### 8.2 CMDB as the Enterprise Configuration Record
The CMDB is the enterprise system of record for:
- **Configuration Item (CI)** relationships and service mapping for critical services.
- Normalized asset attributes needed for operational risk management, change impact analysis, and audits.

Where a tooling source is authoritative for device state (e.g., Intune), the CMDB holds the normalized CI record and relationships to services, locations, and owners, and references the authoritative tool identifier.

### 8.3 Mandatory CMDB Fields
CMDB mandatory fields are defined in Appendix C and must be enforced through ITSM workflows.

## 9. Asset Lifecycle Process (End-to-End)
This section defines the standardized lifecycle process for Norfolk Industries assets. Each step includes minimum controls, required records, and audit evidence expectations.

### 9.1 Step 1 — Request
**Objective:** Ensure business justification, standardization, and approvals prior to procurement or provisioning.

**Process requirements:**
- All requests must be submitted via the ITSM service catalog.
- Requests must include:
  - Requestor identity (validated via Active Directory/Entra ID)
  - Business justification
  - Asset type and model (or “standard build” selection)
  - Cost center and location
  - Required date and criticality
  - For software: intended use, user count, and data classification
  - For cloud: subscription/account, workload owner, tagging plan, and expected spend

**Approval requirements:**
- Cost approval per delegated authority.
- Security review for non-standard software, elevated risk cloud services, and OT-connected assets.
- For production-impacting infrastructure assets, review by Platform Owner and Service Owner; CAB involvement when change enablement is required.

**Minimum evidence:**
- ITSM request record with approvals and timestamps.
- Security review record when triggered by request type.

### 9.2 Step 2 — Procure
**Objective:** Ensure compliant procurement with contract, security, and supplier requirements.

**Process requirements:**
- Procurement must be executed through approved procurement channels.
- Supplier selection must support Supplier Management requirements (security clauses, right-to-audit where required).
- Software and SaaS procurement must record:
  - SKU/part numbers
  - Entitlements, term, renewal date
  - Metrics (per user/per device/per core)
  - Data processing terms (GDPR relevance) and DPO involvement where personal data is processed

**Minimum evidence:**
- Purchase order and supplier invoice records.
- License entitlement documentation.
- Contract or order form for SaaS and cloud commitments.

### 9.3 Step 3 — Receive
**Objective:** Confirm asset receipt, validate integrity, and establish custody.

**Process requirements:**
- Receiving must occur at an approved Norfolk Industries site or designated secure receiving location.
- Verify:
  - Item matches procurement record
  - Serial number captured
  - No tampering or damage
- For high-risk assets (e.g., privileged network appliances), receiving must be performed by authorized personnel and logged.

**Minimum evidence:**
- Receiving log (ITSM task or stockroom system entry).
- Photo evidence for damaged shipments (where applicable).
- Serial number capture record.

### 9.4 Step 4 — Tag (Barcode/RFID)
**Objective:** Ensure assets are uniquely identifiable and trackable.

**Process requirements:**
- All in-scope physical assets must be tagged prior to deployment, unless physically infeasible (exceptions must be documented).
- Tagging standards:
  - Barcode required for all endpoints and standard IT assets.
  - RFID permitted where regionally approved and inventory tooling supports it.
- Tag must be associated to:
  - Serial number
  - Asset record number
  - Location and custodian
- Tags must be tamper-evident where feasible.

**Minimum evidence:**
- Asset record showing tag ID mapped to serial number.
- Stockroom tagging task completion record.

### 9.5 Step 5 — Inventory (Create/Update Asset and CI Records)
**Objective:** Create authoritative records and linkages needed for operations, security, and audit.

**Process requirements:**
- Create asset record in the CMDB/asset module (per ITSM design).
- Create CI record for assets that:
  - Support a service
  - Require change impact analysis
  - Must be included in monitoring, vulnerability scanning, or incident response
- For cloud resources:
  - Enforce tagging prior to production use (see Section 11.4).
  - Link resource groups/accounts/subscriptions to Service Owner and cost center.

**Minimum evidence:**
- CMDB asset record and CI record with mandatory fields completed.
- Integration logs (where automated imports exist).

### 9.6 Step 6 — Deploy
**Objective:** Deploy assets securely, consistently, and with measurable compliance.

**Process requirements by asset type:**
- **Endpoints**
  - Enroll in Intune (and ConfigMgr where needed)
  - Apply baseline security configuration and encryption
  - Install EDR and required monitoring agents
  - Validate device compliance prior to handover
- **Servers / Compute**
  - Build according to Platform Owner standards
  - Patch to current baseline
  - Register in monitoring and backup where required by service
  - Implement privileged access controls for admin accounts (PAM integration where applicable)
- **Network devices**
  - Configuration must follow approved templates
  - Device credentials and secrets handled via approved secure mechanisms
  - Logging to SIEM where required
- **Cloud resources**
  - Must have required tags, policies, and logging enabled
  - Network segmentation must be enforced
- **OT assets (in scope)**
  - Deployment must follow OT change windows and plant governance
  - Remote access must meet strict controls and approvals

**Minimum evidence:**
- Deployment task record with completion checklist.
- Intune compliance report for endpoints.
- Backup/monitoring enrollment evidence where required.
- CAB approval record when change enablement applies.

### 9.7 Step 7 — Maintain (Operate, Patch, Support, and Monitor)
**Objective:** Sustain asset security and availability throughout useful life.

**Process requirements:**
- Assets must remain:
  - Supported (vendor support status tracked)
  - Patched per vulnerability and patch management requirements
  - Monitored for availability and security events as required by criticality
- Maintenance activities include:
  - Warranty tracking and renewals
  - Repair workflows with chain-of-custody controls
  - Configuration changes governed through Change Advisory Board (CAB) for Normal and Emergency Changes as required

**Minimum evidence:**
- Patch/compliance reports.
- Vulnerability scan evidence and remediation tickets.
- Incident and change records referencing affected CIs.

### 9.8 Step 8 — Transfer (User/Location/Ownership Changes)
**Objective:** Maintain accountability and accurate records when assets move.

**Transfer scenarios:**
- User-to-user transfer
- Site-to-site transfer (regional or cross-region)
- Function-to-function transfer (e.g., IT to OT custody where approved)
- Loan issuance and return (short-term lending)

**Process requirements:**
- Transfers must be recorded via ITSM using the Asset Transfer Form (Appendix template).
- Update:
  - Custodian
  - Location
  - Asset status
  - Assigned user (if applicable)
- For cross-region transfers, ensure:
  - Export/import compliance is considered where applicable
  - Data privacy and device encryption requirements are verified

**Minimum evidence:**
- Approved transfer record with dates and signatures/approvals.
- Updated CMDB/asset record history.

### 9.9 Step 9 — Retire (End of Use)
**Objective:** Remove from service while preserving evidence, ensuring data protection, and managing license recovery.

**Retirement triggers:**
- End of life / end of support
- Replacement due to refresh cycles
- Irreparable damage
- Role change or termination (endpoints)
- Cloud resource decommissioning

**Process requirements:**
- Confirm asset is no longer required for service delivery.
- Ensure:
  - Data is backed up or migrated if needed
  - Monitoring and access are removed
  - Licenses are reclaimed or reallocated (software)
  - Network and identity access paths are revoked

**Minimum evidence:**
- Retirement record and updated lifecycle status.
- Backup/migration completion evidence (where applicable).

### 9.10 Step 10 — Dispose (Sanitize and Dispose Securely)
**Objective:** Ensure secure data sanitization and environmentally and legally compliant disposal.

**Process requirements:**
- Data sanitization must be performed using approved methods appropriate to media type and classification.
- Disposal must be executed via:
  - Approved e-waste vendor with certificate of destruction, or
  - Approved internal destruction process (where permitted)
- Record:
  - Sanitization method and date
  - Disposal certificate reference
  - Chain-of-custody evidence from stockroom to vendor pickup

**Minimum evidence:**
- Disposal Certificate (template in Appendix).
- Vendor certificate of destruction.
- CMDB/asset record set to “Disposed” with reference numbers.

## 10. Asset Types and Specific Controls
### 10.1 End-user Devices
Controls:
- Mandatory enrollment in Intune (and ConfigMgr where needed).
- Encryption required for portable devices.
- EDR required (e.g., Microsoft Defender for Endpoint).
- Asset tag required.
- Lost/stolen process required (see Section 14.6).

Records:
- Intune device ID
- Serial number, tag ID
- Assigned user and location
- Compliance state

### 10.2 Servers and Compute
Controls:
- CI record required for production and shared infrastructure.
- Backup enrollment based on service SLO and RPO/RTO requirements.
- Privileged access controlled using PAM (e.g., CyberArk) where applicable.
- Vulnerability scanning coverage required.

Records:
- Hostname, OS, owner, environment (prod/non-prod)
- Patch group and maintenance window
- Monitoring and backup references

### 10.3 Network Devices
Controls:
- CI record required.
- Standard configuration templates and secure management access.
- Centralized logging integration to SIEM where required.

Records:
- Model, serial, firmware
- Site and rack/closet location
- Management IP and support group (controlled access to details)

### 10.4 Software (On-prem, Client, and SaaS)
Controls:
- Entitlement must exist before deployment.
- Installations must be inventoried.
- Usage must be measurable when licensing depends on usage.
- Renewals tracked with notice periods and budget alignment.

Records:
- Software title, publisher, version
- License metric and entitlement count
- Renewal date and owner

### 10.5 Cloud Resources (Azure and AWS)
Controls:
- Subscription/account ownership assigned to Service Owner.
- Mandatory resource tagging and policy compliance.
- Logging enabled (activity logs, relevant service logs) and forwarded to SIEM where required.
- Inventory sync to CMDB for defined resource types.

Records:
- Subscription/account ID
- Resource IDs and tags
- Environment classification and cost center

### 10.6 Operational Technology (OT) Assets (In Scope)
Controls:
- Must respect plant segmentation and strict remote access controls.
- Asset visibility must not disrupt OT operations.
- Changes must align with OT change windows and risk controls.
- Only approved OT assets are represented in CMDB, with limited detail where necessary to reduce exposure.

Records:
- OT asset identifier
- Location (plant/line/area)
- Support group and plant owner/custodian
- Connectivity classification (IT-connected vs isolated)

## 11. Controls for Accuracy, Compliance, and Shadow IT
### 11.1 Inventory Accuracy Controls
Norfolk Industries enforces accuracy through:
- Mandatory record creation at receipt and deployment.
- Automated discovery and imports where feasible.
- Quarterly reconciliation (Section 14.2).
- Exception management (Section 15).

Accuracy targets (minimum expectations):
- Endpoints: near-real-time via Intune reporting; discrepancies resolved within reconciliation window.
- Servers/network: monthly review of CMDB vs monitoring/vulnerability scan inventories.
- Cloud: weekly tagging and inventory compliance reporting.

### 11.2 License Compliance and True-up
Norfolk Industries maintains license compliance through:
- Entitlement records maintained with procurement evidence.
- Installation/usage tracking via endpoint management, SaaS admin portals, and cloud billing data.
- True-up cadence:
  - **Quarterly** for high-spend or high-risk software/SaaS
  - **Semi-annual** for standard software portfolios
  - **On-demand** before renewals or audits

True-up process minimum steps:
1. Extract entitlements and renewal terms.
2. Extract deployment/usage data.
3. Reconcile variances and identify over/under usage.
4. Execute remediation: uninstall/reallocate, buy additional entitlements, or adjust subscription tiers.
5. Record outcomes and retain evidence.

### 11.3 Shadow IT Detection and Response
Shadow IT detection sources:
- Network discovery and firewall logs (where permitted and safe)
- EDR detections and application inventory
- Cloud expense anomalies and new account discovery
- Vulnerability scanning discovery of unmanaged hosts
- SIEM detections for unknown devices/services

Response requirements:
- Create an ITSM record with categorization “Shadow IT Investigation”.
- Identify owner/custodian and business use.
- Perform security risk review under ISMS.
- Execute one of the following outcomes:
  - Onboard into managed lifecycle (preferred)
  - Replace with approved service
  - Remove/decommission if unauthorized or high risk

Evidence:
- Detection alert/report
- Investigation record and outcome
- Asset onboarding or decommission record

### 11.4 Cloud Tagging and Policy Enforcement (Asset Traceability)
Minimum cloud tags (must be enforced via policy and reconciled):
- Service Owner
- Cost center
- Environment (prod/non-prod)
- Data classification
- Region
- Criticality tier

Non-compliant resources must be remediated within defined operational windows, with escalation to Service Owner and Head of IT Infrastructure Services for repeated non-compliance.

## 12. Security and Privacy Requirements
### 12.1 Security Requirements (ISMS-aligned)
- Asset inventory supports security controls including vulnerability response, incident response, and access governance.
- All assets must be attributable to an owner/custodian.
- Asset changes must comply with Change Enablement and CAB requirements.

### 12.2 Data Protection and GDPR Considerations
- Devices and services processing personal data must be identifiable via classification.
- Disposal must ensure personal data is securely destroyed.
- SaaS procurement must involve the Data Protection Officer (DPO) where the service processes personal data on behalf of Norfolk Industries.

### 12.3 SOX Considerations
- Asset records related to financial systems and SOX-relevant applications must be complete and auditable.
- Segregation of duties and evidence retention requirements must be followed for procurement, inventory adjustments, and disposals.

## 13. Integration with ITIL Practices and ITSM
### 13.1 Change Enablement and CAB
- Asset deployments or changes affecting production services require Change records and CAB review per Change Enablement.
- Emergency Changes must still result in updated asset/CI records within defined post-implementation windows.

### 13.2 Incident and Problem Management
- Incident tickets must reference affected CIs when available.
- Problem records may trigger asset refresh, replacement, or lifecycle changes.

### 13.3 Service Configuration Management (CMDB)
- CMDB records must support relationship mapping between assets, services, and dependencies.
- CMDB data quality is maintained through reconciliation, audits, and process controls.

### 13.4 Monitoring and Event Management
- Monitoring onboarding is part of deployment for critical assets.
- Monitoring alerts should be attributable to CIs for faster triage.

## 14. Procedures (Operational, Step-by-Step)
### 14.1 Procedure: Asset Onboarding (Standard Hardware Endpoint)
**Roles involved:** Regional IT Operations, IT Operations Manager, Endpoint Engineer, ITSM Process Owner (process design)

**Steps:**
1. Validate approved request and procurement record.
2. Receive shipment and capture serial number.
3. Tag device with barcode; record tag ID.
4. Create asset record and CI record (if required).
5. Enroll device in Intune; apply standard configuration.
6. Install required security tooling (EDR).
7. Confirm encryption and compliance status.
8. Assign device to user; document handover acknowledgment.
9. Update asset status to “In Use” and record assigned user, location, and custodian.

**Required evidence:**
- ITSM request and fulfillment tasks
- Asset record with tag ID and serial number
- Intune compliance record
- User handover acknowledgment (ITSM task completion)

### 14.2 Procedure: Quarterly Reconciliation (Inventory Accuracy)
**Objective:** Validate completeness and accuracy across authoritative sources and CMDB.

**Frequency:** Quarterly, regionally executed with global governance reporting.

**Steps:**
1. Extract inventory from authoritative sources:
   - Intune/ConfigMgr device list
   - Network inventory list
   - Vulnerability scan discovered assets
   - Cloud inventory exports (Azure/AWS)
   - Procurement/fixed asset register changes
2. Normalize identifiers (serial number, device ID, resource ID).
3. Compare to CMDB:
   - Missing in CMDB
   - Present in CMDB but not found in authoritative sources
   - Conflicting owner/location/status
4. Investigate discrepancies:
   - Confirm decommissioned vs missing vs shadow IT
   - Validate site transfers and loan returns
5. Remediate:
   - Create/update asset records
   - Retire/dispose records where appropriate
   - Open incident/security investigation for unknown assets
6. Report results:
   - Accuracy metrics
   - Aging of unresolved discrepancies
   - Root cause categories and corrective actions

**Required evidence:**
- Reconciliation report (dated, attributable)
- Discrepancy ticket list with resolution status
- Approval/attestation by IT Operations Manager and IT Governance Manager

### 14.3 Procedure: Barcode/RFID Tagging Standard
**Requirements:**
- Barcode format must be unique and not reused.
- Tags are controlled stock (stockroom controlled).
- RFID use requires regional approval and must map to the same asset record fields.

**Steps:**
1. Issue tag from controlled stock.
2. Affix tag to defined location on device (consistent placement standard).
3. Scan/record tag ID in asset record.
4. Verify by second check for high-value assets (network and servers).

**Evidence:**
- Tag issuance log
- Asset record showing tag ID association

### 14.4 Procedure: Stockroom Controls
**Objective:** Prevent loss, theft, and unrecorded movements.

**Controls:**
- Restricted access: authorized Regional IT Operations personnel only.
- Visitor log for non-authorized entry.
- Segregated areas for:
  - New stock pending tagging
  - Tagged stock ready for deployment
  - Returned devices pending wipe
  - Devices pending repair
  - Devices pending disposal pickup
- Cycle counts monthly; full reconciliation quarterly aligned with Section 14.2.
- Any variance requires an ITSM investigation record.

**Evidence:**
- Access roster and review record
- Cycle count reports
- Variance investigation tickets

### 14.5 Procedure: Asset Lending (Short-Term Loan)
**Use cases:** Temporary replacement during repair, short-term contractor device where permitted.

**Steps:**
1. Request submitted in ITSM with business justification and return date.
2. Validate user identity and authorization.
3. Issue loaner from stockroom; record:
   - Asset tag/serial
   - Loan start date and expected return date
   - Borrower and approving manager
4. Ensure device meets security baseline and is enrolled in management.
5. On return:
   - Inspect device condition
   - Confirm data handling requirements
   - Reimage/wipe as required
   - Update status to “In Stock” or “Pending Repair”

**Evidence:**
- Loan record and borrower acknowledgment
- Return inspection record

### 14.6 Procedure: Lost or Stolen Asset Handling
**Objective:** Rapidly reduce risk, support incident response, and maintain audit trail.

**Steps:**
1. User reports loss/theft via Service Desk immediately.
2. Service Desk creates Incident record; references asset tag/serial and assigned user.
3. Regional IT Operations:
   - Initiates remote lock/wipe as appropriate (Intune/EDR capabilities)
   - Disables relevant credentials or sessions where risk warrants (coordinate IAM Engineer)
4. Security Engineer coordinates investigation if data exposure is suspected.
5. Update asset record status to “Lost/Stolen” and note incident reference.
6. Initiate replacement workflow (new request/procure).
7. Close incident with documented actions and outcomes.

**Evidence:**
- Incident record with timestamps
- Remote wipe/lock proof
- Asset record status update
- Security investigation notes when applicable

## 15. Exceptions and Risk Acceptance
Exceptions are permitted only where a documented business need exists and compensating controls are applied.

### 15.1 Exception Triggers
- Physical tagging infeasible (e.g., certain OT devices)
- Asset cannot enroll in Intune/ConfigMgr due to technical constraints
- Legacy OT endpoints requiring constrained security tooling
- Emergency deployment without complete records (must be remediated post-implementation)

### 15.2 Approval and Recording
- Exceptions must be requested using the Exception Form template (Appendix).
- High-risk exceptions require approval aligned to the RACI table (in practice: Head of IT Infrastructure Services and CISO involvement as appropriate).
- Exceptions must have:
  - Risk statement
  - Compensating controls
  - Expiration date
  - Evidence of approval

### 15.3 Exception Review
- Exceptions are reviewed at least quarterly by IT Governance Manager with Service Owner and Platform Owner input.
- Expired exceptions must be closed via remediation or renewed with updated justification.

## 16. Metrics, Reporting, and Continual Improvement
Norfolk Industries measures asset management effectiveness using:

### 16.1 Core Metrics
| Metric | Definition | Frequency | Owner |
|---|---|---|---|
| Inventory completeness (endpoints) | % of devices in Intune that exist in CMDB with mandatory fields | Monthly | IT Operations Manager |
| Inventory accuracy (reconciliation variance) | # and % of records with discrepancies after quarterly reconciliation | Quarterly | IT Governance Manager |
| License compliance variance | Entitled vs deployed/used variance per key software title | Quarterly/Semi-annual | Service Owner |
| Shadow IT detections | Count of detected unauthorized assets/services and closure time | Monthly | Security Engineer |
| Disposal evidence completeness | % of disposed assets with disposal certificates and sanitization evidence | Quarterly | IT Operations Manager |
| Stockroom variance | Count/value of stockroom discrepancies | Monthly | Regional IT Operations |

### 16.2 Reporting Requirements
- Regional reports roll up to Global IT Operations.
- Executive summaries provided to Head of IT Infrastructure Services.
- Material issues affecting security posture are escalated to CISO.

### 16.3 Continual Improvement
- Root cause analysis for recurring reconciliation discrepancies.
- Process improvements managed by ITSM Process Owner.
- Automation improvements prioritized by Platform Owner (e.g., CMDB integrations).

## 17. Training and Awareness
- Regional IT Operations personnel must complete training on:
  - Stockroom controls
  - Tagging procedures
  - Chain of custody and transfer controls
  - Disposal and sanitization requirements
- Service Desk must be trained on:
  - Lost/stolen workflow
  - Request intake requirements for asset requests
- Annual refresher training is required for roles performing asset lifecycle activities, with completion evidence retained.

## 18. Evidence Retention and Audit Readiness
### 18.1 Evidence Principles (standards.json)
Norfolk Industries requires evidence to be:
- **Time-bound, attributable, and repeatable.**
- Inclusive of **approvals, logs, and validation artifacts** where applicable.

### 18.2 Minimum Retention Expectations
Retention must meet legal, regulatory, and contractual requirements. At minimum, retain:
- Procurement records and entitlements for the duration of the asset life plus the period required by finance and compliance.
- Disposal certificates and sanitization evidence for audit cycles and required retention periods.
- Reconciliation reports and discrepancy remediation evidence for ongoing audit readiness.

### 18.3 Audit Support
IT Governance Manager coordinates audit evidence collection with support from Service Owner, Platform Owner, and Regional IT Operations. Internal Audit independently assesses control effectiveness.

A sample audit evidence list is provided in Appendix D.

## 19. Control Mapping to Standards (ISO/IEC 27001, NIST CSF, SOC 2, ITIL 4, COBIT 2019)
This section maps key controls in this document to conceptual standard requirements and ensures audit traceability.

### 19.1 Control-to-Standard Mapping Table
| Control Area / Control | Description (Norfolk Industries) | Primary Evidence | ISO/IEC 27001 (conceptual Annex A) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain |
|---|---|---|---|---|---|---|---|
| Asset inventory completeness | Maintain accurate asset and CI records with mandatory fields | CMDB exports, reconciliation reports | Asset management controls (inventory/ownership) | Identify | Security, Availability | Service Configuration Management | APO, BAI, DSS, MEA |
| Chain of custody | Transfers, loans, and disposals documented and approved | Transfer forms, loan logs, disposal certs | Asset handling and accountability | Protect | Security | Service Configuration Management | DSS, MEA |
| Secure deployment baseline | Enroll endpoints in Intune, install EDR, enforce encryption | Intune compliance, EDR enrollment | Secure configuration, endpoint protection | Protect | Security | Information Security Management | DSS |
| License compliance and true-up | Entitlements reconciled to deployments/usage | Entitlement records, true-up reports | Compliance and asset control | Identify / Protect | Security, Confidentiality | Supplier Management / Service Configuration Management | APO, MEA |
| Shadow IT detection | Detect unauthorized assets/services and remediate | SIEM alerts, investigation tickets | Monitoring and control enforcement | Detect / Respond | Security | Monitoring and Event Management | DSS |
| Secure disposal and sanitization | Sanitization and disposal certification | Disposal certificates, vendor COD | Media handling and disposal | Protect / Recover | Security, Confidentiality | Service Continuity Management | DSS, MEA |
| Quarterly reconciliation | Formal reconciliation and remediation workflow | Quarterly reconciliation pack | Governance and monitoring | Identify / Detect | Availability, Security | Continual improvement across practices | MEA |

### 19.2 Evidence Quality Requirements
- Evidence must be reproducible from systems (ITSM, CMDB, Intune, cloud inventory).
- Approvals must show approver identity and timestamps.
- Reconciliation and true-up outputs must be versioned and dated.

---

## Appendix A: Asset Classification Matrix (Template and Standard)
### A.1 Asset Classification Matrix
| Classification Dimension | Level | Definition | Examples | Minimum Controls |
|---|---|---|---|---|
| Data Sensitivity | Public | Approved for public release | Marketing website content | Standard controls; inventory required if hosted by Norfolk Industries |
| Data Sensitivity | Internal | Internal business information | Internal documentation, non-sensitive operational data | Managed access; device enrollment required |
| Data Sensitivity | Confidential | Sensitive business information | Engineering data, supplier contracts | Encryption, access controls, enhanced monitoring where applicable |
| Data Sensitivity | Restricted | Highest sensitivity, regulatory/critical | GDPR personal data at scale, SOX-critical records, privileged credentials | Strong access control, PAM where applicable, strict disposal controls |
| Service Criticality | Non-critical | Limited operational impact | Lab devices | Standard inventory controls |
| Service Criticality | Important | Regional operational impact | Site services, standard applications | Monitoring and patching expectations |
| Service Criticality | Critical | Multi-site impact | Identity services dependencies, core network | CI relationships required, CAB governed changes |
| Service Criticality | Mission-critical | Safety/plant availability impact | OT-connected services, critical manufacturing services | Strict change windows, enhanced monitoring, OT governance alignment |
| OT Impact (OT only) | Safety-impacting | May impact safety | Safety PLC networks | Strict OT approvals, minimized scanning, controlled access |
| OT Impact (OT only) | Availability-impacting | May impact line uptime | SCADA/HMI infrastructure | Strict change windows, validated maintenance procedures |

### A.2 Classification Application Rules
- Default classification for unknown assets is **Internal** and **Important** until assessed.
- Assets supporting identity, remote access, security controls, or manufacturing plant operations are at least **Critical** in service criticality.

## Appendix B: Reconciliation Checklist (Quarterly)
### B.1 Quarterly Reconciliation Checklist
| Step | Check | Evidence Produced | Pass/Fail Criteria |
|---|---|---|---|
| 1 | Export Intune/ConfigMgr device inventory | Export file/report with date | Export covers all regions in scope |
| 2 | Export CMDB asset and CI inventory | CMDB export with timestamp | Includes mandatory fields |
| 3 | Export vulnerability scan discovered assets | Scan inventory report | Coverage for targeted networks |
| 4 | Export cloud inventory (Azure/AWS) | Resource inventory reports | Includes required tags fields |
| 5 | Compare and identify variances | Variance report | Variances categorized and counted |
| 6 | Investigate missing CMDB records | Investigation tickets | Each variance has a ticket |
| 7 | Remediate records and statuses | Updated CMDB records | Remediations completed or risk accepted |
| 8 | Confirm disposals have certificates | Disposal evidence list | 100% disposed assets have certificates |
| 9 | Management attestation | Signed/approved reconciliation report | Approval recorded in ITSM |

## Appendix C: CMDB Mandatory Fields (Norfolk Industries Minimum Standard)
### C.1 Mandatory Fields for Asset Records
| Field | Description | Example | Required For |
|---|---|---|---|
| Asset ID | Unique asset identifier | A-123456 | All assets |
| Tag ID | Barcode/RFID identifier | NI-BC-000123 | Physical assets (unless exception approved) |
| Serial Number | Manufacturer serial | SN12345 | Physical assets |
| Asset Type | Category | Laptop, Switch, Server | All assets |
| Manufacturer | Vendor name | Dell, Cisco | Physical assets |
| Model | Model identifier | Latitude 7xxx | Physical assets |
| Purchase Date | Date acquired | 2025-03-01 | Purchased assets |
| Warranty End Date | Support expiry | 2028-03-01 | Physical assets where warranty applies |
| Cost Center | Financial owner | CC-10020 | All assets |
| Location | Site/building/room | NA-CHI-DC1 | All assets |
| Custodian | Operational custodian | Regional IT Operations (NA) | All assets |
| Assigned User | Named user where applicable | j.smith | Endpoints/loaners |
| Lifecycle Status | Inventory state | In Stock / In Use / Pending Repair / Retired / Disposed / Lost/Stolen | All assets |
| Disposal Reference | Disposal certificate reference | DC-2025-00421 | Disposed assets |

### C.2 Mandatory Fields for CI Records (where CI required)
| Field | Description | Example |
|---|---|---|
| CI Name | Standard naming | NA-CHI-SRV-APP001 |
| CI Type/Class | CI taxonomy | Server / Network Device / Cloud Resource |
| Environment | Production/non-production | Production |
| Service Mapping | Linked service | Manufacturing MES Connectivity |
| Owner | Service Owner | (Named role assignment) |
| Support Group | Operational support team | Regional IT Operations (EU) |
| Relationship Links | Dependencies | Linked to network, storage, app CIs |
| Monitoring Status | Monitoring onboarding | Enabled |
| Backup Status | Backup onboarding | Enabled/Not Required with justification |

## Appendix D: Sample Audit Evidence List (Asset Management)
### D.1 Evidence Catalog (Examples)
| Audit Objective | Evidence Item | Source System | Evidence Characteristics |
|---|---|---|---|
| Prove assets are inventoried | CMDB export of assets and CIs with mandatory fields | ITSM/CMDB | Time-bound export, attributable |
| Prove endpoints are managed | Intune compliance/device inventory report | Intune | Timestamped report, includes device IDs |
| Prove license compliance | License entitlement file + deployment inventory + true-up report | Procurement + Intune/ConfigMgr + SaaS portals | Repeatable reconciliation method |
| Prove secure disposal | Disposal certificates + chain-of-custody logs | ITSM + vendor certificates | Includes serial/tag IDs and dates |
| Prove reconciliation performed | Quarterly reconciliation pack with approvals | ITSM + CMDB | Signed/approved by responsible roles |
| Prove shadow IT control | SIEM alerts + investigation tickets + outcomes | SIEM + ITSM | Traceable closure and remediation |
| Prove stockroom controls | Cycle count reports + variance investigations + access roster review | Stockroom log + ITSM | Time-bound and reviewed |

---

## Appendix E: Forms and Templates (Norfolk Industries Standard)
All forms below must be submitted and retained through the ITSM tool to ensure attributable approvals and retention.

### E.1 Asset Request Form (ITSM Catalog Submission Template)
| Field | Required | Description |
|---|---:|---|
| Requestor | Yes | Auto-populated from identity |
| Region/Site | Yes | Location of use |
| Asset Type | Yes | Endpoint/server/network/software/cloud/OT (if in scope) |
| Standard Option Selected | Yes | Select from approved catalog models where applicable |
| Business Justification | Yes | Why needed and impact if not provided |
| Required Date | Yes | Delivery/implementation target |
| Cost Center | Yes | Financial chargeback |
| Data Sensitivity | Yes | Public/Internal/Confidential/Restricted |
| Service Criticality | Yes | Non-critical/Important/Critical/Mission-critical |
| Approver | Yes | Delegated cost/business approver |
| Security Review Needed | Conditional | Triggered for non-standard, SaaS, cloud, OT, or Restricted data |

### E.2 Asset Transfer Form (Chain of Custody)
| Field | Required | Description |
|---|---:|---|
| Asset ID and Tag ID | Yes | Must match CMDB record |
| Serial Number | Yes | Verification field |
| From Custodian | Yes | Current custodian |
| To Custodian | Yes | New custodian |
| From Location | Yes | Site/building |
| To Location | Yes | Site/building |
| Transfer Type | Yes | Permanent transfer / Loan / Repair / Disposal staging |
| Effective Date | Yes | Date/time of handover |
| Approver | Yes | Manager approval where required |
| Notes | No | Condition, accessories included |

### E.3 Disposal Certificate (Internal Record)
| Field | Required | Description |
|---|---:|---|
| Asset ID, Tag ID, Serial Number | Yes | Full identifier set |
| Disposal Method | Yes | Vendor destruction / internal destruction / recycling |
| Sanitization Method | Yes | Method appropriate to media and classification |
| Sanitization Date | Yes | Date/time performed |
| Performed By | Yes | Name/role or vendor |
| Chain-of-Custody Reference | Yes | Pickup log or ITSM task |
| Vendor Certificate Reference | Conditional | Required if vendor used |
| Approver | Yes | Regional IT Operations approval |
| Final Status Update Confirmation | Yes | CMDB updated to Disposed with reference |

### E.4 Exception Form (Asset Management Exception)
| Field | Required | Description |
|---|---:|---|
| Requestor | Yes | Role and contact |
| Asset(s) in Scope | Yes | Asset IDs/serials/resources |
| Exception Type | Yes | Tagging / enrollment / scanning / record completeness |
| Business Justification | Yes | Why exception is needed |
| Risk Statement | Yes | Security/availability/compliance impact |
| Compensating Controls | Yes | Additional monitoring, segmentation, restricted access |
| Expiration Date | Yes | Must be time-bound |
| Approvals | Yes | Per RACI and risk level |
| Review Notes | Yes | Quarterly review outcomes |

---