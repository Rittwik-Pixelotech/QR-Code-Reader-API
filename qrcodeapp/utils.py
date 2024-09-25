from pyzbar.pyzbar import decode
from PIL import Image
from .models import QRCode


class QRCodeProcessor:

    def process_image(self, image_path):
        """
        Detects and decodes QR codes from the given image and stores them in the database.
        :param image_path: Path to the image file.
        :return: List of decoded QR codes and their positions.
        """
        try:
            image = Image.open(image_path)
            qr_codes = decode(image)
            return self._store_and_format_response(qr_codes)
        except Exception as e:
            return {"error": str(e)}

    def _store_and_format_response(self, qr_codes):
        """
        Stores the decoded QR codes into the database and formats the response.
        :param qr_codes: List of detected QR code objects.
        :return: JSON formatted response containing QR code content and coordinates.
        """
        response = {"qr_codes": []}
        for qr_code in qr_codes:
            content = qr_code.data.decode("utf-8")
            x_position = qr_code.rect.left
            y_position = qr_code.rect.top

            # Save QR code details in the database
            qr_code_obj = QRCode(
                content=content, x_position=x_position, y_position=y_position
            )
            qr_code_obj.save()

            # Add to the response
            data = {"content": content, "x": x_position, "y": y_position}
            response["qr_codes"].append(data)
        return response
