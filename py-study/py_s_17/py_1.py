from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

#打开一个图片
im=Image.open('py-study/py_s_17/as.jpg')
#获得图片的宽和高
w,h=im.size
print(f'宽：{w}高：{h}')
#缩小一半
im.thumbnail((w//2,h//2))
print(f'宽：{w//2}高：{h//2}')
#保存
print(f'宽：{w}高：{h}')
im.save('py-study/py_s_17/as-xiao.jpg','jpeg')

w2,h2=im.size
print(f'宽：{w2}高：{h2}')
im.thumbnail((2*w2,2*h2))
im.save('py-study/py_s_17/as-huanyuan.jpg','jpeg')
ass=im.crop((0,0,200,200))
ass.save('py-study/py_s_17/caijian.jpg','jpeg')
asss2=ass.transpose(Image.ROTATE_180)
asss2.save('py-study/py_s_17/duanzhuan.jpg','jpeg')
# im.paste(asss2,(0,0,200,200))
# im.show()

ass2=ass.filter(ImageFilter.BLUR)
ass2.save('py-study/py_s_17/filterBlur.jpg','jpeg')
#paste，将一个图片插入另一个图片
im.paste(ass2,(0,0,200,200))
im.show()

ass3=ass.filter(ImageFilter.BoxBlur(100))
ass3.save('py-study/py_s_17/filterBoxBlur.jpg','jpeg')
ass4=ass.filter(ImageFilter.SMOOTH)
ass4.save('py-study/py_s_17/filterSmooth.jpg','jpeg')

#放大 不行
# im.thumbnail((380,500))
# #im.thumbnail((2*w,2*h))
# print(f'w:{2*w}h:{2*h}')
# im.save('py-study/py_s_17/as-da.jpg','jpeg')

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
image.save('py-study/py_s_17/kongbai.jpg','jpeg')
# # 创建Font对象:
# font = ImageFont.truetype('arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')