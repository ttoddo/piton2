

import requests
import time



import requests
import time

api_url = "https://api.telegram.org/bot"
token = '7192786510:AAFsxcMLd6rDW1SFqoCw8HMhgaRs4GuFntQ'
offset = -1
while True:
    updates = requests.get(f'{api_url}{token}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            if 'sticker' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне стикер')
            elif 'photo' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне фото')
            elif 'voice' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне голосовое')
            elif 'video' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне видео')
            elif 'audio' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне аудио')
            elif 'location' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне геопозицию')
            elif 'forward_origin' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты переслал мне сообщение')
            elif 'animation' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне гифку')
            elif 'poll' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне опрос')
            elif 'story' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне историю')
            elif 'contact' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне контакт')
            elif 'video_note' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне кружочек')
            elif 'text' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне просто текст')
            elif 'document' in result['message'].keys():
                requests.get(f'{api_url}{token}/sendMessage?chat_id={chat_id}&text=Ого ты отправил мне документ')
            time.sleep(1)