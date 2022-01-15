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
    
    def test_more_compicated_encode(self):
        cleartext = "daareeekkkkk"
        ciphertext = "1111111101110111101101101101010101010"
        code = {'d': '11111', 'a': '1110', 'r': '11110', 'e': '110', 'k': '10'}
        ct, cd = darek_huffman.encode.encode(cleartext)
        self.assertEqual(ciphertext,ct) 
        self.assertEqual(code,cd)

unittest.main()
