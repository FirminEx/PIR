from server_new import Server
from client_new import Client
import random
import time
import sys

sys.set_int_max_str_digits(999999999) 


def assert_result(): 
  server = Server(3, 3)
  client = Client(16)
  request_column = 2
  request_row = 2

  (v, public_key) = client.request(3, request_column)
  server_answer = server.answer(v, public_key)
  
  assert(client.decrypt_answer(server_answer, request_row) == server.db[request_row][request_column])
  
assert_result()
  
prime_size = 16
db_columns = 3
db_rows = 3
  

def mesure_time(db_size):
  client = Client(prime_size)
  server = Server(db_columns, db_rows)
  request_column = random.randint(0, db_columns - 1)
  request_row = random.randint(0, db_rows - 1)
  
  start = time.time()
  (v, public_key) = client.request(db_size, request_column)
  end = time.time()
  client_time = end - start


  start = time.time()  
  server_answer = server.answer(v, public_key)
  end = time.time()
  server_time = end - start

  print(server_answer, server.db[request_row])
  assert(client.decrypt_answer(server_answer, request_row) == server.db[request_row][request_column])
  return (client_time, server_time)
  

print(mesure_time(5))
print(mesure_time(10))
print(mesure_time(15))
print(mesure_time(20))
print(mesure_time(25))
print(mesure_time(30))
