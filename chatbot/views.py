from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ChatMessage, Conversation
from .serializers import ChatMessageSerializer
from .services import get_ai_response

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_input = request.data.get("message")
        if not user_input:
            return Response({"error": "Message is required"}, status=400)

        # Create or get conversation
        conversation = Conversation.objects.filter(user=request.user).last()
        if not conversation:
            conversation = Conversation.objects.create(user=request.user)

        # Save user message
        user_msg = ChatMessage.objects.create(conversation=conversation, role="user", message=user_input)

        # Get AI response
        ai_text = get_ai_response(user_input, user=request.user)
        ai_msg = ChatMessage.objects.create(conversation=conversation, role="assistant", message=ai_text)

        return Response({
            "user_message": ChatMessageSerializer(user_msg).data,
            "ai_message": ChatMessageSerializer(ai_msg).data
        })
