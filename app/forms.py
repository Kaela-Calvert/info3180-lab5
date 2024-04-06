# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from wtforms import StringField, TextAreaField
# from wtforms.validators import InputRequired

# class MovieForm(FlaskForm):
#     title = StringField('Title', validators=[InputRequired()])
#     description = TextAreaField('Description', validators=[InputRequired()])
#     poster = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png','jpeg'], 'Please check that you are uploading an image!')])

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Poster', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])