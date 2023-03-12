import tkinter as tk
import datetime


root = tk.Tk()
root.title("Botbot")


def send():
    message = e.get().lower()
    e.delete(0, tk.END)

    # Vérifier le type de message
    message_type = check_message_type(message)

    if message_type == "greeting":
        add_bot_message("Hello! How are you today?")
    elif message_type == "farewell":
        add_bot_message("Goodbye! Have a nice day!")
    elif message_type == "thanks":
        add_bot_message("You're welcome!")
    elif message_type == "time":
        now = datetime.datetime.now()
        time_string = now.strftime("%H:%M")
        add_bot_message("It's " + time_string + " right now.")
    elif message_type == "small_talk":
        add_bot_message("That's interesting!")
    else:
        add_bot_message("I'm sorry, I don't understand. Can you please rephrase that?")


def check_message_type(message):
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye"]
    thanks = ["thanks", "thank you"]
    small_talk = ["how are you", "what's up"]

    if any(word in message for word in greetings):
        return "greeting"
    elif any(word in message for word in farewells):
        return "farewell"
    elif any(word in message for word in thanks):
        return "thanks"
    elif any(word in message for word in small_talk):
        return "small_talk"
    elif "time" in message or "heure" in message:
        return "time"
    else:
        return "unknown"


def add_bot_message(message):
    # Ajouter un message de Botbot à la zone de texte
    text.configure(state="normal")
    text.insert(tk.END, "Botbot: ")
    text.insert(tk.END, message + "\n")
    text.configure(state="disabled")


# Créer la zone de texte pour les messages
text = tk.Text(root, state="disabled")
text.grid(row=0, column=0, columnspan=2)

# Ajouter une barre de défilement pour la zone de texte
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.grid(row=0, column=2, sticky="ns")
text.configure(yscrollcommand=scrollbar.set)

# Créer le champ d'entrée pour les messages
e = tk.Entry(root, width=100)
e.grid(row=1, column=0)

# Créer le bouton pour envoyer un message
send_button = tk.Button(root, text="Send", command=send)
send_button.grid(row=1, column=1)

# Ajouter un message de bienvenue
add_bot_message("Hello! I'm Botbot. How can I help you?")

root.mainloop()
