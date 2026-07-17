---
title: "Interim Findings: How Well Does Federal Guidance Cover the OWASP CI/CD Top 10?"
date: 2026-07-17
draft: false
tags: ["DevSecOps", "CI/CD Security", "NIST", "OWASP", "Research", "Supply Chain Security"]
description: "700 mapping cells later: interim results from my SANS research mapping federal cybersecurity guidance against the OWASP Top 10 CI/CD Security Risks, and the four gap areas every pipeline owner should check."
---

# Interim Findings: How Well Does Federal Guidance Cover the OWASP CI/CD Top 10?

Last month I [introduced my SANS research project](/blog/cicd-security-research-whitepaper/): a structured mapping of federal cybersecurity guidance against the risks that actually show up in CI/CD pipelines. The control-extraction and mapping phase is now done, and the interim numbers are worth sharing.

The usual caveat applies, and I mean it: these are interim results from a single coder. An independent reliability audit is pending, and no final calls get made until it has run. I flag this not as fine print but because reporting what the evidence says, before you know whether you like it, is the whole job. It is the same discipline I bring to security audits.

## The numbers so far

From a corpus of federal guidance documents (NIST SP 800-204D, the NSA/CISA joint advisory on defending CI/CD environments, the SSDF in SP 800-218, SP 800-53, SP 800-161r1, and Executive Order 14028, among others), I extracted 72 controls and rated 70 of them against all ten categories of the OWASP Top 10 CI/CD Security Risks. That is 700 mapping cells, each rated fully, partially, or not addressed, with verbatim quote evidence behind every rating.

Rolled up to the category level:

- **6 of 10 categories are fully addressed** somewhere in the corpus: flow control, identity and access management, pipeline-based access controls abuse (poisoned pipeline execution), credential hygiene, artifact integrity, and logging and visibility.
- **4 of 10 are only partially addressed**: dependency chain abuse, pipeline-based access controls, insecure system configuration, and ungoverned third-party services.
- **0 categories are unaddressed.** Federal guidance now touches every category of the OWASP CI/CD taxonomy at least at the objective level.

## What surprised me

I pre-registered a hypothesis that federal guidance would be broad but shallow: most categories touched, few covered with operational depth. The data is currently trending against my own hypothesis, and the reason is instructive.

Two documents carry almost all of the operational weight: NIST SP 800-204D (2024) and the NSA/CISA cybersecurity information sheet on CI/CD environments (2023). These are not framework documents that tell you to "manage risk." They name tool-recognizable mechanisms: sandboxed CI runs, push protection, enforced commit signing, provenance-gated deployment admission, secrets-manager indirection. The older framework documents (SP 800-53, the SSDF, EO 14028) rate almost uniformly "partially": objectives named, implementation left to you.

The practical takeaway: if you own a pipeline and you have only read the framework-level guidance, the two documents above are where the actionable material lives.

## The four gaps that should worry you

Across the entire corpus, four areas remain thin. These are the places where a pipeline owner gets the least help from official guidance, and in my experience they are also where real-world incidents concentrate:

1. **Dependency-resolution abuse mechanics.** Guidance covers pinning and verification objectives, but not the specific failure modes: dependency confusion, typosquatting, mutable-tag references on third-party actions.
2. **Pipeline-node credential scoping.** What a specific runner or pipeline node should be allowed to reach is largely left as an exercise for the reader.
3. **CI/CD server and runner hardening.** Hardening guidance for the pipeline infrastructure itself is objective-level at best.
4. **Governance of third-party CI/CD service integrations.** Only one corpus item even names third-party services in development processes as a control target.

If you want a quick self-check: could you say, today, which third-party actions or services your pipelines call, whether those references are pinned to immutable versions, and what credentials each pipeline node can reach? Those three questions cover most of the gap surface above.

## Why this matters beyond the US federal space

I now work with EU organizations on NIS2 readiness, and the overlap is direct. NIS2's risk-management measures explicitly include supply-chain security, and your CI/CD pipeline is the part of your supply chain you actually control. The four gap areas above are precisely where I look first in an audit, because they are the places where neither US federal guidance nor most internal policies give teams concrete answers.

## What's next

The reference-compromise mapping (SolarWinds, Codecov, 3CX) is in progress, and the independent reliability audit comes after that. If the audit downgrades some borderline ratings, the picture shifts back toward my original hypothesis; if it holds, the "guidance is more operational than expected" story stands. Either way, the final whitepaper will report it.

If you run pipelines in a regulated environment and want to compare notes, my inbox is open.
