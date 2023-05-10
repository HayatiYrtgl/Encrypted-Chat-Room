import os
import threading
import time
from socket import socket, AF_INET, SOCK_STREAM
import random
from cryptography.fernet import Fernet
import json

"""THE SERVER SİDE"""

# creating fernet key to encryption process


def key_generator():

    # to encrypt a file we generate a key

    key = Fernet.generate_key()

    # write the key and don't forget

    with open("serverkey.key", "wb") as serverkey:

        serverkey.write(key)

# creating unpredictable random dictionary


def random_dictionary():

    # creating random dictionary with random values

    words_dictionary = list("abcçdefgğhıijklmnoöprsştuüvyzqwx()/\ .,?!->1234567890")

    # to update an list

    dictionary = {}

    values = random.sample(range(0, 10000000000), k=52)

    # match random values and words of dictionary

    for key, value in zip(words_dictionary, values):

        # add the dictionary key-value pairs

        dictionary.update({key: value})

    # save as json file

    with open("server_dictionary.json", "w", encoding="utf-8") as file:

        json.dump(dictionary, file, ensure_ascii=False, indent=5)

# encrypt json file


def encrypt_data():

    """this section gathers all functions in """
    """run other functions"""

    key_generator()

    random_dictionary()

    # encrypt the data with serverkey

    # read hashed serverkey

    with open("serverkey.key", "rb") as serverkey:

        key = serverkey.read()

    # variable for encryption

    encryptor = Fernet(key)

    # read original file to encrypt

    with open("server_dictionary.json", "rb") as original_file:

        original = original_file.read()

    # encryption

    encrypted_file = encryptor.encrypt(original)

    # writing the file

    with open("encrypted_dictionary.txt", "wb") as last:

        encrypted_dictionary = last.write(encrypted_file)

    return encrypted_dictionary


# just import encrypt data function it is already includes others

# create crypto

encrypt_data()


