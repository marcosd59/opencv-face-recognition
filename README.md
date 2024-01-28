# Proyecto de Reconocimiento Facial con OpenCV y Python

## Descripción
Este proyecto implementa un sistema de reconocimiento facial utilizando OpenCV, Python y aprendizaje profundo. El sistema puede identificar rostros en imágenes y videos en tiempo real. Se basa en el uso de la biblioteca `face_recognition` junto con OpenCV para el procesamiento de imágenes y el manejo de videos.

## Características
- Reconocimiento facial en imágenes estáticas.
- Reconocimiento facial en video en tiempo real.
- Uso de codificaciones faciales y algoritmos de aprendizaje profundo.

## Requisitos Previos
- Python 3.x
- OpenCV
- dlib
- face_recognition
- imutils

## Instalación
Para instalar las dependencias necesarias, ejecute el siguiente comando:

```bash
pip install opencv-python dlib face_recognition imutils
```

## Estructura del Proyecto
- `encode_faces.py`: Script para generar codificaciones de rostros a partir de un dataset de imágenes.
- `recognize_faces_image.py`: Script para reconocer rostros en imágenes estáticas.
- `recognize_faces_video.py`: Script para reconocer rostros en video en tiempo real.
- `dataset/`: Directorio para almacenar el dataset de rostros.
- `models/`: Directorio para almacenar modelos entrenados y codificaciones.
- `README.md`: Este archivo.

## Uso
1. **Codificación de Rostros**:
   - Coloque las imágenes en el directorio `dataset/`.
   - Ejecute `python encode_faces.py`.

2. **Reconocimiento en Imágenes**:
   - Ejecute `python recognize_faces_image.py --image path/to/image.jpg`.

3. **Reconocimiento en Video**:
   - Ejecute `python recognize_faces_video.py`.

## Autores
- Marcos Damián Pool Canul