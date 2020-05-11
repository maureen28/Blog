from flask import render_template, url_for, flash,redirect, request, abort
from flask import Blueprint
from flask_login import current_user, login_required
from app import db
from app.models import Post, Comment
from app.posts.forms import PostForm, CommentForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data , author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('pitch.html', title='New Blog Post',form=form, legend='New Blog Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id = post_id).all()
    return render_template('post.html', title=post.title, post=post,comments = comments)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your pitch post has been updated successfully!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('pitch.html', title='Update Post',form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/post/<int:post_id>/comment", methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, post_id = post_id )
        db.session.add(comment)
        db.session.commit()
        flash('Comment has been added!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    return render_template('comment.html', title='Comment Here', form=form, legend='Comment Here')

@posts.route("/post/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    post = Post.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.home", id = post.id))