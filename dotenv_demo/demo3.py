import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),  # 非隐私，示例数据
    **dotenv_values(".env.secret"),  # 隐私密钥和配置参数
    # **os.environ,  # override loaded values with environment variables
}
print(config)