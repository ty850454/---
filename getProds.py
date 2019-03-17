import os
import json

imgPath = "C:\\Users\\ty850\\Desktop\\新建文件夹 (2)\\品牌图片"
infoPath = "C:\\Users\\ty850\\Desktop\\新建文件夹 (2)\\品牌介绍"
typePath = "C:\\Users\\ty850\\Desktop\\新建文件夹 (2)\\品牌型号"

imgs = os.listdir(imgPath)
infos = os.listdir(infoPath)


class ProdInfo:
  name = ""
  title = ""
  types = ""
  def __init__(self, name, title):
    self.name = name
    self.title = title
  def __str__(self):
    return 'prod (%s, %s)' % (self.name, self.title)

def ProdInfo2Json(obj):
  print(obj)
  return {
    "name": obj.name,
    "title": obj.title
  }


result = []
for img in imgs:
  if img.endswith(".png"):
    img = img[0 : -4]
    for info in infos:
      if img in info:
        result.append(ProdInfo(img, info[0 : -5]))

print(json.dumps(result, default=ProdInfo2Json, ensure_ascii=False, indent=2))