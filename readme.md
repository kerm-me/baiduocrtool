## 简介

用于调用 百度 OCR API 做 PDF 公式混合识别。

## 使用

`pip3 install -r requirements.txt`

首先需要申请百度 API。

将 APP_ID  API_KEY  SECRET_KEY 填入`config.yaml`中，注意冒号后空格。

运行 `python app.py 文件名不带后缀带冒号` 即可。

例如 `python app.py '往年题'`