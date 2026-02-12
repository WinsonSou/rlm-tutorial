# Infrastructure Automation & DevOps Policy (Norfolk Industries)

## 1. Purpose
This policy establishes mandatory governance, security, and operational requirements for infrastructure automation and DevOps practices within Norfolk Industries. It ensures that Infrastructure as Code (IaC), automation scripts, and CI/CD pipelines are designed, approved, operated, and evidenced in alignment with the Information Security Management System (ISMS), ITIL 4 practices, ISO/IEC 27001, ISO/IEC 22301, COBIT 2019, NIST CSF concepts, SOC 2 Trust Services Criteria, GDPR, and SOX obligations.

## 2. Scope
### 2.1 In scope
This policy applies to:
- All automation that creates, modifies, or deletes Configuration Items (CIs) in:
  - Microsoft Azure (primary cloud)
  - AWS (secondary cloud)
  - On-prem data centers
- Automation affecting:
  - Network, compute, storage, databases, identity (Active Directory and Entra ID (Azure AD), then Entra ID), endpoint management (Microsoft Intune and ConfigMgr where needed)
  - Security tooling integrations (SIEM such as Microsoft Sentinel, EDR such as Microsoft Defender for Endpoint, vulnerability scanning such as Tenable/Nessus, PAM such as CyberArk)
  - Monitoring, backup, and logging platforms
- CI/CD pipelines and related tooling (source control, build agents, artifact repositories, secret stores, and deployment orchestrators)
- Automation used to support or access Operational Technology (OT) networks or systems, including jump hosts and remote access pathways, where managed by IT Infrastructure Services

### 2.2 Out of scope
- Application DevOps practices for business applications not managed by IT Infrastructure Services (except where they interact with infrastructure CIs or shared pipeline platforms)
- OT control logic (e.g., PLC programming) not managed by IT Infrastructure Services; however, any IT-hosted tooling that can affect OT network access remains in scope

## 3. Policy statements
Norfolk Industries requires that:
1. All infrastructure changes performed via automation are governed by Change Enablement and integrated with the Change Advisory Board (CAB) where applicable.
2. IaC is the default method for provisioning and configuration of infrastructure CIs whenever technically feasible.
3. Source-controlled automation must follow mandatory code review, separation of duties, and secret management controls.
4. Deployment pipelines must enforce environment promotion, approvals, and traceability from change request to code version to deployment evidence.
5. Logging, monitoring, and rollback capabilities are designed into automation to support 24×7 operations and service continuity.
6. Automation that can impact OT connectivity or segmentation is subject to elevated risk controls and must align to strict remote access controls.

## 4. Definitions
All terms use canonical Norfolk Industries terminology and the glossary in effect for this document set.

| Term | Definition |
|---|---|
| IT Infrastructure Services | The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations. |
| Global IT Operations | Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure. |
| Regional IT Operations | Regional teams executing day-to-day operations, local support, and implementation aligned to global governance. |
| Information Security Management System (ISMS) | The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001. |
| Change Advisory Board (CAB) | The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management. |
| Configuration Item (CI) | Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references. |
| Operational Technology (OT) | Systems and networks that monitor or control physical processes, including SCADA, PLCs, MES and plant networks. |
| Service Level Objective (SLO) | A target level of service reliability or performance, measured by agreed metrics. |
| Recovery Point Objective (RPO) | Maximum tolerable amount of data loss measured in time. |
| Recovery Time Objective (RTO) | Target time to restore a service after disruption. |

## 5. Roles and responsibilities
Roles and descriptions are authoritative per roles.json.

### 5.1 Policy governance
- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes.
- **CISO**: Accountable for information security program and ISMS oversight.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **ITSM Process Owner**: Owns ITIL-aligned process design (Change/Incident/Problem/CMDB) and continual improvement.
- **Internal Audit**: Independently assesses control design and operating effectiveness.

