# import Libary
import cv2

# jika memakai masker maka berniali tidak benar
mask_on = False

# haarcascade yang digunakan
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

# load video
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah

    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Deteksi mata
        eye = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.putText(frame, 'eye', (x + ex, y + ey), 1, 2, (0, 255, 0), 2)

        # Deteksi hidung
        nose = nose_cascade.detectMultiScale(gray, 1.18, 35)
        for (sx, sy, sw, sh) in nose:
            cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)
            cv2.putText(frame, 'nose', (x + sx, y + sy), 1, 3, (255, 0, 0), 2)

        if len(nose) == 0:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(frame, 'Mask on', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(frame, 'Mask off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

    cv2.putText(frame, 'jumlah wajah : ' + str(len(face)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Face', frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# # import Libary
# import sys
# import cv2
# import numpy as np
# from PyQt5 import QtCore, QtWidgets, QtGui
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUi
#
# class ShowImage(QMainWindow):
#     #membuat fungsi __init__
#     def __init__(self):
#         loadUi('gui.ui', self)  #meload gui
#         self.Image = None
#         self.pushButton.clicked.connect(self.camStart)
#
#     def camstart(self):
#         #jika memakai masker maka berniali tidak benar
#         mask_on = False
#
#         #haarcascade yang digunakan
#         face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#         eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#         nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
#
#         # load video
#         cap = cv2.VideoCapture(0)
#
#         while True:
#             _, frame = cap.read()
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#             # deteksi wajah
#
#             face = face_cascade.detectMultiScale(gray, 1.3, 5)
#             for (x, y, w, h) in face:
#                 if mask_on:
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
#                     cv2.putText(frame, 'Mask off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#                 else:
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(frame, 'Mask on', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#
#                 roi_gray = gray[y:y + h, x:x + w]
#                 roi_color = frame[y:y + h, x:x + w]
#
#                 # Deteksi mata
#                 eye = eye_cascade.detectMultiScale(roi_gray)
#                 for (ex, ey, ew, eh) in eye:
#                     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#                     cv2.putText(frame, 'eye', (x + ex, y + ey), 1, 2, (0, 255, 0), 2)
#
#                     # Deteksi hidung
#                     nose = nose_cascade.detectMultiScale(gray, 1.18, 35)
#                     for (sx, sy, sw, sh) in nose:
#                         cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)
#                         cv2.putText(frame, 'nose', (x + sx, y + sy), 1, 3, (255, 0, 0), 2)
#
#                     if len(nose)>0:
#                         mask_on = True
#                     else:
#                         mask_on = False
#
#             cv2.putText(frame, 'jumlah wajah : ' + str(len(face)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             cv2.imshow('Face', frame)
#
#             if cv2.waitKey(30) & 0xff == ord('q'):
#                 break
#
#         cap.release()
#         cv2.destroyAllWindows()
#
# app = QtWidgets.QApplication(sys.argv)
# windows = ShowImage()
# windows.setWindowTitle('Show Image GUI')
# windows.show()
# sys.exit(app.exec_())

#image
# import cv2
# #jika memakai masker maka berniali tidak benar
# mask_on = False
#
# # haarcascade yang digunakan
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
#
# # load citra
# image_path = 'mask.jpg'
# frame = cv2.imread(image_path)
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# # deteksi wajah
# face = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x, y, w, h) in face:
#     roi_gray = gray[y:y + h, x:x + w]
#     roi_color = frame[y:y + h, x:x + w]
#
#     # Deteksi mata
#     eye = eye_cascade.detectMultiScale(roi_gray)
#     for (ex, ey, ew, eh) in eye:
#         cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#         cv2.putText(frame, 'eye', (x + ex, y + ey), 1, 2, (0, 255, 0), 2)
#
#     # Deteksi hidung
#     nose = nose_cascade.detectMultiScale(gray, 1.18, 35)
#     for (sx, sy, sw, sh) in nose:
#         cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)
#         cv2.putText(frame, 'nose', (x + sx, y + sy), 1, 3, (255, 0, 0), 2)
#
#     if len(nose)<1:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
#         cv2.putText(frame, 'Mask on', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#     else:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
#         cv2.putText(frame, 'Mask off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
#
# cv2.putText(frame, 'jumlah wajah : ' + str(len(face)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# cv2.imshow('Face', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()