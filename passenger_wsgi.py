from a2wsgi import ASGIMiddleware
from main import app

application = ASGIMiddleware(app)