# Hypothesis Log

A record of the debugging process — what was guessed, how it was tested, and what the outcome was.
Each bug follows the format: **Hypothesis → Test → Result**.

---

## Bug 1 — Whitespace-only description accepted

---

**Hypothesis 1:** The validation check might be missing entirely for edge-case inputs like spaces.

**Test:** Read the `submit()` method in `triage.py` and look for the description check.

**Result:** The check exists — `if not description`. But looking closely, a string of spaces is not falsy in Python. The check is there, it just does not account for whitespace-only strings. Narrowed down to the condition itself.

---

**Hypothesis 2:** The condition needs to strip whitespace before evaluating emptiness.

**Test:** Manually run `bool("   ")` in a Python shell.

**Result:** Returns `True` — confirming that `if not "   "` evaluates to `False`. Changed the condition to `if not description.strip()`. Re-ran `test_whitespace_only_description_raises_error`.

**Result:** Test passes. Bug 1 fixed.

---

## Bug 2 — Low-severity cases appear at the top of the queue

---

**Hypothesis 1:** The sort might be using `reverse=True`, flipping the order.

**Test:** Read `active_cases()` in `triage.py` and check the `sorted()` call.

**Result:** No `reverse=True` present. The sort call looks correct. The sort key uses `c.severity.value` — moved attention to the enum values themselves.

---

**Hypothesis 2:** The `Severity` enum values might be assigned incorrectly, causing the sort to behave backwards.

**Test:** Open a Python shell and print `Severity.CRITICAL.value` and `Severity.LOW.value`.

**Result:** `CRITICAL = 4`, `LOW = 1`. Sorting ascending puts the smallest number first, so `LOW` (1) sorts before `CRITICAL` (4). The values are inverted. Changed the enum to `CRITICAL = 1, HIGH = 2, MEDIUM = 3, LOW = 4`.

**Result:** `test_critical_case_appears_before_lower_severity` and `test_full_severity_ordering` both pass. Bug 2 fixed.

---

## Bug 3 — Resolving by ID resolves the wrong case

---

**Hypothesis 1:** The `resolve()` method might have a string comparison issue — perhaps comparing IDs with different casing or extra whitespace.

**Test:** Print the `case_id` argument and `case.id` inside the loop to compare them side by side.

**Result:** The IDs look identical in format. But noticed that the loop resolves a case on every run regardless of what ID is passed — even a completely made-up ID. The comparison is not the problem; the ID check might be missing entirely.

---

**Hypothesis 2:** The `if` condition inside the loop might not be checking `case.id` at all.

**Test:** Read the `resolve()` loop carefully.

**Result:** Confirmed — the condition is `if not case.resolved`, with no `case.id == case_id` check. The method resolves the first open case it finds and returns immediately. Added `case.id == case_id` back to the condition: `if case.id == case_id and not case.resolved`.

**Result:** `test_resolve_returns_the_correct_case`, `test_resolve_nonexistent_id_raises_error`, and `test_resolve_nonexistent_id_leaves_queue_unchanged` all pass. Bug 3 fixed.
