import unittest
import darek_huffman

class jakiśtest(unittest.TestCase):
    def test_encode(self):
        cleartext = "daa"
        ciphertext = "111010"
        code = { "d" : "11" , "a" : "10" }
        ct, cd = darek_huffman.encode.encode(cleartext)
        self.assertEqual(ciphertext,ct) 
        self.assertEqual(code,cd)
        
    def test_decode(self): 
        cleartext = "daa"
        ciphertext = "111010"
        code = { "d" : "11" , "a" : "10" }
        cl = darek_huffman.decode.decode(ciphertext,code)
        self.assertEqual(cleartext,cl) 


unittest.main()
