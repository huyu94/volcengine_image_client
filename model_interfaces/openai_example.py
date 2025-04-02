import os 

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model = 'doubao-1-5-lite-32k-250115',
    openai_api_key = os.getenv("ARK_API_KEY"),
    openai_api_base = 'https://ark.cn-beijing.volces.com/api/v3'
)

response = model.invoke("nihao")
print(response)
