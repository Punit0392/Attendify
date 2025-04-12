import tkinter as tk
import cv2
import face_recognition
import pandas as pd
from datetime import datetime
import os
import threading
import winsound 

known_faces_dir = r'D:\Attendance with face\known_faces'
known_faces = []
known_names = []

for filename in os.listdir(known_faces_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_faces.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])

def play_success_sound():
    winsound.Beep(1000, 200)  

def play_fail_sound():
    winsound.Beep(400, 400)
def capture_image():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('📸 Press Space to capture', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    cam.release()
    cv2.destroyAllWindows()
    return frame if ret else None

def recognize_face(captured_image):
    face_encodings = face_recognition.face_encodings(captured_image)
    if not face_encodings:
        print("No faces detected.")
        return None
    captured_encoding = face_encodings[0]
    matches = face_recognition.compare_faces(known_faces, captured_encoding)
    if True in matches:
        return known_names[matches.index(True)]
    return None

def mark_attendance(student_name):
    attendance_dir = os.path.join(os.path.dirname(__file__), 'attendance_logs')
    os.makedirs(attendance_dir, exist_ok=True)
    file = os.path.join(attendance_dir, 'attendance.xlsx')

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    try:
        df = pd.read_excel(file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    new_record = pd.DataFrame({"Name": [student_name], "Date": [date], "Time": [time]})
    df = pd.concat([df, new_record], ignore_index=True)
    df.to_excel(file, index=False)

def mark_attendance_gui(status_label):
    image = capture_image()
    if image is None:
        threading.Thread(target=play_fail_sound).start()
        status_label.config(text="❌ Failed to capture image.", fg="red")
        return
    student_name = recognize_face(image)
    if student_name is None:
        threading.Thread(target=play_fail_sound).start()
        status_label.config(text="🙅‍♂️ Student not recognized ❌", fg="orange")
    else:
        mark_attendance(student_name)
        threading.Thread(target=play_success_sound).start()
        status_label.config(text=f"✅ Attendance marked for {student_name} 😊", fg="green")

def setup_gui():
    root = tk.Tk()
    root.title("Attendify - Modern Attendance System")
    root.geometry("700x500")
    root.config(bg="#1e272e")

    title = tk.Label(root, text="Attendify 📸", font=("Helvetica", 36, "bold"), bg="#1e272e", fg="#00cec9")
    title.pack(pady=40)

    status_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#1e272e", fg="white")
    status_label.pack(pady=20)

    mark_btn = tk.Button(
        root, text="📸 Mark Attendance", font=("Helvetica", 18, "bold"),
        bg="#00b894", fg="white", activebackground="#00cec9",
        relief="flat", width=25, height=2,
        command=lambda: mark_attendance_gui(status_label)
    )
    mark_btn.pack(pady=20)

    exit_btn = tk.Button(
        root, text="❌ Exit", font=("Helvetica", 14), bg="#d63031", fg="white",
        command=root.quit, relief="flat", width=20, height=2
    )
    exit_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
