from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.shortcuts import render
from .models import Conversation
from .services.openai_client import generate_response
from .services.intent_router import detect_intent
from .services.conversation_manager import build_message_history
from .utils.rate_limit import check_rate_limit
def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def advanced_chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body)
    msg = data.get("message", "")
    user_id = data.get("user", None)

    if not user_id:
        return JsonResponse({"error": "User ID required"}, status=400)

    user = User.objects.get(id=user_id)

    
    if not check_rate_limit(user):
        return JsonResponse({"reply": "Please wait a second before sending another message."})

    
    intent = detect_intent(msg)

    
    user_history = Conversation.objects.filter(user=user)

    
    messages = build_message_history(user_history, msg, intent)

    
    reply = generate_response(messages)

    
    Conversation.objects.create(user=user, message=msg, reply=reply)

    return JsonResponse({
        "intent": intent,
        "reply": reply,
        "model_used": "gpt-5.1"
    })
