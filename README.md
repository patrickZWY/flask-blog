# flask-blog

to create db, do:
from flaskblog import app, db
app.app_context().push()
db.create_all()

to experiment with queries:
from flaskblog.models import User, Post
User.query.all()

start virtual env: source name-of-virtual-folder/bin/activate

to download packages, pip install -r requirements.txt

macos airplay listening on port 5000
lsof -i :5000 to check
