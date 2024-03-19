import subprocess
import json



CHANNEL = 'kvartiri_tbilisi2023'

apartments_from_telegramm = {}

path = r'C:\Users\tr211\Python\python_advanced\test_and_more\rad\kvartiri_tbilisi2023.json'

def upload_posts(num_posts, channel):
    command = f'snscrape --max-result {num_posts} --jsonl telegram-channel {channel} > {channel}.json'
    subprocess.run(command, shell=True)

# def translate_to_russ(path_json_file):
    '''
    that funk return error?
    '''
#     with open(path_json_file, 'r') as f:
#             data = json.load(f)
#             for i in data:
#                 apartments_from_telegramm['ads'] = i['content']
#             return apartments_from_telegramm

def translate_to_russ(path_json_file):
    with open(path_json_file, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                apartments_from_telegramm['ads'] = data['content']
            except json.JSONDecodeError:
                #can put logging
                print(f"Skipping invalid JSON data: {line.strip()}")

if __name__=='__main__':
    upload_posts(20, CHANNEL)
    translate = translate_to_russ(path)
    print(translate)

# json_string = '{"_type": "snscrape.modules.telegram.TelegramPost", "url": "https://t.me/s/kvartiri_tbilisi2023/86190", "date": "2024-03-19T07:03:06+00:00", "content": "#Сдаётся #сдаю #сдам📌Район: #Сабуртало📐Общая площадь: 180 м².📋Количество комнат | Спальни: 5/3🏗️Этаж: 8/8🛑балкон/лодж: 1/1🏛️Состояние: новый ремонт💵Цена: 950 💵https://t.me/tornikegorange", "outlinks": ["https://t.me/s/kvartiri_tbilisi2023?q=%23Сдаётся", "https://t.me/s/kvartiri_tbilisi2023?q=%23сдаю", "https://t.me/s/kvartiri_tbilisi2023?q=%23сдам", "https://t.me/s/kvartiri_tbilisi2023?q=%23Сабуртало", "https://t.me/tornikegorange"], "linkPreview": null, "outlinksss": "https://t.me/s/kvartiri_tbilisi2023?q=%23Сдаётся https://t.me/s/kvartiri_tbilisi2023?q=%23сдаю https://t.me/s/kvartiri_tbilisi2023?q=%23сдам https://t.me/s/kvartiri_tbilisi2023?q=%23Сабуртало https://t.me/tornikegorange", "_snscrape": "0.7.0.20230622"}'
# data = json.loads(json_string)
# print(data['content'])

