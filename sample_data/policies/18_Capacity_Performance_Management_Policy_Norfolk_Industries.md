# Capacity & Performance Management Policy (Norfolk Industries)

## 1. Purpose
This policy defines how Norfolk Industries governs, measures, forecasts, and improves capacity and performance for IT Infrastructure Services to ensure reliable 24×7 operations, predictable service outcomes, cost-effective scaling, and risk-managed change. It establishes consistent requirements for baselines, monitoring, forecasting, review cadences, and remediation planning across hybrid cloud (Microsoft Azure primary, AWS secondary) and on-prem data centers, with appropriate considerations for Operational Technology (OT) connectivity and segmentation.

## 2. Scope
### 2.1 In Scope
This policy applies to:
- All services delivered by IT Infrastructure Services, including network, compute, cloud, endpoint, identity, monitoring, and backup platforms.
- All production, disaster recovery, and shared services supporting business-critical operations across North America, Europe, and APAC.
- Capacity and performance telemetry, dashboards, alerts, and reports used by Global IT Operations and Regional IT Operations.
- Capacity-impacting changes governed through Change Enablement and the Change Advisory Board (CAB).
- Dependencies used by IT Infrastructure Services (including managed service providers and cloud service providers) where Norfolk Industries is responsible for outcomes.

### 2.2 Out of Scope
- Application-level performance management owned outside IT Infrastructure Services (unless explicitly designated as a shared responsibility by a Service Owner).
- OT plant control performance engineering inside plant control systems; however, IT/OT connectivity capacity and remote access controls remain in scope.

## 3. Policy Statement
Norfolk Industries shall:
1. Define service-relevant capacity and performance metrics with documented baselines and thresholds.
2. Continuously monitor critical infrastructure components and services, with alerting aligned to Service Level Objectives (SLOs) and risk.
3. Perform routine forecasting using standardized planning horizons and methods to anticipate demand and prevent performance-related incidents.
4. Review capacity monthly, tune thresholds based on observed behavior, and maintain documented remediation plans for identified constraints.
5. Ensure capacity-related changes are assessed for risk, validated, and approved through the Change Advisory Board (CAB) where required.
6. Retain time-bound, attributable, and repeatable evidence of monitoring, reviews, decisions, and remediation actions in alignment with the Information Security Management System (ISMS) and audit requirements (ISO/IEC 27001, SOC 2, SOX, GDPR, NIST concepts).

## 4. Definitions
All defined terms are aligned to the Norfolk Industries glossary:
- **IT Infrastructure Services**: The Norfolk Industries function responsible for network, compute, cloud, endpoint, identity, monitoring, backup, and related infrastructure platforms and operations.
- **Global IT Operations**: Central team providing governance, standards, core platform operations, and global coordination for IT infrastructure.
- **Regional IT Operations**: Regional teams executing day-to-day operations, local support, and implementation aligned to global governance.
- **Information Security Management System (ISMS)**: The governance framework of policies, processes, and controls used by Norfolk Industries to manage information security risk and meet ISO/IEC 27001.
- **Change Advisory Board (CAB)**: The cross-functional governance body responsible for reviewing and approving Normal and Emergency Changes per Change Management.
- **Configuration Item (CI)**: Any component that needs to be managed to deliver an IT service, including hardware, software, cloud resources, and documentation references.
- **Service Level Objective (SLO)**: A target level of service reliability or performance, measured by agreed metrics.
- **Recovery Point Objective (RPO)**: Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO)**: Target time to restore a service after disruption.
- **Operational Technology (OT)** and **Information Technology (IT)**: OT systems monitor/control physical processes; IT systems provide business and enterprise services.

## 5. Roles and Responsibilities
### 5.1 Policy Governance
- **CIO**: Executive owner of IT strategy and governance for Norfolk Industries.
- **Head of IT Infrastructure Services**: Accountable for infrastructure platforms, standards, operations, and service outcomes.
- **CISO**: Accountable for information security program and ISMS oversight.
- **IT Governance Manager**: Owns governance processes, policy lifecycle, compliance tracking, and audit coordination for IT Infrastructure Services.
- **Internal Audit**: Independently assesses control design and operating effectiveness.
- **Data Protection Officer (DPO)**: Oversees privacy governance and GDPR alignment (relevant where performance data includes personal data such as user identifiers).

