from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Optional

class PostForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  link = StringField('Link', validators=[URL(), Optional()])
  content = TextAreaField('Content', validators=[DataRequired()], render_kw={"rows": 7, "cols": 11})
  submit = SubmitField('Post')

