from wtforms_sqlalchemy.orm import model_form
from flask_wtf import FlaskForm
from wtforms import Field, widgets
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import models


class TagListField(Field):
    widget = widgets.TextInput()

    def __init__(self, label="", validators=None, remove_duplicates=True, **kwargs):
        super().__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates
        self.data = []

    def process_formdata(self, valuelist):
        data = []
        if valuelist:
            data = [x.strip() for x in valuelist[0].split(",")]

        if not self.remove_duplicates:
            self.data = data
            return

        self.data = []
        for d in data:
            if d not in self.data:
                self.data.append(d)

    def _value(self):
        if self.data:
            # vvv FIX IS HERE vvv
            # แปลง Tag object เป็นชื่อ (string) ก่อนนำไป join
            return ", ".join([str(d.name) if isinstance(d, models.Tag) else str(d) for d in self.data])
            # ^^^ FIX IS HERE ^^^
        else:
            return ""


BaseNoteForm = model_form(
    models.Note, base_class=FlaskForm, exclude=["created_date", "updated_date"], db_session=models.db.session
)

class NoteForm(BaseNoteForm):
    tags = TagListField("Tag")

class TagEditForm(FlaskForm):
    name = StringField("Tag Name", validators=[DataRequired()])
    submit = SubmitField("Update Tag")