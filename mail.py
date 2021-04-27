import email_to

def tutto(lista_ore):
    
    for prenotaz in lista_ore:
        # ora della prenotazione
        ora = prenotaz[-6:]
        # nome dell' utente che si è prenotato
        nome = prenotaz[:-8]

        email_server = email_to.EmailServer("smtp.gmail.com", 587, "shadowruler.bot@gmail.com", "Qwerty1234!")

        message = email_server.message()
        message.add("## Prenotazione sessione di gioco\n")
        message.add(f"### Hey {nome},\n ti sei prenotato per una sessione di gioco oggi alle {ora}!\n### Buon Divertimento da Shadow-Ruler.")
        message.style = "h2 { color: #8ccfe2} h3 { color: #171b29}"

        message.send("daniele.beltrami13@gmail.com", "someone@else.com", "Sessione di gioco")

        print(f"Inviata email con prenotazione a {nome} alle {ora}")
    return