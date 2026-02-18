---
description: Orchestrate end-to-end Feature Development (Design → Implement → Verify)
argument-hint: [ticket-id/spec-path]
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, TodoWrite
---

# Feature Development Run

Coordinate end-to-end feature implementation workflow following mobile agent-coordination protocol.

## Workflow

Follows mobile agent-coordination protocol:

1. **Check Registry** - Look for prior related work or architectural constraints
2. **Context Injection** - Provide feature specifications and domain rules
3. **Sequential Execution** - Design → Implement → Verify
4. **Update Registries** - Add report to `_registry.md`, tech debt if issues found

## Process

1. **Specification Analysis**
   - Load Project Context (`CLAUDE.md`, `INDEX.md`)
   - Identify Domain (`investments`, `fx`, `cards`, `onboarding`)

2. **Design Stage** (feature-software-engineer design agent)
   - Analyze requirements, define technical contract (domain,logic,presentation, data, State, API, DTOs)
   - Consult `mobile-architect` if strict architectural changes are needed (e.g. new module,service)
   - Create Implementation Plan at `.claude/reports/implementation/plan-[feature]-YYYYMMDD.md`

3. **Implementation Stage** (feature-software-engineer implement agent)
   - Write code for Domain, Data, and Presentation layers
   - Consult Domain Specialists (`investments-specialist`, `fx-specialist`, etc.) for specific business rules
   - Implement based on approved plan

4. **Verification Stage** (feature-software-engineer verify agent)
   - Execute test suite (Unit, Widget, Integration)
   - Verify code quality and compliance with standards
   - Generate verification report at `.claude/reports/tests/verify-[feature]-YYYYMMDD.md`

5. **Update Registries**
   - Add to `_registry.md`: Feature summary and artifacts
   - Add to `_tech-debt.md`: Any shortcuts taken or deferred items

## Arguments

- **$1**: Feature Specification (File path, Ticket ID, or Description)
  - Can be a file path to a spec
  - Can be a direct description string

## Examples

```bash
# Run from a spec file
/feature specs/new-login-flow.md

# Run with a quick description
/feature "Implement PIX transfer screen with validation"
```

## Output

**Report Location:** `.claude/reports/implementation/impl-[feature]-YYYYMMDD.md`

**Artifacts:**
- Source Code (`lib/`)
- Tests (`test/`)
- Implementation Plan (`.claude/reports/implementation/plan-...`)
- Verification Report (`.claude/reports/tests/verify-...`)

## Skills Invoked

- `agent-coordination` - Core protocol
- `flutter-architecture-patterns` - For design compliance
- Domain Skills (e.g., `fx-rules`) - For business logic

## Registry Updates

After completion, add to `.claude/reports/_registry.md`:
```
- impl-[feature]-YYYYMMDD | Complete | [feature summary]
```

If issues found, add to `.claude/reports/_tech-debt.md`:
```
- [ ] **TD-NNN**: [Issue description]
  - **Impact:** [Priority]
  - **Source:** impl-[feature]-YYYYMMDD.md
```
