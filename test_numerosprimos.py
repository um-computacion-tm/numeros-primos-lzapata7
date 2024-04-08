import unittest

from numerosprimos import is_prime

class TestIsPrime (unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertEqual(result,True)
 
    def test_with_2(self):
        result = is_prime(2)
        self.assertEqual(result,True)      
        
    def test_with_3(self):
        result = is_prime(3)
        self.assertEqual(result,True)     
        
    def test_with_4(self):
        result = is_prime(4)
        self.assertEqual(result,False)  

    def test_with_5(self):
        result = is_prime(5)
        self.assertEqual(result,True) 

    def test_with_6(self):
        result = is_prime(6)
        self.assertEqual(result,False) 
    
    def test_with_18(self):
        result = is_prime(18)
        self.assertEqual(result,False)
        
    def test_with_23(self):
        result = is_prime(23)
        self.assertEqual(result,True)
        
    def test_with_387(self):
        result = is_prime(387)
        self.assertEqual(result,False)

    def test_with_88732(self):
        result = is_prime(88732)
        self.assertEqual(result,False)
        
    def test_with_17771(self):
        result = is_prime(17771)
        self.assertEqual(result,False)
if __name__ == '__main__':
    unittest.main()