### 5.2 Delivery and operations
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for a defined infrastructure service.
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain (e.g., network, cloud, endpoint).
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- **Cloud Engineer / Systems Engineer / Network Engineer / Endpoint Engineer / IAM Engineer / Security Engineer**: Implement and support automation per standards and procedures.

### 5.3 RACI (policy-level)
This table is consistent with raci_master.csv and applies to this policy.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Standard approval | I | A | C | R | C | R | C | C | I |
| Procedure ownership | I | A | C | R | R | R | R | C | I |
| Exception approval (high risk) | A | R | R | C | C | C | C | C | I |
| CAB chairing | I | A | C | C | R | R | R | R | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy compliance requirements (mandatory controls)
### 6.1 Source control and repository governance
1. All automation code (IaC, scripts, pipeline definitions) must be stored in an enterprise-approved source control repository with:
   - Immutable commit history and authenticated access via Entra ID
   - Branch protection on the default branch
   - Required pull request (PR) reviews before merge
2. Direct commits to protected branches are prohibited.
3. Repository access must follow least privilege and be reviewed on a defined cadence aligned to ISMS access control practices.

### 6.2 Infrastructure as Code (IaC) standards
IaC must follow these standards:
- **Idempotency**: Repeated runs converge to the desired state without unintended side effects.
- **Modularity**: Reusable modules with clear inputs/outputs and versioning.
- **Immutability preference**: Prefer immutable patterns (replace rather than patch) for compute images and platform components when feasible.
- **Tagging/metadata**: All provisioned resources must include required governance tags (owner, environment, service, data classification where applicable, cost center).
- **State management**:
  - State files must be protected as sensitive assets.
  - State backends must enforce encryption at rest and access logging.
  - State locking must be enabled where supported.
- **Policy-as-code**:
  - Platform guardrails (e.g., Azure Policy) must be integrated where applicable to prevent non-compliant deployments.
- **Drift detection**:
  - Managed infrastructure must be subject to periodic drift detection; unmanaged drift must result in remediation via IaC or documented exception.

### 6.3 CI/CD pipeline requirements
1. Pipelines must enforce:
   - Authenticated execution and role-based authorization
   - Separation of duties between code authors and deploy approvers for Production (see Section 7)
   - Artifact integrity (signed artifacts or checksum validation where supported)
   - Immutable build artifacts and versioned releases
2. Build and deployment logs must be retained and searchable for audit and incident response, aligned to SIEM ingestion where appropriate.
3. Pipeline runners/agents must be hardened and patched; ephemeral runners are preferred for high-risk environments.

### 6.4 Secret management
1. Secrets (API keys, credentials, certificates, tokens) must never be stored in plaintext in:
   - Source code repositories
   - Pipeline definitions (unless referenced via secret variables/integrations)
   - Documentation stored in general-access repositories
2. Secrets must be stored and accessed via approved secret management mechanisms and integrated with PAM (e.g., CyberArk) where applicable.
3. Secrets must be rotated:
   - On a defined schedule based on risk
   - Immediately upon suspected compromise
   - Upon personnel changes that impact privileged access
4. Pipeline access to secrets must use short-lived credentials where feasible and must be scoped to the minimum required permissions.

### 6.5 Logging, monitoring, and alerting
1. Automation executions must generate logs that include:
   - Who initiated the run (identity)
   - What code version was executed (commit hash/release tag)
   - Target environment and scope
   - Execution result and changes applied
2. Critical pipeline events must be monitored and alertable through enterprise monitoring and/or SIEM integrations (e.g., Microsoft Sentinel), including:
   - Failed deployments to Production
   - Policy violations
   - Unauthorized access attempts to secrets or deployment approvals

### 6.6 OT/IT integration safeguards
1. Automation that changes connectivity, firewall rules, remote access gateways, jump hosts, or identity controls related to OT network segmentation must:
   - Be treated as high risk and require CAB oversight as a Normal Change unless qualifying as Emergency Change
   - Include explicit rollback plans and validation steps
   - Be executed in approved maintenance windows unless Emergency Change criteria are met

