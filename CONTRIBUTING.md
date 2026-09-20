# Contributing

Thank you for considering a contribution. This list covers **US federal-contracting and federal-agency cybersecurity compliance**: cloud authorization (FedRAMP, GovRAMP), the DoD contractor certification stack (CMMC, NIST SP 800-171/171A, DFARS 252.204-7012), the federal-agency control catalogue and risk process (NIST SP 800-53, SP 800-37/RMF), agency-level statute (FISMA), the general-contractor baseline (FAR 52.204-21), sector-specific safeguarding rules (CJIS Security Policy, IRS Publication 1075), cryptographic validation (FIPS 140-2/140-3), the zero-trust/SBOM mandate (Executive Order 14028), foundational federal PII obligations (Privacy Act of 1974), the CUI Registry, and DoD cloud impact levels (the SRG).

## What belongs here

- Official regulations, statutes, executive orders, and their supporting guidance documents.
- Implementation guidance: control catalogues, assessment procedures, SSP/readiness-assessment templates, authorization and accreditation processes.
- Commercial GRC and compliance-automation platforms with a mature, named feature set for federal compliance (FedRAMP, CMMC, NIST 800-171/800-53, or eMASS-adjacent RMF workflows).
- Certification and training paths specific to federal compliance, RMF, or CMMC assessment practice.
- Government and standards bodies that own or maintain the frameworks above.

## What does not belong here

- Generic federal IT or federal acquisition content with no cybersecurity compliance angle.
- Frameworks outside this list's current scope. NIST CSF, ISO/IEC 27001, and PCI-DSS are covered by the [Security Frameworks](https://github.com/garynair/security-frameworks) companion list; COBIT, COSO, and SOX/ITGC/ITAC by the [IT Audit & Controls](https://github.com/garynair/it-audit-controls) companion list. NIST SP 800-53 and SP 800-37 **are** in scope here even though NIST CSF is not: 800-53 and 800-37 are federal-agency-specific control catalogues that FedRAMP, FISMA, and CMMC build directly on, distinct from the general-purpose, sector-agnostic NIST CSF that the Security Frameworks list covers. If in doubt, check the companion lists before submitting here.
- ITAR/EAR (export control). This is a distinct trade-compliance practice area, not a cybersecurity compliance one, and is out of scope for this list entirely — it is not covered by any companion list either.
- Vendor marketing content without a substantive free tier, open-source component, or named feature.
- Self-promotion of products you have not used or do not work with.

## How to submit

1. Open an issue titled `[Submission]: Resource Name`, or open a PR directly.
2. Add the entry in alphabetical order within the relevant section, in the format: `- [Name](URL) - one sentence on what it is, one sentence on why a practitioner would care.`
3. No marketing language, no unverified performance claims.
4. If you are the author or maintainer of the resource, disclose that in the issue or PR description.

## Style

- British English in the description copy.
- No emojis.
- Avoid banned vocabulary (delve, leverage, harness, robust, seamless, holistic, transformative, paradigm). Plain language wins.
- Flag superseded, sunset, or retired guidance and programmes explicitly (as this list does for FIPS 140-2's transition to 140-3) rather than presenting them as current.

## Quality bar

- Must be publicly accessible (official government source, free tier, or open-source), or a mature commercial platform with a named feature set.
- Must be actively maintained (commit or update within 12 months, or a standards/regulatory body with an active update cycle).
- Description must be factual, and every URL must resolve to the resource it claims to describe. Do not submit a link you have not verified.

## Review

A maintainer reviews PRs within seven days. Most PRs that meet the criteria above land within two weeks.

## Licence

By contributing you agree your contribution is released under CC0 1.0 Universal.
