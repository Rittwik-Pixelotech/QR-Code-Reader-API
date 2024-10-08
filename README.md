# QR-Code-Reader-API

## Overview

This Django-based API processes images to detect and decipher QR codes using the `pyzbar` library. 
It extracts the embedded information within each QR code and returns it in a structured JSON format, including the position of each QR code.

## Features:
- Upload an image containing QR codes.
- Detect multiple QR codes within a single image.
- Extract content and position for each QR code.
- Structured JSON response format.
- Logging for debugging and monitoring.

## Tech Stack:
- **Python 3.11.9**
- **Django 5.1.1**
- **Django REST Framework**
- **pyzbar**
- **Pillow**

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rittwik-Pixelotech/QR-Code-Reader-API.git
   cd django-qr-code-reader
