
import os
from utils.image_process import image_to_base64_code
from volcengine.visual.VisualService import VisualService
import json
from pprint import pprint as pp


def main():
    visual_service = VisualService()

    
    base64_image = image_to_base64_code('/home/lixiang/图片/me.jpg')

    # 请求Body
    form = {
        "req_key": "img2img_disney_3d_style_usage",
        "binary_data_base64": [base64_image],
        # "image_urls":[
        #     "https://ibb.co/GfnqwQzm"
        # ],
        "return_url": True,
    }

    # 调用接口并处理异常
    try:
        resp = visual_service.cv_process(form)
        pp(f"Raw response: {resp}")
    except json.JSONDecodeError as e:
        pp(f"JSON decode error: {e}")
    except Exception as e:
        pp(f"Error occurred: {e}")


if __name__ == '__main__':
    main()