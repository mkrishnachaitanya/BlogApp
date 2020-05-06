import datetime
from .db import db

class Blog(db.Document):
    title = db.StringField(required=True)
    body = db.StringField(required=True)
    tags = db.ListField(required=True)
    article_image_url = db.URLField(required=True)
    published_at = db.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))