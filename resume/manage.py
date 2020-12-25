"""Launches and renders routes for paced's resume page."""

import os

import yaml
from flask import redirect, render_template, send_from_directory
from utils import launchServer

# Necessary settings
DEBUG = False
CSSFILES = [
    "css/kube.css",
    "css/font-awesome.css",
    "css/custom.css",
]

JSFILES = [
    "js/jquery.js",
    "js/kube.js",
    "js/jquery.teletype.js",
    "js/readmore.min.js",
    "js/user.js",
]

app = launchServer(DEBUG, CSSFILES, JSFILES)

# Configured content objects:

identityStream = file(os.path.join(app.root_path,
                                   'content/identity.yaml'), 'r')
identity = yaml.load(identityStream)

educationStream = file(os.path.join(app.root_path,
                                    'content/education.yaml'), 'r')
education = yaml.load(educationStream)

experienceStream = file(os.path.join(app.root_path,
                                     'content/experience.yaml'), 'r')
experience = yaml.load(experienceStream)

projectsStream = file(os.path.join(app.root_path,
                                   'content/projects.yaml'), 'r')
projects = yaml.load(projectsStream)


@app.context_processor
def inject_debug():
    """Inject debug state into every template."""
    return dict(debug=app.debug)


@app.errorhandler(404)
def notFound(e):
    """View for 404 page."""
    return render_template('404.html.jinja', identity=identity,
                           ext="NotFound"), 404


@app.route('/', methods=['GET'])
def mainSite():
    """Home page with logo and basic navigation, links, etc."""
    return render_template('index.html.jinja', identity=identity,
                           active="home", ext="")


@app.route('/resume/', methods=['GET'])
def resume():
    """Resume with experience and education."""
    return render_template('resume.html.jinja', identity=identity,
                           active="resume", ext="Resume", exp=experience,
                           edu=education)


@app.route('/cv/', methods=['GET'])
def cvRedirect():
    """Redirect common misspelling to correct page."""
    return redirect("/resume", code=302)


@app.route('/portfolio/', methods=['GET'])
def portfolio():
    """Portfolio items in full view."""
    return render_template('portfolio.html.jinja', identity=identity,
                           active="portfolio", ext="Portfolio",
                           p=projects)


@app.route('/projects/', methods=['GET'])
def projectsRedirect():
    """Redirect common misspelling to correct page."""
    return redirect("/portfolio", code=302)


@app.route('/work/', methods=['GET'])
def workRedirect():
    """Redirect common misspelling to correct page."""
    return redirect("/portfolio", code=302)


@app.route('/works/', methods=['GET'])
def worksRedirect():
    """Redirect common misspelling to correct page."""
    return redirect("/portfolio", code=302)


@app.route('/contact/', methods=['GET'])
def contact():
    """Contact forms."""
    return render_template('contact.html.jinja', identity=identity,
                           active="contact", ext="Contact")


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Contact forms."""
    return send_from_directory('static/', 'sitemap.xml')


@app.route('/thanks/', methods=['GET'])
def thanks():
    """Quick redirect on finishing a contact form."""
    return render_template('thanks.html.jinja', identity=identity,
                           active="contact", ext="SaysThanks")


@app.route('/secret/', methods=['GET'])
def secret():
    """Sneaky secret page."""
    return render_template('secret.html.jinja', identity=identity,
                           active="", ext="IsMildlyChuffed"), 403


@app.route('/favicon.ico')
def favicon():
    """Favicon for IE-based browsers."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicons/favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots():
    """Robot file for SEO."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt')


@app.route('/humans.txt')
def humans():
    """Human file for SEO."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'humans.txt')


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')
