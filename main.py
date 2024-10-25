import customtkinter as ctk
from PIL import Image

janela = ctk.CTk()
tela_largura = janela.winfo_screenwidth()
tela_altura = janela.winfo_screenheight()
barra_tarefas = 60
janela.geometry(f"{tela_largura}x{tela_altura - barra_tarefas}+0+0")
ctk.set_appearance_mode("light")

frame = ctk.CTkFrame(janela, width=350,height=490)
frame_2 = ctk.CTkFrame(janela, width=986, height=490)
frame_3 = ctk.CTkFrame(janela, width=1346, height=188)

img = Image.open("resistor.png")
resistor_img = ctk.CTkImage(light_image=img, size=(320, 123))

img_2 = Image.open("capacitor.png")
capacitor_img = ctk.CTkImage(light_image=img_2, size=(320, 123))

img_3 = Image.open("indutor.png")
indutor_img = ctk.CTkImage(light_image=img_3, size=(320, 123))

btn_label_r = ctk.CTkButton(frame_2, text="", fg_color="transparent")


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
                       font=("Montserrat bold", 20),
                       command=event,
                       width=100,
                       button_length=200,
                       variable=switch_var,
                       onvalue="Ativado",
                       offvalue="Desativado")

switch.place(x=1156, y=608)

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
    entrada_r = ctk.CTkInputDialog(title="Valor do resistor" ,text="Digite o valor do resistor: ")
    print(entrada_r.get_input())
    resistor_board = ctk.CTkImage(light_image=img, dark_image=img, size=(80,31))
    btn_label_r.configure(width=80, height=31, image=resistor_board)
    btn_label_r.place(x=450, y =220)
    btn_label_r.bind("<Button-1>", start_drag)
    btn_label_r.bind("<B1-Motion>", dragging)

def start_drag(event):
    # Registra a posição inicial do mouse
    btn_label_r.startX = event.x
    btn_label_r.startY = event.y

def dragging(event):
    # Move o componente para onde o mouse vai
    x = btn_label_r.winfo_x() - btn_label_r.startX + event.x
    y = btn_label_r.winfo_y() - btn_label_r.startY + event.y
    btn_label_r.place(x=x, y=y)


btn = ctk.CTkButton(master=janela, text="iniciar", fg_color= "orange", command=tela_1, width=300, height=100, font=("Montserrat bold", 40), corner_radius=10)
btn.pack(pady=250)
resistor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=resistor_img, command=valor_resistor)
indutor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=indutor_img)
capacitor_btn = ctk.CTkButton(frame, width=330, height=123, text= " ", fg_color="transparent", image=capacitor_img)

janela.mainloop()