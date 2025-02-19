from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    latest_posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()
    return render_template('home.html', posts=posts, latest_posts=latest_posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.app_context_processor
def inject_latest_posts():
    latest_posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()
    return dict(latest_posts=latest_posts)
