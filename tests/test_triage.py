import pytest
from triage import TriageQueue, Severity


# ---------------------------------------------------------------------------
# Story 1 — Submit a Triage Case
# ---------------------------------------------------------------------------

# AC 1: System creates the case, assigns a unique ID, and confirms submission
def test_submit_creates_case_with_correct_fields():
    queue = TriageQueue()
    case = queue.submit("Server is down", "critical")
    assert case.description == "Server is down"
    assert case.severity == Severity.CRITICAL
    assert case.id is not None
    assert case.resolved is False


def test_submitted_cases_have_unique_ids():
    queue = TriageQueue()
    case1 = queue.submit("First issue", "high")
    case2 = queue.submit("Second issue", "high")
    assert case1.id != case2.id


# AC 2: Empty description is rejected
def test_empty_description_raises_error():
    queue = TriageQueue()
    with pytest.raises(ValueError, match="cannot be empty"):
        queue.submit("", "high")




# AC 3: Invalid severity is rejected with a helpful message
def test_invalid_severity_raises_error():
    queue = TriageQueue()
    with pytest.raises(ValueError):
        queue.submit("Valid description", "urgent")


def test_invalid_severity_error_lists_valid_options():
    queue = TriageQueue()
    with pytest.raises(ValueError, match="Critical"):
        queue.submit("Valid description", "P1")


# AC 4: Same-severity cases appear oldest-first
def test_same_severity_cases_ordered_oldest_first():
    queue = TriageQueue()
    case1 = queue.submit("First high case", "high")
    case2 = queue.submit("Second high case", "high")
    cases = queue.active_cases()
    assert cases[0].id == case1.id
    assert cases[1].id == case2.id

# ---------------------------------------------------------------------------
# Story 2 — Resolve a Triage Case
# ---------------------------------------------------------------------------

# AC 1: Resolved case no longer appears in the active queue
def test_resolved_case_removed_from_active_queue():
    queue = TriageQueue()
    case = queue.submit("Fix login bug", "medium")
    queue.resolve(case.id)
    assert len(queue.active_cases()) == 0



# AC 4: After resolving the only Critical case, next highest severity is first
def test_resolving_critical_promotes_next_severity():
    queue = TriageQueue()
    critical = queue.submit("Critical outage", "critical")
    queue.submit("High issue", "high")
    queue.resolve(critical.id)
    cases = queue.active_cases()
    assert cases[0].severity == Severity.HIGH


# AC 5: Queue shows empty message after last case is resolved
def test_queue_is_empty_after_resolving_last_case():
    queue = TriageQueue()
    case = queue.submit("Only case", "low")
    queue.resolve(case.id)
    assert queue.is_empty() is True


# ---------------------------------------------------------------------------
# Story 3 — Show a Triage Case
# ---------------------------------------------------------------------------

