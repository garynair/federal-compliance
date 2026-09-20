# Federal Compliance

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

A curated list of statutes, regulations, control catalogues, and tooling for **US federal-contracting and federal-agency cybersecurity compliance** — the layered set of obligations that govern any organisation building, hosting, or selling technology to the federal government.

**Scope:** Anything that materially helps a practitioner scope, implement, assess, or authorise against US federal cybersecurity compliance obligations — cloud authorisation programmes, DoD contractor requirements, the federal-agency risk management framework, statutory and contractual baselines, and sector-specific safeguarding rules. NIST CSF, ISO/IEC 27001, and PCI-DSS sit outside this list's scope and are covered by the companion [Security Frameworks](https://github.com/garynair/security-frameworks) list; COBIT, COSO, and SOX/ITGC/ITAC by the companion [IT Audit & Controls](https://github.com/garynair/it-audit-controls) list. One deliberate exception: NIST SP 800-53 and SP 800-37 (the Risk Management Framework control catalogue) *are* covered here, even though NIST CSF is not — see "Why These Frameworks Matter" below for why. ITAR and EAR (export control) are a distinct trade-compliance practice area and are excluded entirely.

**Why now:** Several pillars of this landscape hit hard deadlines in 2026. Cryptographic modules validated only under FIPS 140-2 stop being usable for federal systems after 21 September 2026, forcing a hard cut-over to FIPS 140-3-validated modules. CMMC Level 2 is now a live contract requirement under DFARS 252.204-7021, phasing in through a transition period that runs until 10 November 2028, after which any contract touching FCI or CUI requires it outright. FedRAMP's modernisation effort, FedRAMP 20x, is in Phase 3 as of 2026, with Class A/B/C submission tracks live and a public submission pipeline opening in FY26 Q4 — a materially different authorisation model from the legacy Rev5 process. StateRAMP itself has rebranded to GovRAMP, broadening its remit beyond state and local government. And NIST finalised Revision 3 of both SP 800-171 and its companion assessment-procedures publication SP 800-171A in May 2024, meaning any programme still built around Revision 2 is already out of date. Executive Order 14028 itself remains in force and un-rescinded, but it has been amended twice since: EO 14144 (January 2025) expanded it with software-attestation and post-quantum requirements, then EO 14306 (June 2025) pruned back several of those additions while explicitly preserving the NIST SP 800-218 secure-software-development thread and adding new AI-security and post-quantum deadlines — the zero-trust and SBOM expectations under OMB M-22-09 continue to apply unchanged.

Contributions welcome.

---

## Contents

