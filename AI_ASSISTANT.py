import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import webbrowser

class AIAssistant:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Assistant")
        self.master.geometry("100x100")

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        self.listen_button = tk.Button(master, text="Listen", command=self.listen)
        self.listen_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        # Set the voice to female
        self.engine.setProperty('voice', voices[1].id)

        self.commands = {
            "hello": self.say_hello,
            "what's your name": self.say_name,
            "how are you": self.say_how_are_you,
            "open google": self.open_google,
            "open facebook": self.open_facebook,
            "open youtube": self.open_youtube,
             "open instagram": self.open_instagram,
       
        }

    def say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
        self.text_area.insert(tk.END, f"AI: {message}\n")
        self.text_area.see(tk.END)

    def listen(self):
        with sr.Microphone() as source:
            self.text_area.insert(tk.END, "Listening...\n")
            self.text_area.see(tk.END)
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio).lower()
                self.text_area.insert(tk.END, f"You said: {command}\n")
                self.text_area.see(tk.END)
                self.process_command(command)
            except sr.UnknownValueError:
                self.text_area.insert(tk.END, "Sorry, I didn't catch that.\n")
                self.text_area.see(tk.END)
            except sr.RequestError:
                self.text_area.insert(tk.END, "Could not request results from Google Speech Recognition service.\n")
                self.text_area.see(tk.END)

    def process_command(self, command):
        if command in self.commands:
            self.commands[command]()
        elif command == "exit":
            self.say("Goodbye!")
            self.master.quit()
        else:
            self.say("Sorry, I don't understand that command.")

    def say_hello(self):
        self.say("Hello! How can I assist you today?")

    def say_name(self):
        self.say("I am your AI assistant.")

    def say_how_are_you(self):
        self.say("I'm just a bunch of code, but I'm doing great! How about you?")

    def open_google(self):
        webbrowser.open("https://www.google.com")
        self.say("Opening Google")
    
    
    def open_facebook(self):
        webbrowser.open("https://www.facebook.com")
        self.say("Opening Facebook")
    
    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/")
        self.say("Opening YouTube")

            
    def open_instagram(self):
        webbrowser.open("https://www.instagram.com")
        self.say("Opening Instagram")

if __name__ == "__main__":
    root = tk.Tk()
    assistant = AIAssistant(root)
    root.mainloop()
