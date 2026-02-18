---
description: Multi-level code review with peer, architecture, security, and reliability checks.
argument-hint: <path> [--quick|--security|--all]
allowed-tools: Read, Glob, Grep, Bash
---

# Full Review Protocol (Mobile)

Multi-level code review adapted for Mobile Engineering standards.

**Before proceeding:** Read the `agent-coordination` skill at `agente-orchestrator/skills/agent-coordination/SKILL.md` for registry management, verification scripts, and coordination protocols.

## Review Target

**Path to review:** $1  
**Options:** $ARGUMENTS

## Quick Reference

- `/review-full src/` — Full 4-level review
- `/review-full src/ --quick` — L1 only (peer review)
- `/review-full src/ --security` — L1 + L3 (peer + security)
- `/review-full src/ --all` — Force all 4 levels

---

## Pre-Review Analysis

Before starting, analyze the target to determine which review levels apply:

<analysis>
!find $1 -type f \( -name "*.dart" -o -name "*.yaml" \) 2>/dev/null | head -20 | xargs wc -l 2>/dev/null | tail -1 || echo "0 total"
!git diff --stat HEAD~1 -- $1 2>/dev/null | tail -1 || echo "No git history"
</analysis>

<prior_work>
!cat .claude/reports/_registry.md 2>/dev/null | grep -i "review\|security\|arch\|test" | head -10 || echo "No prior reviews found"
</prior_work>

---

## Review Levels

### Level 1: Peer Review (Always Required)

Invoke the `code-quality` agent with mode=review:

```
Task(code-quality, "
Mode: review
Target: $1

Focus areas:
- Flutter/Dart best practices (lints)
- Widget structure and rebuild optimization
- State management correct usage (Bloc/Riverpod)
- Error handling completeness

Severity classification:
- BLOCKING: Must fix before merge
- NON-BLOCKING: Should fix, can defer
- NIT: Nice to have improvements

Output: .claude/reports/review/L1-peer-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L1 report entry.

---

### Level 2: Architecture Review

**Trigger when ANY of these apply:**
- Change exceeds 200 lines
- New Modules/Packages created
- Changes to `domain` layer entities/repositories
- State management logic changes

Invoke the `mobile-architect` agent with mode=system:

```
Task(mobile-architect, "
Mode: system
Target: $1

Context from L1: [Include key findings from peer review]

Assessment criteria:
- Alignment with Clean Architecture layers
- Dependency injection correctness
- Modularization boundaries (no circular deps)
- State management pattern consistency

Output: .claude/reports/arch/L2-arch-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L2 report entry.

---

### Level 3: Security Review

**Trigger when change touches ANY of:**
- Authentication/Authorization
- Secure Storage (Keychain/Keystore)
- Network calls (Dio/Http) / SSL Pinning
- User Input forms
- ProGuard/Obfuscation config

Invoke the `security-mobile` agent with mode=scan:

```
Task(security-mobile, "
Mode: scan
Target: $1

Context from L1/L2: [Include relevant findings]

Security checklist:
- OWASP Mobile Top 10 vulnerabilities
- Insecure Data Storage checks
- Hardcoded secrets/keys
- Network security configuration

Output: .claude/reports/security/L3-security-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L3 report entry.

---

### Level 4: Reliability Review

**Trigger when change affects ANY of:**
- Critical user flows (crash risks)
- Performance critical widgets (Lists/Animations)
- Offline support / Cache logic
- Native platform channels

Invoke the `test-engineer` agent for reliability/coverage check:

```
Task(test-engineer, "
Mode: qa-strategy
Target: $1

Context from L1/L2/L3: [Include relevant findings]

Reliability assessment:
- Test coverage for new logic
- Widget test boundaries
- Edge case handling (Network errors, Empty states)
- Potential crash scenarios

Output: .claude/reports/tests/L4-reliability-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L4 report entry.

---

## Execution Flow

Based on the `$ARGUMENTS` provided:

1. **`--quick`**: Execute L1 only, skip all other levels
2. **`--security`**: Execute L1 + L3, skip L2 and L4
3. **`--all`**: Execute all four levels regardless of triggers
4. **No flag**: Analyze target and apply triggers automatically

**Sequencing rule:**  
Each level MAY need prior level's output → Execute sequentially, verify between each.

---

## Post-Review Actions

### Verify Deliverables

After each agent completes, run verification:

```bash
.claude/skills/agent-coordination/scripts/verify.sh "[category]" "[name]" "[date]"
```

### Update Registries

1. **Always:** Add each report to `_registry.md`
2. **If issues deferred:** Add to `_tech-debt.md`

---

## Aggregated Summary Report

After completing applicable levels, generate:

```markdown
# Full Review Summary: $1

**Review Date:** YYYY-MM-DD
**Reviewed By:** Mobile Agent System

## Levels Completed
- [x] L1: Peer Review
- [ ] L2: Arch Review (if applicable)
- [ ] L3: Mobile Security Review (if applicable)
- [ ] L4: Reliability Review (if applicable)

## Blocking Issues (Must Fix)
| Level | Issue | Location | Severity |
|-------|-------|----------|----------|
| L1 | [description] | file:line | BLOCKING |

## Verdict
- [ ] **APPROVED**: Ready to merge
- [ ] **CHANGES REQUESTED**: Blocking issues remain

## Report Links
- L1: `.claude/reports/review/L1-peer-YYYYMMDD.md`
- L2: `.claude/reports/arch/L2-arch-YYYYMMDD.md`
- L3: `.claude/reports/security/L3-security-YYYYMMDD.md`
- L4: `.claude/reports/tests/L4-reliability-YYYYMMDD.md`
```

**Output:** `.claude/reports/review/full-review-YYYYMMDD.md`

**Final step:** Add summary report to `_registry.md`.
