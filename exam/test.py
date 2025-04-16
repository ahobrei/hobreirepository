import unittest
from main import count_vowels 

class TestCountVowels(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)
    
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)
    
    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)
    
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)
    
    def test_mixed_case(self):
        self.assertEqual(count_vowels("AbCdeEfGh"), 3)  

if __name__ == "__main__":
    unittest.main()
