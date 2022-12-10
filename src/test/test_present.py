import unittest
from src.classes.present import PRESENT


class TestPresentApi(unittest.TestCase):

  def test_encryption_80_bits_key(self) -> None:
    key = "00000000000000000000"
    plain_text = "0000000000000000"
    present = PRESENT(key)
    cipher_text = present.encrypt(plain_text)
    self.assertEqual(cipher_text, "5579c1387b228445")

  def test_encryption_128_bits_key(self) -> None:
    key = "0123456789abcdef0123456789abcdef"
    plain_text = "0123456789abcdef"
    present = PRESENT(key)
    cipher_text = present.encrypt(plain_text)
    self.assertEqual(cipher_text, "0e9d28685e671dd6")

  def test_decryption_80_bits_key(self) -> None:
    key = "00000000000000000000"
    cipher_text = "5579c1387b228445"
    present = PRESENT(key)
    plain_text = present.decrypt(cipher_text)
    self.assertEqual(plain_text, "0000000000000000")

  def test_decryption_128_bits_key(self) -> None:
    key = "0123456789abcdef0123456789abcdef"
    cipher_text = "0e9d28685e671dd6"
    present = PRESENT(key)
    plain_text = present.decrypt(cipher_text)
    self.assertEqual(plain_text, "0123456789abcdef")

if __name__ == "__main__":
  unittest.main()