from django.shortcuts import render
import os
import logging
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .utils import QRCodeProcessor

# Set up logging
logger = logging.getLogger(__name__)


class QRCodeReaderAPI(APIView):
    """
    API View for reading QR codes from uploaded images and storing them in the database.
    """

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            image_file = request.FILES.get("image")
            if not image_file:
                logger.warning("No image file was provided.")
                return Response({"error": "No image file provided"}, status=400)

            temp_image_path = os.path.join(settings.MEDIA_ROOT, "temp_image.png")
            with open(temp_image_path, "wb+") as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            processor = QRCodeProcessor()
            result = processor.process_image(temp_image_path)

            os.remove(temp_image_path)

            return Response(result)
        except Exception as e:
            logger.exception(
                f"An error occurred while processing the request: {str(e)}"
            )
            return Response(
                {"error": "An error occurred while processing the request"}, status=500
            )
