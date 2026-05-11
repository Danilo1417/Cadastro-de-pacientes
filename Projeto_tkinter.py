from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Configurações de cores (Paleta Moderna)
COLOR_BG = "#f0f2f5"        # Cinza bem claro (fundo)
COLOR_WHITE = "#ffffff"     # Branco puro (cards)
COLOR_PRIMARY = "#007bff"   # Azul moderno
COLOR_SUCCESS = "#28a745"   # Verde sucesso
COLOR_TEXT = "#333333"      # Cinza escuro para texto

janela = Tk()
janela.title("Hospital Central - Cadastro")
janela.geometry("900x850")
janela.configure(bg=COLOR_BG)

# Estilização Global
style = ttk.Style()
style.theme_use("clam") # Tema base mais flexível

# Estilizando as Abas (Notebook)
style.configure("TNotebook", background=COLOR_BG, borderwidth=0)
style.configure("TNotebook.Tab", font=("Segoe UI", 10), padding=[15, 5])
style.map("TNotebook.Tab", background=[("selected", COLOR_PRIMARY)], foreground=[("selected", "white")])

# Notebook
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True, padx=20, pady=20)

# Criando Frames com fundo branco para as abas
aba1 = Frame(abas, bg=COLOR_WHITE, padx=30, pady=30)
aba2 = Frame(abas, bg=COLOR_WHITE, padx=10, pady=10)
abas.add(aba1, text="Novo Cadastro")
abas.add(aba2, text="Pacientes Cadastrados")

def cadastrar():
    campos = [entry_nome.get(), entry_cpf.get(), entry_data.get(), 
              entry_telefone.get(), entry_email.get(), entry_convenio.get(), entry_emergencia.get()]
    
    if "" in campos:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
    else:
        tabela.insert("", END, values=campos)
        for entry in [entry_nome, entry_cpf, entry_data, entry_telefone, entry_email, entry_convenio, entry_emergencia]:
            entry.delete(0, END)
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

# Título da Aba
Label(aba1, text="Ficha de Cadastro", font=("Segoe UI", 16, "bold"), bg=COLOR_WHITE, fg=COLOR_PRIMARY).pack(pady=(0, 20))

# Função auxiliar para criar labels e entries bonitos
def criar_campo(label_text):
    Label(aba1, text=label_text, font=("Segoe UI", 10), bg=COLOR_WHITE, fg=COLOR_TEXT).pack(anchor="w", pady=(10, 2))
    entry = Entry(aba1, font=("Segoe UI", 11), bg="#f8f9fa", fg=COLOR_TEXT, 
                  highlightthickness=1, highlightbackground="#dee2e6", relief="flat")
    entry.pack(fill="x", ipady=5) # ipady dá altura interna ao campo
    return entry

entry_nome = criar_campo("Nome Completo")
entry_cpf = criar_campo("CPF")
entry_data = criar_campo("Data de Nascimento")
entry_telefone = criar_campo("Telefone")
entry_email = criar_campo("E-mail")
entry_convenio = criar_campo("Convênio / Plano de Saúde")
entry_emergencia = criar_campo("Contato de Emergência")

# Botão Estilizado (Sem tk. pois usamos Button direto)
btn_cadastro = Button(
    aba1, 
    text="CADASTRAR PACIENTE",
    bg=COLOR_SUCCESS,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    bd=0,
    cursor="hand2",
    activebackground="#218838",
    activeforeground="white",
    command=cadastrar
)
btn_cadastro.pack(fill="x", pady=30, ipady=10)

### Aba 2 - Tabela Estilizada
style.configure("Treeview", font=("Segoe UI", 10), rowheight=30, background=COLOR_WHITE)
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

colunas = ("Nome", "CPF", "Nasc.", "Telefone", "Email", "Convênio", "Emergência")
tabela = ttk.Treeview(aba2, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=100, anchor="center")

tabela.pack(fill="both", expand=True)

janela.mainloop()