from paillier import Paillier
import sys

class Client: 
  def __init__(self, bits):
    self.phe = Paillier(bits)
    
  def request(self, db_size: int, column_index: int):
    if(column_index > db_size):
      raise Exception('Index out of range')
    
    enc0 = self.phe.encrypt(0, self.phe.public_key)
    v = [enc0 for i in range(db_size)]
    v[column_index] = self.phe.encrypt(1, self.phe.public_key)
    print('client payload', sys.getsizeof(v))
    return (v, self.phe.public_key)
  
  def decrypt_answer(self, answer: int, row_index):
    return self.phe.decrypt(answer[row_index])
    
