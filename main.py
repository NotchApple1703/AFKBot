import secrets
import webbrowser

import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")


def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.resizable(False, False)
        self.update_title()

        self.columnconfigure(0, weight=1)

        self.bg_img = ctk.CTkImage(Image.open("assets/bg.png"), size=(500, 300))
        self.bg_label = ctk.CTkLabel(self, text="", image=self.bg_img)
        self.bg_label.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.start_button = ctk.CTkButton(self, width=150, height=50, text="Start", font=("", 17, "bold"),
                                          corner_radius=10,
                                          background_corner_colors=("#7aaadb", "#77a9dc", "#90bbe5", "#92bbe2"),
                                          command=self.start)
        self.start_button.grid(row=0, column=0)

        self.stop_button = ctk.CTkButton(self, width=150, height=50, text="Stop", font=("", 17, "bold"),
                                         corner_radius=10,
                                         background_corner_colors=("#e4bc81", "#55351e", "#714528", "#8b5c32"),
                                         command=self.stop)
        self.stop_button.grid(row=1, column=0)

        self.github_button = ctk.CTkButton(self, width=150, height=50, text="GitHub", font=("", 17, "bold"),
                                           corner_radius=10,
                                           background_corner_colors=("#a37343", "#a27242", "#654026", "#7b573d"),
                                           command=open_github)
        self.github_button.grid(row=2, column=0)

        self.credit_label = ctk.CTkLabel(self, width=500, text="Credit: GorouFlex aka KRJ | Version: 1.2.1 (1F2167E)")
        self.credit_label.grid(row=3, column=0, sticky="s")

    def update_title(self):
        self.title(secrets.token_hex(14))
        self.after(1000, self.update_title)

    def start(self):
        ...

    def stop(self):
        ...


if __name__ == '__main__':
    app = Main()
    app.mainloop()
