import unittest 
import os
from utils import *

class TestUtils(unittest.TestCase):

  def test_read_file(self):
    employees: str = read_file(self.input_file)
    for e in employees:
      employees_names = []
      employees_names.append(e.name)
      for e in employees:
          self.assertTrue('RENE' in employees_names)
          self.assertTrue('ASTRID' in employees_names)
  

  def test_split_time(self):
    time = '10:00-13:00'
    time = time.split('-')  
    result = split_time(time)
    self.assertEqual(result,(10,13))





  if __name__ == "__main__":
    unittest.main()