from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, PasswordField, FileField, SelectField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Enter the underground")


class MiiUploadForm(FlaskForm):
    mii = FileField("Mii Selection", validators=[FileRequired()])
    name = StringField("Mii Name", validators=[DataRequired()])
    color1 = StringField("Color 1 (Hex)", validators=[DataRequired()])
    color2 = StringField("Color 2 (Hex)", validators=[DataRequired()])
    upload = SubmitField("Add Mii")


class MovieUploadForm(FlaskForm):
    movie = FileField("Movie", validators=[FileRequired()])
    title = StringField("Movie title", validators=[DataRequired(), Length(max=48)])
    thumbnail = FileField("Movie thumbnail", validators=[FileRequired()])
    # Choices for the select field are only evaluated once, so we must set it when necessary.
    category = SelectField("Movie category", validators=[DataRequired()])
    upload = SubmitField("Add Movie")


class ParadeForm(FlaskForm):
    miiid = StringField("Mii ID", validators=[DataRequired()])
    company = StringField("Company", validators=[DataRequired()])
    image = StringField("Image Encoded in Base64", validators=[DataRequired()])
    submit = SubmitField("Create")


class KillMii(FlaskForm):
    # Form for deleting a concierge mii
    given_mii_id = StringField("Mii ID", validators=[DataRequired()])
    submit = SubmitField("Delete!")


class ConciergeForm(FlaskForm):
    prof = StringField("Profession", validators=[DataRequired()])
    message1 = StringField("Message 1", validators=[DataRequired()])
    message2 = StringField("Message 2", validators=[DataRequired()])
    message3 = StringField("Message 3", validators=[DataRequired()])
    message4 = StringField("Message 4", validators=[DataRequired()])
    message5 = StringField("Message 5", validators=[DataRequired()])
    message6 = StringField("Message 6", validators=[DataRequired()])
    message7 = StringField("Message 7", validators=[DataRequired()])
    movieid = StringField("Movie ID", validators=[DataRequired()])
    submit = SubmitField("Create!")

    # def validate_miiid(self, miiid):
    #     query = ConciergeMii.query.filter_by(mii_id=miiid.data).first()
    #     if query is not None:
    #         raise ValidationError("Mii ID taken, add 1 to it")


class PosterForm(FlaskForm):
    pass
