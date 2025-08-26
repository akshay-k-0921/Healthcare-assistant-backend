from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_ai_response

class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response({"error": "Message is required"}, status=400)
        
        ai_reply = get_ai_response(user_message)
        return Response({"reply": ai_reply})
