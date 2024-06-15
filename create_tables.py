from heroquest import db, create_app
from heroquest.models import *

app = create_app()
with app.app_context():
    db.create_all()
