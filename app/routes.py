from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegistrationForm, PostForm, AddCommentForm
from flask_login import logout_user, login_required, current_user
from .models import create_user, create_post, get_posts, update_posts
from .database import get_pyMongoDb

bp = Blueprint('main', __name__)
my_user = {}

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print('Form data1:', email)

        # Check if credentials match
        app_database = get_pyMongoDb()
        user = app_database.db.users.find_one({'email': email})
        if user['password'] == password:
            global my_user
            my_user = user
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html', form=form)


@bp.route('/signup', methods=['Get', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        app_database = get_pyMongoDb()
        print('user', app_database)

        if app_database.db.users.find_one({'email': email}):
            flash('Email is already registered. Please log in.', 'danger')
        else:
            create_user(email, password, username)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('main.login'))

    return render_template('signup.html', form=form)


@bp.route('/home', methods=['Get', 'POST'])
def home():
    list_of_posts = get_posts()

    newPostForm = PostForm()
    if request.method == 'POST' and newPostForm.validate_on_submit():
        create_a_post(newPostForm)
        return redirect(url_for('main.home'))

    addCommentForm = AddCommentForm()
    if request.method == 'POST' and addCommentForm.validate_on_submit():
        update_posts({})
        form_type = request.form.get('form_type')
        if form_type == 'comment':
            comment_text = request.form.get('comment')
            post_id = request.form.get('post_id')

            if comment_text and post_id:
                print(post_id, comment_text)
                # update_result = update_post(post_id, comment_text)
                # if update_result:
                #     response = {
                #         'status': 'success',
                #         'post_id': post_id
                #     }
                #     return jsonify(response)
                # else:
                response = {
                    'status': 'error',
                    'message': 'Failed to update post.'
                }
                return jsonify(response)
        print(addCommentForm.comment.data)
        # addCommentForm(newPostForm)

    return render_template('home_page/home_page.html', newPostForm=newPostForm, addCommentForm=addCommentForm, posts=list_of_posts)


def create_a_post(postData):
    newPost = postData.post.data
    if request.method == 'POST':
        post = {
            'posted_by': {'user_id': my_user['_id'], 'user_name': my_user['username'], 'user_email': my_user['email'], },
            'posted_content': {'content': newPost},
        }
    create_post(post)
    flash('Posted successfully!', 'success')
