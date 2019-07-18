import webapp2
import jinja2
import os

the_jinja_enviorment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
     def get(self):
        template = the_jinja_enviorment.get_template('/templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)
