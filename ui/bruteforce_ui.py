import customtkinter as ctk
from modules.bruteforce import hydra, john
from ui.utils import format_result

class BruteforceFrame(ctk.CTkFrame):
    def __init__(self, parent, switch):
        super().__init__(parent)

        ctk.CTkLabel(self, text="BRUTEFORCE MODULE", font=("Arial", 20)).pack(pady=10)

        self.target = ctk.CTkEntry(self, placeholder_text="Target IP")
        self.target.pack(pady=5)

        self.service = ctk.CTkEntry(self, placeholder_text="Service (ssh/http)")
        self.service.pack(pady=5)

        self.user = ctk.CTkEntry(self, placeholder_text="Username")
        self.user.pack(pady=5)

        self.wordlist = ctk.CTkEntry(self, placeholder_text="Wordlist path")
        self.wordlist.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=200)
        self.output.pack(pady=10)

        ctk.CTkButton(self, text="HYDRA", command=self.run_hydra).pack(pady=5)
        ctk.CTkButton(self, text="JOHN", command=self.run_john).pack(pady=5)

    def show(self, text):
        self.output.delete("0.0", "end")
        self.output.insert("0.0", text)

    def run_hydra(self):
        self.show(hydra(
            self.target.get(),
            self.service.get(),
            self.user.get(),
            self.wordlist.get()
        ))

    def run_john(self):
        self.show(john(self.wordlist.get()))
    def run_hydra(self):
        result = hydra(
        self.target.get(),
        self.service.get(),
        self.user.get(),
        self.wordlist.get()
    )
    self.show(format_result(result))

    def run_john(self):
        result = john(self.wordlist.get())
        self.show(format_result(result))