from Credentialsclass import Credentials
import unittest
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.myCred = Credentials("Facebook", "MbaireNat", "nicole")

        def test_Init_(self):
            self.assertEqual(self.myCred.account, "Facebook")
        self.assertEqual(self.myCred.username, "MbaireNat")
        self.assertEqual(self.myCred.password, "nicole")
    def tearDown(self):
        Credentials.creden_list = []
    def test_save_credentials(self):
        self.myCred.saveCred()
        test_cred = Credentials("Facebook", "MbaireNat", "nicole")
        test_cred.saveCred()
        self.assertEqual(len(Credentials.creden_list),2)

    def test_displayCredentials(self):
        self.assertEqual(Credentials.displayCredentials(), Credentials.creden_list)
    
   
    
if __name__ == "__main__":
    unittest.main()
