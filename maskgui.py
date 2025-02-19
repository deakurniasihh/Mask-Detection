#import Libary
import sys
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class ShowImage(QMainWindow): #membuat q main window
    def __init__(self): #membuat function
        super(ShowImage, self).__init__() #memangill show image main window
        loadUi('gui.ui', self) #meload gui
        self.Image = None #menyimpan gambar yang dimuat
        self.loadBtn.clicked.connect(self.loadClicked)
        self.detectBtn.clicked.connect(self.imgMaskDetect)
        self.openCamBtn.clicked.connect(self.maskDetect)

    def loadClicked(self): #membuat function
        image, filter = QFileDialog.getOpenFileName(self, 'Open file',
                                                    'D:\\Kuliah\\Semester 4\\Pengolahan Citra Digital\\Pendeteksi masker')  # memilih foto yang diingikan
        self.loadImage(image)  # menginputkan gambar

    def loadImage(self, flname): #membuat function
        self.Image = cv2.imread(flname) #memuat gambar yaang diberikan fungsi cv2  akan disimpan di atribut image dan inisialisaidi self
        self.displayImage() #menampilkan image

    def displayImage(self, windows=1):
        qformat = QImage.Format_Indexed8
        #memformat Image

        if len(self.Image.shape) == 3:
            if (self.Image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888

            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.Image, self.Image.shape[1], self.Image.shape[0], self.Image.strides[0],
                     qformat)

        img = img.rgbSwapped()

        if windows == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.imgLabel.setScaledContents(True)

        if windows == 2:
            self.imgLabel2.setPixmap(QPixmap.fromImage(img))
            self.imgLabel2.setAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.imgLabel2.setScaledContents(True)



    def imgMaskDetect(self):
        # haarcascade yang digunakan
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        # Load model Haar cascade masker
        mask_cascade = cv2.CascadeClassifier('haarcascade_mask.xml')

        frame = self.Image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # deteksi wajah
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Deteksi mata
            eye = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye:  # untuk setiap mata yang terdeteksi
                # roi color, letak pixel yang digunakan untuk menggambar persegi panjang, warna green, dan ketebalan garis
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                # frame,text eye, letak pixel yang digunakan untuk menulis teks, ketebalan font, ukuran font,
                # warna green, dan ketebalan teks
                cv2.putText(frame, 'eye', (x + ex, y + ey), 1, 2, (0, 255, 0), 2)

            # Deteksi masker
            masks = mask_cascade.detectMultiScale(roi_gray)
            if len(masks) == 0:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(frame, 'Mask Off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(frame, 'Mask On', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

        cv2.putText(frame, 'jumlah wajah : ' + str(len(faces)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        self.Image = frame
        self.displayImage(2)

    def maskDetect(self):
        # haarcascade yang digunakan
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        # Load model Haar cascade masker
        mask_cascade = cv2.CascadeClassifier('haarcascade_mask.xml')

        # Load video
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Deteksi wajah
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                #Deteksi masker
                masks = mask_cascade.detectMultiScale(roi_gray)
                if len(masks) == 1: #jika tidak ada makser yang terdeteksi
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    cv2.putText(frame, 'Mask Off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(frame, 'Mask On', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

            # cv2.putText(frame, 'Jumlah Wajah: ' + str(len(faces)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
            #             2)
            cv2.imshow('Face and Mask Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

app = QtWidgets.QApplication(sys.argv) #membuat objek QApplication yang merupakan inti dari aplikasi Qt
windows = ShowImage() #untuk membuat window pada aplikasi GUI
windows.setWindowTitle('Face Mask Detection') #mengatur judul window pada aplikasi GUI
windows.show() #memunculkan window gui pada layar/screen
sys.exit(app.exec_()) #untuk keluar dari aplikasi GUI