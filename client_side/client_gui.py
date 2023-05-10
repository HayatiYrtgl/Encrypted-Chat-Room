import tkinter as tk
from client_code import *
from threading import Thread
from functools import partial
# creating client window

client_window = tk.Tk()

# creating object

# connect to server

connect_to_server()

# client configurations

client_window.title(f"KULLANICI: İNFERNAL USER ^(__)^")

client_window.geometry("600x550+430+160")

client_window.config(bg="gray14")

client_window.resizable(False, False)

# textarea, label entry and button

"""mainlabel side"""

main_label = tk.Label(client_window, text="INFERNAL DATE", font=("Rosewood Std Regular", 32), fg="green", bg="gray14")

main_label.pack()

"""textarea side"""

main_texarea = tk.Text(client_window, borderwidth=5, bg="gray70")

main_texarea.pack(pady=20, padx=30)

"""entry side"""

main_message_area = tk.Entry(font="9", width=35, fg="red", borderwidth=4, bg="gray70")

main_message_area.pack(pady=0, padx=30, side=tk.LEFT)

"""button side"""

main_button = tk.Button(client_window, text="Gönder", command=partial(message_sender, main_message_area),
                        borderwidth=5, bg="brown4")

main_button.place(x=455, y=505, width=100)

# threading message receiver

message_recv_thread = Thread(target=message_receiver, args=(main_texarea,)).start()

client_window.mainloop()


