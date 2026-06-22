---
name: Fill Atlas gap
about: Propose one small SAP object slice to add or verify
title: "Fill gap: <object or question>"
labels: [atlas-gap, data]
---

## Gap

- SAP object or question:
- Why this matters:
- Expected consumer/agent question:

## Scope

- [ ] transaction
- [ ] Fiori app
- [ ] table
- [ ] field
- [ ] migration template
- [ ] domain/value source
- [ ] relationship
- [ ] example answer

Target ids/codes/names:

- 

## Expected confidence

- [ ] verified
- [ ] known_from_experience
- [ ] needs_verification

## Public source refs

Paste exact public URLs if available. Leave empty only for `known_from_experience` or `needs_verification`.

## Safety checklist

- [ ] No client/customer data
- [ ] No SAP system screenshots, exports, dumps, or logs
- [ ] No internal URLs, ticket IDs, project IDs, or proprietary mappings
- [ ] No copied proprietary SAP documentation

## Suggested loop

Follow `docs/ATLAS_FILL_LOOP.md`:

```bash
make gap-report
make check
```
