# flask-blog

to create db, do:
from flaskblog import app, db
app.app_context().push()
db.create_all()

to experiment with queries:
from flaskblog.models import User, Post
User.query.all()