## 7. Separation of duties (SoD) and approvals
### 7.1 General SoD rules
1. For Production deployments, the person who approves deployment must not be the sole author and executor of the change.
2. Minimum approval requirements:
   - **Non-Production**: At least one PR approver distinct from the author.
   - **Production**: At least two approvers for PR merge, plus an independent deployment approver (manual gate) unless the CAB has approved an alternative control design documented by the IT Governance Manager.
3. Elevated-risk areas (identity, network security controls, OT access pathways, logging/monitoring pipelines, backup/restore automation) require a Security Engineer or IAM Engineer review, as applicable.

### 7.2 Change Advisory Board (CAB) integration for approvals
1. Normal Changes impacting Production CIs must have an approved change record and align to CAB schedules.
2. Standard Changes may use pre-approved templates if the automation pattern is repeatable, low risk, and formally cataloged by the ITSM Process Owner with approval from the Head of IT Infrastructure Services.
3. Emergency Changes are permitted only to restore service or mitigate active risk; they must be retrospectively reviewed by the CAB with full evidence.

## 8. Change control integration (ITIL 4 Change Enablement)
### 8.1 Change record requirements
All Production-affecting automation runs must reference a change record in the ITSM tool and include:
- Impacted service and CIs
- Risk assessment and testing evidence
- Planned implementation window
- Rollback plan and verification steps
- Approvals (CAB where required)
- Linkages to code version (PR, commit, release artifact)

### 8.2 Environment promotion and release strategy
1. Environments must be logically separated (e.g., Dev/Test/Stage/Production) with distinct credentials, subscriptions/accounts, and network segmentation where feasible.
2. Promotions must be performed via pipeline stages using the same artifact/version:
   - Build once, promote the same artifact across environments
3. Manual approvals (gates) must be enforced for Production and for any environment that impacts shared services used by multiple regions.
4. Configuration differences between environments must be parameterized; hard-coded environment-specific values are prohibited.

### 8.3 Rollback and backout
1. Each Production pipeline must define a rollback strategy appropriate to the change type:
   - IaC rollback (re-apply last known good state/version)
   - Blue/green or canary rollback (traffic shift back)
   - Snapshot/backup restore (for data-impacting changes)
2. Rollback steps must be tested periodically (at least annually for critical services) and evidenced.

## 9. Secure development and engineering standards
### 9.1 Code quality and review
1. Mandatory PR checks:
   - Linting/format validation
   - Static analysis where available
   - Policy checks (e.g., forbidden configurations)
2. PR review must verify:
   - Least privilege IAM roles/policies
   - Network security posture (segmentation, firewall rules)
   - Logging enabled by default
   - Resource tagging and ownership metadata
3. Merge strategy must preserve traceability (e.g., squash with PR reference or merge commits with PR linkage).

### 9.2 Dependency and module management
1. Third-party modules/providers must be sourced from trusted registries and pinned to approved versions.
2. Module version upgrades must follow change control and include regression testing evidence.
3. Where possible, Norfolk Industries must maintain internal module registries for commonly used patterns to reduce risk and increase consistency.

### 9.3 Secure configuration baselines
1. Platform Owners maintain baseline configurations for their domains (cloud, network, endpoint, identity).
2. IaC modules must implement baseline controls by default and require explicit, reviewed justification for deviations via the exception process.

## 10. Pipeline security and runtime hardening
1. Pipeline identity must use managed identities or federated identity where feasible; long-lived credentials are discouraged and must be justified.
2. Build agents must:
   - Run with least privilege
   - Be isolated from Production networks unless required
   - Be monitored via EDR where applicable
3. Artifact repositories must enforce access control, immutability for releases, and retention aligned to audit requirements.

## 11. Data protection and privacy (GDPR)
1. Automation must respect data minimization:
   - Do not export, replicate, or log personal data unless required for operational purposes.
