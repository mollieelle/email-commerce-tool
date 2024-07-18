from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmailDraft
from .serializers import EmailDraftSerializer
import logging

# Set up logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def create_email_draft(request):
    if request.method == 'POST':
        serializer = EmailDraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Log validation errors
        logger.error('Validation errors: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)