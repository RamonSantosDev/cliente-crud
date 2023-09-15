from tkinter import *


class Gui():
    # Classe da interface Gráfica
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk()
    window.wm_title("PYSQL VERSÃO 1.0")

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")

    entNome = Entry(window, textvariable=txtNome , width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome , width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail , width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF , width=width_entry)
    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    lblnome.grid(row=0, column=0 , padx=x_pad , pady=y_pad)
    lblsobrenome.grid(row=1, column=0 , padx=x_pad , pady=y_pad)
    lblemail.grid(row=2, column=0 , padx=x_pad , pady=y_pad)
    lblcpf.grid(row=3, column=0 , padx=x_pad , pady=y_pad)
    entNome.grid(row=0, column=1 , padx=x_pad , pady=y_pad)
    entSobrenome.grid(row=1, column=1 , padx=x_pad , pady=y_pad)
    entEmail.grid(row=2, column=1 , padx=x_pad , pady=y_pad)
    entCPF.grid(row=3, column=1 , padx=x_pad , pady=y_pad)
    listClientes.grid(row=0, column=2 , rowspan=10 , padx=x_pad , pady=y_pad)
    scrollClientes.grid(row=0, column=3 , rowspan=10 , padx=x_pad , pady=y_pad)
    btnViewAll.grid(row=4, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)
    btnBuscar.grid(row=6, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)
    btnInserir.grid(row=8, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)
    btnUpdate.grid(row=10, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)
    btnDel.grid(row=12, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)
    btnClose.grid(row=14, column=0 , rowspan=2 , padx=x_pad , pady=y_pad)

    # Adicionar SWAG (aparência) à interface
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure (padx=x_pad , pady=y_pad , sticky='N')



