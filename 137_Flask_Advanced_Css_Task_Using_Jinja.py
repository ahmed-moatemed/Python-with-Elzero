# --------------------------------------
# -- Flask => Advanced Css Task Jinja --
# --------------------------------------


from flask import Flask, render_template


skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():

    return render_template("homepage.html", 
                           title="Home Page",
                           custom_css="home")


@skills_app.route("/about")
def aboutpage():

    return render_template("about.html", title="About Page")


@skills_app.route("/content")
def contentpage():

    return render_template("content.html", 
                           title="Content Page", 
                           custom_css="content")

@skills_app.route("/add")
def addpage():

    return render_template("add.html", 
                           title="Add Page", 
                           custom_css="add")

if __name__ == "__main__":

    skills_app.run(debug= True, port= 9000)