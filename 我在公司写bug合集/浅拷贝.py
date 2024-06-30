# scrapy爬数据的时候不知道为啥莫名其妙我把item定义写到了外层循环，结果就数据不一致了，应该定义在内层循环里的

import pprint
def incorrect_initialization():
    data_list = [
        {"类别": "水果", "种类": [{"名称": "苹果"}, {"名称": "香蕉"}]},
        {"类别": "蔬菜", "种类": [{"名称": "西红柿"}, {"名称": "黄瓜"}]}
    ]
    results = []
    for data in data_list:
        item = {}
        category = data["类别"]
        for kind in data["种类"]:
            name = kind["名称"]

            item["类别"] = category
            item["名称"] = name
            results.append(item)

    return results

pprint.pprint(incorrect_initialization())