2. Logs must avoid capturing secrets or unnecessary personal data.
3. If automation processes personal data (e.g., identity attributes), access and processing must be restricted and auditable in alignment with guidance from the Data Protection Officer (DPO).

## 12. Service continuity and resilience (ISO/IEC 22301)
1. Automation supporting backup, restore, or failover must align to documented RTO and RPO requirements for the applicable service.
2. Regional IT Operations must be able to execute approved runbooks for recovery in the event of pipeline platform outages.
3. Critical pipeline components must be resilient (redundant where feasible) and monitored 24×7.

## 13. Incident management and operational response
### 13.1 Automation-related incidents
Incidents include (but are not limited to):
- Unauthorized changes deployed via pipeline
- Secrets exposure in repositories or logs
- Failed Production deployments causing service degradation
- Misconfiguration impacting OT/IT segmentation

All such incidents must be handled through Incident Management and integrated with Security incident response when security impact is suspected.

### 13.2 Evidence capture during incidents
At minimum, responders must preserve:
- Pipeline run identifiers and logs
- Code versions and PR references
- Change record identifiers (if present; if missing, create as part of incident follow-up)
- Identity of initiator and approver
- Affected CIs and scope of change

## 14. Exceptions
1. Exceptions to this policy require documented risk acceptance and approval aligned to the ISMS exception process.
2. High-risk exceptions (e.g., bypassing PR reviews, using long-lived Production credentials, disabling audit logs, modifying OT access controls without CAB review) require approval per the “Exception approval (high risk)” RACI and must include compensating controls and expiration dates.
3. The IT Governance Manager coordinates exception records and ensures evidence is retained.

## 15. Enforcement
Non-compliance may result in:
- Removal of repository or pipeline access
- Forced remediation plans managed by the Head of IT Infrastructure Services
- Audit findings and reporting through governance channels
- Escalation to the CIO and CISO for material risks, including SOX-impacting control breakdowns

## 16. Metrics and reporting
Global IT Operations will report (at minimum) the following metrics to governance stakeholders:
- Percentage of Production deployments with linked change records
- PR review compliance rate (author vs approver separation)
- Number of Emergency Changes related to automation
- Secrets incidents (detections of plaintext secrets, rotations due to exposure)
- Deployment failure rate and mean time to recover for automation-caused incidents
- Drift detection findings and remediation cycle time

## 17. Audit and evidence
### 17.1 Evidence principles
Evidence must be time-bound, attributable, and repeatable. Evidence must include approvals, logs, and validation artifacts where applicable.

### 17.2 Minimum evidence set
For Production-affecting automation:
- Approved change record (or Emergency Change with retrospective CAB review)
- PR with reviewers and approvals
- Pipeline run logs showing commit/release version and outcome
- Test/validation evidence (automated test results, smoke test confirmations)
- Deployment approval evidence (manual gate or CAB approval)
- Rollback plan and, when executed, rollback evidence
- Access reviews and secret rotation records where relevant

## 18. Control mappings (standards alignment)
This section provides conceptual mappings for audit and design assurance.

| Policy control area | ISO/IEC 27001 (Annex A concept) | NIST CSF function | SOC 2 TSC | ITIL 4 practice | COBIT 2019 domain |
|---|---|---|---|---|---|
| Repository access control, branch protection, PR reviews | Access Control, Secure Development | Protect | Security | Information Security Management | APO / DSS |
| Change record linkage, CAB approvals, Standard/Emergency Change governance | Change Management, Operations Security | Protect / Respond | Availability, Security | Change Enablement | BAI / DSS |
| Secret management and rotation | Cryptography, Identity and Access | Protect | Security, Confidentiality | Information Security Management | APO / DSS |
| Pipeline logging, monitoring, SIEM integration | Logging and Monitoring, Operations Security | Detect / Respond | Security, Availability | Monitoring and Event Management | DSS / MEA |
| Environment separation, promotion gates, artifact integrity | Secure Development, System Acquisition | Protect | Security, Processing Integrity | Change Enablement | BAI |
| Rollback, recovery testing, continuity | Business Continuity, Backup | Recover | Availability | Service Continuity Management | DSS |
| OT/IT segmentation change safeguards | Network Security, Access Control | Protect | Security, Availability | Information Security Management | APO / DSS |

