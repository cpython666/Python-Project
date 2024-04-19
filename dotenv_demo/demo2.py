from dotenv import load_dotenv
import os
# 加载 .env 文件中的环境变量
load_dotenv()
# 获取环境变量的值
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
print(database_url)
print(api_key)