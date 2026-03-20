# My RBAC Assessment Project 

Hey!   
This is my submission for the Role-Based Access Control (RBAC) task. I built a simple Task Manager using Python, Flask, and SQLite to show how role-based access works in a real web app.

---

##  What I implemented

- **User Roles:**  
  The app supports two roles — `admin` and `user`, which are stored in the database.

- **Access Control:**  
  - Normal users can only view and create tasks.  
  - Admin users can delete tasks and also remove other users.

- **Security (Middleware):**  
  I created a custom Python decorator called `@admin_required`.  
  It checks if the logged-in user is an admin before allowing delete actions.  
  If someone tries to access admin routes directly, they’ll get a **403 error**.

- **Dynamic UI:**  
  The frontend changes based on the user role using Jinja templates.  
  For example:
  - Normal users won’t even see delete buttons  
  - Admins get full control options  

---

##  How to run the project

1. Open terminal in the project folder
2. Initialize the database:
- python init_db.py
3. Run the application:

- python app.py

4. Open in browser:

- http://127.0.0.1:5000
  Test Accounts

You can use these pre-created accounts:

Admin (Full Access)
Username: admin
Password: admin123

User (Limited Access)
Username: user1
Password: user123

Thanks for checking out my project! 🙌

3. Install required libraries:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
