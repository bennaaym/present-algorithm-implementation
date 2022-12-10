from typing import List


p_box: List[int] = [
    0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
    4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
    8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
    12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63
  ]

inverse_p_box: List[int] = [p_box.index(x) for x in range(64)]

class PLayer:
  p_box = p_box
  inverse_p_box = inverse_p_box

  @classmethod
  def permute(cls, state: int) -> int:
    output = 0
    for i in range(64):
      output += ((state >> i) & 0x01) << cls.p_box[i]
    return output

  @classmethod
  def inverse_permute(cls, state: int) -> int:
    output = 0
    for i in range(64):
      output += ((state >> i) & 0x01) << cls.inverse_p_box[i]
    return output

