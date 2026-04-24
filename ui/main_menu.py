import customtkinter as ctk
from modules import recon, bruteforce, network, osint, exploit

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("1000x650")
app.title("MR Framework - FINAL")

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)

output = ctk.CTkTextbox(frame, height=300)
output.pack(pady=10)

def show(result):
    output.delete("0.0", "end")
    output.insert("0.0", result)

# 🔍 RECON
ctk.CTkButton(frame, text="WHOIS", command=lambda: show(recon.whois("google.com"))).pack()

# 🔴 BRUTEFORCE
ctk.CTkButton(frame, text="HYDRA TEST", command=lambda: show(bruteforce.hydra("ip","ssh","admin","wordlist"))).pack()

# 🌐 NETWORK
ctk.CTkButton(frame, text="IP INFO", command=lambda: show(network.ip_info())).pack()

# 🧠 OSINT
ctk.CTkButton(frame, text="USERNAME", command=lambda: show(osint.username_gen("alex"))).pack()

# 💣 EXPLOIT
ctk.CTkButton(frame, text="SEARCH EXPLOIT", command=lambda: show(exploit.search("apache"))).pack()

app.mainloop()