# Triage Application

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Test

```bash
pytest
```

## Deactivate virtual environment

```bash
deactivate
```

---

## How to Use

When you run the app you will see a menu with four options:

```
=== Triage Application ===

1. View queue
2. Submit case
3. Resolve case
4. Quit
```

### 1. View queue

Displays all open cases sorted by severity — Critical cases appear first, then High, Medium, and Low. Cases at the same severity level are shown oldest-first.

```
#     ID         Severity   Description
-------------------------------------------------------
1     3a2f1b4c   Critical   Database server unresponsive
2     9d4e7a1f   High       Login page returning 500 error
3     1c8b2d9e   Medium     Report export running slowly
```

### 2. Submit a case

You will be prompted for two things:

- **Description** — a plain-English summary of the issue (cannot be empty)
- **Severity** — one of: `Critical`, `High`, `Medium`, or `Low` (case-insensitive)

```
Description: Login page returning 500 error
Severity (Critical / High / Medium / Low): High

Case submitted. ID: 9d4e7a1f | Severity: High
```

If you enter an invalid severity or an empty description, the app will display an error and return you to the menu without creating a case.

### 3. Resolve a case

You will be prompted for the case ID shown in the queue. Once resolved, the case is permanently removed from the active queue.

```
Enter case ID to resolve: 3a2f1b4c

Resolved — [Critical] Database server unresponsive (ID: 3a2f1b4c)
```

If the ID does not match any open case, the app will display an error and nothing in the queue will change.

### 4. Quit

Exits the application. All cases are held in memory only — they will not persist after the app closes.
