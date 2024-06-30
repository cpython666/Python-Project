from faker import Faker
fake = Faker()
print('user-agent:',fake.user_agent())
print('name:',fake.name())
print('address:',fake.address())
print('text:',fake.text())
print('--------')

fake = Faker('zh_CN')
print('女生人名:',fake.name_female())
print('男生人名:',fake.name_male())
print('电话号码：',fake.phone_number())
print('文本：',fake.text())
for _ in range(5):
    print(fake.name())
    print(fake.address())
print('--------')
    
fake = Faker(['zh_CN', 'ja_JP', 'ko_KR'])

for _ in range(6):
    print(fake.name())