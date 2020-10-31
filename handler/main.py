from tornado.web import RequestHandler
import utils.pichandler

# 各个页面路由

class IndexHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self):
        pic_list = utils.pichandler.get_pic()
        self.render('index.html', pic_list = pic_list)


class ExploreHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self):
        thumb_list = utils.pichandler.get_thumb_pic()
        self.render('explore.html', thumbs = thumb_list)


class PostHandler(RequestHandler):
    """
    指定请求的资源
    """
    def get(self, post_id):
        self.render('post.html', post_id=post_id)


class UploadHandler(RequestHandler):
    """
    图片上传 
    """
    def get(self):
        self.render('upload.html')

    def post(self):
        # 获取前端传过来的name属性Pic，返回一个list
        pic_list = self.request.files.get('pic', [])
        utils.pichandler.save_pic(pic_list)
        self.write('上传成功')