# User Stories and Acceptance Criteria

> **Note for students:** Each story below contains only one acceptance criterion.
> Your task is to read the implementation, identify the remaining behaviors,
> and write the missing acceptance criteria and tests yourself.

---

## Story 1 — Submit a Triage Case

**As an** operator,
**I want to** submit a new case with a description and severity level,
**so that** it enters the triage queue and can be addressed in priority order.

### Acceptance Criteria

1. **Given** I provide a description and a valid severity level,
   **when** I submit the case,
   **then** the system creates the case, assigns it a unique ID, and confirms the submission.

---

## Story 2 — Resolve a Triage Case

**As an** operator,
**I want to** mark a case as resolved by its ID,
**so that** the queue only shows cases that still need attention.

### Acceptance Criteria

1. **Given** a case exists in the queue,
   **when** I resolve it by its ID,
   **then** the system marks it as closed and it no longer appears in the active queue.
