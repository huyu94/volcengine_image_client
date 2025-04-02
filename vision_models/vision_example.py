import os
from volcenginesdkarkruntime import Ark
from utils import encode_image

model = 'doubao-1.5-vision-pro-32k-250115'
client = Ark(api_key=os.getenv("ARK_API_KEY"))

def send_picture_by_url(model_id: str, image_url: str):
    # 创建一个对话请求
    response = client.chat.completions.create(
        # 指定您部署了视觉理解大模型的推理接入点ID
        model = model,
        messages = [
            {
                # 指定消息的角色为用户
                "role": "user",  
                "content": [  
                    # 文本消息，希望模型根据图片信息回答的问题
                    {"type": "text", "text": "支持输入是图片的模型系列是哪个？"},  
                    {"type": "image_url", "image_url": {"url":  "https://ark-project.tos-cn-beijing.volces.com/doc_image/ark_demo_img_1.png"}
                    # 图片信息，希望模型理解的图片
                    # {"type": "image_url", "image_url": {"url":  image_url}
                    },
                ],
            }
        ],
    )
    print(response.choices[0].message.content)





def send_picture_by_base64(model_id: str, image_path: str):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
    # 替换 <Model> 为模型的Model ID
    model=model_id,
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "图片里讲了什么?",
            },
            {
            "type": "image_url",
            "image_url": {
            # 需要注意：传入Base64编码前需要增加前缀 data:image/{图片格式};base64,{Base64编码}：
            # PNG图片："url":  f"data:image/png;base64,{base64_image}"
            # JEPG图片："url":  f"data:image/jpeg;base64,{base64_image}"
            # WEBP图片："url":  f"data:image/webp;base64,{base64_image}"
                "url":  f"data:image/<IMAGE_FORMAT>;base64,{base64_image}",
                'detail': "high"
            },
            },
        ],
        }
    ],
    )
    print(response.choices[0])