### 5.2 Operational Ownership
- **Service Owner**: Accountable for end-to-end service performance, roadmap, risk posture, and compliance for a defined infrastructure service.
- **Platform Owner**: Accountable for technical platform architecture and engineering standards for a domain (e.g., network, cloud, endpoint).
- **IT Operations Manager**: Responsible for operational execution, shift/on-call readiness, and incident response coordination.
- Engineering roles (as applicable): **Cloud Engineer**, **Systems Engineer**, **Network Engineer**, **Endpoint Engineer**, **IAM Engineer**, **Security Engineer**.

### 5.3 RACI (Capacity & Performance Management)
RACI is aligned to the Norfolk Industries RACI master and applied to this policy’s key activities.

| Activity | CIO | Head of IT Infrastructure Services | CISO | IT Governance Manager | Service Owner | Platform Owner | IT Operations Manager | ITSM Process Owner | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|
| Policy approval | A | R | C | R | C | C | C | C | I |
| Procedure ownership (capacity review & remediation procedure) | I | A | C | R | R | R | R | C | I |
| Standard approval (metrics, thresholds, dashboards) | I | A | C | R | C | R | C | C | I |
| Audit evidence coordination | I | R | C | R | R | R | C | C | A |

## 6. Policy Requirements
### 6.1 Capacity Planning Horizons
Norfolk Industries shall use the following standardized horizons for capacity planning:

| Horizon | Timeframe | Primary Purpose | Minimum Required Outputs |
|---|---:|---|---|
| Operational | 0–30 days | Prevent immediate performance incidents and SLA/SLO risks | Alert tuning changes, short-term remediation actions, confirmed headroom |
| Tactical | 1–6 months | Align demand with procurement, reserved capacity, and project delivery | Forecast by domain, planned upgrades, cloud commitment adjustments |
| Strategic | 6–24 months | Inform budgeting, architecture roadmaps, and major platform shifts | Multi-region growth assumptions, datacenter lifecycle impacts, cloud strategy impacts |

### 6.2 Baselines and Headroom Targets
1. **Baselines** shall be established per service and domain using a stable observation window (minimum 30 days) and must reflect:
   - Typical business cycles (weekday/weekend; month-end; plant maintenance windows) where applicable.
   - Regional differences (North America, Europe, APAC).
2. **Headroom targets** shall be defined and approved by the Service Owner and Platform Owner, with review by the IT Operations Manager. Minimum targets:
   - Production services: maintain sustained utilization headroom sufficient to absorb normal variability and single-node failure where applicable.
   - Critical shared services (identity, core network, monitoring): define N+1 or equivalent resilience assumptions in the capacity model.
3. **Exception handling**: If headroom targets cannot be met due to constraints, a remediation plan (Section 11) and change plan (Section 12) are required; high-risk exceptions must be escalated consistent with Norfolk Industries governance.

### 6.3 Forecasting Methods
Forecasts shall use at least two of the following methods per domain, selected based on data quality and volatility:
- **Trend-based forecasting**: linear or seasonal trend on utilization and growth (e.g., CPU, storage consumed, bandwidth).
- **Workload-driven forecasting**: forecast based on known drivers such as onboarding volumes, plant deployments, project demand, or MES/SCADA connectivity expansions.
- **Event-based forecasting**: incorporate known peaks (month-end close, patch cycles, planned migrations).
- **Unit economics / cost forecasting (cloud)**: project cost and capacity using tagged consumption, reserved instances/savings plans, and planned architecture changes.

Forecasts must:
- Identify assumptions and data sources.
- Provide projected “time-to-threshold” for key constraints.
- Identify recommended actions (scale up/out, optimize, retire, re-architect).

### 6.4 Monitoring, Alerting, and Thresholds
1. Monitoring shall be implemented for all in-scope services and supporting CIs using approved enterprise tooling (e.g., Microsoft Sentinel for security events; Microsoft Defender for Endpoint for endpoints; infrastructure monitoring appropriate to domain).
2. Thresholds shall be:
   - **Documented** with rationale (baseline, SLO impact).
   - **Tiered** (Warning, Critical) and mapped to response expectations.
   - **Reviewed monthly** and adjusted to reduce noise while preventing missed degradation.
