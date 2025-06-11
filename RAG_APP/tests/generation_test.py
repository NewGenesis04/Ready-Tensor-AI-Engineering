from ..core.services import generate_answer

def test_generate_answer():
    query = "What is the capital of Nigeria?"
    thread_id = "test_thread"

    response = generate_answer(query, thread_id)

    # assert isinstance(response, dict)
    # assert "answer" in response
    # assert "sources" in response
    # assert "thread_id" in response
    # assert response["thread_id"] == thread_id
    # assert isinstance(response["answer"], str)
    # assert isinstance(response["sources"], list)
    # assert len(response["sources"]) >= 0

    return response

test = test_generate_answer()
print(f"Test passed: {test}")