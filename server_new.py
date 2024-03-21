import random
import math
import sys

class Server:
  def __init__(self, db_columns, db_rows):
    random_ceil = 2 ** 16
    self.db = [[random.randint(1, random_ceil) for _ in range(db_columns)] for _ in range(db_rows)]
    self.db_rows = db_rows
    self.db_columns = db_columns
    
  def answer(self, v, public_key):
    t = [math.prod([v[i] ** self.db[i][j] for i in range(self.db_columns)]) for j in range(self.db_rows)]
    print('server payload', sys.getsizeof(t))
    return t
    