3. Alert routing must support 24×7 operations and follow on-call processes managed by the IT Operations Manager.

### 6.5 Domain Metrics (Minimum Standard Set)
The following minimum metrics must be collected and reviewed. Service Owners may add service-specific indicators.

#### 6.5.1 Compute (On-prem and IaaS)
- CPU utilization (average, p95), CPU ready/steal time (where applicable)
- Memory utilization (average, p95), paging/swapping rates
- Disk IOPS and latency (read/write), queue depth
- Host and cluster contention (oversubscription ratios, failover capacity)
- Virtualization capacity (vCPU:pCPU ratios, memory overcommit policy adherence)
- Service health indicators (availability, error rates) when infrastructure-related

#### 6.5.2 Storage (SAN/NAS/Object/Cloud)
- Capacity used vs provisioned, growth rate (GiB/day, GiB/week)
- Thin provisioning risk indicators (overcommit ratio, reclaim effectiveness)
- Latency and throughput (p95/p99 where available)
- Snapshot/backup capacity consumption impacts
- Data lifecycle indicators (stale volumes, orphaned snapshots)

#### 6.5.3 Network (LAN/WAN/Internet/VPN)
- Bandwidth utilization (average, p95) per link and per site
- Packet loss, jitter, latency (baseline and deviation)
- Interface errors/discards, retransmissions
- Firewall throughput and session counts
- VPN/remote access concurrency and throughput (especially for OT remote access zones)

#### 6.5.4 Cloud Capacity and Cost (Azure primary, AWS secondary)
- Compute scaling indicators (instance/vCPU counts, autoscale events, throttling)
- Storage consumption and transaction metrics (where applicable)
- Network egress/ingress and inter-region traffic
- Service quota utilization and time-to-quota (subscriptions/accounts)
- Cost metrics: daily cost, month-to-date, forecast to month-end, anomaly detection
- Commitment coverage (reserved instances/savings plans) and utilization effectiveness
- Tagging coverage and cost allocation completeness (as a capacity/cost governance control)

## 7. Procedures (Policy-Mandated)
### 7.1 Monthly Capacity Review Procedure
Monthly capacity reviews shall be performed for each major platform and for business-critical services.

**Minimum steps:**
1. **Data capture** (Platform Owner / IT Operations Manager)
   - Export last 30/90 days of key metrics per domain.
   - Capture incident/problem linkage where capacity/performance contributed.
2. **Baseline validation**
   - Confirm baseline still represents “normal” operations.
   - Document any major shifts (deployments, migrations, new sites, OT connectivity changes).
3. **Forecast update**
   - Update time-to-threshold for top constraints.
   - Validate assumptions with Service Owners and Regional IT Operations.
4. **Threshold tuning**
   - Adjust alert thresholds based on observed p95/p99 behavior and incident learnings.
   - Validate that tuning does not mask early warning signals.
5. **Remediation actions**
   - Identify required actions (optimize, scale, retire, re-architect).
   - Assign owners and due dates; determine whether CAB approval is required.
6. **Evidence and publishing**
   - Publish the monthly capacity review report and dashboard snapshots to the approved repository.
   - Record actions as ITSM tasks/changes linked to affected CIs.

### 7.2 Threshold Tuning Procedure
Threshold tuning must follow controlled changes and be evidence-based.

**Rules:**
- Warning thresholds should provide actionable lead time to prevent Critical conditions.
- Critical thresholds must align to operational risk (performance degradation, failover risk, SLO breach risk).
- Changes to thresholds that materially affect alerting coverage are treated as controlled changes and must be recorded in the ITSM tool with linkage to the relevant CI(s).

**Inputs:**
- Baseline (30+ days), p95/p99, incident history, maintenance windows, and known batch cycles.

**Outputs:**
- Updated threshold configuration, validation notes, and post-change monitoring confirmation.

### 7.3 Remediation Plan Procedure
When constraints are identified (or forecasted), a remediation plan is required.

**Plan content (minimum):**
- Constraint description and impacted services/CIs.
- Current utilization and baseline metrics; time-to-threshold.
- Risk statement (availability, performance, security, continuity).
- Options analysis (scale, optimize, configuration change, architectural change).
- Chosen action with cost and timeline.
- Required governance (CAB involvement, maintenance window, testing).
- Validation approach (success metrics and observation period).
- Back-out plan (for change-related remediation).

