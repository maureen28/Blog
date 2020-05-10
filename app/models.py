from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique= True, nullable = False )
    email = db.Column(db.String(120), unique= True, nullable = False )
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpeg' )
    password = db.Column(db.String(60), nullable = False )
    posts = db.relationship('Post', backref = 'author', lazy = True)
  
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
       return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    category = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
    
    def __repr__(self):
        return f'Post("{self.title}","{self.date_posted}")'

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_at = db.Column(db.DateTime)
    comment_by = db.Column(db.String)
    like_count = db.Column(db.Integer, default = 0)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(cls, id):
        gone = Comment.query.filter_by(id = id).first()
        db.session.delete(gone)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id = id).all()
        return comments        


    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # User like logic
    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id = self.id, post_id = post.id)
            db.session.add(like)

    # User dislike logic
    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id = self.id,
                post_id = post.id).delete()

    # Check if user has liked post
    def has_liked_post(self, post):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == post.id).count() > 0

    def __repr__(self):
        return f"User {self.username}"


class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)


class PostLike(db.Model):
    __tablename__ = "post_like"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))


class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
        