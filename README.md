Attendify – Face Recognition Based Attendance System
Attendify is a Python-based desktop application designed to automate and modernize the student attendance process using facial recognition technology. It combines the capabilities of OpenCV for real-time webcam integration, the face_recognition library for identity verification, and Tkinter for an intuitive graphical user interface.
This project is ideal for classrooms, training sessions, or any environment where maintaining accurate attendance records is essential and efficiency is a priority.

Features
Live Webcam Integration – Captures images in real-time using the device's webcam.
Face Recognition – Identifies and matches faces using the face_recognition library.
Automated Attendance Logging – Records student name, date, and time into a structured Excel file.
Excel File Generation – Creates and appends to attendance.xlsx located in the attendance_logs directory.
Audio Feedback – Beep sound notifications for success or failure events (requires Windows OS)
Error Handling – Displays status messages for failed detection, unrecognized faces, or camera issues.
Modern GUI – Clean and interactive interface using Tkinter.
Easy Face Dataset Setup – Place .jpg or .png images named after students in the known_faces folder.

Folder Structure
├── main.py                   # Main application script
├── attendance_logs/          # Auto-created folder for Excel logs
├── known_faces/              # Folder containing images of known users

How It Works
Load Known Faces: The application reads all images from the known_faces directory and encodes them using the face_recognition library.
Capture Face: When the user clicks "Mark Attendance," the webcam activates and captures a frame.
Face Matching: The captured image is compared against the known encodings.
Attendance Logging: If a match is found, the student's name along with the current date and time is appended to attendance.xlsx.
Feedback Display: The GUI updates with recognition status and plays a sound accordingly.

Requirements
Python 3.10.x (i prefer this because it is more stable and can handle face_recognition library easily)
OpenCV (cv2)
face_recognition
pandas
tkinter (pre-installed with Python)
winsound (for Windows sound feedback)

How to Use
Clone or download the repository.
Install dependencies using pip install -r requirements.txt.
Add student face images to the known_faces/ folder with filenames as their names (e.g., john_doe.jpg).
Run the application using:
python main.py
Use the GUI to mark attendance.