Remediation plans must be tracked to completion and reviewed at the next monthly capacity review.

## 8. Tooling, Data Quality, and CMDB Linkage
1. Monitoring and capacity data must be attributable and linked to the relevant **Configuration Item (CI)** where feasible.
2. Data quality requirements:
   - Time synchronization and consistent timestamps across regions.
   - Metric retention sufficient for required horizons: at least 90 days for operational/tactical trending; longer retention where needed for strategic planning and audit evidence.
3. Dashboards must define:
   - Metric name, source, aggregation, percentile logic, and thresholds.
   - Ownership (Service Owner / Platform Owner) and review cadence.
4. Capacity data must be protected per the ISMS; access shall be role-based via Active Directory and Entra ID (Azure AD) on first mention, then Entra ID.

## 9. OT/IT Considerations
1. Capacity management for IT services supporting OT connectivity (remote access, VPN, jump hosts, firewalls, segmented plant networks) must account for:
   - Strict remote access controls and segmented network design.
   - Peak access during maintenance windows and incident response scenarios.
2. Performance changes affecting OT-connected zones require risk review and implementation controls to avoid unintended disruption of plant operations.
3. Metrics collected from OT-connected network segments must follow least privilege and monitoring access controls; avoid unnecessary collection of sensitive operational data.

## 10. Service Level Objectives (SLO) Alignment
1. Capacity and performance thresholds must be aligned to SLOs for applicable services (for example: remote access availability, identity authentication responsiveness, network latency targets for core sites).
2. Where performance is a leading indicator for availability, thresholds shall prioritize early detection to prevent SLO breach.
3. SLO reporting must reference capacity trends when degradation risk is increasing.

## 11. Remediation and Continual Improvement
1. Capacity/performance issues that trigger recurring incidents shall be evaluated for **Problem Management** linkage and root cause elimination.
2. Continual improvement actions may include:
   - Rightsizing, auto-scaling adjustments, caching, network path optimization.
   - Retirement of unused resources, storage tiering, quota management.
   - Cloud commitment optimization and tagging enforcement (capacity-to-cost governance).
3. Completed remediation must be validated against defined success metrics and recorded as evidence.

## 12. Change Enablement and CAB Requirements
1. Capacity-affecting changes (scaling, configuration adjustments, network changes, storage expansion, quota changes) must follow ITIL 4 Change Enablement and Norfolk Industries change governance.
2. The **Change Advisory Board (CAB)** must review and approve Normal Changes with material risk to availability, security, compliance, or OT connectivity.
3. Emergency capacity changes must be documented and retrospectively reviewed, including:
   - Reason for emergency classification.
   - Risk acceptance and compensating controls.
   - Post-implementation validation and lessons learned.

## 13. Compliance, Risk, and Audit Evidence
1. This policy is part of the ISMS control environment and supports audit readiness for ISO/IEC 27001, SOC 2, SOX, and GDPR (where applicable).
2. Evidence must follow Norfolk Industries evidence principles:
   - Time-bound, attributable, repeatable.
   - Include approvals, logs, and validation artifacts where applicable.
3. Capacity-related evidence must be retained according to Norfolk Industries records management requirements and be accessible for Internal Audit review.

## 14. Standards and Control Mapping
The control mapping below is conceptual and aligned to required frameworks.

| Policy Control Area | ISO/IEC 27001 (Annex A concept) | NIST CSF | SOC 2 TSC | ITIL 4 Practice | COBIT 2019 Domain | Typical Evidence |
|---|---|---|---|---|---|---|
| Monitoring & thresholding | Logging/monitoring and operational controls | Detect | Security, Availability | Monitoring and Event Management | DSS | Dashboard definitions, alert configs, event samples |
| Capacity planning & forecasting | Operational planning and risk treatment | Identify, Protect | Availability | Service Continuity Management | APO, BAI | Forecast reports, assumptions, approval notes |
| Change control for capacity changes | Change management controls | Protect, Respond | Security, Availability | Change Enablement | BAI | Change records, CAB minutes, implementation validation |
| Continual improvement | Management review and continual improvement | Identify, Recover | Availability | Continual Improvement (via practice integration) | MEA | Post-review action logs, trend improvements |
| Evidence and auditability | Documentation and control evidence | Identify | Security, Availability, Confidentiality, Privacy | Information Security Management | MEA | Evidence register, access logs, report archive |

