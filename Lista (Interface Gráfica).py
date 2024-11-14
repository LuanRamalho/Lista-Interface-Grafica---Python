import tkinter as tk
from tkinter import messagebox, simpledialog

class ListaApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista Interativa")
        master.geometry("400x400")
        master.config(bg="#f0f0f0")  # Cor de fundo suave

        self.lista = []

        # Label com estilo
        self.label = tk.Label(master, text="Elementos na Lista:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333")
        self.label.pack(pady=10)

        # Listbox com borda arredondada
        self.listbox = tk.Listbox(master, height=10, width=40, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2, relief="solid")
        self.listbox.pack(pady=10)

        # Botão "Adicionar Elemento"
        self.adicionar_button = tk.Button(master, text="Adicionar Elemento", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.adicionar_elemento)
        self.adicionar_button.pack(pady=5, fill="x")

        # Botão "Remover Elemento"
        self.remover_button = tk.Button(master, text="Remover Elemento", font=("Arial", 12), bg="#f44336", fg="white", command=self.remover_elemento)
        self.remover_button.pack(pady=5, fill="x")

    def adicionar_elemento(self):
        elemento = simpledialog.askstring("Adicionar Elemento", "Digite o elemento a ser adicionado:")
        if elemento:
            self.lista.append(elemento)
            self.atualizar_lista()
            messagebox.showinfo("Elemento Adicionado", f"Elemento '{elemento}' adicionado à lista.")

    def remover_elemento(self):
        try:
            selecionado = self.listbox.curselection()[0]
            elemento_removido = self.lista[selecionado]
            del self.lista[selecionado]
            self.atualizar_lista()
            messagebox.showinfo("Elemento Removido", f"Elemento '{elemento_removido}' removido da lista.")
        except IndexError:
            messagebox.showwarning("Erro", "Nenhum elemento selecionado.")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for item in self.lista:
            self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaApp(root)
    root.mainloop()
