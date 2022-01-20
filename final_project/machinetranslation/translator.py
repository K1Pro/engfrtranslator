"""Tranlator Python File"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Text translated to French from English"""
    if english_text is None:
        return None
    else:
        trans_res = language_translator.translate(\
            text=english_text, model_id='en-fr')
        translation = trans_res.get_result()
        french_text = translation['translations'][0]['translation']
        return french_text

def french_to_english(french_text):
    """Text translated to English From French"""
    if french_text is None:
        return None
    else:
        trans_res = language_translator.translate(\
            text=french_text, model_id='fr-en')
        translation = trans_res.get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    
