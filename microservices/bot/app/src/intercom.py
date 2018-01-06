import requests
import json
import os

accessToken = os.environ['ACCESS_TOKEN']
adminId = os.environ['ADMIN_ID']


def buildNote(message, lang, translation):
    response = "Original Message: "+message+ "\nLanguage Code: "+lang+"\nTranslation: " + translation + "\n\n To reply in the same language, please add a note of the format '/translate language_code sentence'\nExample: /translate fr How can I help you?"
    return response


def sendNote(convId, message):
    url = "https://api.intercom.io/conversations/" + convId + "/reply"
    bearer = "Bearer " + accessToken
    headers = {
        "Authorization": bearer,
        "Content-type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "body": message ,
        "type": "admin",
        "admin_id": adminId,
        "message_type": "note"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    respObj = r.json()
    print ("Send Note Responce: ")
    print (respObj)
    print ("==========================================================================")

def sendMessage(convId, message):
    url = "https://api.intercom.io/conversations/" + convId + "/reply"
    bearer = "Bearer " + accessToken
    headers = {
        "Authorization": bearer,
        "Content-type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "body": message ,
        "type": "admin",
        "admin_id": adminId,
        "message_type": "open"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    respObj = r.json()
    print ("Send Message Responce: ")
    print (respObj)
    print ("==========================================================================")
