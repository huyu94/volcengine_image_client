
import os
from utils.image_process import image_to_base64_code
from volcengine.visual.VisualService import VisualService
import json
from pprint import pprint as pp


def main():
    visual_service = VisualService()

    # 从环境变量中读取 AK 和 SK
    visual_service.set_ak()
    visual_service.set_sk()
    
    base64_image = image_to_base64_code('/home/lixiang/图片/old_pic.jpeg')

    # 请求Body
    form = {
        "req_key": "lens_opr",
        "binary_data_base64": [base64_image],
        # "image_urls":[
        #     "https://ibb.co/GfnqwQzm"
        # ],
        "if_color": 1,
        "return_url": True,
    }

    # 调用接口并处理异常
    try:
        resp = visual_service.convert_photo_v2(form)
        pp(f"Raw response: {resp}")
    except json.JSONDecodeError as e:
        pp(f"JSON decode error: {e}")
    except Exception as e:
        pp(f"Error occurred: {e}")


if __name__ == '__main__':
    main()