import unittest

from translator import english_to_french,french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Pepitoooo")
    
    def test2(self):
        self.assertNotEqual(english_to_french("You"),"Merci")
    
    def test3(self):
        self.assertEqual(english_to_french("Bonjour"),"Bonjour")

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    
    def test2(self):
        self.assertNotEqual(french_to_english("Toi"),"Bye")

unittest.main()