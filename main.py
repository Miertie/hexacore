import customtkinter as ctk
from core.router import recon

# UI настройки
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("MR Tool")
app.geometry("600x400")

# Ввод
entry = ctk.CTkEntry(app, placeholder_text="Enter target")
entry.pack(pady=10)

# Вывод
output = ctk.CTkTextbox(app, height=200)
output.pack(pady=10)

# Кнопка WHOIS
def run_whois():
    target = entry.get()
    result = recon("whois", target)
    output.delete("0.0", "end")
    output.insert("0.0", result)

# Кнопка NMAP
def run_nmap():
    target = entry.get()
    result = recon("nmap", target)
    output.delete("0.0", "end")
    output.insert("0.0", result)

btn1 = ctk.CTkButton(app, text="WHOIS", command=run_whois)
btn1.pack(pady=5)

btn2 = ctk.CTkButton(app, text="NMAP", command=run_nmap)
btn2.pack(pady=5)

app.mainloop()