import random
from paillier import Paillier
import math
from client import Client
import sys

class Server: 
  def __init__(self, db_size: int):
    self.db_size = db_size
    random_ceil = 2 ** 16
    self.db = [random.randint(1, random_ceil) for _ in range(db_size)]
    
  def answer(self, v, public_key: (int, int)):
    t = math.prod([v[i] ** self.db[i] for i in range(self.db_size)])
    print('server payload', sys.getsizeof(t))
    return t
    
    

    