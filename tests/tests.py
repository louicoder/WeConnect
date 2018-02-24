import unittest
from models.user import User
from models.business import Business
from models.review import Reviews

class testingUser(unittest.TestCase):   
    
    def setUp(self):
        self.user = User(1, 'louis', 'louis@email.com', 'secretPassword')

    def test_userInstance(self):        
        self.assertIsInstance(self.user, User)        

    def test_createUser_successful(self):
        result = self.user.createUser(1, 'louis', 'louis@email.com', 'secretPassword')
        self.assertTrue(result)

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

    # def test_deleteBusiness(self):
    #     result = self.biz.deleteBusiness(1)
    #     self.assertFalse(result)

    def test_getOwnBusiness(self):
        result = self.biz.getOwnBusinesses(1)
        self.assertEqual(result, '')

    def test_getAllBusinesses(self):
        result = self.biz.getAllBusinesses()
        self.assertEqual(result, [])


class testReviews(unittest.TestCase):
    """this test class is for testing the class Reviews"""
    def setUp(self):
        self.review = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')    

    def test_reviewInstance(self):
        review = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')
        self.assertIsInstance(review, Reviews)

    def test_createNewReview(self):        
        final =self.review.createNewReview(1, 1, 1, 'louis', 'review')
        self.assertTrue(final)

    def test_getBusinessReviews(self):
        # result = Reviews(1, 1, 1, 'currentuser', 'your business is thrilling')
        final = self.review.getBizReviews(1)
        self.assertFalse(final)

if __name__ == '__main__':
    unittest.main()