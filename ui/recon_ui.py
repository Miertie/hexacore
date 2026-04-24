import customtkinter as ctk
from modules.recon import whois, nmap, dns, subdomain

class ReconFrame(ctk.CTkFrame):
    def __init__(self, parent, switch):
        super().__init__(parent)

        title = ctk.CTkLabel(self, text="RECON MODULE", font=("Arial", 20))
        title.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Target (domain/IP)")
        self.entry.pack(pady=10)

        self.output = ctk.CTkTextbox(self, height=250)
        self.output.pack(pady=10)

        ctk.CTkButton(self, text="WHOIS", command=self.run_whois).pack(pady=5)
        ctk.CTkButton(self, text="NMAP", command=self.run_nmap).pack(pady=5)
        ctk.CTkButton(self, text="DNS", command=self.run_dns).pack(pady=5)
        ctk.CTkButton(self, text="SUBDOMAIN", command=self.run_sub).pack(pady=5)

    def show(self, text):
        self.output.delete("0.0", "end")
        self.output.insert("0.0", text)

    from ui.utils import format_result
    from modules.recon import whois, nmap, dns, subdomain