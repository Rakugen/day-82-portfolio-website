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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)




@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

