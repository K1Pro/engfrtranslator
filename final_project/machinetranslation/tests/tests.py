import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Nom'),'Name')
        self.assertNotEqual(french_to_english('Pays'),'Country')
        
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('tired'),'fatigué')
        self.assertNotEqual(english_to_french('excited'),'excité')
        
unittest.main()        
