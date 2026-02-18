# Mobile Agent Orchestration (`agente-orchestrator/`)

**Production-grade multi-agent coordination system with tiered delegation, institutional memory, and explicit tech-debt tracking.**

This directory provides reusable configuration layers for Claude Code that enable sophisticated agent orchestration across the mobile project.

## What This Solves

Three critical problems in Claude Code agent usage:

1. **Context Amnesia**: Agents forget prior work within 15-20 minutes
2. **Coordination Chaos**: Multiple agents overwrite each other's work
3. **Delegation Limits**: Manual oversight required for every decision

**Solution**: A tiered delegation architecture with persistent memory (registry + tech-debt tracking) that extends productive context windows to 2+ hours while enabling the Main Agent to consistently apply documented engineering criteria.

---

## Core Architecture

### Tiered Agent System

```
Tier 1: Workflow Orchestrators
├── code-quality              → Multi-level review chain (L1→L2→L3→L4)
├── test-engineer             → Test execution with failure triage
├── architect                 → System architecture, modularization strategy
└── feature-software-engineer → End-to-end mobile feature owner (Design -> Implement -> Verify)

Tier 2: Specialized Execution
├── security-mobile           → OWASP Mobile checks, data storage security
├── flutter-platform-engineer → Core libraries (Networking, Storage), Design System maintenance
├── analytics-specialist      → Taxonomy governance, event tracking implementation
└── docs                      → Technical documentation

Tier 3: Domain Specialists
├── investments-specialist    → Financial math, tax rules (IOF/IR), asset specificities
└── fx-specialist             → Foreign Exchange logic, IOF, VET, currency precision

```

### Dual-Registry Model

**`_registry.md`** — What was done
- Tracks completed work, deliverables, and outcomes
- Main agent reads this for context before starting new tasks
- Updated after every significant task completion

**`_tech-debt.md`** — What was deferred
- Explicit tracking of shortcuts, workarounds, and deferred improvements
- Links each debt item to its source (commit, report, or incident)
- Prevents silent degradation of code quality

### 4-Step Coordination Protocol

1. **Registry Check** → Main agent reads prior work
2. **Context Injection** → Relevant context distributed to specialized agents
3. **Sequencing** → Sequential or parallel execution based on dependencies
4. **Verification** → Quality gates ensure standards are met

---

## Quick Start

### 1. Install Project-Level Configuration

```bash
# In your project directory
mkdir -p agente-orchestrator/
```

This creates:
- `INDEX.md` context file (this file)
- Institutional memory structure (registries + categorized report folders)
- Project-specific commands and skills

### 2. Start Using

```bash
# Start end-to-end feature development
/feature "Implement PIX transfer"

# Multi-level code review
/review-full src/authentication/

# Local CI pipeline before pushing
/ci

# View and manage tech debt
/debt

# Create RFC for system design
/rfc authentication-system
```

---

## Key Features

### Multi-Level Review Chain

The `/review-full` command implements graduated review escalation:

```
L1: Peer Review (code-quality agent)
    ↓ Triggers: Always runs
L2: Architecture Review (architect agent)
    ↓ Triggers: >200 lines, new APIs, schema changes, new modules
L3: Security Review (security-mobile agent)
    ↓ Triggers: Auth/authz, user input, external APIs, database queries, crypto
L4: Reliability Review (test-engineer agent)
    ↓ Triggers: Infrastructure, service dependencies, error handling, caching
```

**Why**: Main Agent applies documented escalation criteria by reading code, ensuring consistent decisions without relying on memory.

### Local CI Pipeline

The `/ci` command runs the full quality gate before pushing:

```
1. Lint → Check code style
2. Type-check → Verify type safety
3. Build → Ensure compilation succeeds
4. Test → Run test suite with coverage
5. Security scan → OWASP checks
```

**Why**: Catch issues locally before CI/CD, faster feedback cycles.

### Explicit Tech-Debt Tracking

The `_tech-debt.md` registry captures:
- What shortcut was taken
- Why it was necessary (time pressure, missing info, external dependency)
- Where it lives (file paths, commit SHAs)
- Impact severity (cosmetic → critical)
- Remediation plan

**Why**: Prevents "just this once" from becoming permanent, maintains quality over time.

---

## Repository Structure

```
agente-orchestrator/
├── INDEX.md                     # You are here
├── agents/                      # Tiered agent definitions (formerly subagents)
├── skills/                      # Mobile-specific skills
└── commands/                    # Playbooks for executing mobile tasks
```
