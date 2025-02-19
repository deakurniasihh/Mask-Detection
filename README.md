Wearing a mask can prevent respiratory droplets from spreading into the environment and being inhaled by others. For example, masks were used during the COVID-19 pandemic, a highly contagious viral infection caused by SARS-CoV-2. As of May 24, 2022, WHO recorded over 523 million confirmed cases and more than six million deaths worldwide, including six million cases and 156 thousand deaths in Indonesia. Transmission occurs through direct contact, contaminated objects, and airborne particles. Additionally, masks protect healthcare workers from nosocomial infections. Although the pandemic has officially ended, maintaining good health remains essential. Therefore, an application has been developed to detect mask usage and raise health awareness.

• Operation Greyscale 
Determines the width and height of the image. Then multiply the pixel value into the grayscale formula which is 0.299 * R + 0.587 * G + 0.114 * B. The last entry of the pixels value that has been converted to gray scale into the array.

• Operation Face Detection 
Start face detection using face_cascade.detectMultiScale(). Once the face is detected, determine the position and also the size of the face.

• Operation Eyes Detection 
Perform eye detection On ROI (Region Of Interest) using eye_cascade.detectMultiScale() in ROI which is a grayscale image of the face part.

• Operation Nose Detetction
Detect nose using nose_cascade.detectMultiScale() in ROI which is a grayscale image of the face part

We used 10 sample test objects including close and distant photos, and we also tested photos that have more than one face. Out of ten sample tests, 7 of them were correctly detected (70%). 

One of the causes of miss detection is because the nose objects are too small and undetected and also the lighting factors have an influence on the detection.

• Photo One More Object
![Image](https://github.com/user-attachments/assets/d22459c7-7fa9-45e6-8bfa-138764c64972)

• Object One More Object
![Image](https://github.com/user-attachments/assets/75122df4-85b8-4cce-b9fe-0bc1af683a14)

• Photo From Close Distance
![Image](https://github.com/user-attachments/assets/3f5cec5a-6ae9-4afb-b870-ec9b0c27fb37)

• Object From Close Distance
![Image](https://github.com/user-attachments/assets/32e7e953-f15f-44d5-b07a-3650284dc989)

• Object From Long Distance 
![Image](https://github.com/user-attachments/assets/5481f27e-a10f-4202-a82a-8cfe776cdb4f)
