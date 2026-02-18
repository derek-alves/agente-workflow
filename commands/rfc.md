---
description: Create or review RFC (Request for Comments) design document using mobile-architect agent
---

# RFC Command (Mobile)

Invoke `mobile-architect` agent for design document lifecycle management.

## Usage

```
/rfc [topic]                    # Create new RFC
/rfc review [RFC-path]          # Review existing RFC
/rfc decision [RFC-path]        # Record decision on RFC
/rfc list                       # List all RFCs
```

## Create New RFC

```
/rfc [topic description]
```

```
Task(mobile-architect, "
Mode: system

Topic: [user's topic description]

Create comprehensive RFC covering:
1. Problem statement and motivation
2. Proposed solution with technical design (Flutter/Dart context)
3. Architecture impact (Modules, State, API)
4. Alternatives considered
5. Security, privacy, performance considerations
6. Rollout plan with milestones

Assign next RFC number based on existing files in .claude/reports/arch/

Output: .claude/reports/arch/RFC-[NNNN]-[slug].md
")
```

## Review RFC

```
/rfc review [path-to-rfc]
```

```
Task(mobile-architect, "
Mode: review

RFC: [path-to-rfc]

Provide technical review:
1. Feasibility assessment (Flutter capability)
2. Alignment with Clean Architecture
3. State Management implications
4. Scalability concerns
5. Specific change requests

Output: .claude/reports/arch/review-RFC-[NNNN]-YYYYMMDD.md
")
```

## Record Decision

```
/rfc decision [path-to-rfc] [approve|reject|revise]
```

```
Task(mobile-architect, "
Mode: system

RFC: [path-to-rfc]
Decision: [approve/reject/revise]

Record:
1. Decision and rationale
2. Conditions (if approved)
3. Required revisions (if revise)
4. Rejection reasons (if rejected)
5. Next steps

Update RFC status in original document.

Output: .claude/reports/arch/decision-RFC-[NNNN]-YYYYMMDD.md
")
```

## List RFCs

```
/rfc list
```

```bash
# List all RFCs in architecture folder
echo "# RFC Registry"
echo ""
echo "| RFC | Title | Status | Date |"
echo "|-----|-------|--------|------|"
for f in .claude/reports/arch/RFC-*.md; do
    num=$(basename "$f" | grep -oE 'RFC-[0-9]+')
    title=$(head -1 "$f" | sed 's/^# //')
    status=$(grep -m1 "Status:" "$f" | sed 's/.*Status:\*\* //')
    date=$(grep -m1 "Created:" "$f" | sed 's/.*Created:\*\* //')
    echo "| $num | $title | $status | $date |"
done
```

## When to Write an RFC (Mobile)

| Change Type | RFC Required? |
|-------------|---------------|
| New module or feature package | ✅ Yes |
| State Management pattern change | ✅ Yes |
| New Core Library (Network, Storage) | ✅ Yes |
| Design System major update | ✅ Yes |
| CI/CD Pipeline change | ✅ Yes |
| Bug fix | ❌ No |
| UI tweak | ❌ No |

## RFC Output Location

- RFCs: `.claude/reports/arch/RFC-NNNN-[slug].md`
- Reviews: `.claude/reports/arch/review-RFC-NNNN-YYYYMMDD.md`
- Decisions: `.claude/reports/arch/decision-RFC-NNNN-YYYYMMDD.md`
