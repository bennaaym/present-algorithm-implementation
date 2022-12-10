class AddRoundKeyLayer:

  @staticmethod
  def add_round_key(state: int, round_key: int) -> int:
    return state ^ round_key