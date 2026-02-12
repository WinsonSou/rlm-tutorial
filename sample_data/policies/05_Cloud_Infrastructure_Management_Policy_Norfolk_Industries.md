# Cloud Infrastructure Management Policy (Norfolk Industries)

## 1. Purpose
This policy defines mandatory requirements for provisioning, configuring, securing, operating, and continuously improving cloud infrastructure used by Norfolk Industries across Microsoft Azure (primary) and AWS (secondary). It establishes governance aligned to the Information Security Management System (ISMS), supports 24×7 operations, and enables regional execution through consistent controls, guardrails, and evidence.

## 2. Scope
### 2.1 In Scope
- All cloud resources, services, and configurations hosted in Microsoft Azure and AWS, including:
  - Subscriptions/accounts, management groups/organizational units, resource groups, VPCs/VNets, IAM/RBAC, key management, logging, monitoring, backup, and network controls.
  - CI/CD systems and pipelines that deploy or change cloud resources (Infrastructure as Code (IaC) and application infrastructure components).
  - Integration with on-prem data centers, Entra ID (Azure AD) / Active Directory, SIEM, EDR, vulnerability scanning, and ITSM tooling.
- All personnel and third parties with administrative, engineering, or operational access to cloud environments.

### 2.2 Out of Scope
- Application code-level secure development requirements (covered by separate secure SDLC standards).
- Operational Technology (OT) plant network controls except where OT systems connect to cloud services; such connectivity must meet the strict remote access and segmentation requirements of Norfolk Industries OT/IT integration standards.

## 3. Policy Statements (Mandatory Requirements)
1. Cloud environments must be built and operated using the Norfolk Industries landing zone model, with centralized guardrails and controlled regional execution.
2. All cloud changes must follow ITIL 4 Change Enablement, with Change Advisory Board (CAB) oversight for Normal and Emergency Changes as defined by Change Management procedures.
3. Identity and access must be integrated with Entra ID and must enforce least privilege, role separation, and audited access paths.
4. Network architecture must default to private connectivity where feasible, with explicit egress controls and strong segmentation.
5. Cloud resources must be discoverable and accountable through mandatory tagging and CMDB alignment for Configuration Items (CIs).
6. Logging, monitoring, and security telemetry must be enabled by default and integrated with the SIEM.
7. Backup and disaster recovery patterns must be implemented according to defined Recovery Point Objective (RPO) and Recovery Time Objective (RTO) requirements per service.
8. Exceptions require documented risk acceptance and approval per this policy.

## 4. Governance, Roles, and Responsibilities
### 4.1 Governance Model
- **Global IT Operations** defines standards, landing zone architecture, global controls, and cross-region operational coordination.
- **Regional IT Operations** executes day-to-day operations, implements workloads within approved guardrails, and supports local regulatory or business requirements while adhering to centralized governance.

### 4.2 Roles (from roles.json)
| Role | Responsibilities in this policy |
|---|---|
| CIO | Executive owner of IT strategy and governance; accountable for high-risk exception outcomes where required. |
| Head of IT Infrastructure Services | Accountable for cloud platform outcomes, standards, and operational performance. |
| CISO | Accountable for ISMS oversight; security policy conformance and risk management. |
| IT Governance Manager | Governance processes, compliance tracking, audit coordination, evidence readiness. |
| Service Owner | Accountable for end-to-end service performance, compliance, risk posture for a defined cloud-enabled service. |
| Platform Owner | Accountable for cloud landing zone architecture and engineering standards. |
| IT Operations Manager | Operational execution, 24×7 readiness, incident coordination. |
| Cloud Engineer | Implements and supports cloud infrastructure per standards and procedures. |
| IAM Engineer | Implements identity lifecycle, RBAC, privileged access controls. |
| Security Engineer | Security tooling, detection/response integrations, control validation. |
| ITSM Process Owner | Owns ITIL-aligned process design and continual improvement. |
| Internal Audit | Independent assessment of control design and operating effectiveness. |
| Data Protection Officer (DPO) | Oversees privacy governance and GDPR alignment for cloud data processing. |

