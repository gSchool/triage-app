# User Stories and Acceptance Criteria

---

## Story 1 — Submit a Triage Case

**As an** operator,
**I want to** submit a new case with a description and severity level,
**so that** it enters the triage queue and can be addressed in priority order.

### Acceptance Criteria

1. **Given** I provide a description and a valid severity level,
   **when** I submit the case,
   **then** the system creates the case, assigns it a unique ID, and confirms the submission.


2. **Given** I enter a severity level that is not Critical, High, Medium, or Low,
   **when** I submit the case,
   **then** the system rejects the submission and lists the valid severity options.

3. **Given** I submit multiple cases with the same severity level,
   **when** I view the queue,
   **then** cases at the same severity are shown oldest-first.

4. **Given** I submit a case successfully,
   **when** I view the queue,
   **then** the new case appears in the correct position based on its severity.

---

## Story 2 — Resolve a Triage Case

**As an** operator,
**I want to** mark a case as resolved by its ID,
**so that** the queue only shows cases that still need attention.

### Acceptance Criteria

1. **Given** a case exists in the queue,
   **when** I resolve it by its ID,
   **then** the system marks it as closed and it no longer appears in the active queue.

2. **Given** I resolve a case,
   **when** the action completes,
   **then** the system confirms which case was closed and displays its description and severity.

3. **Given** I enter an ID that does not match any open case,
   **when** I attempt to resolve it,
   **then** the system displays an error and no cases in the queue are affected.

4. **Given** the queue has cases at multiple severity levels,
   **when** I resolve the only Critical case,
   **then** the next case shown at the top of the queue is the highest-severity remaining case.

5. **Given** I resolve the last remaining case,
   **when** I view the queue afterward,
   **then** the system displays a message indicating the queue is empty.
