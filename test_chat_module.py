import chat_module

def test_validate_chat_json():
    """A test for validate_chat_json"""
    test = "test_files/chat_test.json"
    data = chat_module.validate_chat_json(test)
    assert data == {"message_id": 1, "conversation_id": 1, "sender_id": 1234, "recipient_id": 5678,
                    "message_date": "2001-01-24 12:30:55", "message_txt": "This is a message!"}