### 4.3 RACI Alignment (selected activities)
This policy follows the Norfolk Industries RACI master. Where not explicitly restated, the master applies.

| Activity | Primary Accountable / Responsible (summary) |
|---|---|
| Policy approval | CIO (A), Head of IT Infrastructure Services (R), IT Governance Manager (R), CISO (C) |
| Standard approval (landing zone, tagging, guardrails) | Head of IT Infrastructure Services (A), Platform Owner (R), IT Governance Manager (R), CISO (C) |
| CAB chairing | Head of IT Infrastructure Services (A), Service Owner / Platform Owner / IT Operations Manager / ITSM Process Owner (R as applicable) |
| Audit evidence coordination | Head of IT Infrastructure Services (R), IT Governance Manager (R), Internal Audit (A) |

## 5. Cloud Landing Zone Model
### 5.1 Objectives
The landing zone model ensures:
- Consistent security baseline, auditability, and cost allocation.
- Segregation of duties and blast-radius reduction.
- Repeatable provisioning using IaC and policy-as-code.
- Regional execution without diverging from global controls.

### 5.2 Azure Structure (Management Groups and Subscriptions)
Norfolk Industries uses Azure management groups to enforce policy and RBAC at scale.

#### 5.2.1 Management Group Hierarchy (conceptual)
- **Norfolk-Root**
  - **Platform**
    - **Identity**
    - **Connectivity**
    - **Management**
    - **Security**
  - **LandingZones**
    - **Production**
    - **NonProduction**
    - **Sandbox** (restricted; time-bound)
  - **Decommissioned** (no workloads; retention for evidence and forensic preservation as required)

#### 5.2.2 Subscription Types
- **Platform Subscriptions**: Identity, Connectivity, Management, Security (owned by Global IT Operations / Platform Owner).
- **Workload Subscriptions**:
  - **Production**: customer/business-impacting workloads; stricter controls.
  - **NonProduction**: development/test; restricted data classes and connectivity.
  - **Sandbox**: experimentation with enforced guardrails, budget limits, and expiration.

### 5.3 AWS Structure (Organizations and Accounts)
Norfolk Industries uses AWS Organizations with organizational units (OUs) and accounts.

#### 5.3.1 OU Structure (conceptual)
- **Platform OU**: shared services (networking, logging, security tooling).
- **Workloads OU**:
  - **Production OU**
  - **NonProduction OU**
  - **Sandbox OU**
- **Suspended/Decommissioned OU**

#### 5.3.2 Account Types
- **Log Archive Account** (centralized immutable logging patterns where implemented).
- **Security Tooling Account** (security services and cross-account integrations).
- **Network/Shared Services Account** (central connectivity patterns where implemented).
- **Workload Accounts** (per product/service, environment-separated).

### 5.4 Resource Organization
- Azure resources must be grouped into **resource groups** aligned to lifecycle and ownership (application/service boundary).
- AWS resources must be organized with account-level separation and consistent tagging.

### 5.5 Guardrails and Policy-as-Code
Norfolk Industries enforces guardrails using policy-as-code:
- **Azure Policy** and initiative assignments at management group/subscription scope.
- **AWS Service Control Policies (SCPs)** and AWS Config rules where applicable.
- Guardrails are version-controlled and deployed via CI/CD with approvals (see Section 12).

Guardrails must include (minimum):
- Mandatory tagging enforcement (deny or audit with time-bound remediation requirements).
- Location/region restrictions aligned to data residency and DPO guidance.
- Disallow public exposure by default (public IPs, public storage access) unless explicitly approved.
- Encryption at rest requirements for storage services.
- Logging and monitoring enablement requirements.
- Restricted services list (high-risk services require Platform Owner and CISO review).

## 6. Resource Tagging and Configuration Management
### 6.1 Tagging Requirements
All cloud resources must include the mandatory tags defined in Appendix A. Tagging is required for:
- Cost allocation and chargeback/showback.
- Ownership and operational routing for incidents and changes.
- Compliance and audit reporting.
- CMDB correlation to Configuration Items (CIs).

