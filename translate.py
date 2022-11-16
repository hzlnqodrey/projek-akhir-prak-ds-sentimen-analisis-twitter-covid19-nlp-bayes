import os

from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"serviceKey.json"

translate_client = translate_v2.Client()

text = "Saya siapa dan kamu dimana"

target = "en"

output = translate_client.translate(text, target_language=target)

print(output)
print(output['translatedText'])