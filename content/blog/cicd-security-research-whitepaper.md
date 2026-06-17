---
title: "From Pipeline to Policy: Writing a Research Whitepaper on Federal CI/CD Security"
date: 2026-06-17
draft: false
tags: ["DevSecOps", "CI/CD Security", "NIST", "Research", "Federal Security"]
description: "How my hands-on experience building CI/CD pipelines turned into a formal research whitepaper mapping federal security guidance against real-world pipeline vulnerabilities."
---

# From Pipeline to Policy: Writing a Research Whitepaper on Federal CI/CD Security

One of the most rewarding parts of the SANS Master's program has been the push to take what you've seen in production and turn it into something rigorous. For my research project, I'm doing exactly that — writing a whitepaper that bridges the gap between federal CI/CD security guidance and what actually shows up in real pipelines.

## Where the Idea Came From

I've spent years building and maintaining CI/CD pipelines across GitHub Actions, GitLab CI/CD, and Azure DevOps. Two patterns kept showing up regardless of team size or agency:

1. **Code shipping through pipelines with no SAST or SCA checks** — vulnerable or malicious dependencies reaching production undetected.
2. **Third-party Actions and packages pulled in without version pinning or integrity verification** — giving arbitrary external code access to repository secrets and runner environments.

These aren't edge cases. They're the norm. And yet when I went looking for federal guidance that spoke directly to CI/CD pipeline configurations, I found that most of it was either too high-level or not written for the pipeline context at all.

That changed in 2024 when NIST published **SP 800-204D** — the federal government's first publication written specifically for CI/CD pipelines, issued in direct response to Executive Order 14028's mandate to secure the software supply chain.

## The Research Question

The question I'm investigating:

> *To what extent does NIST SP 800-204D address the security risks observable in a real federal agency CI/CD pipeline?*

The problem this solves is practical: without a concrete mapping between SP 800-204D and observable pipeline configurations, the document stays aspirational. Federal engineers need a defensible path from *identifying a pipeline risk* to *justifying a fix under existing federal authority*. That's what this research tries to provide.

## The Approach

The study is a structured control-mapping exercise. I identified seven security findings in a real, publicly available federal agency GitHub repository — everything reproducible by any reviewer with a free GitHub account — and then applied a coding rubric to rate how well SP 800-204D addresses each one.

The rubric is straightforward:
- **Fully addressed** — SP 800-204D provides both the security objective and operational implementation guidance for the relevant pipeline component
- **Partially addressed** — the objective is stated but implementation is left to interpretation
- **Not addressed** — no relevant control is identifiable

The hypothesis is that SP 800-204D will cover several of the findings at the intent level, but a non-zero gap surface will remain — particularly for findings that touch FedRAMP boundary controls and application-configuration concerns, which fall outside the document's explicit scope.

## What I'm Finding

The findings range across the OWASP Top 10 CI/CD Security Risks taxonomy: absent SAST/SCA, unpinned third-party Actions, broken dependency management configuration, unverified tool installation, and a few operational issues that blur the line between pipeline security and broader cloud security posture.

What's interesting is that SP 800-204D is actually quite good on the supply-chain side — pinning, verification, provenance. Where it gets thin is the operational and boundary questions: what happens when a pipeline exports production data to infrastructure outside your authorization boundary? What does the document say about environment separation when both prod and dev share the same backing service? Those are the gaps I expect to document.

## Why This Matters

EO 14028 made software pipeline security a national policy priority. SP 800-204D is the clearest attempt yet to translate that priority into actionable controls. But a policy document is only as useful as its connection to practice.

The goal of this whitepaper is modest and specific: demonstrate a repeatable mapping protocol, surface where the guidance lands and where it doesn't, and give practitioners something they can cite when making the case for pipeline security investment to leadership.

I'm planning to coordinate disclosure with the relevant agency security contacts and CISA before publication, consistent with standard coordinated-disclosure norms.

## What's Next

The initial pipeline analysis is complete. The control-mapping phase is underway. Once the RPC has independently re-coded the mappings and we've resolved any disagreements, I'll write up the final analysis.

More updates to follow as the paper comes together. If you're working in the federal DevSecOps space and have thoughts on SP 800-204D or pipeline security gaps, I'd love to hear from you.

---
