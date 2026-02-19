---
description: Orchestrate full task execution (analyze → implement → test)
argument-hint: [task-spec]
---

# Task Build

Coordinate end-to-end task execution following agent-coordination protocol.

## Workflow

Follows agent-coordination protocol:

1. **Check Registry** - Look for prior related tasks, existing implementations
2. **Context Injection** - Provide prior results and context to agents
3. **Sequential Execution** - Analyze → Implement → Test (with verification)
4. **Update Registries** - Add report to `_registry.md`, tech debt if issues found

## Process

1. **Validate Spec**
   - Read and analyze the provided spec thoroughly
   - Verify it contains: objective, acceptance criteria, scope, and constraints
   - If missing information → Stop and ask user for the required details
   - Only proceed when spec has all necessary information to execute

2. **Analysis Stage** (software-engineer agent, mode: analyze)
   - Analyze the problem thoroughly
   - Break down requirements and identify constraints
   - Generate structured implementation plan
   - Document risks and assumptions

3. **Implementation Stage** (software-engineer agent, mode: implement)
   - Follow requirements strictly from the analysis plan
   - Write code with excellence following established patterns
   - Execute each step from the implementation plan in order

4. **Testing Stage** (software-engineer agent, mode: test)
   - Write unit/integration tests for implemented code
   - Run existing test suites to verify no regressions
   - Validate build passes without errors

5. **Quality Gate**
   - If all tests pass → Mark task as complete
   - If tests fail → Return to implementation with failure context
   - Generate final task report

6. **Update Registries**
   - Add to `_registry.md`: task summary and result
   - Add to `_tech-debt.md`: any deferred improvements

## Arguments

- **$1**: Task spec content
  - Full specification with objective, scope, acceptance criteria, and constraints
  - If omitted: Prompt user for the spec

## Examples

```bash
# Run with inline spec
/task/build "Objective: Add JWT auth. Scope: auth middleware, login endpoint. Criteria: tokens expire in 1h, refresh flow works."

# Run with spec file reference
/task/build @specs/auth-feature.md

# Run without args (will prompt for spec)
/task/build
```

## Output

**Report Location:** `.claude/reports/implementation/impl-task-[slug]-YYYYMMDD.md`

**Artifacts:**
- Implementation plan: `.claude/reports/implementation/plan-[slug].md`
- Test results: `.claude/reports/implementation/tests-[slug].md`

## Skills Invoked

- `agent-coordination` - Protocol for agent orchestration and registry management

## Registry Updates

After completion, add to `.claude/reports/_registry.md`:
```
- impl-task-[slug]-YYYYMMDD | Complete | [result summary]
```

If issues found, add to `.claude/reports/_tech-debt.md`:
```
- [ ] **TD-NNN**: [Issue description]
  - **Impact:** [Priority]
  - **Source:** impl-task-[slug]-YYYYMMDD.md
```
