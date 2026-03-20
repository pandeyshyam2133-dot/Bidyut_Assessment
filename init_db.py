from app import app, db, User, Task
from werkzeug.security import generate_password_hash
import os

# Delete the old database file so we can start fresh
if os.path.exists("instance/app.db"):
    os.remove("instance/app.db")

with app.app_context():
    db.create_all()

    # Create an Admin
    admin = User(username='admin', password=generate_password_hash('admin123'), role='admin')
    
    # Create multiple standard Users
    user1 = User(username='user1', password=generate_password_hash('user123'), role='user')
    user2 = User(username='johndoe', password=generate_password_hash('password'), role='user')
    user3 = User(username='janedoe', password=generate_password_hash('password'), role='user')
    
    db.session.add_all([admin, user1, user2, user3])

    # Create lots of dummy tasks
    tasks = [
        Task(title='Fix the server bug reported by QA'),
        Task(title='Update CSS styling on the login page'),
        Task(title='Write assessment documentation'),
        Task(title='Attend team meeting at 2 PM'),
        Task(title='Review pull requests from junior devs')
    ]
    db.session.add_all(tasks)

    db.session.commit()
    print("Database initialized successfully with 4 users and 5 tasks!")