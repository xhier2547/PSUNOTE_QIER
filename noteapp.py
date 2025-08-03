import flask

import models
import forms


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "This is secret key"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://coe:CoEpasswd@localhost:5432/coedb"

models.init_app(app)


@app.route("/")
def index():
    db = models.db
    notes = db.session.execute(
        db.select(models.Note).order_by(models.Note.title)
    ).scalars()
    return flask.render_template(
        "index.html",
        notes=notes,
    )


@app.route("/notes/create", methods=["GET", "POST"])
def notes_create():
    form = forms.NoteForm()
    if not form.validate_on_submit():
        print("error", form.errors)
        return flask.render_template(
            "notes-create.html",
            form=form,
        )
    
    # The form's populate_obj works here because we are creating a new note
    # and manually handling the tags relationship immediately after.
    note = models.Note()
    form.populate_obj(note) 
    note.tags = []

    db = models.db
    for tag_name in form.tags.data:
        tag = (
            db.session.execute(db.select(models.Tag).where(models.Tag.name == tag_name))
            .scalars()
            .first()
        )

        if not tag:
            tag = models.Tag(name=tag_name)
            db.session.add(tag)

        note.tags.append(tag)

    db.session.add(note)
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

@app.route("/notes/<int:note_id>/delete", methods=["POST"])
def notes_delete(note_id):
    db = models.db
    note = db.get_or_404(models.Note, note_id)
    
    db.session.delete(note)
    db.session.commit()
    
    return flask.redirect(flask.url_for("index"))

@app.route("/tags/<int:tag_id>/delete", methods=["POST"])
def tags_delete(tag_id):
    db = models.db
    tag = db.get_or_404(models.Tag, tag_id)

    db.session.delete(tag)
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

# vvv THIS ENTIRE FUNCTION HAS BEEN CORRECTED vvv
@app.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
def notes_edit(note_id):
    db = models.db
    note = db.get_or_404(models.Note, note_id)
    # Pass the note object to the form for GET requests to pre-fill the fields
    form = forms.NoteForm(obj=note)

    if form.validate_on_submit():
        # DO NOT use form.populate_obj(note) here as it causes an error
        # with the tags relationship.
        
        # Instead, manually update the note's attributes from the form data.
        note.title = form.title.data
        note.description = form.description.data

        # And manually handle the tags, converting strings to Tag objects.
        note.tags = []
        for tag_name in form.tags.data:
            tag = (
                db.session.execute(db.select(models.Tag).where(models.Tag.name == tag_name))
                .scalars()
                .first()
            )

            if not tag:
                tag = models.Tag(name=tag_name)
                db.session.add(tag)

            note.tags.append(tag)
        
        db.session.commit()
        return flask.redirect(flask.url_for("index"))

    # For a GET request, or if validation fails on POST, render the edit page.
    return flask.render_template("note-edit.html", form=form)
# ^^^ END OF CORRECTION ^^^

@app.route("/tags/<int:tag_id>/edit", methods=["GET", "POST"])
def tags_edit(tag_id):
    db = models.db
    tag = db.get_or_404(models.Tag, tag_id)
    form = forms.TagEditForm(obj=tag)

    if form.validate_on_submit():
        tag.name = form.name.data
        db.session.commit()
        return flask.redirect(flask.url_for("tags_view", tag_name=tag.name))

    return flask.render_template("tag-edit.html", form=form, tag=tag)


@app.route("/tags/<tag_name>")
def tags_view(tag_name):
    db = models.db
    tag = (
        db.session.execute(db.select(models.Tag).where(models.Tag.name == tag_name))
        .scalars()
        .first()
    )
    if not tag:
        return "Tag not found", 404
        
    notes = db.session.execute(
        db.select(models.Note).where(models.Note.tags.any(id=tag.id))
    ).scalars()

    # Pass the entire tag object to the template
    return flask.render_template(
        "tags-view.html",
        tag=tag,
        notes=notes,
    )


if __name__ == "__main__":
    app.run(debug=True)