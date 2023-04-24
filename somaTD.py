import tkinter as tk
import pyttsx3
import speech_recognition as sr

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        speech = recognizer.recognize_google(audio)
        return speech
    except Exception as e:
        print("Error:", e)
        return ""

# Main function
def read_and_listen():
    original_text = text_to_read.get("1.0", "end-1c")
    speak(original_text)

    recognized_text = recognize_speech()
    feedback = "Correct" if recognized_text.lower() == original_text.lower() else "Incorrect"
    feedback_label.config(text=f"Feedback: {feedback}")

# Create the main window
root = tk.Tk()
root.title("Book Reading App")

# Add a text widget
text_to_read = tk.Text(root, wrap=tk.WORD, height=8, width=40)
text_to_read.pack(padx=10, pady=10)

# Add a button
read_button = tk.Button(root, text="Read and Listen", command=read_and_listen)
read_button.pack(pady=10)

# Add a label for feedback
feedback_label = tk.Label(root, text="Feedback:")
feedback_label.pack(pady=10)

# Start the main loop
root.mainloop()
