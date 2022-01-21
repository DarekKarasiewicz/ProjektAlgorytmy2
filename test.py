import unittest
import darek_huffman

class Huffman_test():
    def test_encode(self):
        ct, cd = darek_huffman.encode.encode(self.cleartext)
        self.assertEqual(self.ciphertext,ct) 
        self.assertEqual(self.code,cd)
        
    def test_decode(self): 
        cl = darek_huffman.decode.decode(self.ciphertext,self.code)
        self.assertEqual(self.cleartext,cl) 

class Simple_test(Huffman_test,unittest.TestCase):
    cleartext = "daa"
    ciphertext = "111010"
    code = { "d" : "11" , "a" : "10" }

    
class Compicated_test(Huffman_test,unittest.TestCase):
    cleartext = "daareeekkkkk"
    ciphertext = "1111111101110111101101101101010101010"
    code = {'d': '11111', 'a': '1110', 'r': '11110', 'e': '110', 'k': '10'}


unittest.main()
