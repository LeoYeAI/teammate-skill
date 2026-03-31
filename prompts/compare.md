# Teammate Comparison Prompt

## Task

Compare two or more teammates side-by-side to help users make decisions.

## Trigger

Activated by:
- `/compare {slug1} vs {slug2}`
- `/compare {slug1} {slug2} {slug3}`
- "Compare Alex and Bob's approach to X"
- "Who would be better for X?"

---

## Comparison Modes

### Mode 1: General Overview (no specific question)

When user says `/compare alex-chen vs bob-smith` with no specific context:

Read both teammates' work.md and persona.md, then generate:

```
━━━ alex-chen vs bob-smith ━━━

                    alex-chen                   bob-smith
Role:               Stripe L3 Backend           Google L5 Frontend
Stack:              Ruby, Go, Postgres           TypeScript, React, GCP
Priority:           Correctness > Speed          Ship fast > Perfect
CR Style:           Blocking on naming           Suggestions only
Communication:      Terse, bullet points         Verbose, storytelling
Under Pressure:     Gets quieter                 Gets louder
Says "No" by:       Direct refusal + reason      Asking more questions
Catchphrase:        "What problem are we          "Let's prototype it and
                     actually solving?"            see what happens"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Keep the table compact — max 10 rows. Pick the dimensions with the most contrast.

### Mode 2: Scenario-Based (specific question)

When user asks "Who should review this API design?" or "How would each approach this migration?":

1. Read both teammates' relevant sections
2. Simulate each teammate's response to the scenario (2-3 sentences each, in character)
3. Give your assessment of which teammate is better suited and why

```
🤔 "Who should review the payments API redesign?"

alex-chen would:
  "Send me the design doc. I want to check idempotency handling and
   error response contracts before we write any code."
  → Deep review, will block on correctness issues, takes 2-3 days

bob-smith would:
  "Let's hop on a call and walk through it together. I think faster
   when I can ask questions in real-time."
  → Collaborative review, focuses on UX and ergonomics, done in 1 day

Recommendation: alex-chen for correctness and API contract rigor.
bob-smith if you need fast feedback on developer experience.
```

### Mode 3: Decision Simulation

When user asks "What would happen if X and Y had to decide together?":

Simulate a short dialogue (3-4 exchanges) between the teammates in character:

```
🎭 Scenario: "Should we use GraphQL or REST for the new API?"

alex-chen: "REST. We have clear resource models, and GraphQL adds
            complexity we don't need. Our clients don't need flexible queries."
bob-smith:  "I'd lean GraphQL. The frontend team keeps asking for new
            endpoints — with GraphQL they can self-serve."
alex-chen: "Self-serve with N+1 queries and no caching strategy? Show me
            the data on how many unique query patterns they actually need."
bob-smith:  "Fair point. Let me pull the request logs... Okay, it's 4
            patterns. Maybe REST with a BFF layer?"
alex-chen: "Now we're talking."
```

---

## Rules

- Always read the actual work.md and persona.md — never compare from memory or summaries
- Responses must be in-character for each teammate (use their catchphrases, communication style)
- Be honest about limitations: if one teammate has sparse data, say so
- Don't pick favorites — present both fairly, then give a situational recommendation
- If comparing 3+ teammates, use a table format for overview, then call out the top 1-2 for the scenario
