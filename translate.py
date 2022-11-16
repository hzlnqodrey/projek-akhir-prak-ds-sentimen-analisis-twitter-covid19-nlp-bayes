import os

from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"serviceKey.json"

translate_client = translate_v2.Client()

text = "Saya siapa dan kamu dimana dia rifki kamu qodri"


output = translate_client.translate(text, target_language="en")

print(output)
print(output['translatedText'])