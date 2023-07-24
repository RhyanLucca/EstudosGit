import customtkinter as ctk

app = ctk.CTk()
app.title("Aula 19 - ProgressBar")
app.geometry("700x500")

ctk.CTkLabel(app, text="Aula 19 - ProgressBar", font=("Arial bold", 20)).pack(pady=20)

progressbar = ctk.CTkProgressBar(app, 
                                 width=100, 
                                 height=30, 
                                 corner_radius=30, 
                                 fg_color="red",
                                 progress_color="yellow")
progressbar.pack(pady=20)
#progressbar.start()
#progressbar.step()
#progressbar.stop()

app.mainloop()