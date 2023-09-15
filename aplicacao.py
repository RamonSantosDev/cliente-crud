from Frontend import *
from tkinter import *
import Backend as core

app = None
selected = None


#visualização dos resultados.
def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, (r[0], r[1], r[2], r[3], r[4]))


#search_command() e insert_command() realizam a busca e a inserçãode dados no banco respectivamente.
def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, (r[0], r[1], r[2], r[3], r[4]))


def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()


def update_command():
    if selected:
        core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
        view_command()
    else:
        # Exiba uma mensagem de erro ou faça alguma ação apropriada se nenhum item estiver selecionado.
        print("Nenhum item selecionado para atualizar.")


def del_command():
    id = selected[0]
    core.delete(id)
    view_command()


#Armazena os valores informados e alimenta os campos de input com as informações.
def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    return selected


if __name__ == "__main__":
    app = Gui()

    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    app.window.mainloop()

