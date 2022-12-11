import codecs
from typing import List

class Util:

  @staticmethod
  def string_to_number(string: str) -> int:
    return int(codecs.encode(string, "hex"), 16)

  @staticmethod
  def number_to_string(number: int, size: int) -> str:
    output = '%0*x' % (size * 2, number)
    output = codecs.decode(output, "hex")
    return output

  @staticmethod
  def string_to_hex_string(string: str) -> str:
    return "".join([str(hex((int(str(ord(char)))))[2:]) for char in string])

  @staticmethod
  def hex_string_to_string(hex_string: str) -> str:
    return "".join([chr(int(hex_string[i] + hex_string[i + 1], 16)) for i in range(0, len(hex_string), 2)])

  @staticmethod
  def split_to_64_blocks(string: str) -> List[str]:
    blocks: List[str] = []
    for i in range(0, len(string), 16):
      blocks.append(string[i:i+16])
    return blocks