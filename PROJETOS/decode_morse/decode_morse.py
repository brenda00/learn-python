import os
import sys
import datetime
import pandas as pd
from config import file_path, dict_morse

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços
    output : palavra escrito em letras e algarismos
    '''
    text_decoded = []
    words_encoded = msg.split("  ")
    for word_encoded in words_encoded:
        letters_encoded = word_encoded.split(" ")
        word_decoded = []
        for letter in letters_encoded:
            word_decoded.append(dict_morse[letter])
        text_decoded.append("".join(word_decoded))
    return " ".join(text_decoded)

def save_clear_msg_csv_hdr(msg_claro):
    '''
    input : mensagem em texto claro
    output : palavra escrito em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

def encode_morse(msg):
    dict_alphabet_to_morse = {letter: morse for morse, letter in dict_morse.items()}
    words = msg.split(' ')
    words_encoded = []
    for word in words:
        letters_encoded = []
        for letter in word:
            letter_encoded = dict_alphabet_to_morse[letter.upper()]
            letters_encoded.append(letter_encoded)
        words_encoded.append(" ".join(letters_encoded))
    msg_encoded = "  ".join(words_encoded)
    return msg_encoded


if __name__ == "__main__":
    #msg = encode_morse(sys.argv[1])
    #print(msg)
    msg_claro = decode_morse(sys.argv[1])
    save_clear_msg_csv_hdr(msg_claro)
    #print(save_clear_msg_csv_hdr.__doc__)
    #print(pd.to_pickle.__doc__)