### 6.2 CMDB and CIs
- Subscriptions/accounts, core platform components, and critical workload resources must be represented as CIs in the ITSM tool CMDB.
- CI records must include:
  - Owning Service Owner and Platform Owner.
  - Environment classification (Production/NonProduction/Sandbox).
  - Links to IaC repositories and pipelines.
  - RPO/RTO and backup/DR approach.

## 7. Identity, Access Management, and Privileged Access
### 7.1 Identity Integration
- Entra ID is the authoritative identity provider for interactive user access to Azure and for federated access patterns to AWS where implemented.
- Shared accounts are prohibited except for explicitly defined break-glass accounts (Section 7.4).

### 7.2 RBAC and Least Privilege
- Access must be role-based and scoped to the minimum required resources.
- Production access must be time-bound where supported (Privileged Access Management and just-in-time elevation).
- Separation of duties must be enforced between:
  - Platform engineering (baseline and guardrails)
  - Workload engineering (application resources)
  - Security monitoring and response
  - Approval authorities (CAB/Service Owner)

### 7.3 Administrative Access Standards
- Administrative access must use:
  - Multi-factor authentication
  - Approved privileged access workflows (PAM where applicable)
  - Named accounts linked to HR identity lifecycle
- Admin rights must be reviewed at least quarterly by the Service Owner with IAM Engineer support; evidence must be retained.

### 7.4 Break-Glass Accounts
Break-glass access is permitted only to restore control during identity outages or severe incidents.

Requirements:
- Break-glass accounts must be:
  - Minimal in number (at least two, to avoid single point of failure)
  - Monitored with high-severity alerts in the SIEM
  - Excluded from conditional access only when explicitly required for resilience, with compensating controls documented
- Credentials must be stored in the approved PAM solution, with access logged and reviewed by the CISO delegate (Security Engineer) and IT Governance Manager.
- Break-glass usage must trigger an incident record and a post-incident review.

### 7.5 Secrets and Key Management (Key Vault Approach)
- Secrets, keys, and certificates must be stored in centralized managed services:
  - Azure Key Vault for Azure workloads.
  - AWS managed secret storage services for AWS workloads.
- Requirements:
  - No secrets in source code, pipeline variables without secret protection, or plaintext configuration files.
  - Keys must be rotated per Section 15.4.
  - Access policies/RBAC must be least privilege and auditable.
  - Use managed identities/service principals/roles instead of long-lived credentials whenever possible.
  - Customer-managed keys are required for regulated or high-risk data classes per ISMS requirements and DPO guidance where applicable.

## 8. Cloud Network Architecture and Connectivity
### 8.1 Network Segmentation and Standard Patterns
- Workloads must be deployed into segmented networks aligned to environment and sensitivity:
  - Separate VNets/VPCs for Production and NonProduction.
  - Separate subnets for application tiers and management components.
- OT connectivity to cloud requires explicit approval and must maintain OT segmentation principles, including strict remote access controls.

### 8.2 Azure VNets and AWS VPCs
- VNets/VPCs must use standardized IP address management to prevent overlap and support routing to on-prem environments.
- Network security controls must include:
  - Network security groups / security groups with least privilege rules.
  - Default deny inbound; restrict east-west traffic where feasible.
  - Administrative ports allowed only via approved management paths (bastion, privileged access workstations, or equivalent approved pattern).

### 8.3 Peering and Transit
- VNet peering / VPC peering must be approved via Change Enablement and designed to prevent unintended transitive routing unless explicitly required.
- Centralized transit patterns (hub-and-spoke) are preferred for Production workloads:
  - Hub managed by Platform Owner.
  - Spokes owned by workload teams under guardrails.

### 8.4 Private Endpoints and Service Exposure
- Private endpoints/private link patterns are required for platform services (storage, databases, key management) where supported and feasible.
- Public endpoints must be disabled by default for Production; exceptions require risk review and approval (Section 16).
- Ingress must use approved edge controls (WAF/reverse proxy patterns) as defined by platform standards.

### 8.5 Egress Controls
- Egress must be controlled using:
  - Centralized firewall/NAT egress where implemented.
  - Explicit allow-lists for Production where feasible.
  - DNS controls aligned to corporate standards.