## 15. Reporting and Communication
1. Monthly capacity review outcomes must be communicated to:
   - Global IT Operations (governance and coordination)
   - Regional IT Operations (execution and site impacts)
   - Service Owners (risk and roadmap implications)
2. Significant risks (e.g., projected threshold breach within tactical horizon for critical services) must be escalated to the Head of IT Infrastructure Services and, where security-relevant, the CISO.
3. Communications must use agreed operational channels and include:
   - What is constrained, when it will breach thresholds, and user/service impact.
   - Proposed remediation and required change windows.

## 16. Training and Awareness
1. Platform Owners and engineers responsible for monitoring and tuning must be trained on:
   - Metric interpretation (percentiles, saturation vs utilization).
   - Forecasting methods used by Norfolk Industries.
   - Change Enablement requirements and CAB expectations.
2. IT Operations staff must be trained to:
   - Recognize capacity-related incident patterns.
   - Execute runbooks for immediate stabilization actions.
3. Training completion records must be available for audit upon request.

## 17. Exceptions
1. Exceptions to this policy must be documented with:
   - Scope of exception (service/CIs/regions)
   - Duration and review date
   - Risk assessment and compensating controls
   - Approval aligned to governance requirements
2. High-risk exceptions must be escalated to appropriate leadership consistent with Norfolk Industries governance and ISMS risk treatment practices.

## 18. Enforcement
1. Non-compliance may result in:
   - Increased incident risk and service disruption
   - Audit findings and compliance exposure (SOC 2, SOX, ISO/IEC 27001)
   - Required corrective action plans owned by the Service Owner and Platform Owner
2. The Head of IT Infrastructure Services is accountable for ensuring remediation of repeated non-compliance; the IT Governance Manager coordinates tracking and evidence for audits.

## 19. Document Control
### 19.1 Ownership
- **Policy Owner:** IT Governance Manager  
- **Executive Sponsor:** Head of IT Infrastructure Services  
- **Security Oversight:** CISO  

### 19.2 Review Cadence
- Reviewed at least annually, and additionally upon significant platform changes (cloud strategy shifts, datacenter changes, monitoring tool changes) or audit findings.

### 19.3 Versioning and Publication
- The controlled version of this policy shall be published in the approved Norfolk Industries policy repository with access controls enforced via Active Directory and Entra ID.
- Superseded versions must be retained per records management requirements.

---

## Appendix A: Capacity Dashboard Definitions (Standard)
This appendix standardizes dashboard definitions to ensure consistent interpretation across Global IT Operations and Regional IT Operations.

### A.1 Dashboard Naming and Ownership
| Dashboard | Owner Role | Review Cadence | Primary Audience |
|---|---|---|---|
| Compute Capacity & Performance | Platform Owner | Monthly (and weekly for critical clusters) | IT Operations Manager, Service Owner |
| Storage Capacity & Performance | Platform Owner | Monthly | Service Owner, Regional IT Operations |
| Network Capacity & Performance | Platform Owner | Monthly (and weekly for critical links) | Network Engineer, IT Operations Manager |
| Cloud Capacity & Cost | Service Owner (cloud service) | Monthly (and weekly for spend controls) | Head of IT Infrastructure Services, Cloud Engineer |
| OT Connectivity Capacity (IT-side) | Platform Owner | Monthly | Global IT Operations, Regional IT Operations |

### A.2 Metric Definition Table (Minimum)
| Domain | Metric | Definition / Calculation | Aggregation | Threshold Approach | Notes |
|---|---|---|---|---|---|
| Compute | CPU utilization | % CPU used per host/VM | avg + p95 | Baseline p95 + safety margin; Critical near saturation | Include CPU ready/steal where applicable |
| Compute | Memory utilization | % RAM used; include swap rate | avg + p95 | Critical when sustained paging impacts performance | Alert on sustained swap activity |
| Compute | Disk latency | Read/write latency (ms) | p95/p99 | Critical when latency risks application timeouts | Tie to storage backend metrics |
| Storage | Capacity used | Used GiB / total GiB | daily trend | Warning at forecasted threshold within horizon; Critical near full | Include snapshot and backup impacts |
| Storage | Growth rate | Delta used per day/week | trend | Use for time-to-threshold | Flag unusual spikes |
| Network | Link utilization | Throughput / link capacity | avg + p95 | Critical when sustained p95 threatens QoS | Include peak windows |
| Network | Latency/jitter/loss | Path health metrics | avg + p95 | Threshold based on site baselines and service needs | Particularly important for remote access |
| Cloud | Quota utilization | Used quota / available quota | daily trend | Warning at 80% with time-to-exhaustion | Includes subscription limits |
| Cloud | Cost forecast | MTD + forecast to month-end | daily | Alert on anomaly vs trend or budget band | Requires tagging/cost allocation discipline |

