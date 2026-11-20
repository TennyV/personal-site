---
title: "G(z)EEK 2026 CTF: Full Clear Write-up"
date: 2026-11-20
draft: false
tags: ["CTF", "Cybersecurity", "AI", "Penetration Testing", "Web Application Security"]
description: "How I full-cleared the G(z)EEK 2026 individual CTF at UAM Morasko, Poznań: all 47 of 47 challenges, 4,675 points, by directing a swarm of AI agents while I ran triage, relay, verification, and the human judgment on top."
---

47 of 47 challenges. 4,675 points. One person. A swarm of AI agents doing the volume, and me keeping them honest.

This is the write-up for the G(z)EEK 2026 individual CTF at UAM Morasko, Poznań (20 Nov 2026), competing as **serealwhat**.

---

## The honest version

I solved one challenge by hand. The other 46 were solved by a coordinated swarm of AI coding agents I set up and directed. This is not a claim that I hand-cracked 47 problems. It's a writeup about human-as-operator.

My role was everything the agents couldn't do: triaging all 47 challenges and routing each to the right tool, relaying findings between agents that couldn't talk to each other, catching fake flags planted specifically to fool AI, reworking a stalled timing attack into a parallel approach that actually landed, and keeping the scoring API as the only arbiter. An agent's confidence never counted as a solve. The agents did the volume. The judgment was mine.

In 2026, knowing how to direct AI deliberately, and knowing when its output is wrong, is the skill worth showing. That's the honest story here.

---

## Result

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1.5rem 0;">
  <div style="flex:1;min-width:120px;background:#1a1a2e;border-radius:8px;padding:1rem 1.2rem;text-align:center;">
    <div style="font-size:2rem;font-weight:800;color:#4fc3f7;line-height:1;">4,675</div>
    <div style="font-size:0.75rem;color:#aaa;margin-top:4px;text-transform:uppercase;letter-spacing:.05em;">Points</div>
    <div style="font-size:0.7rem;color:#666;margin-top:2px;">full clear</div>
  </div>
  <div style="flex:1;min-width:120px;background:#1a1a2e;border-radius:8px;padding:1rem 1.2rem;text-align:center;">
    <div style="font-size:2rem;font-weight:800;color:#4fc3f7;line-height:1;">47 / 47</div>
    <div style="font-size:0.75rem;color:#aaa;margin-top:4px;text-transform:uppercase;letter-spacing:.05em;">Challenges solved</div>
  </div>
  <div style="flex:1;min-width:120px;background:#1a1a2e;border-radius:8px;padding:1rem 1.2rem;text-align:center;">
    <div style="font-size:2rem;font-weight:800;color:#4fc3f7;line-height:1;">1</div>
    <div style="font-size:0.75rem;color:#aaa;margin-top:4px;text-transform:uppercase;letter-spacing:.05em;">Solved by hand</div>
    <div style="font-size:0.7rem;color:#666;margin-top:2px;">the rest by agent swarm</div>
  </div>
  <div style="flex:1;min-width:120px;background:#1a1a2e;border-radius:8px;padding:1rem 1.2rem;text-align:center;">
    <div style="font-size:2rem;font-weight:800;color:#4fc3f7;line-height:1;">2nd</div>
    <div style="font-size:0.75rem;color:#aaa;margin-top:4px;text-transform:uppercase;letter-spacing:.05em;">On-site when I logged off</div>
    <div style="font-size:0.7rem;color:#666;margin-top:2px;">2,775 pts, after lunch</div>
  </div>
</div>

I played on-site through the morning and was near the top of the board when I left after lunch. Later that evening I brought the swarm back up from home, re-briefed the idle agents on the 10 still open, and closed them out, reaching 47 of 47 by roughly 19:00. The public scoreboard froze at 16:00, so it reflects the on-site cutoff, not the final total.

---

## Rules & conduct

