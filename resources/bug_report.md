# Bug Report

Three bugs are present in `triage.py`. Each one deviates from a specific acceptance criterion.
Run `pytest` to see which tests fail, then use this report to guide your investigation.

---

## Bug 1 — Whitespace-only descriptions are accepted

**File:** `triage.py` — `TriageQueue.submit()`

**Acceptance Criteria violated:** Story 1, AC 2
> "Given I leave the description empty, when I submit the case, then the system rejects the submission and tells me a description is required."

**How to replicate:**

```python
from triage import TriageQueue

queue = TriageQueue()
case = queue.submit("   ", "high")  # should raise ValueError — it does not
print(case.description)             # prints an empty string
```

**What goes wrong:**
The validation checks whether the raw input string is falsy (`if not description`). A string of spaces is not falsy, so it passes the check. The description is then stripped before being stored, meaning the case is created with an empty description — silently.

**Failing test:** `test_whitespace_only_description_raises_error`

---

## Bug 2 — Low-severity cases appear at the top of the queue

**File:** `triage.py` — `Severity` enum

**Acceptance Criteria violated:** Story 1, AC 5
> "Given I submit a case successfully, when I view the queue, then the new case appears in the correct position based on its severity."

**How to replicate:**

```python
from triage import TriageQueue

queue = TriageQueue()
queue.submit("Low priority task", "low")
queue.submit("Critical outage", "critical")

cases = queue.active_cases()
print(cases[0].severity.label())  # prints "Low" — should print "Critical"
```

**What goes wrong:**
The `Severity` enum assigns numeric values in reverse order (`CRITICAL = 4`, `LOW = 1`). When cases are sorted ascending by `severity.value`, lower numbers sort first — so `LOW` (value 1) appears before `CRITICAL` (value 4).

**Failing tests:** `test_critical_case_appears_before_lower_severity`, `test_full_severity_ordering`

---

## Bug 3 — Resolving by ID resolves the wrong case

**File:** `triage.py` — `TriageQueue.resolve()`

**Acceptance Criteria violated:** Story 2, AC 3
> "Given I enter an ID that does not match any open case, when I attempt to resolve it, then the system displays an error and no cases in the queue are affected."

**How to replicate:**

```python
from triage import TriageQueue

queue = TriageQueue()
real_case = queue.submit("Real case", "medium")

queue.resolve("totally-fake-id")  # should raise ValueError — it does not
print(len(queue.active_cases()))  # prints 0 — real_case was silently resolved
```

**What goes wrong:**
The `resolve()` loop checks only whether a case is unresolved (`if not case.resolved`) — it never compares `case.id` to the `case_id` argument. This means the method always resolves the first open case it finds, regardless of which ID was passed in.

**Failing tests:** `test_resolve_returns_the_correct_case`, `test_resolve_nonexistent_id_raises_error`, `test_resolve_nonexistent_id_leaves_queue_unchanged`
