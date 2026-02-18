---
description: View and manage tech debt registry
---

# Tech Debt Command (Mobile)

Manage technical debt tracking.

## Usage

```
/debt                          # View debt summary
/debt add [description]        # Add new debt item
/debt resolve [TD-NNN]         # Mark item resolved
/debt review                   # Full registry review
```

## View Summary

```
/debt
```

Read `.claude/reports/_tech-debt.md` and display summary by priority.

## Add Debt

```
/debt add "Description" --priority [critical|high|medium|low]
```

1. Get next TD number
2. Add to `_tech-debt.md`
3. Report confirmation

## Resolve Debt

```
/debt resolve TD-NNN
```

1. Find item in registry
2. Mark as `[x]`
3. Move to Resolved section

## Full Review

```
/debt review
```

Invoke analysis:

```
Task(code-quality, "
Mode: qa-strategy

Audit tech debt registry at .claude/reports/_tech-debt.md

Assess:
1. Are priorities accurate?
2. Any items that should be escalated?
3. Stale items (>90 days without progress)?
4. Items that may no longer be relevant?
5. Missing debt items based on codebase review?

Output recommendations for registry cleanup.
")
```

## Debt Types (Mobile)

| Type | Example | Typical Priority |
|------|---------|-----------------|
| Code | Massive Build methods, Logic in UI | Medium |
| Test | Golden file missing, Low coverage | High |
| Dependency | Outdated packages, Deprecated APIs | High |
| Architecture | Circular dependencies, Tight coupling | Critical |
| UI/UX | Jank, Non-standard components | Low |
| Security | Cleartext traffic, Insecure storage | Critical |
