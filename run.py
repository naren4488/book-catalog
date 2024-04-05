from app import create_app, db  # app/__init__ (ROOT PACKAGE)
from app.auth.models import User


# if __name__ == '__main__':
#     app = create_app('dev')
#     with app.app_context():
#         db.create_all()
#         if not User.query.filter_by(user_name='harry').first():
#             User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
#     app.run(port=8000)


app = create_app('prod')
with app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    except Exception as e:
        print(e)
