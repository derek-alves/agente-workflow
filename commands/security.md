---
description: Run security scan on codebase or specific path using security-mobile agent
---

# Security Scan Command (Mobile)

Invoke `security-mobile` agent for security analysis.

## Usage

```
/security [path]                    # Full OWASP Mobile scan
/security [path] --storage          # Insecure storage check
/security [path] --network          # Network config check
```

## Default Mode: Scan

```
Task(security-mobile, "
Mode: scan

Target: [path or entire codebase]

Perform comprehensive security scan:

1. OWASP Mobile Top 10 Check
   - M1: Improper Platform Usage
   - M2: Insecure Data Storage
   - M3: Insecure Communication
   - M4: Insecure Authentication
   - M5: Insufficient Cryptography
   - ...

2. Flutter Specifics
   - Detect SecureStorage vs SharedPreferences usage for sensitive data
   - Detect uncleartext traffic permitted (AndroidManifest/Info.plist)
   - Hardcoded API keys in Dart files

3. Dependency Vulnerabilities
   - Check `pubspec.lock` for vulnerable packages (using `dart pub outdated` if possible)

Output: .claude/reports/security/security-scan-[target]-YYYYMMDD.md
")
```

## Storage Focus

```
/security [path] --storage
```

```
Task(security-mobile, "
Mode: audit

Target: [path]

Audit Data Storage:
- Review all persistence implementations (Hive, SharedPrefs, SQFlite)
- Ensure PII/Tokens are NOT in plain text
- Verify use of `flutter_secure_storage` or EncryptedSharedPreferences

Output: .claude/reports/security/storage-audit-[target]-YYYYMMDD.md
")
```

## Network Focus

```
/security [path] --network
```

```
Task(security-mobile, "
Mode: audit

Target: [path]

Audit Network Security:
- Verify SSL Pinning implementation
- Check for cleartext traffic exceptions
- Review API Client configuration (timeouts, interceptors)

Output: .claude/reports/security/network-audit-[target]-YYYYMMDD.md
")
```

## Output Format

```markdown
# Mobile Security Scan Report

## Executive Summary
- **Risk Level:** Critical | High | Medium | Low
- **Critical Issues:** [count]

## Critical Findings

### SEC-001: [Title]
- **Severity:** Critical
- **Category:** [OWASP Mobile Category]
- **Location:** `[file:line]`
- **Description:** [what's wrong]
- **Recommendation:** [how to fix]

## Remediation Priority
1. **Immediate:** [critical issues to fix now]
2. **Short-term:** [high issues for next sprint]

## Scan Coverage
- Files scanned: [count]
```

## Integration with Review

Security scan is automatically included in `/review-full` as Level 3 when changes touch sensitive areas.
