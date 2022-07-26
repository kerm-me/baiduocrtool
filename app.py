import fitz
from aip import AipOcr
import os
import yaml
import json
import sys


def generate_pic(name):
    try:
        os.makedirs('{}/imgs'.format(name))
    except:pass
    doc = fitz.open('{}.pdf'.format(name))
    zoom_x = 2.5 # horizontal zoom
    zomm_y = 2.5 # vertical zoom
    mat = fitz.Matrix(zoom_x, zomm_y) # zoom factor 2 in each dimension
    # pix = page.get_pixmap()
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        pix.save('{}/imgs/page{}.png'.format(name,page.number))
    return len(doc)

def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

def formula_api(name,total):
    with open('config.yaml','r',encoding='UTF-8') as f:
        s = yaml.load(f.read(), Loader=yaml.SafeLoader)
    client = AipOcr(s['APP_ID'], s['API_KEY'], s['SECRET_KEY'])
    txt = ''
    try:
        os.makedirs('{}/results'.format(name))
    except:pass
    for i in range(total):
        image = get_file_content('{}/imgs/page{}.png'.format(name,i))
        options = {}
        options["recognize_granularity"] = "small"
        res_image = client.formula(image, options)
        print('识别第{}/{}页'.format(i+1,total+1))
        with open('{}/results/{}.json'.format(name,i+1),'w',encoding='UTF-8') as f:
            f.write(json.dumps(res_image))
        for j in res_image['words_result']:
            txt = txt  + j['words'] + '\n'
    with open('{}/results.txt'.format(name),'w',encoding='UTF-8') as f:
        f.write(txt)

def handle(name):
    try:
        total = generate_pic(name)
        formula_api(name,total)
    except Exception as e:
        print(e,'处理失败，请确认API额度充足，运转正常，如无法解决请复制本行，到 Github 提交 Issue')

handle(sys.argv[1])
# handle(
#     'n 维球体积计算'
# )




