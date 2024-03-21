from paillier import Paillier

class Client: 
  def __init__(self, bits):
    self.phe = Paillier(bits)
    
  def request(self, db_size: int, index: int):
    if(index > db_size):
      raise Exception('Index out of range')
    
    enc0 = self.phe.encrypt(0, self.phe.public_key)
    v = [enc0 for i in range(db_size)]
    v[index] = self.phe.encrypt(1, self.phe.public_key)
    return (v, self.phe.public_key)
  
  def decrypt_answer(self, answer: int):
    return self.phe.decrypt(answer)
    
