from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdatePostForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    post = TextAreaField('Update Post', validators=[Required()])
    submit = SubmitField('Update')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave A Comment', validators=[Required()])
    alias = StringField('Comment )
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg', 'png'])])
    email = StringField('Email ', validators=[DataRequired(),Email()])
    submit = SubmitField('Update')
    