- Egress logs must be retained and integrated with the SIEM.

## 9. Security Monitoring, Logging, and Vulnerability Management
### 9.1 Logging and SIEM Integration
- Cloud audit logs and platform logs must be enabled by default:
  - Azure activity logs and diagnostics logs for critical services.
  - AWS CloudTrail and service logs where applicable.
- Logs must be forwarded to the SIEM (for example, Microsoft Sentinel) and retained per ISMS requirements and legal/regulatory obligations.
- Logging configurations are guardrails and must be deployed as policy-as-code.

### 9.2 EDR and Workload Protection
- Where supported, workloads must be onboarded to the approved EDR solution (for example, Microsoft Defender for Endpoint) and monitored by Security Engineer and IT Operations Manager processes.

### 9.3 Vulnerability Scanning
- Cloud compute instances, containers, and exposed services must be scanned using the approved vulnerability scanning tool (for example, Tenable/Nessus) or native cloud capabilities where approved by the CISO.
- Findings must be prioritized based on business impact and exposure and tracked to remediation closure in the ITSM tool.

## 10. Data Protection and Privacy
- Data classification and handling requirements apply equally in cloud environments.
- Encryption in transit must use approved protocols and configurations.
- Encryption at rest is mandatory for Production workloads.
- Data residency and cross-border transfer requirements must be validated with the Data Protection Officer (DPO) for applicable workloads.
- Access to personal data must be logged and reviewable.

## 11. Service Continuity: Backup, DR, and Resilience
### 11.1 Continuity Requirements
- Each cloud-enabled service must define and test:
  - Service Level Objective (SLO)
  - Recovery Point Objective (RPO)
  - Recovery Time Objective (RTO)
- Backup and DR configurations must be implemented and evidenced.

### 11.2 Standard DR Patterns
Approved patterns include:
- **In-region resilience**: availability zones, redundant services.
- **Cross-region DR**: warm standby or active-active where justified by business impact.
- **Immutable backups**: where supported and required for ransomware resilience.

### 11.3 Backup Controls
- Backups must be:
  - Automated
  - Monitored for success/failure
  - Tested via restore validation on a defined schedule
- Backup storage must be protected from deletion or tampering using role separation and protective controls.

## 12. Cloud Change Management, IaC, and CI/CD Controls
### 12.1 Change Enablement Requirements
- All changes to cloud infrastructure must be executed via approved mechanisms:
  - IaC templates/modules for infrastructure components
  - Approved change pipelines with peer review and approvals
- Emergency Changes are permitted only under defined criteria and must be reviewed retrospectively by the CAB.

### 12.2 Infrastructure as Code (IaC)
- Cloud infrastructure must be provisioned using IaC for:
  - Subscriptions/accounts baseline configuration
  - Networking, identity bindings, and critical platform services
  - Production workload infrastructure
- IaC repositories must enforce:
  - Code review (minimum two reviewers for Production)
  - Security scanning (static analysis and secret scanning)
  - Versioning and release tagging
  - Traceability to change records

### 12.3 CI/CD Approvals and Promotion
- Production deployments must require:
  - Approved change record in the ITSM tool
  - CAB approval when required by Change Management policy
  - Separation between build and release permissions
- Promotion between environments must be controlled and logged.

## 13. Cost Management and Capacity Management
### 13.1 Cost Management
- Budgets and alerts must be configured at subscription/account and workload levels.
- Tagging (Appendix A) must support showback/chargeback (Appendix C).
- Cost anomalies must be investigated and documented by the Service Owner and IT Operations Manager.

### 13.2 Capacity Management
- Platform Owner and Service Owner must ensure:
  - Capacity planning for critical services
  - Autoscaling configurations where appropriate
  - Quota management and request processes
- Capacity risks must be recorded and tracked within service risk registers under the ISMS.

## 14. Supplier and Shared Responsibility Management
- Cloud provider responsibilities and Norfolk Industries responsibilities must be documented per service.
- Managed services, third-party marketplace offerings, and SaaS integrations must undergo security and privacy review aligned to ISMS requirements.
- Contracts and supplier controls must support audit rights and evidence availability where applicable.

