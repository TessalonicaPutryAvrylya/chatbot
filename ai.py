import random
import tkinter as tk
from tkinter import scrolledtext

messages = {
    "greeting": ["halo", "hai", "selamat", "pagi", "siang", "sore", "malam"],
    "joki": ["joki", "bisa joki apa","ada joki apa","mau joki", "macam joki","ada, mau joki"],
    "contact": ["kontak","cara order","order","cara menghubungi"],
    "finish": ["selesai", "keluar", "quit","terimakasih","Iya"],
}
responses = {
    "greeting": ["Halo! Selamat datang di Layanan Joki Coding.", "Hi, ada yang bisa saya bantu?"],
    "joki": ["Kami menyediakan jasa joki untuk coding. Silakan bertanya lebih lanjut!"],
    "contact": ["Silakan menghubungi kami melalui WhatsApp +62 123-456-789"],
    "finish": ["Apakah Anda ingin mengakhiri chat kita? Input 'Selesai' untuk mengakhiri."],
    "unknown": ["Saya tidak mengerti maksud Anda, silakan bertanya lagi.", "Maaf, saya tidak dapat memahami pertanyaan Anda."],
}

def get_response(user_input):
    user_input = user_input.lower() 
    response_category = None 
    for category, messages_list in messages.items():
        for message in messages_list:
            if message in user_input:
                response_category = category
                break
    if response_category is not None:
        return random.choice(responses[response_category])
    else:
        return random.choice(responses["unknown"])

def run_chatbot_gui():
    def send_message():
        user_input = entry_box.get("1.0", tk.END).strip()
        entry_box.delete("1.0", tk.END)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Anda: " + user_input + "\n")
        if user_input.lower() in messages["finish"]:
            chat_box.insert(tk.END, "Bot: Terima kasih telah menggunakan chatbot kami.\n")
            chat_box.config(state=tk.DISABLED)
            root.after(1500, root.destroy)
        else:
            response = get_response(user_input)
            chat_box.insert(tk.END, "Bot: " + response + "\n")
            chat_box.see(tk.END)
            chat_box.config(state=tk.DISABLED)
    root = tk.Tk() 
    root.title("Layanan Joki Coding")
    root.geometry("400x400")
    root.configure(bg="#F0F0F0")
    chat_box = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
    chat_box.grid(row=0, padx=10, pady=10, columnspan=2, sticky="nsew")
    chat_box.tag_configure("center", justify="center")
    entry_box = tk.Text(root, wrap=tk.WORD, width=40, height=3, font=("Arial", 12))
    entry_box.grid(row=1, column=0, padx=10, pady=5)
    send_button = tk.Button(root, text="Kirim", width=10, font=("Arial", 12), command=send_message)
    send_button.grid(row=1, column=1, padx=5, pady=5)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.mainloop()

run_chatbot_gui()