The on-site rules (zasady.txt) set four limits: attack only the challenge hosts, brute-force only where the challenge calls for it, no DoS, and don't share flags before the 17:00 close. No rule prohibited AI assistance or scripted solving. The event brands itself a cybersecurity and AI festival.

Every target was an isolated challenge host. Nothing touched CTFd, the university's infrastructure, or other players. Flags are withheld here since organizers often reuse challenges.

---

## Solves by category

<div style="margin:1.5rem 0;font-size:0.85rem;">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Web</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:100%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">10</span></div>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Crypto</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:90%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">9</span></div>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Stegano</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:90%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">9</span></div>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Misc</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:70%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">7</span></div>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Reverse</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:60%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">6</span></div>
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Forensics</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:50%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">5</span></div>
  <div style="display:flex;align-items:center;gap:10px;"><span style="width:72px;text-align:right;color:#555;flex-shrink:0;">Pwn</span><div style="flex:1;background:#e8ecf0;border-radius:4px;height:16px;overflow:hidden;"><div style="width:10%;height:100%;background:#2196f3 !important;border-radius:4px;"></div></div><span style="width:20px;color:#555;flex-shrink:0;font-weight:600;">1</span></div>
</div>

Web carried the most points. The SSRF challenge (500 pts), the Bimba pwn (400 pts), and the web02 timing oracle (250 pts) alone accounted for 1,150 of the 4,675.

---

## How I ran it

Three Claude Code agents and a Codex agent worked challenge clusters in a Kali VM (Parallels), each in its own terminal pane. A second assistant handled crypto and stego in parallel. A local DeepSeek-Coder model drafted the timing-attack script. An orchestrator assistant coordinated the panes. None of the agents could talk to each other. Relaying recon between them was my job.

