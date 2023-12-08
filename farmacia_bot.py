import openai
import tkinter as tk
from tkinter import scrolledtext

# Substitua 'SUA_CHAVE_API' pela sua chave de API do GPT-3.5
openai.api_key = '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'

def obter_resposta(prompt):
    try:
        resposta = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return resposta.choices[0].text.strip()
    except Exception as e:
        return str(e)

class FarmaciaVirtualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmácia Virtual")

        self.chat_history = scrolledtext.ScrolledText(root, height=10, width=50)
        self.chat_history.pack(pady=10)

        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(root, text="Enviar", command=self.send_message)
        self.send_button.pack()

        self.farmacia_prompt = "Bem-vindo à Farmácia Virtual! Como posso ajudar você hoje?"
        self.append_message(self.farmacia_prompt)

    def send_message(self):
        user_input_text = self.user_input.get()
        self.append_message(f"Cliente: {user_input_text}")

        if user_input_text.lower() in ['sair', 'adeus', 'tchau']:
            self.append_message("Farmácia: Obrigado por escolher a Farmácia Virtual. Tenha um ótimo dia!")
            self.root.quit()
        else:
            resposta_bot = interagir_com_farmacia(user_input_text)
            self.append_message(f"Farmácia: {resposta_bot}")

    def append_message(self, message):
        current_text = self.chat_history.get("1.0", tk.END)
        self.chat_history.delete("1.0", tk.END)
        updated_text = current_text + message + "\n"
        self.chat_history.insert(tk.END, updated_text)

def interagir_com_farmacia(pergunta_usuario):
    prompt = f"Cliente: {pergunta_usuario}\nFarmácia:"
    resposta_bot = obter_resposta(prompt)
    return resposta_bot

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmaciaVirtualApp(root)
    root.mainloop()