## 15. Operational Procedures (Mandatory)
All procedures in this section must be performed using the ITSM tool for request/change/incident records, and must retain evidence according to Section 18.

### 15.1 Procedure: Create a Cloud Subscription/Account
**Trigger:** New workload/service or new environment requires a dedicated subscription/account.

**Steps:**
1. **Request submission** (Requester via Service Desk): submit the completed subscription/account request form (Appendix B) as a service request.
2. **Validation** (Service Owner, Platform Owner):
   - Confirm business justification, environment classification, and data classification.
   - Confirm required regions and connectivity.
   - Confirm SLO/RPO/RTO and backup/DR pattern selection.
3. **Security review** (CISO delegate: Security Engineer; consult DPO as needed):
   - Validate logging, encryption, network exposure, and identity model.
4. **Approval** (Head of IT Infrastructure Services or delegated approver per governance; CAB if required):
   - Approve creation and baseline guardrail application.
5. **Provisioning** (Cloud Engineer):
   - Create subscription/account in the correct management group/OU.
   - Apply baseline guardrails (policy-as-code/SCPs), logging, budgets, and mandatory tags.
   - Configure RBAC/IAM roles and privileged access model.
6. **CMDB registration** (IT Operations Manager / ITSM Process Owner support):
   - Create/associate CI records for the subscription/account and critical platform components.
7. **Handover** (Service Owner):
   - Confirm operational readiness: monitoring, backup, alerts, on-call routing, runbooks.

**Evidence (minimum):**
- Approved service request, approvals, management group/OU placement, policy assignment logs, budget configuration screenshots/exports, CMDB CI record link.

### 15.2 Procedure: Onboard an Application Team to Cloud
**Trigger:** A product/service team requires access and a deployment pathway.

**Steps:**
1. **Initiate onboarding** (Service Owner): open an onboarding request with the target subscription/account and environment.
2. **Access model** (IAM Engineer + Platform Owner):
   - Define RBAC roles (readers, contributors, approvers).
   - Enforce least privilege and just-in-time access for Production.
3. **Deployment model** (Cloud Engineer + ITSM Process Owner):
   - Confirm approved IaC modules and pipelines.
   - Ensure change record integration and approval gates.
4. **Network and data access** (Network controls validation by Platform Owner):
   - Validate private endpoints, DNS, egress, and connectivity requirements.
5. **Security tooling** (Security Engineer):
   - Verify SIEM forwarding, EDR onboarding where applicable, vuln scanning enrollment.
6. **Operational readiness** (IT Operations Manager):
   - Confirm alert routing, escalation paths, and runbooks for the service.
7. **Acceptance** (Service Owner):
   - Document acceptance that onboarding requirements are met.

**Evidence (minimum):**
- Access approval records, RBAC assignments export, pipeline approval configuration, security onboarding verification.

### 15.3 Procedure: Approve Cloud Guardrail Exceptions
**Trigger:** A workload cannot comply with a guardrail (for example, requires public endpoint, nonstandard region, or nonstandard service).

**Steps:**
1. **Exception request** (Service Owner): submit exception request via ITSM with:
   - Control(s) impacted, reason, duration, compensating controls, residual risk, and rollback plan.
2. **Risk review** (CISO + Platform Owner):
   - Validate compensating controls and required monitoring.
   - Determine if privacy review is needed (DPO).
3. **Approval path**:
   - **High-risk exceptions** require CIO (A) and Head of IT Infrastructure Services (R) per RACI master.
   - Non-high-risk exceptions require Head of IT Infrastructure Services (or delegated authority) with CISO consultation.
4. **Implementation** (Cloud Engineer):
   - Implement exception using policy-as-code where feasible (scoped exemption with expiration).
5. **Monitoring** (Security Engineer + IT Operations Manager):
   - Add targeted detections/alerts.
6. **Review and expiry** (IT Governance Manager):
   - Track exception expiry; enforce renewal review or closure.

**Evidence (minimum):**
- Exception request, approvals, compensating control documentation, implementation proof, monitoring configuration, expiry tracking.

