
class ChessKing:
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}

    def __init__(self, color='white', square=None):
        self.color = color
        if square is None:
            self.square = 'e1' if color == 'white' else 'e8'
        else:
            self.square = square

    def __repr__(self):
        return f"ChessKing(color={self.color}, square={self.square})"

    def __str__(self):
        return f"Chess King [{self.color}] on square {self.square}."

    def is_turn_valid(self, new_turn: str) -> bool:
        self.new_turn = new_turn

        num = int(self.square[-1])
        har = self.square[0]

        num_minus = max(num - 1, 1)
        num_sum = min(num + 1, 8)
        num_itog = [str(i) for i in range(num_minus, num_sum + 1)]

        index_car = list(ChessKing.files.keys()).index(har)

        har_itog = [list(ChessKing.files.keys())[i] for i in range(index_car - 1, index_car + 2) if 0 <= i < 8]

        combination = [var + intt for var in har_itog for intt in num_itog]

        if self.new_turn in combination:
            return True
        else:
            return False
        
    def turn(self, step: str ):
        self.step = step

        if self.is_turn_valid(step):
            self.square = step
            return print(f"Ход выполнен, новая координата {self.square}")
        else:
            raise TypeError(f"Ход не возможен , {self.step} - не корректный ход")



wk = ChessKing()
print(wk.color)
print(wk.square)

print(wk.turn("e2"))
print(wk.square)
print(wk.turn("f1"))
print(wk.square)

w = ChessKing("blac")
print(w.color)
print(w.square)

print(w.turn("d7"))
print(w.square)
print(w.turn("d8"))
print(w.square)
print(w.turn("d5"))

"""
white
e1
Ход выполнен, новая координата e2
None
e2
Ход выполнен, новая координата f1
None
f1
blac
e8
Ход выполнен, новая координата d7
None
d7
Ход выполнен, новая координата d8
None
d8
Traceback (most recent call last):
  File "/home/vsevolod/Рабочий стол/Krjukov/2024.05.20/test.py", line 68, in <module>
    print(w.turn("d5"))
  File "/home/vsevolod/Рабочий стол/Krjukov/2024.05.20/test.py", line 47, in turn
    raise TypeError("Ход не возможен - ход не выполнен")
TypeError: Ход не возможен , d5 - не корректный ход

"""