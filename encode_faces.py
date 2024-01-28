# encode_faces.py

import face_recognition
import cv2
import pickle
import os

# Ruta al directorio del dataset de caras
dataset_path = './known_people/'
# Archivo para guardar las codificaciones
encoding_file = 'encodings.pickle'
# Método de detección (hog o cnn)
detection_method = 'hog'

# Inicializar la lista de codificaciones conocidas y nombres
knownEncodings = []
knownNames = []

# Recorrer las carpetas del dataset
for label in os.listdir(dataset_path):
    dir_path = os.path.join(dataset_path, label)

    if not os.path.isdir(dir_path):
        continue

    # Recorrer los archivos de cada carpeta
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        # Cargar imagen y convertir de BGR (OpenCV) a RGB (dlib)
        image = face_recognition.load_image_file(file_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detectar coordenadas (x, y) de los cuadros delimitadores correspondientes a cada cara
        boxes = face_recognition.face_locations(rgb, model=detection_method)

        # Computar las incrustaciones faciales para cada cara
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(label)

# Guardar codificaciones de rostros
with open(encoding_file, 'wb') as f:
    f.write(pickle.dumps({'encodings': knownEncodings, 'names': knownNames}))

print("Codificaciones de rostros guardadas en", encoding_file, knownNames)