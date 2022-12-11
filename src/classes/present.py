from classes.key_scheduler import KeySchedular
from classes.add_round_key import AddRoundKeyLayer
from classes.s_box_layer import SBoxLayer
from classes.p_layer import PLayer
from classes.util import Util
import codecs


class PRESENT:
  rounds = 32
  def __init__(self, key: str) -> None:
    self.__key_schedular = KeySchedular(codecs.decode(key, "hex"))
  
  def encrypt(self, plain_text: str) -> str:
    state: int = Util.string_to_number(codecs.decode(plain_text, "hex"))
    for i in range(self.rounds - 1):
      state = AddRoundKeyLayer.add_round_key(state, self.__key_schedular.round_keys[i])
      state = SBoxLayer.substitute(state)
      state = PLayer.permute(state)
    
    cipher_text = AddRoundKeyLayer.add_round_key(state, self.__key_schedular.round_keys[-1])
    cipher_text =  Util.number_to_string(cipher_text, 8)
    cipher_text = codecs.encode(cipher_text, "hex")
    return str(str(cipher_text)[2:-1])

  
  def decrypt(self, cipher_text: str) -> str:
    state: int = Util.string_to_number(codecs.decode(cipher_text, "hex"))
    for i in range(self.rounds - 1):
      state = AddRoundKeyLayer.add_round_key(state, self.__key_schedular.round_keys[-i - 1])
      state = PLayer.inverse_permute(state)
      state = SBoxLayer.inverse_substitute(state)
    
    plain_text = AddRoundKeyLayer.add_round_key(state, self.__key_schedular.round_keys[0])
    plain_text = Util().number_to_string(plain_text, 8)
    plain_text = codecs.encode(plain_text, "hex")
    return str(str(plain_text)[2:-1])