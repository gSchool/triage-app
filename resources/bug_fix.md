# Bug Fix Reference

All three bugs were in `triage.py`. Each fix is a single-line change.

---

## Fix 1 — Whitespace-only descriptions now correctly rejected

**File:** `triage.py` — `TriageQueue.submit()`

**Before:**
```python
if not description:
```

**After:**
```python
if not description.strip():
```

**Why it works:**
`"   "` (spaces only) is a non-empty string, so `if not description` evaluates to `False` and the check is skipped. Adding `.strip()` removes leading and trailing whitespace before the check, so a string of spaces collapses to `""` and correctly raises the error.

---

## Fix 2 — Severity values restored to correct order

**File:** `triage.py` — `Severity` enum

**Before:**
```python
class Severity(Enum):
    CRITICAL = 4
    HIGH = 3
    MEDIUM = 2
    LOW = 1
```

**After:**
```python
class Severity(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4
```

**Why it works:**
`active_cases()` sorts by `severity.value` ascending. With the inverted values, `LOW` (1) sorted before `CRITICAL` (4). Restoring the correct mapping means `CRITICAL` (1) now sorts first, which is the intended behavior.

---

## Fix 3 — resolve() now matches by case ID

**File:** `triage.py` — `TriageQueue.resolve()`

**Before:**
```python
for case in self._cases:
    if not case.resolved:
        case.resolve()
        return case
```

**After:**
```python
for case in self._cases:
    if case.id == case_id and not case.resolved:
        case.resolve()
        return case
```

**Why it works:**
The original condition only checked whether a case was open — it never compared `case.id` to the requested `case_id`. Adding `case.id == case_id` ensures the method resolves exactly the requested case, and passes through to the `ValueError` at the end of the loop when no match is found.
