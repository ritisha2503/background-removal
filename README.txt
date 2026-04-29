Project Title:
Background Removal via K-Means

Description:
This project implements real-time background removal from a webcam feed using K-means clustering. 
Each frame captured from the webcam is segmented into clusters based on color. The largest cluster 
is assumed to correspond to the background. A mask is created to separate the foreground (person) 
from the background, and the background is replaced with a predefined stock image similar to a 
virtual background feature used in video conferencing platforms.

REQUIREMENTS:
The program requires the following software and libraries:

1. Python 3.8 or above
2. OpenCV (cv2)
3. NumPy

INSTALLATION:

Install the required libraries using pip:

pip install opencv-python
pip install numpy

FILES REQUIRED:

1. task2.py (main python script)
2. background.jpg (image used as virtual background)

Make sure the path of the background image in the code matches the location on your system.

RUNNING THE PROGRAM:

1. Connect a webcam to the system.
2. Open the terminal or command prompt.
3. Navigate to the project directory.
4. Run the program using:

python task2.py

OUTPUT WINDOWS:

The program will display three windows:

1. Webcam
   Shows the original webcam feed.

2. Clustered
   Shows the K-means clustered representation of the frame.

3. Virtual Background
   Shows the final output where the background is replaced by the chosen background image.

CONTROLS:

Press the key 'q' to exit the program.

NOTES:

• The frame is resized to a smaller resolution for faster K-means computation.
• The algorithm assumes the background occupies the largest region in the frame.
• Best results are obtained with a uniform background such as a plain wall.

AUTHOR:
Ritisha Bajaj