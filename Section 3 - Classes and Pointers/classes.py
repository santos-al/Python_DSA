class Cookie:
  def __init__(self, color: str) -> None:
    self.color = color

  def get_color(self) -> str :
    return self.color

  def set_color(self, color: str) -> None:
    self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie("blue")