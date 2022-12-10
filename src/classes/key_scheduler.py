from typing import List
from src.classes.util import Util
from src.classes.s_box_layer import SBoxLayer

class KeySchedular:
  def __init__(self, key: str) -> None:
    self.__round_keys: List[int] = self.__generate_round_keys(key)

  # getters
  @property
  def round_keys(self) -> List[int]:
    return self.__round_keys

  # private method
  def __generate_round_keys(self, key: str) -> List[int]:
    if len(key) * 8 == 80:
      return self.__generate_round_keys_80(Util.string_to_number(key))
    
    if len(key) * 8 == 128:
      return self.__generate_round_keys_128(Util.string_to_number(key))
    
    raise Exception("Key must be 80-bits or 128-bits")

  def __generate_round_keys_80(self, key: str) -> List[int]:
    """
    Generate the round keys for 80-bits long secret key
    """
    round_keys: List[int] = []
    for i in range(1, 33): 
      round_keys.append(key >> 16)
      key = ((key & (2**19 - 1)) << 61) + (key >> 19)
      key = (SBoxLayer.s_box[key >> 76] << 76) + (key & (2**76 - 1))
      key ^= i << 15
    return round_keys

  def __generate_round_keys_128(self, key: str) -> List[int]:
    round_keys: List[int] = []
    for i in range(1 ,33):
      round_keys.append(key >> 64)
      key = ((key & (2**67 - 1)) << 61) + (key >> 67)
      key = (SBoxLayer.s_box[key >> 124] << 124) + (SBoxLayer.s_box[(key >> 120) & 0xF] << 120) + (key & (2**120 - 1))
      key ^= i << 62
    return round_keys
