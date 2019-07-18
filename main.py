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
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_enviorment.get_template('/templates/new_post.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
    def post(self):
        post_title = self.request.get('postTitle')
        post_content = self.request.get('postContent')
        Name = self.request.get('aurthorName')

        template_vars = {
        'post title':
        'post content':
        'Name': 
        }


app = webapp2.WSGIApplication([
    ('/', Home),
    ('/blogmake', BlogHandler),
], debug=True)
