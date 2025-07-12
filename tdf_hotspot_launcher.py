import subprocess
import tkinter as tk
from tkinter import messagebox

def start_hotspot():
    ssid = "TDF Entertainment Network"
    password = "quizstorm"
    try:
        subprocess.run(["start", "ms-settings:network-mobilehotspot"], shell=True)
        messagebox.showinfo("Mobile Hotspot", f"✅ Your hotspot SSID is: {ssid}\n🔐 Password: {password}\n\nPlease toggle the hotspot ON in the window that just opened.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open hotspot settings.\n{str(e)}")

app = tk.Tk()
app.title("TDF Hotspot Launcher")
app.geometry("350x200")
tk.Label(app, text="Start Your Offline Hotspot", font=("Segoe UI", 12)).pack(pady=20)
tk.Button(app, text="Open Hotspot Settings", command=start_hotspot, font=("Segoe UI", 10)).pack(pady=10)
app.mainloop()
