import json
from tkinter import messagebox
from json import load

from cryptography.fernet import Fernet
import os

# this blew code for client side to decrypt files

"""THE CLİENT SİDE"""
"""this function needs two arguments to run,
firstly the key (it must be sent by server side),
secondly the encrypted dictionary (it must be sent by server side)"""


def decrypt_data():

    # try this function if file is exists no problem else return false

    try:

        # read the key, key must be sent by server

        with open("config_file/serverkey.key", "rb") as serverkey:

            key = serverkey.read()

        decryptor = Fernet(key)

        # read the encrypted data

        with open("config_file/crypted_dictionary.txt", "rb") as encrypted_dictionary:

            encrypted = encrypted_dictionary.read()

        # decryption with variable

        decrypted = decryptor.decrypt(encrypted)

        # write decrypted file

        with open("config_file/decrypted_dictionary.json", "wb") as decrypted_dictionary:

            result = decrypted_dictionary.write(decrypted)

        return result

    # expect file not found

    except FileNotFoundError:

        messagebox.showerror("HATA", "DOSYA BULUNAMADI SERVERDAN İSTEKTE BULUNUN")


"""after received the crypto files
CLİENT SİDE"""


# decrypt or encrypt to file with using class cryptor


class ParserCryptor:

    # constructor

    def __init__(self):

        self.message = ""

        self.string = ""

        self.encrypt_dictionary = {}

        self.decrypt_dictionary = {}

        # auto run required functions if file is exists

        self.decrypt_encrypted_dictionary()

        self.create_encrypt_dictionary()

        self.create_reverse_decryption_dictionary()

    # use server key and decrypt encrypted dictionary

    def decrypt_encrypted_dictionary(self):

        # try to solve the file with key

        try:

            decrypt_data()

        except (FileExistsError, FileNotFoundError):

            pass

    # decrypt encrypted dictionary from json

    def create_encrypt_dictionary(self):

        try:

            # open file and appoint the var decryot dictionary

            with open("config_file/decrypted_dictionary.json", "rb") as file:

                # with json func var changed

                self.encrypt_dictionary = load(file)

            return self.encrypt_dictionary

        except (FileExistsError, FileNotFoundError):

            # if file not found send message

            pass

    # create reverse dictionary to encrypt messages

    def create_reverse_decryption_dictionary(self):

        # if create_decrypt_dictionary function is true try else don't try

        if self.create_encrypt_dictionary():

            # keys and values but reverse

            self.keys = self.encrypt_dictionary.values()

            self.values = self.encrypt_dictionary.keys()

            # for loop to update encrypt dictionary

            for key, value in zip(self.keys, self.values):
                # update dict key must be string

                self.decrypt_dictionary.update({str(key): value})

                with open("config_file/reverse_message.json", "w") as file:

                    json.dump(self.decrypt_dictionary, file, ensure_ascii=False, indent=4)

        # else don't try to convert the dict

        else:

            messagebox.showerror("HATA", "ŞİFRELEME İÇİN GEREKLİ OLAN DOSYALAR BULUNAMADI")

    # encrypt message with function

    def encrypt_message(self, user_message):

        # for merging string

        self.user_string = ""

        # get user message and find value of words

        self.listed_message = list(user_message)

        # with for loop find in encrypt dict

        for word in self.listed_message:
            self.user_string += str(self.encrypt_dictionary[word]) + ","

        return self.user_string

