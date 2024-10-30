import customtkinter as ctk
from PIL import ImageTk, Image

janela = ctk.CTk()
tela_largura = janela.winfo_screenwidth()
tela_altura = janela.winfo_screenheight()
barra_tarefas = 60
janela.geometry(f"{tela_largura}x{tela_altura - barra_tarefas}+0+0")
print(tela_largura)
print(tela_altura - barra_tarefas)
ctk.set_appearance_mode("light")

frame = ctk.CTkFrame(janela, width=350,height=490)
frame_2 = ctk.CTkFrame(janela, width=986, height=490)
frame_3 = ctk.CTkFrame(janela, width=1346, height=188)

img = Image.open("resistor.png")
img = img.resize((320, 123), Image.Resampling.LANCZOS)
resistor = ImageTk.PhotoImage(img)

img_2 = Image.open("capacitor.png")
img_2 = img_2.resize((320, 123), Image.Resampling.LANCZOS)
capacitor = ImageTk.PhotoImage(img_2)

img_3 = Image.open("indutor.png")
img_3 = img_3.resize((320, 123), Image.Resampling.LANCZOS)
indutor = ImageTk.PhotoImage(img_3)


def destroy():
    btn.destroy()
    switch.destroy()


def event():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("dark")
    elif switch_var.get() == "Desativado":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("System")

switch_var = ctk.StringVar(value="on")

switch = ctk.CTkSwitch(master=janela, 
                       text="MODO ESCURO",
                       font=("Montserrat", 20),
                       command=event,
                       width=100,
                       button_length=200,
                       variable=switch_var,
                       onvalue="Ativado",
                       offvalue="Desativado")

switch.place(x=1156, y=608)

def capacitor():
    pass

def tela_1():
    destroy()
    frame.place(x=10, y=10)
    frame_2.place(x=370, y=10)
    frame_3.place(x=10, y=510)
    resistor_btn.grid(row=0, column=0, pady=10)
    capacitor_btn.grid(row=1, column=0, pady=10)
    indutor_btn.grid(row=3, column=0, pady=10)
    label = ctk.CTkLabel(frame, text="SELECIONE SEUS COMPONENTES", height=10)
    label.grid(row=4, column=0, pady=10)
    
def valor_resistor():
    pass

btn = ctk.CTkButton(master=janela, text="iniciar", fg_color= "orange", command=tela_1, width=300, height=100, font=("Montserrat", 40), corner_radius=10)
btn.pack(pady=250)
resistor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=resistor, command=valor_resistor)
indutor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=indutor)
capacitor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=capacitor)

janela.mainloop()