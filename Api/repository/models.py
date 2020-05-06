import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from .db import db

class Blog(db.Document):
    title = db.StringField(required=True)
    body = db.StringField(required=True)
    tags = db.ListField(required=True)
    article_image_url = db.URLField(required=True)
    published_at = db.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    added_by = db.ReferenceField('User')

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    is_confirmed = db.BooleanField(default=False)
    joined_at = db.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    profile_picture = db.URLField()
    blogs = db.ListField(db.ReferenceField('Blog', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Blog, 'added_by', db.CASCADE) 
