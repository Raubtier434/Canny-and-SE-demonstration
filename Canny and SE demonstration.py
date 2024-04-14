import argparse
import numpy as np
import cv2
parser = argparse.ArgumentParser()
# Импортируются необходимые модули: argparse, numpy и cv2 (библиотека OpenCV).
Создается парсер аргументов командной строки с использованием argparse
parser.add_argument('-i', '--input', help='path to the input image', required=True)
      args = vars(parser.parse_args())
# Аргументы командной строки парсятся и сохраняются в переменную args	
image = cv2.imread(args['input'])# Входное изображение загружается при помощи cv2.imread() и сохраняется в переменную image.
orig_image = image.copy()# Создается копия входного изображения orig_image для дальнейшего использования.
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Изображение image преобразуется из цветового пространства BGR в RGB при помощи cv2.cvtColor().
image = image.astype(np.float32) / 255.0 # Изображение image нормализуется до значений от 0 до 1, разделив на 255, преобразовав в тип данных float32
gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY) # Оттенки серого и 
blurred = cv2.GaussianBlur(gray, (5, 5), 0)# Размытие для четкого обнаружения краев
canny = cv2.Canny(blurred, 50, 200) # Применяется алгоритм Canny для обнаружения границ на размытом изображении при помощи cv2.Canny().
edge_detector = cv2.ximgproc.createStructuredEdgeDetection('model.yml/model.yml')# Создается экземпляр структурированного детектора границ edge_detector при помощи cv2.ximgproc.createStructuredEdgeDetection().
edges = edge_detector.detectEdges(image)# Обнаружение границ проводится на изображении image при помощи метода detectedges() экземпляра edge_detector.
save_name = f"outputs/{args['input'].split('/')[-1].split('.')[0]}"# Показать и сохранить края изображения
# Ниже визуализация и сохранение результатов на диск 
cv2.imshow('Structured forests', edges)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.imwrite(f"{save_name}_forests.jpg", edges*255.0)
cv2.imwrite(f"{save_name}_canny.jpg", canny)