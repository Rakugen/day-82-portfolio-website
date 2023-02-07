# A personal portfolio website to display projects I have worked on

# ToDo #1: Describe website layout + components
# Main page will consist of a rotating carousel of projects w/ an image and description and clicking will link to
# a seperate project page. There will be a navbar on top w/ links to contacts, a page to display all projects.
# Below the carousel will be more info about me/my work/skills as well as contacts w/appropriate links.
# The idea is to have each of my projects saved into a database and have the website dynamically add them to the website
# Homepage's carousel will pull from db of projects only showing some info like image, project name, short description
# Portfolio page will auto-fill with cards of each project w/ some info.
# Specific projects' page will be templated and filled from database with full info.

# Header: contains navbar, Navbar: Home, Portfolio, About, Contact
# Footer: Contacts, Copyrights
# HomePage: carousel w/projects, blurb about me/technologies I've studied
# Portfolio Page: Multi-cards w/ image of each project. on-hover: description. click: goes to specific projects page
# Individual Project Page: Templated design, Description, Technologies, Images/Video
# About Page: More info about me, what I have learned and aim to learn, link to contacts page
# Contact Page: Form to submit a generated email, List of contacts, socials.


# ToDo #2: Create starting points for those components

# ToDo #3: Fill out each component

# ToDo #4: Test each component

# ToDo #5: Write a short blurb about how this website was conceived, created and coded, as well as what
#  technologies was used



from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

# DB Table Creation
# Project table that will hold individual projects with name, short description and thumbnail img for preview,
# comma-separated tags, comma-separated imgs_url, and html formated body
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    thumbnail_url = db.Column(db.String(250), unique=False)
    tags = db.Column(db.String(250), unique=False, nullable=True)
    imgs_url = db.Column(db.String(250), unique=False)
    body = db.Column(db.Text, unique=False)


with app.app_context():
    db.create_all()



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/project/<int:project_id>')
def get_project():
    return render_template("project.html")



if __name__ == "__main__":
    app.run(debug=True)

