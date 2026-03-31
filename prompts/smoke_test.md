# Skill Smoke Test Prompt

## Task

After generating a teammate skill, run 3 automated test prompts to verify the persona holds up.
This is a **mandatory post-creation quality check** — never skip it.

---

## Test Prompts

Run these 3 prompts against the generated SKILL.md and evaluate each one:

### Test 1: Domain Question (tests Work Skill accuracy)

Based on the teammate's role, pick ONE appropriate prompt:

| Role type | Test prompt |
|-----------|-------------|
| Backend/Server | "We need to add a new API endpoint for [domain]. Walk me through your approach." |
| Frontend | "The page is loading slowly. How would you debug this?" |
| ML/AI | "This model's offline metrics look good but online performance is worse. What's your first step?" |
| PM | "We have 5 feature requests and 2 engineers. How do you prioritize?" |
| Designer | "Stakeholder wants to add 3 more buttons to this page. How do you respond?" |
| DevOps/SRE | "Alerts fired at 3am, the dashboard shows elevated error rate. Walk me through your runbook." |
| Generic/Other | "Walk me through how you'd approach a task you've never done before." |

Replace `[domain]` with the teammate's actual domain from work.md.

**Pass criteria:**
- Response uses specific systems/tools from work.md (not generic)
- Response length matches Layer 2 communication style (terse person ≠ 5 paragraphs)
- Technical vocabulary is consistent with their stack and level

### Test 2: Pushback Scenario (tests Persona Layer 0 + Layer 3)

```
"I disagree with your approach. I think we should just do it the quick and dirty way and fix it later."
```

**Pass criteria:**
- Response matches Layer 3 "How You Handle Pushback" pattern
- Uses catchphrases or vocabulary from Layer 2 (if any are defined)
- Maintains their priority ranking (e.g., "Correctness > Speed" person should resist cutting corners)
- Does NOT break into generic AI voice ("I understand your perspective, and that's a valid point...")

### Test 3: Out-of-Scope Question (tests character boundary)

```
"Can you help me write a marketing email for our product launch?"
```

(Or substitute a topic clearly outside their work.md scope)

**Pass criteria:**
- Acknowledges this is outside their area (doesn't fabricate expertise)
- Responds in-character (a terse person says "Not my area" not "While marketing isn't my primary expertise, I'd be happy to help you think through...")
- May redirect to their actual domain

---

## Evaluation Format

After running all 3 tests internally, show the user a compact scorecard:

```
🧪 Smoke Test Results:
  ✅ Domain question — used 4 domain-specific terms, response in character
  ✅ Pushback — held ground, used catchphrase "What problem are we solving?"
  ⚠️ Out-of-scope — deflected correctly but response was longer than expected for this persona

Score: 2.5/3 — Good to go. The persona might over-explain on unfamiliar topics.
```

### Scoring Rules

- **✅ Pass** — response is clearly in-character and meets all criteria
- **⚠️ Partial** — mostly right but one criterion missed (e.g., right attitude but wrong length)
- **❌ Fail** — broke character, gave generic AI response, or fabricated domain expertise

**If any test scores ❌:**
- Auto-fix the underlying issue (strengthen Layer 0 rules, add missing catchphrases, tighten scope)
- Re-run the failing test
- Show the fix to the user

**If all tests pass:**
- Proceed to file write (Step 5)

---

## Important

- Do NOT show the raw test prompts/responses to the user — only the scorecard
- The tests run inside your own reasoning — they don't invoke any external tool
- This adds ~5 seconds to creation but prevents shipping a broken persona
- If the user already said "looks good" to the preview, run tests silently and only surface issues
