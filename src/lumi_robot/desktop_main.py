import customtkinter as ctk
import tkinter as tk

from voice.stt_service import SpeechToTextService
from voice.tts_service import TextToSpeechService
from client.client import BackendClient
import threading
import time
import torch

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LumiApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("LUMI Assistant")
        self.geometry("400x300")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, corner_radius=20)
        self.main_frame.pack(expand=True, padx=30, pady=30)

        self.label = ctk.CTkLabel(self, text="L U M I", font=("Segoe UI", 28, "bold"))
        self.label.pack(pady=(20,10))

        self.canvas = tk.Canvas(self.main_frame, width=200, height=100, bg="#2b2b2b", highlightthickness=0)
        self.canvas.pack(pady=10)

        self.left_eye = self.canvas.create_oval(40,20,90,70, fill="white")
        self.right_eye = self.canvas.create_oval(110,20,160,70, fill="white")

        self.status = ctk.CTkLabel(
            self.main_frame,
            text="Status: Pronto",
            font=("Segoe UI", 14),
            text_color="gray"
        )
        self.status.pack(pady=10)


        self.button = ctk.CTkButton(
            self.main_frame,
            text= "Ativar LUMI",
            command= self.starting_processing_thread,
            width=200,
            height=50,
            corner_radius=25
        )
        self.button.pack(pady=20)

        self.tts = TextToSpeechService()
        self.stt = SpeechToTextService()
        self.backend = BackendClient()

    def starting_processing_thread(self):
        thread = threading.Thread(target=self.processing_flow)
        thread.daemon = True
        thread.start()
    
    def self_update_button(self, text=None, color=None, state=None):
        def update():
            if text:
                self.button.configure(text= text)
            if color:
                self.button.configure(fg_color = color)
            if state:
                self.button.configure(state = state)
        
        self.after(0, update)

    def safe_update_status(self,text, color):
        def update():
            self.status.configure(text= text)
            self.set_eye_color(color=color)
        self.after(0, update)

    def processing_flow(self):

        self.self_update_button(
            text="Processando...",
            color="#0550a0",
            state="disabled"
        )

        transcript = self.activate_lumi()
        reply = self.processing(transcript)
        self.responding(reply)
        self.reset()

    def set_eye_color(self, color):
        self.canvas.itemconfig(self.left_eye, fill=color)
        self.canvas.itemconfig(self.right_eye, fill=color)

    def activate_lumi(self):
        self.safe_update_status(text= "Status: Ouvindo...", color="#4da6ff")
        self.set_eye_color("#4da6ff")

        transcript = self.stt.listen_command()
        if not transcript:
                return 
        return transcript

    def processing(self,transcript):
        self.safe_update_status(text= "Status: Processando...", color="#ffaa00")
        reply = self.backend.send_command(transcript)
        print(reply)
        return reply
    
    def responding(self, reply):
        self.safe_update_status(text= "Status: Respondendo...", color="#00cc66")

        self.tts.speak(reply)

    
    def reset(self):
        self.safe_update_status(text= "Status: Pronto!", color="white")
        self.self_update_button(
            text="Ativar LUMI",
            color="#1f6aa5",
            state="normal"
        )


if __name__ == "__main__":
    app = LumiApp()
    app.mainloop()