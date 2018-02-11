from flask import Flask, render_template
from flask_login import LoginManager
from bearword_blog.bearword_blog import BloggingEngine
from bearword_blog.bearword_blog.dynamodbstorage import DynamoDBStorage
from .routes import setup_auth
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")

# Find database
AWS_PART = 'us-east-2'
BEWO_DYNAMO = os.environ.get('BEWO_DYNAMO', AWS_PART)
dynamo_sources = ['endpoint_url', 'region_name']
dyn_storage = DynamoDBStorage(**{
    dynamo_sources[BEWO_DYNAMO == AWS_PART]: BEWO_DYNAMO,
})
# extensions
blog_engine = BloggingEngine(app, dyn_storage)
login_manager = LoginManager(app)


@app.route("/")
def index():
    return render_template("index.html")

setup_auth(app, login_manager, blog_engine)

if __name__ == "__main__":
    app.run(debug=True, port=8001, use_reloader=True, )

