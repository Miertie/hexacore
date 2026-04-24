import customtkinter as ctk
from modules.network import mac_changer, ip_changer, ip_info, wifi_scan
from ui.utils import format_result

class NetworkFrame(ctk.CTkFrame):
    def __init__(self, parent, switch):
        super().__init__(parent)

        ctk.CTkLabel(self, text="NETWORK MODULE", font=("Arial", 20)).pack(pady=10)

        self.iface = ctk.CTkEntry(self, placeholder_text="Interface (eth0/wlan0)")
        self.iface.pack(pady=5)

        self.mac = ctk.CTkEntry(self, placeholder_text="New MAC (optional)")
        self.mac.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=250)
        self.output.pack(pady=10)

        ctk.CTkButton(self, text="IP INFO", command=self.run_ip_info).pack(pady=5)
        ctk.CTkButton(self, text="IP CHANGE", command=self.run_ip_change).pack(pady=5)
        ctk.CTkButton(self, text="MAC CHANGE", command=self.run_mac).pack(pady=5)
        ctk.CTkButton(self, text="WIFI SCAN", command=self.run_wifi).pack(pady=5)

    def show(self, text):
        self.output.delete("0.0", "end")
        self.output.insert("0.0", text)

    self.show(format_result(ip_info()))
    self.show(format_result(mac_changer(...)))
    self.show(format_result(ip_changer(...)))
    self.show(format_result(wifi_scan(...)))