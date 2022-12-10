import codecs

class Util:

  @staticmethod
  def string_to_number(string: str) -> int:
    return int(codecs.encode(string, "hex"), 16)
  
  @staticmethod
  def number_to_string(number: int, size: int) -> str:
    output = '%0*x' % (size * 2, number)
    output = codecs.decode(output, "hex")
    return output
