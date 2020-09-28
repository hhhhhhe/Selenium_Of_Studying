#coding = utf-8
# 提前图片信息
import pytesseract
from PIL import Image
# 打开图片
image = Image.open("E:/imooc1.png")
# 将图片转换为文字
text = pytesseract.image_to_string(image)
print(text)