- [Why These Frameworks Matter](#why-these-frameworks-matter)
- [How to Approach Implementation](#how-to-approach-implementation)
- [FedRAMP](#fedramp)
- [CMMC](#cmmc)
- [NIST SP 800-171](#nist-sp-800-171)
- [NIST SP 800-53 and SP 800-37 (Risk Management Framework)](#nist-sp-800-53-and-sp-800-37-risk-management-framework)
- [FISMA](#fisma)
- [DFARS 252.204-7012](#dfars-252204-7012)
- [FAR 52.204-21](#far-52204-21)
- [StateRAMP](#stateramp)
- [CJIS Security Policy](#cjis-security-policy)
- [IRS Publication 1075](#irs-publication-1075)
- [FIPS 140-2/140-3](#fips-140-2140-3)
- [Executive Order 14028](#executive-order-14028)
- [Privacy Act of 1974](#privacy-act-of-1974)
- [CUI Registry (NARA)](#cui-registry-nara)
- [DoD Cloud Computing SRG and Impact Levels](#dod-cloud-computing-srg-and-impact-levels)
- [Cross-Framework Mapping and GRC Platforms](#cross-framework-mapping-and-grc-platforms)
- [Assessment, Audit, and Risk Analysis Resources](#assessment-audit-and-risk-analysis-resources)
- [Certifications and Training](#certifications-and-training)
- [Government and Standards Bodies](#government-and-standards-bodies)
- [Learning Resources](#learning-resources)
- [Related Lists](#related-lists)

---

## Why These Frameworks Matter

Federal cybersecurity compliance is layered, not singular: a statute sets the obligation, a control catalogue and process define what "secure" means, a contract clause makes it enforceable, a certification or authorisation programme proves it, and a handful of sector-specific rules bolt on extra requirements for particularly sensitive data. FISMA is the statute: it obligates federal agencies (and by extension their contractors and cloud providers) to run an information-security programme at all. NIST SP 800-53 and SP 800-37 are the control catalogue and process: 800-53 lists the actual security and privacy controls, and 800-37 (the Risk Management Framework, or RMF) defines the seven-step lifecycle — Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor — that agencies and cloud providers run those controls through to get an Authority to Operate. FAR 52.204-21 and DFARS 252.204-7012 are the contract clauses: the FAR clause is the "basic safeguarding" floor that applies to nearly every federal contractor, and the DFARS clause is DoD's much heavier requirement, mandating NIST SP 800-171 and 72-hour cyber incident reporting for anyone handling covered defense information. FedRAMP, CMMC, and StateRAMP/GovRAMP are the certification and authorisation programmes: they are how a cloud service provider or defense contractor proves, to an agency or a prime, that the underlying control set is actually implemented. And CJIS Security Policy and IRS Publication 1075 are sector-specific overlays: they exist because criminal justice information and federal tax information carry safeguarding requirements beyond the general federal baseline.

This is also why NIST SP 800-53 and SP 800-37 sit in this list rather than in the companion [Security Frameworks](https://github.com/garynair/security-frameworks) list alongside NIST CSF. CSF is a voluntary, sector-agnostic, outcome-based framework any organisation can adopt to organise a security programme. SP 800-53 and SP 800-37 are not voluntary in the federal context: they are the specific, mandatory control catalogue and authorisation process that FISMA obligates federal agencies to run, and that FedRAMP and CMMC Level 3 build directly on top of. A commercial company benchmarking itself against CSF and a cloud provider pursuing a FedRAMP Authorization are doing two genuinely different things, even though both frameworks originate from NIST.

In practice, most federal-compliance programmes work outward from the contract: identify which clause applies (FAR-only, or DFARS-plus-CUI), determine the resulting control baseline (800-171 for CUI on non-federal systems, a FedRAMP or RMF baseline for a system an agency itself operates or authorises), and then choose the certification path — a FedRAMP or CMMC C3PAO assessment — that proves it to the customer.

---

## How to Approach Implementation

1. **Identify your contractual triggers.** Determine which clauses are in your contracts: FAR 52.204-21 alone (Federal Contract Information only), or DFARS 252.204-7012/252.204-7021 (Covered Defense Information or CUI, triggering NIST SP 800-171 and eventually CMMC).
2. **Determine whether you are a cloud service provider to a federal agency.** If so, FedRAMP (or StateRAMP/GovRAMP for state and local government customers) governs your authorisation path, not just your control baseline.
3. **Classify your information.** Work out whether you handle Federal Contract Information (FCI), Controlled Unclassified Information (CUI), or neither — check the specific category against the NARA CUI Registry, since the category drives which safeguarding rule (800-171, CJIS, IRS 1075) actually applies.
4. **Select the right control baseline.** Non-federal systems handling CUI implement NIST SP 800-171; a cloud system an agency will authorise runs the full NIST SP 800-53 catalogue at a FedRAMP or agency-selected baseline (Low, Moderate, or High) via the SP 800-37 RMF process.
5. **Build the System Security Plan (SSP) first.** Every path below — FedRAMP, CMMC, RMF — starts with a written SSP documenting your architecture, data flows, and control implementation; treat it as the anchor document, not a deliverable you write after the fact.
6. **Run a readiness or gap assessment before the formal one.** Use SP 800-171A's assessment procedures for a self-assessment, or engage a 3PAO/C3PAO for a formal Readiness Assessment Report ahead of the real authorisation or certification assessment.
7. **Choose your assessment path.** FedRAMP requires a 3PAO-led Security Assessment and agency or JAB sponsorship; CMMC Level 2 requires a C3PAO-led assessment (or, for some contracts, self-assessment); DoD systems more broadly run the full RMF process, documented in eMASS.
8. **Build incident-reporting procedures to the applicable timelines.** DFARS 252.204-7012 requires DoD cyber incident reporting within 72 hours; agency-hosted systems have their own FISMA-driven incident reporting obligations to CISA and OMB.
9. **Layer on sector-specific rules where applicable.** State and local law enforcement systems touching criminal justice information need the CJIS Security Policy; any system receiving Federal Tax Information needs IRS Publication 1075, independent of any FedRAMP or CMMC work already done.
10. **Monitor continuously and expect the deadlines to move.** FIPS 140-2 module validity, CMMC's phased DFARS rollout, and FedRAMP 20x's own transition are all live, dated processes — track the primary sources directly rather than relying on a point-in-time summary, including this one.

---

## FedRAMP

**Path to adoption:** mandatory for cloud service providers hosting federal agency data; authorised (not certified) through a Third Party Assessment Organization (3PAO) assessment and agency or Joint Authorization Board sponsorship.

- [FedRAMP 20x](https://www.fedramp.gov/20x) - GSA's modernisation initiative redesigning cloud authorisation around continuous, automation-based validation rather than point-in-time paperwork; in Phase 3 as of 2026, with Class A/B/C submission tracks live.
- [FedRAMP.gov](https://www.fedramp.gov/) - The official hub for the Federal Risk and Authorization Management Program, run by GSA's FedRAMP Program Management Office, covering rules, baselines, and the authorisation process.
- [FedRAMP Marketplace](https://www.fedramp.gov/marketplace) - The searchable directory of FedRAMP-authorised cloud service offerings, sponsoring agencies, and recognised 3PAOs, the first stop for confirming a vendor's authorisation status.
- [FedRAMP System Security Plan (SSP) Template](https://www.fedramp.gov/resources/documents/rev4/REV_4_FedRAMP-SSP-Moderate-Baseline-Template.docx) - GSA's official Moderate-baseline SSP template, the mandatory starting document every cloud service provider completes to enter the authorisation process.

## CMMC

**Path to adoption:** certifiable via a C3PAO assessment for Level 2; Level 1 is self-assessed and Level 3 is government-led; mandatory under DFARS 252.204-7021, phasing in through 10 November 2028.

- [32 CFR Part 170 (CMMC Program Final Rule)](https://www.govinfo.gov/content/pkg/FR-2024-10-15/pdf/2024-22905.pdf) - The Federal Register publication of the CMMC 2.0 final rule, establishing the three-level certification programme and its assessment requirements.
- [Cyber AB](https://cyberab.org/) - The Cybersecurity Maturity Model Certification Accreditation Body, DoD's sole authorised non-governmental partner for accrediting C3PAOs and certifying assessors.
- [Cyber AB Marketplace](https://cyberab.org/Catalog) - The authoritative public directory of every accredited C3PAO, Certified CMMC Assessor, and Registered Practitioner Organisation in the CMMC ecosystem.
- [DFARS Subpart 204.75 (Cybersecurity Maturity Model Certification)](https://www.acquisition.gov/dfars/subpart-204.75-cybersecurity-maturity-model-certification) - The DFARS subpart requiring CMMC level requirements in DoD solicitations and contracts, with the transition period running until 10 November 2028.
- [DoD CMMC Program Page](https://dodcio.defense.gov/CMMC/) - The DoD CIO's official CMMC hub, covering programme documentation, model updates, and assessment guidance for the defense industrial base.

## NIST SP 800-171

**Path to adoption:** mandatory for any non-federal system processing, storing, or transmitting CUI on a DoD (or other federal) contract; self-assessed or C3PAO-assessed depending on CMMC level.

- [NIST SP 800-171 Revision 3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) - "Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations," finalised May 2024, the current control set non-federal systems must implement to handle CUI.
- [NIST SP 800-171A Revision 3](https://csrc.nist.gov/pubs/sp/800/171/a/r3/final) - The companion assessment-procedures publication, finalised May 2024, defining the Examine/Interview/Test methodology assessors and self-assessors use to verify each 800-171 requirement.
- [Supplier Performance Risk System (SPRS)](https://www.sprs.csd.disa.mil/) - The DoD system of record where contractors post NIST SP 800-171 self-assessment scores and CMMC status, a public prerequisite for contract award.

## NIST SP 800-53 and SP 800-37 (Risk Management Framework)

**Path to adoption:** mandatory for federal information systems and their authorising cloud providers; implemented through the RMF's seven-step lifecycle rather than a standalone certification.

- [NIST SP 800-37 Revision 2](https://csrc.nist.gov/pubs/sp/800/37/r2/final) - "Risk Management Framework for Information Systems and Organizations," finalised December 2018, defining the Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor lifecycle that federal agencies and FedRAMP both run on.
- [NIST SP 800-53 Revision 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) - "Security and Privacy Controls for Information Systems and Organizations," the federal-agency control catalogue underlying FedRAMP baselines, DoD RMF, and CMMC Level 3; most recently updated in Release 5.2.0, August 2025.
- [NIST SP 800-53 Control Catalogue and OSCAL Releases](https://csrc.nist.gov/projects/risk-management/sp800-53-controls) - NIST's searchable, machine-readable release of every 800-53 control, baseline, and overlay in XML, CSV, PDF, and OSCAL formats.

## FISMA

**Path to adoption:** mandatory statutory obligation for federal agencies; extends contractually to contractors and cloud providers operating federal systems. Not certifiable.

- [44 U.S.C. Chapter 35, Subchapter II (FISMA)](https://www.govinfo.gov/content/pkg/USCODE-2023-title44/html/USCODE-2023-title44-chap35-subchapII.htm) - The current codified text of the Federal Information Security Modernization Act of 2014, establishing federal agency information-security obligations and OMB/CISA oversight roles.
- [CISA: Federal Information Security Modernization Act](https://www.cisa.gov/topics/cyber-threats-and-advisories/federal-information-security-modernization-act) - CISA's practitioner hub for FISMA, including annual CIO and Inspector General reporting metrics back to FY2014.
- [OMB M-25-04: FY 2025 FISMA Guidance](https://bidenwhitehouse.archives.gov/wp-content/uploads/2025/01/M-25-04-Fiscal-Year-2025-Guidance-on-Federal-Information-Security-and-Privacy-Management-Requirements.pdf) - The most recent published annual OMB memorandum setting FISMA reporting requirements and metrics for agency CIOs, CISOs, and Inspectors General.

## DFARS 252.204-7012

**Path to adoption:** mandatory contract clause for DoD contractors handling covered defense information; enforced through contract compliance rather than independent certification.

- [DFARS 252.204-7008 (Compliance with Safeguarding Covered Defense Information Controls)](https://www.acquisition.gov/dfars/252.204-7008-compliance-safeguarding-covered-defense-information-controls.) - The companion solicitation-stage clause requiring offerors to represent their NIST SP 800-171 implementation status, or document an approved variance, before contract award.
- [DFARS 252.204-7012 (Official Text)](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) - The clause requiring DoD contractors to implement NIST SP 800-171 and report cyber incidents affecting covered defense information within 72 hours.

## FAR 52.204-21

**Path to adoption:** mandatory basic-safeguarding clause for nearly all federal contractors whose systems touch Federal Contract Information; one tier below the DFARS requirement, with no independent certification.

- [FAR 52.204-21 (Official Text)](https://www.acquisition.gov/far/52.204-21) - "Basic Safeguarding of Covered Contractor Information Systems," the 15-control minimum-security clause that applies to nearly every federal contract, regardless of agency.
- [eCFR: 48 CFR 52.204-21](https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/section-52.204-21) - The Electronic Code of Federal Regulations' current, consolidated rendering of the clause, useful for citing the regulation itself rather than the acquisition.gov summary page.

## StateRAMP

**Path to adoption:** authorised through the same 3PAO-assessment model as FedRAMP, but sponsored by state, local, or education government customers rather than federal agencies; the programme rebranded to GovRAMP in 2025/2026.

- [GovRAMP (formerly StateRAMP)](https://govramp.org/) - The state, local, and education government equivalent of FedRAMP, using a NIST-aligned authorisation framework so a single assessment can satisfy multiple government customers; stateramp.org now redirects here following the organisation's rebrand.
- [GovRAMP Product List](https://govramp.org/product-list/) - The public, continuously updated directory of cloud products and their verification status (Core, Ready, Provisionally Authorized, Authorized), the equivalent of the FedRAMP Marketplace for state and local government buyers.
- [GovRAMP Security Program](https://govramp.org/security-program) - Details the tiered verification framework (Security Snapshot, Core, Ready, Authorized/Provisional) built on NIST SP 800-53 Revision 5, showing practitioners exactly which controls apply at each tier.

## CJIS Security Policy

**Path to adoption:** mandatory for any agency, contractor, or vendor with access to criminal justice information; enforced through state CJIS Systems Officers rather than a single national certification body.

- [FBI Criminal Justice Information Services (CJIS) Division](https://www.fbi.gov/services/cjis) - The FBI division that owns the CJIS Security Policy and the criminal justice information systems (NCIC, III, and others) it protects.
- [CJIS Security Policy v6.1](https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625.pdf) - The current version of the policy, dated 25 June 2026, defining the 13 security policy areas covering everything from encryption to personnel screening for criminal justice information access.

## IRS Publication 1075

**Path to adoption:** mandatory for federal, state, and local agencies (and their contractors) receiving Federal Tax Information; verified through IRS Safeguards Program reviews rather than third-party certification.

- [IRS Publication 1075](https://www.irs.gov/pub/irs-pdf/p1075.pdf) - "Tax Information Security Guidelines for Federal, State and Local Agencies," the IRS's mandatory safeguarding standard for any recipient of Federal Tax Information, covering access control, incident response, and audit logging.
- [IRS Safeguards Program](https://www.irs.gov/privacy-disclosure/safeguards-program) - The IRS office that reviews agency compliance with Publication 1075, including the Safeguard Security Report and on-site review process every recipient agency goes through.

## FIPS 140-2/140-3

**Path to adoption:** mandatory cryptographic-module validation for any federal system using cryptography to protect information; validated through NIST and CCCS's joint Cryptographic Module Validation Program.

- [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) - "Security Requirements for Cryptographic Modules," published March 2019 and now the sole standard for new module validation; FIPS 140-2 testing ended in 2022 and existing FIPS 140-2 validated modules stop being usable for federal systems on 21 September 2026.
- [FIPS 140-2 (Historical)](https://csrc.nist.gov/pubs/fips/140-2/upd2/final) - The predecessor standard, retained here because a large installed base of currently deployed validated modules still cites it; superseded by FIPS 140-3 and listed for historical reference only.
- [NIST Cryptographic Module Validation Program (CMVP)](https://csrc.nist.gov/projects/cryptographic-module-validation-program) - The joint NIST/Canadian Centre for Cyber Security programme that validates cryptographic modules against FIPS 140-3, the definitive source for checking whether a specific module is currently validated.

## Executive Order 14028

**Path to adoption:** binds federal agencies and their software/service suppliers directly; not independently certifiable, but drives specific, dated procurement requirements (SBOMs, zero trust architecture) that flow into agency contracts. Remains in force and un-rescinded as of 2026, though amended by EO 14144 (January 2025) and then EO 14306 (June 2025); the zero-trust and SBOM mandates below continue to apply unchanged.

- [CISA Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom) - CISA's hub for SBOM minimum elements and the Vulnerability Exploitability eXchange (VEX) format that operationalise the order's software-transparency mandate, the current reference for what a compliant SBOM must contain.
- [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model) - CISA's implementation guidance for the order's zero-trust mandate, defining the maturity stages (Traditional, Initial, Advanced, Optimal) agencies and their contractors are assessed against, aligned to OMB M-22-09.
- [Executive Order 14028: Improving the Nation's Cybersecurity](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) - The official Federal Register text (86 FR 26633, signed 12 May 2021) mandating Zero Trust Architecture adoption, Software Bill of Materials (SBOM) requirements for software vendors, and standardised federal incident response, still the baseline driving current federal procurement security requirements.
- [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/Projects/ssdf) - NIST's secure-software-development practice framework, published with an explicit mapping from each EO 14028 Section 4(e) clause to its corresponding SSDF practice, the document software suppliers use to structure their required self-attestation.

## Privacy Act of 1974

**Path to adoption:** mandatory statutory obligation for federal agencies maintaining systems of records on individuals; enforced through Federal Register notice requirements and individual civil remedies rather than certification.

- [5 U.S.C. § 552a (Privacy Act of 1974)](https://www.govinfo.gov/content/pkg/USCODE-2023-title5/html/USCODE-2023-title5-partI-chap5-subchapII-sec552a.htm) - The current codified text establishing federal agencies' obligations to limit collection, secure, and grant individual access to personally identifiable records.
- [DOJ Overview of the Privacy Act of 1974 (2020 Edition)](https://www.justice.gov/opcl/overview-privacy-act-1974-2020-edition) - The Department of Justice's authoritative case-law analysis of the Act's provisions, the standard reference for how courts have actually interpreted its disclosure and access requirements.

## CUI Registry (NARA)

**Path to adoption:** not independently adopted; it is the definitional foundation that NIST SP 800-171, CMMC, DFARS, and agency-specific CUI programmes all point to when identifying what counts as protected information.

- [NARA Controlled Unclassified Information (CUI) Program](https://www.archives.gov/cui) - The National Archives' hub for the CUI Program, established under Executive Order 13556, standardising how the executive branch handles unclassified information requiring safeguarding.
- [CUI Registry](https://www.archives.gov/cui/registry/category-list.html) - The government-wide, authoritative list of every CUI category and subcategory, the document that defines exactly what NIST SP 800-171 and CMMC exist to protect.
- [DoD CUI Program](https://www.dodcui.mil/) - DoD's own implementation of the CUI Program, translating NARA's government-wide registry into DoD-specific marking, handling, and training requirements referenced throughout the DFARS and CMMC ecosystem.

## DoD Cloud Computing SRG and Impact Levels

**Path to adoption:** mandatory for cloud services hosting DoD data above a FedRAMP Moderate baseline; authorised through DISA's Provisional Authorization process layered on top of an existing FedRAMP authorisation.

- [DoD Cloud Computing Security Requirements Guide (SRG)](https://dl.dod.cyber.mil/wp-content/uploads/cloud/) - DISA's guide defining the Impact Levels (IL2, IL4, IL5, IL6) that tier cloud authorisation above baseline FedRAMP according to the sensitivity of the DoD information being hosted, from public-releasable data (IL2) up to National Security Systems (IL6).
- [DoD CIO: Cloud Computing](https://dodcio.defense.gov/) - The DoD CIO hub covering cloud computing policy, including the guidance memoranda the Cloud Computing SRG itself is built on.

---

## Cross-Framework Mapping and GRC Platforms

- [Coalfire Federal](https://coalfirefederal.com/) - Commercial assessment and advisory firm, one of the first Cyber AB-authorised C3PAOs and also the largest FedRAMP 3PAO by market share, covering CMMC, FedRAMP, and FISMA assessments.
- [Drata](https://drata.com/frameworks/fedramp) - Commercial compliance-automation platform with named FedRAMP and CMMC modules, mapping NIST SP 800-53/800-171 controls to continuous evidence collection; one of the first platforms to earn a FedRAMP 20x Low Pilot Authorization.
- [Exostar](https://www.exostar.com/solutions/cmmc-compliance/) - Commercial supply-chain collaboration and compliance platform built specifically for the defense industrial base, with a named CMMC Ready Suite covering guided self-assessment, CUI storage, and SSP/POA&M automation.
- [Secure Controls Framework (SCF)](https://securecontrolsframework.com/) - Free, open (Creative Commons) meta-framework mapping outward to 250+ laws, regulations, and frameworks, including explicit NIST SP 800-53 and CMMC mappings. Shared with the companion [Security Frameworks](https://github.com/garynair/security-frameworks) and [IT Audit & Controls](https://github.com/garynair/it-audit-controls) lists.
- [Telos Xacta](https://www.telos.com/offerings/xacta/) - Commercial cyber GRC platform, FedRAMP High and StateRAMP High authorised itself, with native eMASS interoperability used widely across federal agencies including DHS, the FBI, and the State Department for RMF package management.
- [Vanta](https://www.vanta.com/products/cmmc) - Commercial compliance-automation platform with a named CMMC product covering pre-mapped NIST SP 800-171/172 controls, continuous control monitoring, and guided evidence collection for Levels 1 through 3.

## Assessment, Audit, and Risk Analysis Resources

- [Cyber AB CMMC Assessment Process](https://cyberab.org/CMMC-Ecosystem/Ecosystem-roles/Assessing-and-Certification) - The Cyber AB's official description of the CMMC assessment and certification pathway, covering CCP, CCA, Lead CCA roles and C3PAO organisational authorisation.
- [eMASS (Enterprise Mission Assurance Support Service)](https://www.dcsa.mil/Systems-Applications/Enterprise-Mission-Assurance-Support-Service-eMASS/) - DoD's government off-the-shelf RMF system of record, used to build, review, and approve Authorization to Operate packages across more than 40 federal mission partners.
- [FedRAMP 3PAO Readiness Assessment Report Guide](https://www.fedramp.gov/resources/documents/3PAO_Readiness_Assessment_Report_Guide.pdf) - GSA's official guide for 3PAOs conducting a Readiness Assessment, the formal pre-authorisation evaluation of whether a cloud service provider's environment can meet FedRAMP requirements.
- [NIST SP 800-171A Assessment Procedures](https://csrc.nist.gov/pubs/sp/800/171/a/r3/final) - The Examine/Interview/Test assessment methodology organisations use to self-assess or third-party assess NIST SP 800-171 implementation, organised into 14 control families.

## Certifications and Training

- [(ISC)² Certified in Governance, Risk and Compliance (CGRC)](https://www.isc2.org/certifications/cap) - Formerly the Certified Authorization Professional (CAP); ISC2 renamed the credential to CGRC, but its seven domains still track the RMF's Categorize-through-Monitor lifecycle, and it remains widely held by RMF authorising officials, ISSOs, and security control assessors.
- [Cyber AB Certified CMMC Assessor (CCA)](https://cyberab.org/CMMC-Ecosystem/Ecosystem-roles/Assessors-detail) - The credential required to serve on a C3PAO assessment team conducting official CMMC Level 2 certification assessments; requires an active CCP plus at least five years of cybersecurity experience.
- [Cyber AB Certified CMMC Professional (CCP)](https://cyberab.org/CMMC-Ecosystem/Ecosystem-roles/Assessors-detail) - The foundational Cyber AB credential for anyone working within the CMMC ecosystem, and the required first step toward the CCA assessor credential.
- [DAU (Defense Acquisition University) Cybersecurity Training](https://media.dau.edu/channel/CyberSecurity/62925431) - Free courses for federal employees, defense contractors, and other federal agency staff covering DFARS 252.204-7012, CMMC, and RMF, available at no cost on a space-available basis.
- [NICCS Education and Training Catalog](https://niccs.cisa.gov/) - CISA's National Initiative for Cybersecurity Careers and Studies catalog, indexing federal-compliance-relevant courses (including CMMC and RMF training providers) alongside broader cybersecurity career pathways.

## Government and Standards Bodies

- [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/) - The DHS component responsible for federal civilian cybersecurity coordination, FISMA metrics, and zero-trust implementation guidance under Executive Order 14028.
- [Cyber AB](https://cyberab.org/) - The nonprofit accreditation body and DoD's sole authorised non-governmental partner for the CMMC ecosystem; not a government body itself, but central to how CMMC is actually administered.
- [DoD Chief Information Officer (DoD CIO)](https://dodcio.defense.gov/) - The Department of Defense office responsible for CMMC, DoD cloud computing policy, and the DoD-specific implementation of the Risk Management Framework.
- [FBI Criminal Justice Information Services (CJIS) Division](https://www.fbi.gov/services/cjis) - The FBI division that owns and maintains the CJIS Security Policy governing criminal justice information systems nationwide.
- [GSA FedRAMP Program Management Office](https://www.fedramp.gov/) - The General Services Administration office that runs FedRAMP, including the Marketplace, baselines, and the FedRAMP 20x modernisation initiative.
- [Internal Revenue Service (IRS)](https://www.irs.gov/) - The federal agency that owns IRS Publication 1075 and runs the Safeguards Program reviewing agency handling of Federal Tax Information.
- [National Archives and Records Administration (NARA)](https://www.archives.gov/cui) - The Executive Agent for the CUI Program government-wide, maintaining the CUI Registry that defines what SP 800-171 and CMMC protect.
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/) - The agency that publishes the SP 800-53, SP 800-37, SP 800-171, and FIPS 140 series underlying nearly every framework in this list.
- [Office of Management and Budget (OMB)](https://www.whitehouse.gov/omb/) - The Executive Office of the President component responsible for FISMA oversight and annual federal information-security and privacy guidance memoranda.

## Learning Resources

- [DoD Cyber Exchange Public](https://public.cyber.mil/) - DISA's public-facing training and guidance hub, including the mandatory Cyber Awareness Challenge and CUI-handling training referenced throughout DFARS and CMMC guidance.
- [FedRAMP.gov Documents and Templates](https://www.fedramp.gov/) - GSA's central library of FedRAMP templates, training recordings, and guidance documents, the practical starting point for any CSP beginning the authorisation process.
- [NIST Computer Security Resource Center (CSRC)](https://csrc.nist.gov/) - NIST's hub for every publication referenced in this list — SP 800-53, SP 800-37, SP 800-171, SP 800-171A, and the FIPS 140 series — plus draft publications open for public comment.

---

## Related Lists

- [Healthcare Compliance](https://github.com/garynair/healthcare-compliance) - A companion curated list covering HIPAA, HITECH, and HITRUST CSF, the healthcare-sector equivalent of this list.
- [Security Frameworks](https://github.com/garynair/security-frameworks) - A companion curated list covering NIST CSF, ISO/IEC 27001, and PCI-DSS — the source for the general-purpose frameworks this list deliberately excludes.
- [IT Audit & Controls](https://github.com/garynair/it-audit-controls) - A companion curated list covering COBIT, COSO, and ITGC/ITAC — the source for anything SOX-, ITGC-, or COBIT-related that is out of scope here.
- [FinServ Compliance](https://github.com/garynair/finserv-compliance) - A companion curated list covering GLBA/FFIEC, NYDFS 500, SEC/FINRA, BSA/AML/OFAC, and the prudential-regulator examination framework for financial services.

---

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the criteria a new entry must meet.

## Licence

This list is published under [CC0 1.0 Universal](LICENSE). The linked resources retain their own licences.
