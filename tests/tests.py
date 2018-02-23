import unittest
from models import user
from reviews import Reviews
from user import User

class testingUser(unittest.TestCase):

    # def setUp(self):
    #     sys.path.insert(0, "../mod")
    #     from mod import user
    
    def setUp(self):
        self.user = User(1, 'louis', 'louis@email.com', 'secretPassword')

    def test_userInstance(self):
        # lets test the instance of the user class
        self.assertIsInstance(self.user, User)
        

    def test_createUser_successful(self):
        result = self.user.createUser(1, 'louis', 'louis@email.com', 'secretPassword')
        self.assertFalse(result)

    def test_checkUsernameExists(self):
        result = self.user.checkUsernameExists('louis')
        self.assertFalse(result)

class testingBusiness(unittest.TestCase):

    def setUp(self):
        self.biz = Business(1, 1, 'las computers', 'location', 'bizCategory', 'bizDescription')

    def test_bizInstance(self):
        self.assertIsInstance(self.biz, Business)

    def test_createBusiness(self):
        result = self.biz.createBusiness(1, 1, 'anybusiness', 'anylocation', 'anycategory','the best business')
        self.assertTrue(result)

    def test_checkBusinessExists(self):
        result = self.biz.checkBusinessExists(1)
        self.assertFalse(result)

    def test_updateBusiness(self):
        result = self.biz.updateBusiness(1, 1, 'anybusiness', 'anylocation', 'anycategory','the best business')
        self.assertFalse(result)

    def test_deleteBusiness(self):
        result = self.biz.deleteBusiness(1)
        self.assertFalse(result)

    def test_getOwnBusiness(self):
        result = self.biz.getOwnBusinesses(1)
        self.assertFalse(result)


class testReviews(unittest.TestCase):
    """this test class is for testing the class Reviews"""
    def setUp(self):
        review = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')    

    def test_reviewInstance(self):
        review = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')
        self.assertIsInstance(review, Reviews)

    def test_createReview(self):
        result = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')
        final = result.createNewReview(1, 1, 1, 'louis', 'review')
        self.assertTrue(final)

    def test_getBusinessReviews(self):
        result = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')
        final = result.getBizReviews(1)
        self.assertFalse(final)

if __name__ == '__main__':
    unittest.main()