---

## Appendix B: Monthly Capacity Review Meeting Template (Standard)
### B.1 Meeting Details
| Field | Requirement |
|---|---|
| Meeting Title | Monthly Capacity & Performance Review – IT Infrastructure Services |
| Chair | IT Operations Manager (or delegate) |
| Required Attendees | Service Owner(s), Platform Owner(s), Regional IT Operations representative(s), ITSM Process Owner (as needed) |
| Optional Attendees | Security Engineer (security tooling capacity), CISO delegate (as needed), IT Governance Manager (audit/evidence) |
| Frequency | Monthly |
| Duration | 60–90 minutes |

### B.2 Agenda (Required)
1. Review of prior month actions (status, outcomes, evidence captured)
2. Key incidents/problems with capacity/performance contribution
3. Baseline updates and notable deviations (by region and service)
4. Forecast review (time-to-threshold; assumptions changes)
5. Threshold tuning proposals and approvals
6. Remediation plans (new and ongoing) and required Change Enablement/CAB steps
7. Cloud cost/capacity review (anomalies, commitment coverage, quota risks)
8. OT connectivity capacity considerations (IT-side)
9. Decisions, action items, and due dates

### B.3 Decision and Action Log (To be captured in ITSM)
| Item | Type (Decision/Action/Risk) | Owner Role | Due Date | Linked CI(s) | Linked ITSM Record | Success Metric |
|---|---|---|---|---|---|---|
| Example: Increase core firewall capacity | Action | Platform Owner | Within tactical horizon | Firewall CI(s) | Change record | p95 utilization below target; no packet loss increase |

---

## Appendix C: Evidence List (Capacity & Performance Management)
This evidence list supports ISO/IEC 27001-aligned auditability, SOC 2 readiness, and SOX-relevant operational controls where capacity impacts financial systems availability.

### C.1 Evidence Register (Minimum)
| Evidence Item | Description | Frequency | Owner Role | Storage Location Requirement | Evidence Quality Notes |
|---|---|---|---|---|---|
| Monthly capacity review report | Summary of baselines, forecasts, risks, actions | Monthly | IT Operations Manager | Controlled repository with access control | Must be time-bound and attributable |
| Dashboard snapshots/exports | Key charts showing trends and thresholds | Monthly | Platform Owner | Same as above | Include time range and percentile method |
| Threshold change records | ITSM record(s) for monitoring threshold adjustments | As changes occur | Platform Owner | ITSM tool record | Include rationale and validation notes |
| Remediation plans | Documented constraints and planned actions | As needed | Service Owner | Controlled repository + ITSM linkage | Include time-to-threshold and risk statement |
| Change records & CAB minutes | Approvals for capacity-affecting changes | As needed | ITSM Process Owner / IT Governance Manager | ITSM + CAB record archive | Include implementation validation |
| Post-implementation validation | Evidence that remediation achieved success metrics | Per change | Platform Owner | Change record attachments | Include before/after metrics |
| Cloud cost/capacity reports | Spend forecast, anomaly notes, commitment utilization | Monthly (weekly for critical) | Service Owner | Controlled repository | Must show source data/timeframe |
| Incident/problem linkage | Records demonstrating trend-driven improvements | Monthly | IT Operations Manager | ITSM tool | Reference ticket IDs in reports |

### C.2 Evidence Principles (Mandatory)
Evidence must be:
- **Time-bound** (clear dates and periods)
- **Attributable** (named owner/approver)
- **Repeatable** (same process yields comparable artifacts)
- Inclusive of **approvals, logs, and validation artifacts** where applicable