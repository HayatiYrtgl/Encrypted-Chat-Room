import os.path
import socket
import json
from tkinter import END
from tkinter import messagebox
from message_parser_encryptor import ParserCryptor
# reading configuration file and using in algorithm


def reading_configuration_file():

    # catch errors with try except blocks

    try:

        with open("config_file/configuration.json", "r") as file:

            configuration_file = json.load(file)

            return configuration_file

    except (FileExistsError, FileNotFoundError):

        # give error message

        messagebox.showerror("HATA", "DOSYA BULUNAMADI CONFİGURASYON DOSYASININ İSMİ DEĞİŞMİŞ VEYA YOK !!!!")


config_file = reading_configuration_file()

# After reading the conf file, set port, username and host values

host = config_file["host"]

port = config_file["port"]

username = config_file["username"]

# create client side socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creating object every thread started

# connect to server function

# creating object

parser = ParserCryptor()

# reverse dictionary to decrypt

glob_dict = {}


def connect_to_server():

    # connect the ip and port

    client_socket.connect((host, port))

# message receiver


def message_receiver(text_area_object):

    # with while loop we thread it in gui

    while True:

        # with try except we will catch exceptions

        try:
            """main send message string"""

            main_message = ""

            # get message

            message = client_socket.recv(4096).decode("utf-8")

            # if message is secret code send the username

            if message == "whatisyourusername?":

                # send username

                client_socket.send(username.encode("utf-8"))

            # if key incame

            elif message.startswith("key...===?1?^!"):

                # if key not exists

                if os.path.exists("config_file/serverkey.key"):

                    messagebox.showinfo("BİLGİ", "SERVER ANAHTARINIZ MEVCUT!!")

                else:

                    with open("config_file/serverkey.key", "w") as key_message:

                        key_message.write(message[16:-1])

            # if crypted dictionary came

            elif message.startswith("encryption++++"):

                if os.path.exists("config_file/crypted_dictionary.txt"):

                    messagebox.showinfo("BİLGİ", "SERVER KRİPTOSU ZATEN MEVCUT!!")

                else:

                    with open("config_file/crypted_dictionary.txt", "w") as json_dictionary:

                        json_dictionary.write(message[16:-1])

                # this is the decryptor section
            else:

                # message decryption

                if os.path.exists("config_file/decrypted_dictionary.json"):

                    # if the mssage comes from a user u can parse

                    if "-->" in message:
                        # split from > mark 0.index is username

                        message_sep = message.split(">")

                        # decrypting the message

                        message = message_sep[1].split(",")

                        #open json file

                        with open("config_file/reverse_message.json", "r") as file:

                            reverse_dict = json.load(file)

                        for i in message:

                            if i != "\n":

                                try:

                                    main_message += reverse_dict[i.strip(" ")]

                                except (ValueError, KeyError):

                                    messagebox.showwarning("UYARI", "SERVER KEYİ VE ŞİFRELİ SÖZLÜĞÜ GÜNCELLEYİNİZ!!")

                            else:

                                pass

                        # if decrypting file is exists insert decrypted message and
                        # restoration what took from main message

                        decrypted_returned_message = message_sep[0]+"> "+main_message+"\n"

                        print(decrypted_returned_message)

                        text_area_object.insert(END, decrypted_returned_message)

                    # if > not in the message this is the system message
                    else:

                        text_area_object.insert(END, message)
                else:

                    text_area_object.insert(END, message)

        except:

            raise


# message sender


def message_sender(message_entry_object):
    # get user message from entry and add username send with entry

    user_message = message_entry_object.get()

    # with try excep control file existing situation

    # encryption the messages

    try:

        # user message to encrypt

        user_message = parser.encrypt_message(user_message)

        # send message

        client_socket.send(f"{username}----> {user_message}".encode("utf-8"))

        # clear entry area

        message_entry_object.delete(0, END)

    except:

        # send message

        client_socket.send(f"DUMMY----> {user_message}".encode("utf-8"))

        # clear entry area

        message_entry_object.delete(0, END)





