import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Rekrutacja - Użytkownik")
        self.geometry(f"{380}x{470}")
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid_columnconfigure(2, weight=1)
 
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Sprawdź stan rekrutacji", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(20, 30))
                
        self.surname_label = customtkinter.CTkLabel(self.sidebar_frame, text="Nazwisko:", font=customtkinter.CTkFont(size=14))
        self.surname_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.surname_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Nazwisko")
        self.surname_entry.grid(row=1, column=1, padx=(0, 20), pady=10, sticky="nsew")        

        self.ver_label = customtkinter.CTkLabel(self.sidebar_frame, text="Kod weryfikacyjny:", font=customtkinter.CTkFont(size=14))
        self.ver_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.ver_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Kod weryfikacyjny")
        self.ver_entry.grid(row=2, column=1, padx=(0, 20), pady=10, sticky="nsew")

        self.verify_button = customtkinter.CTkButton(master=self.sidebar_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Sprawdź", command=self.check_recrutation)
        self.verify_button.grid(row=3, column=0, columnspan=2, padx=20, pady=15, sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self.sidebar_frame, width=340)
        self.textbox.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        # set default values
        self.textbox.insert("0.0", "W tym miejscu pojawi się wynik rekrutacji.")

    def check_recrutation(self):
        
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()