### 15.4 Procedure: Rotate Keys, Secrets, and Certificates
**Trigger:** Scheduled rotation, suspected compromise, personnel changes, or policy requirement.

**Steps:**
1. **Identify scope** (Service Owner + IAM Engineer):
   - Enumerate secrets/keys/certificates and dependent services.
2. **Change record** (IT Operations Manager):
   - Create a change record for Production rotations; schedule during approved windows unless emergency.
3. **Perform rotation** (Cloud Engineer / IAM Engineer):
   - Rotate in Key Vault/approved secret storage.
   - Update dependent services using managed identities/roles where feasible.
4. **Validate** (Service Owner):
   - Confirm service functionality and monitor for errors.
5. **Revoke and clean up** (IAM Engineer):
   - Disable old credentials; validate no remaining dependencies.
6. **Evidence capture** (IT Governance Manager support):
   - Record rotation date, approver, and validation outcome.

**Minimum rotation requirements:**
- High-privilege secrets and externally exposed certificates must follow a defined rotation schedule and must be rotated immediately upon suspected compromise.
- Break-glass credential rotation must occur after any use and on a periodic schedule aligned to ISMS requirements.

### 15.5 Procedure: Respond to a Cloud Incident
**Trigger:** Security alert, outage, data exposure risk, or suspected compromise in cloud.

**Steps:**
1. **Detection and triage** (Service Desk Manager / IT Operations Manager):
   - Open an incident record, assign severity, notify on-call.
2. **Containment** (Security Engineer + Cloud Engineer):
   - Restrict access (RBAC lock-down), isolate resources, block egress, disable keys if needed.
3. **Eradication and investigation** (Security Engineer):
   - Collect logs, snapshots, and evidence; preserve forensic integrity.
4. **Recovery** (IT Operations Manager + Service Owner):
   - Restore from backups, execute DR pattern if needed, validate service health against SLO.
5. **Communications** (IT Operations Manager):
   - Provide updates to stakeholders per incident communications procedure; involve DPO for potential privacy incidents.
6. **Post-incident review** (Service Owner + Platform Owner + CISO):
   - Root cause analysis, corrective actions, control improvements, and evidence retention.

**Evidence (minimum):**
- Incident record timeline, SIEM alert details, access changes, containment actions, recovery validation, post-incident review notes.

## 16. Compliance, Risk Management, and Exceptions
- Compliance with this policy is mandatory and measured through continuous control monitoring and periodic reviews.
- Risk decisions must be documented, time-bound, and attributable.
- Exceptions must:
  - Specify duration and scope
  - Define compensating controls
  - Include approval records
  - Be reviewed prior to expiration

## 17. Training and Awareness
- Cloud access requires completion of role-appropriate training:
  - Cloud security and least privilege fundamentals for all cloud users.
  - Advanced platform and incident response training for Cloud Engineer, IAM Engineer, and Security Engineer roles.
- Training completion evidence must be tracked and available for audit.

## 18. Evidence, Metrics, and Auditability
### 18.1 Evidence Principles
Evidence must follow Norfolk Industries evidence principles:
- Evidence must be time-bound, attributable, and repeatable.
- Evidence must include approvals, logs, and validation artifacts where applicable.

### 18.2 Required Evidence Categories
- Landing zone baseline deployments and policy assignments (policy-as-code runs).
- RBAC/IAM assignments and quarterly access reviews.
- Change records, CAB approvals, and pipeline approval logs.
- Logging enablement and SIEM ingestion validation.
- Vulnerability scan results and remediation tracking.
- Backup success reports and restore test results.
- DR test results and post-incident reviews.
- Cost budgets/alerts configuration and cost allocation reports.
- Exception records with expiry tracking.

### 18.3 Operational Metrics (minimum)
| Metric | Owner | Frequency | Target/Expectation |
|---|---|---|---|
| Percentage of cloud resources with mandatory tags | Platform Owner | Weekly | ≥ 98% with remediation plan for gaps |
| Production subscriptions/accounts with baseline guardrails applied | Platform Owner | Monthly | 100% |
| Quarterly access review completion | Service Owner | Quarterly | 100% completion and evidence |
| Backup success rate for critical services | IT Operations Manager | Weekly | ≥ 99% successful jobs with tracked failures |
| Restore test completion for critical services | Service Owner | Quarterly | 100% for in-scope critical services |
| Mean time to detect/respond for cloud security alerts | Security Engineer | Monthly | Trending improvement; report to CISO |

