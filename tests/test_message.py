from datetime import date
from app.models.message import Message


def test_message_instance_created_when_details_are_not_blank():
    message = Message(
        message_id="msg-001",
        date=date(2026, 6, 11),
        message_summary="Patient reports chest pain since this morning.",
    )

    assert isinstance(message, Message)
