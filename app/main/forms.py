from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
import email_validator
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Write Blog')
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    comment = TextAreaField('Write a Comment')
    submit = SubmitField('submit') 

class BioForm(FlaskForm):
    bio = TextAreaField('Introduce yourself')
    submit = SubmitField('submit') 
    
     