import tkinter as tk
from threading import Thread
import time

class TrafficLightGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚦 Modern Traffic Light System")
        self.root.geometry("300x500")
        self.root.config(bg="#1e1e2f")

        # Title
        self.title = tk.Label(root, text="Traffic Light Controller", font=("Helvetica", 16, "bold"),
                              bg="#1e1e2f", fg="white")
        self.title.pack(pady=10)

        # Canvas for light box
        self.canvas = tk.Canvas(root, width=160, height=360, bg="#222", bd=0, highlightthickness=0)
        self.canvas.create_rectangle(30, 20, 130, 340, fill="#444", outline="#111", width=2)
        self.canvas.pack()

        # Lights (as ovals)
        self.red_light = self.canvas.create_oval(50, 40, 110, 100, fill="grey")
        self.yellow_light = self.canvas.create_oval(50, 140, 110, 200, fill="grey")
        self.green_light = self.canvas.create_oval(50, 240, 110, 300, fill="grey")

        # Timer label
        self.timer_label = tk.Label(root, text="System Idle", font=("Helvetica", 14),
                                    bg="#1e1e2f", fg="white")
        self.timer_label.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start, bg="#28a745", fg="white",
                                      font=("Arial", 12), width=15)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, bg="#dc3545", fg="white",
                                     font=("Arial", 12), width=15)
        self.stop_button.pack(pady=5)

        self.running = False

    def set_light(self, color, duration):
        self.canvas.itemconfig(self.red_light, fill="grey")
        self.canvas.itemconfig(self.yellow_light, fill="grey")
        self.canvas.itemconfig(self.green_light, fill="grey")

        if color == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
        elif color == "yellow":
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
        elif color == "green":
            self.canvas.itemconfig(self.green_light, fill="green")

        for t in range(duration, 0, -1):
            self.timer_label.config(text=f"{color.capitalize()} Light - {t}s")
            time.sleep(1)

    def run_lights(self):
        while self.running:
            self.set_light("red", 5)
            self.set_light("yellow", 2)
            self.set_light("green", 5)
            self.set_light("yellow", 2)
        self.timer_label.config(text="System Idle")

    def start(self):
        if not self.running:
            self.running = True
            Thread(target=self.run_lights, daemon=True).start()

    def stop(self):
        self.running = False
        self.set_light("", 0)

def launch_gui():
    root = tk.Tk()
    app = TrafficLightGUI(root)
    root.mainloop()

launch_gui()
