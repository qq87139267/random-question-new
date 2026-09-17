import tkinter as tk
import random
import time
import threading

try:
    with open("students.txt", "r", encoding="utf-8") as f:
        NAMES = [l.strip() for l in f if l.strip() and not l.startswith("#")]
except:
    NAMES = ["张三", "李四", "王五"]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("随机提问")
        self.root.geometry("400x300")
        self.root.configure(bg="black")
        self.running = False
        self.used = []
        self.label = tk.Label(root, text="点击开始", font=("微软雅黑",40,"bold"), fg="lime", bg="black")
        self.label.pack(expand=True)
        self.btn = tk.Button(root, text="开始 (空格)", command=self.toggle, bg="lime", fg="black", font=("微软雅黑",12,"bold"), relief="flat", padx=20, pady=5)
        self.btn.pack(pady=10)
        root.bind("<space>", lambda e: self.toggle())

    def toggle(self):
        if self.running:
            self.running = False
            return
        if not self.used or len(self.used) == len(NAMES):
            self.used = []
        self.running = True
        threading.Thread(target=self.roll, daemon=True).start()
        self.root.after(2000, self.stop)

    def roll(self):
        while self.running:
            n = random.choice([x for x in NAMES if x not in self.used])
            self.label.config(text=n)
            time.sleep(0.05)

    def stop(self):
        self.running = False
        if self.label.cget("text") != "点击开始":
            self.used.append(self.label.cget("text"))

root = tk.Tk()
App(root)
root.mainloop()
