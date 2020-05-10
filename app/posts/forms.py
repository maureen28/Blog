from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[DataRequired()])
    post = TextAreaField("Type Away", validators=[DataRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[DataRequired()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")