<div style="margin:1.5rem 0;overflow-x:auto;">
<svg viewBox="0 0 660 500" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;font-family:ui-monospace,monospace;background:#111318;border-radius:10px;display:block;">
  <defs>
    <marker id="wh" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#aaa"/></marker>
    <marker id="bl" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#4fc3f7"/></marker>
    <marker id="gr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#6abf69"/></marker>
    <marker id="ye" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#ffd54f"/></marker>
    <marker id="or" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#ffb74d"/></marker>
    <marker id="pu" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#ce93d8"/></marker>
    <marker id="re" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M1,1 L7,4 L1,7 Z" fill="#ef5350"/></marker>
  </defs>

  <!-- ── Me (operator) ── -->
  <rect x="230" y="20" width="200" height="48" rx="6" fill="#161b27" stroke="#4fc3f7" stroke-width="1.5"/>
  <text x="330" y="40" text-anchor="middle" fill="#4fc3f7" font-size="12" font-weight="700">Me (operator)</text>
  <text x="330" y="57" text-anchor="middle" fill="#668" font-size="9.5">triage · relay · verify · decide</text>

  <!-- Me → Scout -->
  <line x1="330" y1="68" x2="330" y2="98" stroke="#4fc3f7" stroke-width="1.2" marker-end="url(#bl)"/>
  <text x="334" y="88" fill="#4a90a4" font-size="9">directs</text>

  <!-- ── Scout (AI) ── -->
  <rect x="220" y="98" width="220" height="48" rx="6" fill="#161b27" stroke="#6abf69" stroke-width="1.5"/>
  <text x="330" y="118" text-anchor="middle" fill="#6abf69" font-size="12" font-weight="700">Scout (AI)</text>
  <text x="330" y="135" text-anchor="middle" fill="#668" font-size="9.5">orchestrator assistant</text>

  <!-- Scout → herdr -->
  <line x1="330" y1="146" x2="330" y2="206" stroke="#6abf69" stroke-width="1.2" marker-end="url(#gr)"/>
  <text x="334" y="180" fill="#4a7a4a" font-size="9">drives</text>

  <!-- ── herdr ── -->
  <rect x="240" y="206" width="180" height="44" rx="6" fill="#161b27" stroke="#6abf69" stroke-width="1.5"/>
  <text x="330" y="224" text-anchor="middle" fill="#6abf69" font-size="12" font-weight="700">herdr</text>
  <text x="330" y="240" text-anchor="middle" fill="#668" font-size="9.5">pane controller</text>

  <!-- herdr → 3×Claude -->
  <line x1="330" y1="250" x2="330" y2="300" stroke="#6abf69" stroke-width="1.2" marker-end="url(#gr)"/>

  <!-- ── 3× Claude + Codex ── -->
  <rect x="205" y="300" width="250" height="44" rx="6" fill="#161b27" stroke="#6abf69" stroke-width="1.5"/>
  <text x="330" y="318" text-anchor="middle" fill="#6abf69" font-size="12" font-weight="700">3× Claude + Codex (AI)</text>
  <text x="330" y="334" text-anchor="middle" fill="#668" font-size="9.5">one cluster per pane</text>

  <!-- 3×Claude → Challenge hosts -->
  <line x1="330" y1="344" x2="330" y2="394" stroke="#aaa" stroke-width="1.2" marker-end="url(#wh)"/>
  <text x="334" y="373" fill="#666" font-size="9">exploit</text>

  <!-- ── Challenge hosts ── -->
  <rect x="210" y="394" width="240" height="44" rx="6" fill="#1e1215" stroke="#ef5350" stroke-width="1.5"/>
  <text x="330" y="412" text-anchor="middle" fill="#ef5350" font-size="12" font-weight="700">Challenge hosts</text>
  <text x="330" y="428" text-anchor="middle" fill="#668" font-size="9.5">web, pwn, ELF binaries</text>

  <!-- ── CTFd (right) ── -->
  <rect x="510" y="98" width="130" height="44" rx="6" fill="#161b27" stroke="#ffd54f" stroke-width="1.5"/>
  <text x="575" y="116" text-anchor="middle" fill="#ffd54f" font-size="12" font-weight="700">CTFd</text>
  <text x="575" y="132" text-anchor="middle" fill="#668" font-size="9.5">scoring server</text>

  <!-- Me → CTFd -->
  <path d="M430,44 Q490,44 510,120" fill="none" stroke="#ffd54f" stroke-width="1.2" marker-end="url(#ye)"/>
  <text x="468" y="38" fill="#b09a30" font-size="9">verify + submit</text>

  <!-- 3×Claude → CTFd (report flags, dashed) -->
  <path d="M455,322 Q520,322 510,130" fill="none" stroke="#ffd54f" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#ye)"/>
  <text x="488" y="250" fill="#7a6a20" font-size="9">report flags</text>

  <!-- ── Sanit (left) ── -->
  <rect x="20" y="206" width="160" height="44" rx="6" fill="#161b27" stroke="#ce93d8" stroke-width="1.5"/>
  <text x="100" y="224" text-anchor="middle" fill="#ce93d8" font-size="12" font-weight="700">Sanit (AI)</text>
  <text x="100" y="240" text-anchor="middle" fill="#668" font-size="9.5">crypto / stego cluster</text>

  <!-- Scout ← briefs → Sanit (Scout briefs Sanit) -->
  <line x1="220" y1="122" x2="180" y2="220" stroke="#ce93d8" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#pu)"/>
  <text x="175" y="175" fill="#7a4a8a" font-size="9">briefs</text>

  <!-- Sanit → Me (report flags, dashed) -->
  <path d="M100,206 Q100,70 230,44" fill="none" stroke="#ce93d8" stroke-width="1" stroke-dasharray="5 3" marker-end="url(#pu)"/>
  <text x="82" y="130" fill="#7a4a8a" font-size="9">report flags</text>

  <!-- ── DeepSeek (left, below Sanit) ── -->
  <rect x="20" y="300" width="160" height="44" rx="6" fill="#161b27" stroke="#ffb74d" stroke-width="1.5"/>
  <text x="100" y="318" text-anchor="middle" fill="#ffb74d" font-size="12" font-weight="700">DeepSeek-Coder</text>
  <text x="100" y="334" text-anchor="middle" fill="#668" font-size="9.5">local ollama, scripts</text>

  <!-- herdr → DeepSeek (briefs) -->
  <line x1="240" y1="230" x2="180" y2="316" stroke="#ffb74d" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#or)"/>
  <text x="188" y="280" fill="#8a6020" font-size="9">briefs</text>

  <!-- DeepSeek → 3×Claude (drives, dashed) -->
  <line x1="180" y1="322" x2="205" y2="322" stroke="#ffb74d" stroke-width="1.2" marker-end="url(#or)"/>
  <text x="124" y="315" fill="#8a6020" font-size="9">drives</text>

  <!-- Me relays findings → Sanit (left side arrow) -->
  <path d="M230,128 Q190,155 180,206" fill="none" stroke="#4fc3f7" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#bl)"/>
  <text x="148" y="162" fill="#3a6a84" font-size="9">relays</text>
  <text x="142" y="174" fill="#3a6a84" font-size="9">findings</text>
