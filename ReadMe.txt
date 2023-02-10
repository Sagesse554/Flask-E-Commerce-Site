App Structure

    app.py
        App Execution Entry Point.

    EComSite.db
        App SQLite Database.

    app/__init__.py
        App Initialization.

    app/models.py
        User Data Model.

    app/config.py
        App Configuration.

    app/static/style.css
        Registration and Login pages Style.

    app/static/img/EComSite7.jpg
        Homepage Image.

    app/static/img/EComSite8.jpg
    app/static/img/EComSite11.jpg
    app/static/img/EComSite12.jpg
        User session Images.

    app/routes/authentication.py
        Registration and Login pages Route Functions.

    app/routes/main.py
        Homepage Route Functions.

    app/templates/base1.html
        Homepage and User Session HTML Base Template.

    app/templates/base2.html
        Registration and Login HTML Base Template.

    app/templates/authentication/register.html
        Registration page HTML Template.

    app/templates/authentication/login.html
        Login HTML Template.

    app/templates/main/index.html
        Homepage HTML Template.

    app/templates/main/profile.html
        User Session HTML Template.




App Features

    Independent functional application
        It is possible to try the application in any environment.
        Running the following command in the prompt satisfies the requirements.
        pip install Flask==1.1.4 SQLAlchemy==1.4.39 Flask-Login==0.6.2 Werkzeug==1.0.1
        Finally, run the app.py file and open the web page http://127.0.0.1:5000/

    Registration on the site with personal data

    Registration parameters verification with alert messages
        Email (Unique with at least 10 characters containing an "@").
        Username (Not less than 4 characters).
        Password (Not less than 8 characters).
        Password Confirmation (According to Password).

    Login to main page with registration data

    Connection parameters verification with alert messages
        Username (Not empty).
        Password (According to registration).

    Login to own Profile with personalized message

    Log Out and Homepage return




App Specificities

    Uses an SQLite3 database (integrated in Python) which is created at startup.
    Duplicated Users class model for its import in the authentication file and for the table creation function.