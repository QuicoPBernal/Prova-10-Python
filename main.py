import tkinter as tk
from tkinter import messagebox

def verificar_login():
    email = email_entry.get()
    senha = senha_entry.get()

    if "@" not in email:
        messagebox.showerror("Erro de Login", "Email inválido. Por favor, insira um email com o símbolo '@'.")
        return
      
    if len(senha) < 6:
        messagebox.showerror("Erro de Login", "Senha muito curta. Por favor, insira uma senha com pelo menos 6 caracteres.")
        return

    messagebox.showinfo("Sucesso!", "Login realizado com sucesso!")

janela = tk.Tk()
janela.title("Login")

email_label = tk.Label(janela, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5)

email_entry = tk.Entry(janela)
email_entry.grid(row=0, column=1, padx=5, pady=5)

senha_label = tk.Label(janela, text="Senha:")
senha_label.grid(row=1, column=0, padx=5, pady=5)

senha_entry = tk.Entry(janela, show="*")
senha_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(janela, text="Login", command=verificar_login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()
