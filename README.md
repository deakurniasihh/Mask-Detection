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
