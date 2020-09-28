#coding = utf-8
# 提前图片信息
import pytesseract
from PIL import Image
from showapiRequest import ShowapiRequest
# 打开图片
# image = Image.open("E:/imooc1.png")
# 将图片转换为文字
# text = pytesseract.image_to_string(image)
# print(text)
#r = ShowapiRequest("http://route.showapi.com/184-4","my_appId","my_appSecret")
r = ShowapiRequest("http://route.showapi.com/184-4",
                   "62626", "d61950be50dc4dbd9969f741b8e730f5")
# typeid，35是要识别几位数字的意思
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
# 定义文件上传设置：
r.addFilePara("image", r"E:/imooc1.png")
res = r.post()
#text = res.json()['showapi_res_body']['Result']
print(res.text)  # 返回信息