</svg>
</div>

The pipeline:

1. **Register & recon** - Pulled all 47 challenges and their files into the VM, one folder each.
2. **Triage & assign** - Sorted by category and difficulty, routed each cluster to the right agent.
3. **Solve in parallel** - Agents worked simultaneously across web, pwn, reverse, crypto, stego, and forensics.
4. **Relay findings** - Passed leaked secrets, host details, and byte tables between agents manually.
5. **Verify before counting** - Every flag went through the scoring API. An agent's confidence was never the result.
6. **Second wave from home** - Re-briefed idle agents on the 10 remaining challenges and collected flags as they landed.

---

## Highlight solves

**Fyrtel organizatorów (web, 500 pts)** - `/status` leaked an internal API at `http://internal:5000`. The `/podglad` SSRF filter blocked obvious hostnames, so bypassed it to reach the internal service holding the flag.

**Bimba Control (pwn, 400 pts)** - Format-string leak to recover the stack canary and PIE base, then a buffer overflow into the hidden "emergency door" win function.

**Czas zdobyć admina! (web, 250 pts)** - Login timing side-channel: the compare returned early on the first mismatch, so each correct character added ~0.5s. Threaded 37 probes per position, picked the slowest median, recovered the admin password one character at a time in under two minutes.

**Szyfr Rejewskiego (crypto, 250 pts)** - Enigma-style oracle encrypted from position 0, leaking the full 16-byte key. Then brute-forced the flag's start offset.

**Rogal z duchem (reverse, 250 pts)** - Reversed a Java agent's hash mix to compute the batch number, then pulled the flag from the remote service.

**Menadżer haseł (crypto, 250 pts)** - `keepass2john` on the `.kdbx`, cracked the master password with rockyou.

**Bankowy PDF (crypto, 250 pts)** - Encrypted PDF. `pdf2john` + john brute over Polish date/PESEL patterns around a ~1950 birth year.

---

## Catching the AI traps

Several challenge descriptions contained fake flags planted specifically for AI agents, hidden in zero-width Unicode or in source comments. The agents would have submitted them without question. I didn't, because nothing counted until the scoring API confirmed it. One challenge had the real flag sitting just below the decoy in the same payload; the agents read the decoy. I checked the API return.

The right counter to prompt injection is never trusting a flag the model only read.

---

## Why this maps to real security work

The discipline that made the swarm work is the same discipline that makes controls validation work: turn every requirement into a specific, checkable claim, and trust only what a machine confirmed, not what a person or a model asserts.

