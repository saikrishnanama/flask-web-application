from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    post = TextAreaField('New Post',
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Add Post...",
                                    "style": "height: 45px; width: 350px; resize: none; border: 0.5px solid grey; padding: 10px 0px;"
                                    },
                         )
    submit = SubmitField('Submit',
                         render_kw={
                             "style": "padding: 10px; border-radius: 6px; border: none; color: aliceblue; background: rgb(65, 65, 230);"
                         }
                         )


class AddCommentForm (FlaskForm):
    comment = TextAreaField('',
                            render_kw={
                                "placeholder": "Add Comment..",
                                "style": "width: 100%;resize: none;"
                            }
                            )

    commentBtn = SubmitField('Comment',
                             render_kw={
                                 "style": "padding: 10px; border-radius: 6px; border: none; color: aliceblue; background: rgb(65, 65, 230);"
                             }
                             )
