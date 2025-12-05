from .message_builder import system_messages

def build_message_history(conversation_queryset, new_user_message, intent):
    history = system_messages[intent][:]  # Load system profile for the bot

    for conv in conversation_queryset:
        history.append({"role": "user", "content": conv.message})
        history.append({"role": "assistant", "content": conv.reply})

    history.append({"role": "user", "content": new_user_message})

    return history
