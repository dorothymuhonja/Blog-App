from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import required

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Write Blog')
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    blog = TextAreaField('Write a Comment')
    submit = SubmitField('submit') 

class BioForm(FlaskForm):
    bio = TextAreaField('Introduce yourself')
    submit = SubmitField('submit') 
    
     