## 19. Review Cycle and Policy Maintenance
- This policy must be reviewed at least annually by the IT Governance Manager in coordination with the Head of IT Infrastructure Services and CISO.
- Material changes to cloud provider capabilities, threat landscape, regulatory requirements (including GDPR), or audit findings must trigger an out-of-cycle review.
- Revisions must be version-controlled, approved per RACI master, and communicated to Global IT Operations and Regional IT Operations.

## Appendix A: Cloud Tagging Standard (Mandatory)
### A.1 Tagging Rules
- Tags must be applied at creation time via IaC modules or provisioning workflows.
- Tags must be inherited or enforced using policy-as-code where supported.
- Values must follow defined formats (no free-form for controlled fields).

### A.2 Mandatory Tags
| Tag Key | Allowed Values / Format | Purpose | Applies To |
|---|---|---|---|
| `ni:owner` | Corporate email (named individual) | Operational accountability | All resources |
| `ni:service` | Service name (registered with Service Owner) | Service mapping | All resources |
| `ni:environment` | `production` \| `nonproduction` \| `sandbox` | Control enforcement and reporting | All resources |
| `ni:region` | Cloud region code (provider-specific) | Residency and operations | All resources |
| `ni:costCenter` | Numeric code (SOX-aligned financial structure) | Cost allocation | All resources |
| `ni:businessUnit` | `NA` \| `EU` \| `APAC` \| `Global` | Reporting and routing | All resources |
| `ni:dataClass` | `public` \| `internal` \| `confidential` \| `restricted` | Security controls alignment | Data-bearing resources |
| `ni:rto` | Duration string (e.g., `4h`, `24h`) | Continuity | Services/resources supporting a service |
| `ni:rpo` | Duration string (e.g., `15m`, `1h`) | Continuity | Data-bearing resources |
| `ni:cmdbCiId` | CMDB CI identifier | Traceability | Subscriptions/accounts and critical resources |
| `ni:complianceScope` | `SOX` \| `GDPR` \| `SOC2` \| `None` or combinations in comma-separated list | Compliance reporting | Workloads as applicable |

### A.3 Optional Recommended Tags
| Tag Key | Format | Purpose |
|---|---|---|
| `ni:application` | App/system name | Application mapping |
| `ni:portfolio` | Portfolio name | Portfolio reporting |
| `ni:expirationDate` | `YYYY-MM-DD` | Sandbox lifecycle control |

## Appendix B: Subscription/Account Request Form (Template)
### B.1 Requester and Ownership
| Field | Value |
|---|---|
| Requester name |  |
| Requester email |  |
| Business unit (`NA`/`EU`/`APAC`/`Global`) |  |
| Service Owner (name, email) |  |
| Platform Owner (name, email) |  |
| Primary on-call group / escalation |  |

### B.2 Environment and Classification
| Field | Value |
|---|---|
| Cloud provider | Azure / AWS |
| Environment | production / nonproduction / sandbox |
| Data classification | public / internal / confidential / restricted |
| Compliance scope | SOX / GDPR / SOC2 / None (and details) |
| Intended regions |  |
| Connectivity required | Internet-only / On-prem connectivity / Partner connectivity |

### B.3 Network and Exposure
| Field | Value |
|---|---|
| Public endpoints required | No / Yes (describe and justify) |
| Private endpoints planned | Yes / No (explain) |
| Egress allow-list required | Yes / No |
| OT connectivity involved | No / Yes (describe segmentation and controls) |

### B.4 Continuity and Operations
| Field | Value |
|---|---|
| SLO |  |
| RTO |  |
| RPO |  |
| Backup pattern | In-service backups / Snapshot backups / Immutable backups |
| DR pattern | In-region / Cross-region warm standby / Active-active |
| Monitoring requirements |  |

