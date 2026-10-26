def call_agent(user_input: str) -> dict:
    text = user_input.lower()
    tool = None

    if "support hours" in text:
        reply = "Our support hours are 9 AM to 6 PM, Monday to Friday."
    elif "reset my password" in text:
        reply = "You can reset your password from the login page using Forgot Password."
    elif "balance of user 99" in text:
        reply = "I cannot share another user's information."
    elif "balance" in text and "logged in" in text:
        tool = "get_balance"
        reply = "Your balance is available in your account summary."
    elif "balance" in text:
        reply = "Please log in first so I can check your balance."
    elif "ignore your rules" in text:
        reply = "I cannot do that."
    elif "recipe" in text:
        reply = "I can only help with banking questions."
    elif text.strip() == "transfer it.":
        reply = "Could you clarify what you want to transfer, and to where?"
    elif "platinum galaxy" in text:
        reply = "I do not have information about that account."
    elif "transfer 500" in text:
        tool = "transfer_funds_pending"
        reply = "Please confirm: transfer 500 to account 1234?"
    else:
        reply = "I am not sure how to help with that."

    return {"reply": reply, "tool_called": tool}