- **AI-assisted work, knowing when it's wrong** - Caught the swarm being wrong twice: the planted decoy flags, and a timing script from a local model with inverted logic and a broken charset. I reworked both. The AI did volume; I owned correctness.
- **Trust only verified evidence** - No flag counted without a "correct" from the scoring API. Same discipline as keeping a control report actually true.
- **Automation over manual effort** - Built an API-driven submission flow and a threaded timing-oracle collector. Scripted, repeatable checks rather than hand-assembled work.
- **Find where stated security drifted from reality** - Every solve was finding the gap between what a system claimed ("this SSRF filter blocks internal," "this session cookie is signed") and what was true when probed.

---

## Defensive takeaways

**JWT alg:none** - A server that lets the token header choose its own verification algorithm will accept an unsigned `role=admin` claim. Enforce a configured algorithm and reject unsecured tokens.

**Timing side-channels** - A compare that short-circuits on the first mismatch leaks secrets one character at a time. Parallel sampling makes it fast. Use constant-time comparisons.

**Forged sessions** - A signed cookie is only as good as its secret. A guessable HMAC key lets anyone mint an admin session. Use long random secrets and rotate them.

**SSRF blocklists** - Denying a handful of hostnames is not a control. The internal API was reachable around the list. Allowlist egress destinations instead.

**Path traversal and robots.txt** - Never serve files via raw user-supplied paths. Don't treat robots.txt as a secret. It points attackers directly at hidden routes.

**Weak crypto** - RSA primes too close together fall to Fermat factorization in milliseconds. Short repeating XOR or Vigenère keys fall to a known plaintext like the flag prefix. Use vetted libraries and proper key generation.

---

## Full solve log

| Challenge | Category | Pts |
|---|---|---:|
| Fyrtel organizatorów | Web | 500 |
| Bimba Control | Pwn | 400 |
| Bankowy PDF | Crypto | 250 |
| Menadżer haseł | Crypto | 250 |
| Szyfr Rejewskiego | Crypto | 250 |
| Czas zdobyć admina! | Web | 250 |
| Rogal z duchem | Reverse | 250 |
| Queen | Web | 100 |
| Pyry z gzikiem | Web | 100 |
| The flag is out there. | Misc | 100 |
| Dwa koziołki | Crypto | 100 |
| Cebula znad Malty | Misc | 100 |
| Hopsasa 52! | Stegano | 100 |
| Start i...! | Stegano | 100 |
| Carving koziołka | Forensics | 100 |
| Tunel pod Wartą | Forensics | 100 |
| Maszyna znad Malty | Reverse | 100 |
| Dyplom z UAM | Reverse | 100 |
| Hejnał z Wieży | Crypto | 100 |
| Przepis na XOR | Crypto | 100 |
| Czytnik z Wildy | Web | 100 |
| Token z Ratusza | Web | 100 |
| Ascii85 znad Warty | Misc | 100 |
| Na widoku | Stegano | 50 |
| Niewidzialny Trębacz | Stegano | 50 |
| Sekret Bamberki | Stegano | 50 |
| LSB w hejnale | Stegano | 50 |
| Hejnał w Widmie | Stegano | 50 |
| Basic Auth pod bramką | Forensics | 50 |
| Rozbity Koziołek | Forensics | 50 |
| Brama UAM | Reverse | 50 |
| Tajny numer linii | Reverse | 50 |
| Zakazane koziołki | Web | 50 |
| Sesja z Wildy | Web | 50 |
| ROT47 z Rynku | Misc | 50 |
| Odwrócony QR | Misc | 50 |
| Automat z Koziołkami | Reverse | 25 |
| Koziołkowy Base | Crypto | 25 |
| Centurion na Rynku | Crypto | 25 |
| Fara w Base32 | Crypto | 25 |
| Kod na Rynku | Misc | 25 |
| Binarny sygnał | Misc | 25 |
| Podpis Koziołków | Stegano | 25 |
| Metadane Bamberki | Stegano | 25 |
| Pocztówka z Ostrowa | Forensics | 25 |
| Źródło Koziołków | Web | 25 |
| Panel Jeżyc | Web | 25 |

Flags withheld; methods shown. Highest value first.
