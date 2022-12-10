from functools import reduce 
from typing import List


s_box: List[int] = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
inverse_s_box: List[int] = [s_box.index(x) for x in range(16)]

class SBoxLayer:
  s_box = s_box
  inverse_s_box = inverse_s_box

  @classmethod
  def substitute(cls, state: int) -> int:
    output = 0
    for i in range(16):
      output += cls.s_box[( state >> (i * 4)) & 0xF] << (i * 4)
    return output
  
  @classmethod
  def inverse_substitute(cls, state: int) -> int:
    output = 0
    for i in range(16):
      output += cls.inverse_s_box[( state >> (i * 4)) & 0xF] << (i * 4)
    return output
