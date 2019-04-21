from projectname import app, db
from projectname import SampleModel

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/config/init/')
def init_database():
    print("Creating tables")
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 'Init complete'
