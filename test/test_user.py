import unittest
from app.models import User, Post

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'alcohol')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('alcohol'))
   
class TestPost(unittest.TestCase):
    
   def setUp(self):
        self.user_nimo = User(username = 'nimo',password = 'love123',email = 'nimz69509@gmail.com')
        self.new_post = Post(post_title = 'Fashion',
                            post_content = 'Fashion is like eating, you should not stick to the same menu',
                            user_id = self.user_nimo.id)
        self.new_comment = Comment(comment = 'Nice',
                                    post_id = self.new_post.id,
                                    user_id = self.user_nimo.id)

   def test_instance(self):
        self.assertTrue(isinstance(self.user_nimo, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))
