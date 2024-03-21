from client import Client
from server import Server
import random
import time

def assert_result(): 
  server = Server(10)
  client = Client(128)

  (v, public_key) = client.request(10, 4)
  server_answer = server.answer(v, public_key)

  assert(client.decrypt_answer(server_answer) == server.db[4])


prime_size = 16

def mesure_time(db_size):
  client = Client(prime_size)
  server = Server(db_size)
  index = random.randint(0, db_size - 1)
  
  start = time.time()
  (v, public_key) = client.request(db_size, index)
  end = time.time()
  client_time = end - start
  
  
  start = time.time()  
  server_answer = server.answer(v, public_key)
  end = time.time()
  server_time = end - start
  
  
  assert(client.decrypt_answer(server_answer) == server.db[index])
  return (client_time, server_time)