### B.5 Cost Management
| Field | Value |
|---|---|
| Cost center |  |
| Budget (monthly) |  |
| Alert thresholds | 50% / 75% / 90% / 100% (or specify) |
| Chargeback/showback owner |  |

### B.6 Approvals (recorded in ITSM)
| Required Approval | Approver |
|---|---|
| Service Owner approval |  |
| Platform Owner approval |  |
| Security review (CISO delegate) |  |
| DPO review (if applicable) |  |
| CAB (if required) |  |

## Appendix C: Cost Allocation Model (Standard)
### C.1 Allocation Principles
- Costs must be attributable to a service and cost center using mandatory tags.
- Shared platform costs must be allocated using a consistent driver model and documented monthly.
- Cost reporting must support SOX controls for financial accuracy.

### C.2 Allocation Layers
| Cost Layer | Allocation Basis | Examples |
|---|---|---|
| Workload direct costs | Direct by subscription/account and tags | Compute, storage, managed databases |
| Shared network costs | Proportional by egress volume or fixed split by service tier | Firewalls, NAT, transit |
| Shared security tooling | Fixed per subscription/account plus variable by usage | SIEM ingestion, scanning |
| Shared management services | Fixed split by environment or service count | Monitoring platform, automation |

### C.3 Monthly Cost Review
- Service Owner reviews month-to-date vs budget and validates tagging coverage.
- IT Operations Manager reviews anomalies and capacity-related cost changes.
- IT Governance Manager ensures evidence retention for audit.

## Appendix D: Audit Evidence List (Minimum Set)
| Control Area | Evidence Artifact | Owner | Frequency |
|---|---|---|---|
| Landing zone guardrails | Policy/SCP assignment reports; CI/CD run logs; code repository history | Platform Owner | Monthly and per change |
| Tagging compliance | Tag compliance report; remediation tickets | Platform Owner | Weekly |
| Identity and RBAC | RBAC/IAM exports; quarterly access review sign-off | IAM Engineer / Service Owner | Quarterly |
| Break-glass controls | PAM access logs; SIEM alerts; incident records for use | Security Engineer | Per use + quarterly review |
| Logging/SIEM | SIEM ingestion validation; audit log enablement evidence | Security Engineer | Monthly |
| Vulnerability management | Scan reports; remediation tracking; exception approvals | Security Engineer | Monthly |
| Change management | Change records; CAB approvals; pipeline approvals and deployment logs | ITSM Process Owner / IT Operations Manager | Per change |
| Backup and restore | Backup job reports; restore test results | IT Operations Manager / Service Owner | Weekly + quarterly tests |
| DR testing | DR exercise records; RTO/RPO validation | Service Owner | At least annually (or per service requirement) |
| Cost management | Budget configuration; monthly cost reports; anomaly investigations | Service Owner | Monthly |

## Appendix E: Standards and Control Mapping (Crosswalk)
| Policy Area | ISO/IEC 27001 (Annex A concept) | NIST CSF Function | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Typical Evidence |
|---|---|---|---|---|---|---|
| Landing zone guardrails, policy-as-code | Organizational and technological controls for secure configuration and change control | Protect | Security, Availability | Change Enablement; Service Configuration Management | BAI, DSS, MEA | Policy assignment logs, IaC runs |
| Identity, RBAC, least privilege | Access control | Protect | Security | Information Security Management | APO, DSS | RBAC exports, access reviews |
| Network segmentation, private endpoints, egress controls | Network security | Protect/Detect | Security, Availability | Monitoring and Event Management | DSS | Network configs, firewall logs |
| Logging and monitoring to SIEM | Logging and monitoring | Detect/Respond | Security | Monitoring and Event Management | DSS, MEA | SIEM ingestion, alerts |
| Backup and DR patterns | Continuity and resilience | Recover | Availability | Service Continuity Management | DSS | Backup reports, DR tests |
| Change control via IaC and CI/CD approvals | Change management | Protect | Security, Availability | Change Enablement | BAI | Change records, approvals |
| Cost governance and tagging | Asset management and accountability | Identify | Availability | Service Configuration Management | APO, MEA | Tag compliance, cost reports |

