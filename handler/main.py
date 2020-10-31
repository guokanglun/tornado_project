from tornado.web import RequestHandler

# 各个页面路由

class IndexHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self):
        self.render('index.html')


class ExploreHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self):
        self.render('explore.html')


class PostHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self, post_id):
        self.render('post.html', post_id=post_id)