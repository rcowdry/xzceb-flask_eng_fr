# ```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
# ```

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench():
    #write the code here
    translation = language_translator.translate(
        text='Hello, how are you today?',
        model_id='en-es').get_result()
    print(translation)
    # print(translation)
    # return frenchText

# def frenchToEnglish(frenchText):
#     #write the code here
#     return englishText

englishToFrench()