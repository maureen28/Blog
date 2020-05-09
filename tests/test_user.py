import unittest
from app.models import Post, User, Comment, Quote

class TestPost(unittest.TestCase):
    
   def setUp(self):
        self.user_1 = User(username= 'maureen',password = 'love234r',
                              email = 'nimo@gmail.com')
        self.new_post = Post(post_title = 'Blog',post_content = 'My First Blog', user_id = self.user_1.id)
        self.new_comment = Comment(comment = 'Best app ever',post_id = self.new_post.id, user_id = self.user_1.id)

   def test_instance(self):
        self.assertTrue(isinstance(self.user_1, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.random_quote = Quote("Nimo", "Your beautiful")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "Nimo")
        self.assertEqual(self.random_quote.quote,"Your beautiful")