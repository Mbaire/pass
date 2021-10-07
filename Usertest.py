from Userclass import User
import unittest
class TestUser(unittest.TestCase):
    def setUp(self):
        self.myUser= User("Mbairenat","123456789")
    def test__init__(self):
        self.assertEqual(self.myUser.username,"Mbairenat")
        self.assertEqual(self.myUser.password,"123456789")
    def tearDown(self):
        User.users = []
    def test_save_user(self):
        self.myUser.saveUser()
        test_user = User("Mbairenat","07123456789")
        test_user.saveUser()
        self.assertEqual(len(User.users),2)
    def test_display_users(self):
        self.assertEqual(User.displayUsers(),User.users)
        

if __name__ == "__main__":
    unittest.main()