import customtkinter as ctk
from modules.osint import username_gen, email_guess, info_lookup
from ui.utils import format_result

class OsintFrame(ctk.CTkFrame):
    def __init__(self, parent, switch):
        super().__init__(parent)

        ctk.CTkLabel(self, text="OSINT MODULE", font=("Arial", 20)).pack(pady=10)

        self.name = ctk.CTkEntry(self, placeholder_text="Name / Username")
        self.name.pack(pady=5)

        self.domain = ctk.CTkEntry(self, placeholder_text="Domain (for email)")
        self.domain.pack(pady=5)

        self.query = ctk.CTkEntry(self, placeholder_text="Search query")
        self.query.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=250)
        self.output.pack(pady=10)

        ctk.CTkButton(self, text="USERNAME GEN", command=self.run_user).pack(pady=5)
        ctk.CTkButton(self, text="EMAIL GUESS", command=self.run_email).pack(pady=5)
        ctk.CTkButton(self, text="INFO SEARCH", command=self.run_info).pack(pady=5)

    def show(self, text):
        self.output.delete("0.0", "end")
        self.output.insert("0.0", text)

    def run_user(self):
        self.show(username_gen(self.name.get()))

    def run_email(self):
        self.show(email_guess(self.name.get(), self.domain.get()))

    def run_info(self):
        self.show(info_lookup(self.query.get()))