## 19. Appendices
### Appendix A: CI/CD Pipeline Compliance Checklist (mandatory)
Use this checklist for new pipelines and major pipeline changes. Retain completed checklists as audit evidence.

| Control area | Requirement | Evidence artifact | Pass/Fail | Notes |
|---|---|---|---|---|
| Source control | Default branch protected; no direct commits | Repo settings export/screenshot; policy config |  |  |
| PR reviews | Non-Prod: ≥1 reviewer; Prod: ≥2 reviewers + independent deploy approver | PR record with approvals |  |  |
| SoD | Deploy approver not the sole author/executor | Pipeline approval log; PR + run identity comparison |  |  |
| Change linkage | Production runs reference ITSM change record | Change record ID in pipeline; ITSM link |  |  |
| Artifact integrity | Build once; immutable artifact promoted | Release record; artifact checksum/signature |  |  |
| Secrets | No plaintext secrets in repo or pipeline; secrets in approved store | Secret scan results; vault reference config |  |  |
| Least privilege | Pipeline identities scoped to minimal permissions | IAM role/policy review record |  |  |
| Logging | Run logs include actor, version, env, result | Pipeline logs; SIEM ingestion proof |  |  |
| Monitoring | Alerts for failed Prod deploys and policy violations | Alert rules; incident tickets |  |  |
| Testing | Automated tests + smoke tests documented | Test reports; run summary |  |  |
| Rollback | Documented rollback steps; verified for critical services | Runbook; test evidence |  |  |
| OT/IT safeguards | OT-impacting changes treated as high risk with CAB oversight | CAB minutes/change approval; validation record |  |  |

### Appendix B: IaC Module Standard Template (required structure)
This template defines the minimum structure and documentation required for reusable IaC modules managed by IT Infrastructure Services.

#### B.1 Module header (README content)
- **Module name**
- **Service Owner**
- **Platform Owner**
- **Purpose and scope**
- **Supported environments** (Dev/Test/Stage/Production)
- **Dependencies** (providers, policies, networking prerequisites)
- **Security posture** (logging defaults, encryption defaults, identity model)
- **Inputs** (table of variables with type, allowed values, sensitivity)
- **Outputs** (table of outputs with descriptions and sensitivity)
- **Resource tagging requirements**
- **Operational notes** (monitoring hooks, backup hooks, SLO impacts)
- **Rollback guidance** (how to revert to prior version/state)

#### B.2 Required repository structure
```text
module-root/
  README.md
  CHANGELOG.md
  /src
  /examples
  /tests
  /policies
```

#### B.3 Required engineering practices
- Versioning scheme must be defined and used consistently (semantic versioning recommended).
- Each module must include:
  - At least one example deployment
  - Automated tests appropriate to the tooling
  - Policy checks to prevent insecure defaults (e.g., public exposure without explicit approval)

### Appendix C: Standard Operating Procedures (SOPs)
These SOPs are mandatory operating patterns for automation managed by IT Infrastructure Services. They may be implemented in tooling-specific formats, but the steps and evidence requirements apply.

#### C.1 SOP — Create new automation (IaC, script, or pipeline)
1. **Initiate work**
   - Confirm Service Owner and Platform Owner.
   - Identify impacted CIs and environments.
2. **Design**
   - Define desired state, rollback strategy, and monitoring requirements.
   - Identify secret dependencies and ensure approved storage integration.
3. **Implement**
   - Use internal modules where available; otherwise create module per Appendix B.
   - Add tagging/metadata enforcement.
4. **Test**
   - Execute automated tests and validate in non-Production.
   - Document results in pipeline logs or test reports.
5. **Security review**
   - Perform peer review; include Security Engineer/IAM Engineer review when scope includes security or identity controls.
