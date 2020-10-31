import glob
from PIL import Image

# 保存图片
def save_pic(pic_list):
    for pic in pic_list:
        # 图片名
        filename = pic['filename']
        # 图片二进制数据
        content = pic['body']

        # 保存路径
        path = './static/images/upload/{}'.format(filename)

        with open(path, 'wb') as f:
            f.write(content)
        # 缩略图
        get_thumb(path, filename)

# 获取图片
def get_pic():
    pic_list = glob.glob('static/images/upload/*')
    return pic_list

# 保存缩略图
def get_thumb(path, filename):
    im = Image.open(path)
    im.thumbnail((200, 200))
    thumb_path = './static/images/thumb/{}'.format(filename)
    im.save(thumb_path)

# 获取缩略图
def get_thumb_pic():
    pic_list = glob.glob('static/images/thumb/*')
    return pic_list

