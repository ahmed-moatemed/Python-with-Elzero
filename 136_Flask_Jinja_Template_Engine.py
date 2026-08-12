# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------


from flask import Flask, render_template


skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():

    return render_template("homepage.html", title="Home Page")


@skills_app.route("/about")
def aboutpage():

    return render_template("about.html", title="About Page")


if __name__ == "__main__":

    skills_app.run(debug= True, port= 9000)