6. **Prepare change**
   - For Production impact, create a change record with implementation plan, risks, and rollback steps.
7. **Release**
   - Create versioned artifact/release and ensure promotion path is defined.

**Required evidence**: design notes (tracked in repo), PR approvals, test results, secret store references, change record (if Prod-impacting).

#### C.2 SOP — Code review (pull request)
1. Verify scope aligns to requested change and impacted CIs are identified.
2. Validate:
   - Least privilege IAM
   - Network segmentation and firewall rules
   - Logging/monitoring enabled
   - No secrets in code (run secret scan)
   - Tagging compliance
3. Confirm test coverage and successful pipeline checks.
4. Approve or request changes; approvals must satisfy SoD rules for the target environment.

**Required evidence**: PR review record, automated check results, secret scan output.

#### C.3 SOP — Deploy automation (environment promotion)
1. Confirm approvals:
   - PR merged with required reviewers
   - Change record approved (Normal/Standard) for Production
2. Execute pipeline promotion using the immutable artifact/version.
3. Perform post-deployment validation:
   - Smoke tests
   - Monitoring checks
   - CI verification (resource state matches expected)
4. Update change record with completion notes and evidence links.

**Required evidence**: pipeline run logs, approval gate logs, validation outputs, change record completion.

#### C.4 SOP — Monitor automation and handle failures
1. Monitor pipeline health dashboards and alerting integrations 24×7 as applicable.
2. On failure:
   - Triage scope (which CIs, which environment, what changed)
   - Determine whether rollback is required
3. If rollback needed:
   - Execute documented rollback method
   - Validate restoration and update incident/change records

**Required evidence**: alert notifications, run logs, rollback run evidence, validation records.

#### C.5 SOP — Handle automation-caused incidents
1. Open an incident via the ITSM tool and classify severity.
2. Preserve evidence:
   - Pipeline run IDs, logs, and artifacts
   - Related PRs/commits/releases
   - Identity and approval records
3. If security impact suspected:
   - Engage CISO-aligned security response via Security Engineer coordination
   - Rotate impacted secrets and revoke tokens as needed
4. Remediate:
   - Roll back or patch through controlled pipeline execution
   - Initiate Problem Management for recurring issues
5. Post-incident:
   - Document root cause, corrective actions, and control improvements
   - If Emergency Change was used, ensure retrospective CAB review is completed

**Required evidence**: incident ticket, timeline, containment actions, secret rotation records (if applicable), CAB retrospective approval for Emergency Changes.

### Appendix D: Audit Evidence List (minimum set)
Maintain the following evidence artifacts for audits and internal control validation.

| Evidence item | Description | Owner role | Retention expectation |
|---|---|---|---|
| Repository protection settings | Export or screenshots showing branch protection, required reviewers | Platform Owner | Per ISMS retention schedule; must cover audit period |
| PR records | Approvals, reviewers, checks, linked work items | Service Owner | Per ISMS retention schedule; must cover audit period |
| Pipeline run logs | Actor, commit hash, environment, outcome, timestamps | IT Operations Manager | Per ISMS retention schedule; must cover audit period |
| Change records | Approved change, CAB decisions, implementation results | ITSM Process Owner | Per ITSM/ISMS retention schedule; must cover audit period |
| CAB minutes/approvals | Evidence of CAB review/approval for Normal/Emergency | Head of IT Infrastructure Services | Per governance retention schedule |
| Secret management records | Vault references, rotation logs, access logs | Security Engineer | Per ISMS retention schedule |
| Access reviews | Periodic review of repo and pipeline permissions | IT Governance Manager | Per ISMS retention schedule |
| Drift detection reports | Findings and remediation evidence | Platform Owner | Per ISMS retention schedule |
| Rollback tests | Evidence of rollback procedure validation for critical services | IT Operations Manager | Per BCMS/ISMS retention schedule |
| Monitoring/alert configuration | Alerts for failures and security-relevant events | Security Engineer | Per ISMS retention schedule |

