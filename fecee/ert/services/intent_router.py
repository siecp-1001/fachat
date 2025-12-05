def detect_intent(message):
    message = message.lower()
    
    if "refund" in message or "return" in message:
        return "billing"

    if "price" in message or "buy" in message or "order" in message:
        return "sales"

    if "problem" in message or "not working" in message or "error" in message:
        return "technical"

    return "general"
