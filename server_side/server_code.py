import socket
from threading import Thread

# create network port ip

host = "0.0.0.0"

port = int(input("Lütfen Bağlantıyı açacağınız portu giriniz (ngrokta önceden açılmış olmalı) :"))

# create network socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect port ip

server_socket.bind((host, port))

# listen network

server_socket.listen()

# create client list and usernames

clients = []

usernames = []

# send message every clients


def distributor(message):

    for client in clients:

        client.send((message+"\n").encode("utf-8"))

# catch messages which ones come from clients


def message_receiver(client):
    # with infinity loop get messages from every clients
    while True:

        try:

            # catch message and distribute

            message = client.recv(2048).decode("utf-8")

            # get secret message and send everything about crypto

            if "code_all" in message:

                print(f"{message} İstekte Bulundu")

                with open("crypto_send_files/serverkey.key", "rb") as key:

                    key_message = key.read()

                    client.send(f"key...===?1?^!{key_message}".encode("utf-8"))

                # send server dict

            elif "encryption_on" in message:

                with open("crypto_send_files/encrypted_dictionary.txt", "rb") as crypto_dict:

                    send_dict = crypto_dict.read()

                    client.send(f"encryption++++{send_dict}".encode("utf-8"))

                # save the log

                with open("Server_log.txt", "a", encoding="utf-8") as log:

                    log.write(f"{message} İstekte Bulundu\n")

            # if it is normal message

            else:

                distributor(message)

        except (OSError, ValueError):

            # if we cannot send the message the connection could be failed so remove the client

            index = clients.index(client)

            clients.remove(client)

            client.close()

            # remove username and send disconnected message

            username = usernames[index]

            distributor(f"{username} disconnected")

            usernames.remove(username)


# main function of server

def start_server():

    while True:

        client, address = server_socket.accept()

        # add client to list

        clients.append(client)

        # firs conversation is for username

        # ask for username

        client.send("whatisyourusername?".encode("utf-8"))

        # get username

        username = client.recv(1024).decode("utf-8")

        usernames.append(username)

        # distribute ... has joined

        distributor(f"{username} chate katıldı\n")

        # you have connected text sending

        client.send("###############################################\n"
                    "#    PRODUCE-BY CODE_DEM STUDİO               #\n"
                    "#    You have connected the İnfernal Date     #\n"
                    "###############################################\n".encode("utf-8"))

        # creating server log and print in cmd

        with open("Server_log.txt", "a", encoding="utf-8") as log:

            log.write(f"{str(address[0])}---->{username}\n")

        # with threading get message every time

        message_receive_thread = Thread(target=message_receiver, args=(client,))

        message_receive_thread.start()


# before starting server create log.txt

start_server()
