# OpenCV-Face-Recognition

Este repositorio contiene un proyecto de reconocimiento facial utilizando OpenCV, Python y técnicas de Deep Learning. El proyecto incluye scripts para codificar rostros desde un dataset de imágenes conocidas, y luego usar estas codificaciones para reconocer rostros en nuevas imágenes y videos.

## Estructura del Proyecto

El proyecto incluye los siguientes archivos y carpetas:

- `encode_faces.py`: Script para generar codificaciones de rostros a partir de un conjunto de imágenes conocidas.
- `recognize_faces_image.py`: Script para reconocer rostros en imágenes estáticas.
- `recognize_faces_video.py`: Script para reconocer rostros en videos en tiempo real.
- `known_people/`: Directorio que contiene subdirectorios con imágenes de personas conocidas. Cada subdirectorio debe tener el nombre de la persona.
- `unknown_pictures/`: Directorio que contiene imágenes para probar el reconocimiento facial.
- `encodings.pickle`: Archivo generado que almacena las codificaciones de rostros.

## Instalación

Para ejecutar los scripts, necesitas tener instalado Python y las siguientes bibliotecas:

- OpenCV
- dlib
- face_recognition
- imutils (opcional)

Puedes instalar estas dependencias con:

```bash
pip install opencv-python dlib face_recognition imutils
```

## Uso

### Generar codificaciones de rostros

Primero, debes generar las codificaciones de rostros a partir de tu conjunto de imágenes conocidas:

```bash
python encode_faces.py
```

Este script procesará las imágenes en `known_people/` y creará `encodings.pickle`.

### Reconocimiento facial en imágenes

Para reconocer rostros en imágenes estáticas, usa:

```bash
python recognize_faces_image.py
```

### Reconocimiento facial en videos

Para reconocer rostros en tiempo real a través de una cámara web, usa:

```bash
python recognize_faces_video.py
```