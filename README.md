# Passport_Size_Photo_Cropping
Using OpenCV face recognition to detect face from a picture and crop passport size photo for that face. The passport size photo is calculated from the face detected using simple mathematical calculations.

### The project involves:
1. Detecting the face from the pictures inside the original folder.
2. Cutting a frame of passport photo size around that face.
3. Saving the cropped pic in a cropped folder. If face is not detected then saving it in not detected folder.

### Machine Learning Modules Used: 
+ OpenCV - To detect face from input image and creating the output image.
+ OS - For reading images from input folder and saving the output images to the respective folders.

## Sample Input Images :

<img align="center" src="Original_Images/sample5.jpg?raw=true" width="250"> <img align="center" src="Original_Images/sample8.jpg?raw=true" width="250"> <img align="center" src="Original_Images/sample6.jpg?raw=true" width="250">

## Sample Output Images :

<img align="top" src="Cropped_Images/sample5.jpg?raw=true" width="250"> <img align="top" src="Cropped_Images/sample6.jpg?raw=true" width="250"> <img align="top" src="Cropped_Images/sample8.jpg?raw=true" width="250">