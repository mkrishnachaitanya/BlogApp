# urls.py
from .blog import BlogsApi, BlogApi
from .user import SignUpApi, LoginApi, GetUserDetailsApi ,RefreshAccessTokenApi

def initialize_urls(api):
    api.add_resource(BlogsApi, "/api/blogs")
    api.add_resource(BlogApi, "/api/blog/<id>")
    api.add_resource(GetUserDetailsApi, "/api/user")
    api.add_resource(SignUpApi, "/api/user/register")
    api.add_resource(LoginApi, "/api/user/login")
    api.add_resource(RefreshAccessTokenApi, "/api/user/refresh")