from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List
import uuid


class Severity(Enum):
    CRITICAL = 4  # BUG 2: values are inverted — LOW sorts before CRITICAL
    HIGH = 3
    MEDIUM = 2
    LOW = 1

    @classmethod
    def from_string(cls, value: str) -> "Severity":
        mapping = {
            "critical": cls.CRITICAL,
            "high": cls.HIGH,
            "medium": cls.MEDIUM,
            "low": cls.LOW,
        }
        normalized = value.strip().lower()
        if normalized not in mapping:
            raise ValueError(
                f"'{value}' is not valid. Choose from: Critical, High, Medium, Low."
            )
        return mapping[normalized]

    def label(self) -> str:
        return self.name.capitalize()


@dataclass
class Case:
    description: str
    severity: Severity
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: datetime = field(default_factory=datetime.now)
    resolved: bool = False

    def resolve(self) -> None:
        self.resolved = True


class TriageQueue:
    def __init__(self):
        self._cases: List[Case] = []

    def submit(self, description: str, severity_input: str) -> Case:
        if not description:  # BUG 1: missing .strip() — whitespace-only descriptions are accepted
            raise ValueError("Description cannot be empty.")
        severity = Severity.from_string(severity_input)
        case = Case(description=description.strip(), severity=severity)
        self._cases.append(case)
        return case

    def active_cases(self) -> List[Case]:
        open_cases = [c for c in self._cases if not c.resolved]
        return sorted(open_cases, key=lambda c: (c.severity.value, c.created_at))

    def resolve(self, case_id: str) -> Case:
        for case in self._cases:
            if not case.resolved:  # BUG 3: ID is never checked — resolves first open case regardless of case_id
                case.resolve()
                return case
        raise ValueError(f"No open case found with ID '{case_id}'.")

    def is_empty(self) -> bool:
        return len(self.active_cases()) == 0
