from typing import List
from src.classes.util import Util
from src.classes.present import PRESENT 
import os


class UI:
  def menu(self):
    options = {
      1: self.__encrypt_ui,
      2: self.__decrypt_ui
    } 
    
    print("(1) Encryption")
    print("(2) Decryption")
    option = int(input("Choose and option: "))

    options[option]()

  
  def clear_screen(self):
    os.system("cls")

  def __encrypt_ui(self):
    key = input("Key (20-digit or 32-digit hex): ")
    plain_text = input("Message (text): ")
    plain_text_blocks = Util.split_to_64_blocks(Util.string_to_hex_string(plain_text))
    present = PRESENT(key)
    output_blocks: List[str] = []
    
    for block in plain_text_blocks:
      output_blocks.append(present.encrypt(block))

    print("Cipher blocks: "," ".join(output_blocks))

  def __decrypt_ui(self):
    key = input("Key (20-digit or 32-digit hex): ")
    cipher_blocks = input("Cipher (Blocks) : ")
    cipher_blocks = cipher_blocks.split(" ")
    present = PRESENT(key)
    output_blocks: List[str] = []

    for block in cipher_blocks:
      output_blocks.append(present.decrypt(block))

    print("Message (text):", "".join([Util.hex_string_to_string(block) for block in output_blocks]))