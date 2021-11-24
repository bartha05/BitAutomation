from seleniumbase import BaseCase
from datetime import datetime
from datetime import timedelta
import requests
import json

API = 'http://10.11.132.5:7002/api/'
FIXSPOT = 'v1.2/fixspot/'
CONFIGURATION = 'v1.0/configuration/'
EVENT = 'v1.0/event/'
REMOTESERVICE = 'v1.0/remoteservice/'
headers = {'Accept':'*/*', 'Content-Type': 'application/json'}

class TrafficSpotService(BaseCase):
    response = None
    def validate_response_code(self, exected_code):
        code = self.response.status_code
        print("\n\nStatus code of response is",code,"\n")
        if (code != exected_code):
            text = self.response.text
            print(text)
        self.assert_equal(code,exected_code)

    #-----------------------------------------------------------------------------------------------------

    def test_3101_fixspot_GET_getstatistics(self):
        URL = API+FIXSPOT+'getstatistics'
        fromDate = (datetime.now()-timedelta(minutes=75)).isoformat()
        toDate = (datetime.now()-timedelta(minutes=60)).isoformat()
        data = '{"fromDate": "'+fromDate[0:-3]+'Z","toDate": "'+toDate[0:-3]+'Z"}'
        self.response = requests.get(URL, headers=headers, data = data)
        self.validate_response_code(200)
        json = self.response.json()
        n = len(json)
        print("\nNumber of the events in the last 15 minutes is",n,"\n")
        for i in json:
            print(i)
            self.assert_true("eventCreatedAt" in i)
            self.assert_true("eventProcessedAt" in i)

    #-----------------------------------------------------------------------------------------------------

    def test_1101_conf_GET_Configuration(self):
        URL = API+CONFIGURATION
        self.response = requests.get(URL, headers=headers)
        self.validate_response_code(200)
        json = self.response.json()
        for i in json:  
            print("\n ∙ ",i,"=",json[i])

    def test_1102_conf_POST_Configuration(self):
        URL = API+CONFIGURATION
        with open('seleniumbase\data\conf.json') as json_file:
            conf = json.load(json_file)
        print("\n",conf)
        data = '{"version": "4.0","json": "'+json.dumps(conf).replace("\"","'")+'"}'
        self.response = requests.post(URL, headers=headers, data=data)
        self.validate_response_code(201)
        json2 = self.response.json()
        for i in json2:
            print("\n ∙ ",i,"=",json2[i])

    def test_1103_conf_PUT_Configuration(self):
        URL = API+CONFIGURATION
        with open('seleniumbase\data\conf.json') as json_file:
            conf = json.load(json_file)
        print("\n",conf)
        data = '{"version": "1.0","json": "'+json.dumps(conf).replace("\"","'")+'"}'
        self.response = requests.put(URL, headers=headers, data=data)
        self.validate_response_code(201)
        json2 = self.response.json()
        for i in json2:
            print("\n ∙ ",i,"=",json2[i])

    def test_1104_conf_GET_ConfigVersion(self):
        URL = API+CONFIGURATION+'1.0'
        self.response = requests.get(URL, headers=headers)
        print("\n",self.response.url)
        self.validate_response_code(200)
        json = self.response.json()
        for i in json:
            print("\n ∙ ",i,"=",json[i])

    #-----------------------------------------------------------------------------------------------------

    def test_1201_event_GET_SystemNode(self):
        URL = API+EVENT+'systemnode'
        self.response = requests.get(URL, headers=headers)
        self.validate_response_code(200)
        text = self.response.text
        print("\nType of the current node is",text)
        self.assert_equal(text.strip('"'),"TrafficSpot")

    def test_1202_event_GET_GetAllUnPosted(self):
        URL = API+EVENT+'getallunposted'
        self.response = requests.get(URL, headers=headers)
        self.validate_response_code(200)
        json = self.response.json()
        n = len(json)
        print("\nNumber of all events that were not yet uploaded is",n)
        print("\nThe details of the first event:")
        for i in json[0]:
            print("\n ∙ ",i,"=",json[0][i])
        TrafficEventFields = ['$type','Direction','Speed','SpeedQuality','AxelsNumber','AxelQuality','Length','Category','CategoryQuality','PlateRear','PlateRearConfidence','NationalityRear','Lane','WimMeasurement','LaserMeasurement','Markers','Id','SourceDeviceId','EventId','Type','CreatedAt','ProcessedAt','ProcessingTime','PlateFront','PlateFrontConfidence','NationalityFront','Location','SynchronizationInfo','Images']
        for i in TrafficEventFields:
            self.assert_true(i in json[0])
        print("\nIDs of first 10 unposted events:\n")
        for i in range(10):
            print(json[i]["Id"])

    def test_1203_event_GET_ByMessageId(self):
        URL = API+EVENT+'bymessageid'
        params = {'messageId': '0000348b-498c-4e23-ab8c-ac4653b0e7db'}
        self.response = requests.get(URL, headers=headers, params=params)
        self.validate_response_code(200)

    def test_1204_event_PUT_MarkSent(self):
        URL = API+EVENT+'marksent'
        date = (datetime.now()-timedelta(minutes=60)).isoformat()
        data = '{"eventId": "00012109222132052230", "sentAt": "'+date[0:-3]+'Z", "acknowledgedAt": "'+date[0:-3]+'Z"}'
        self.response = requests.put(URL, headers=headers, data = data)
        self.validate_response_code(202)

    def test_1205_event_PUT_MarkImageAsSent(self):
        URL = API+EVENT+'markimageassent'
        date = (datetime.now()-timedelta(minutes=60)).isoformat()
        data = '{"eventId": "00012109222132052230", "sentAt": "'+date[0:-3]+'Z", "acknowledgedAt": "'+date[0:-3]+'Z"}'
        self.response = requests.put(URL, headers=headers, data = data)
        self.validate_response_code(202)

    #-----------------------------------------------------------------------------------------------------

    def test_1301_rese_GET_RemoteService(self):
        URL = API+REMOTESERVICE
        self.response = requests.get(URL, headers=headers)
        self.validate_response_code(200)
        json = self.response.json()
        for i in json:  
            print("\n ∙ ",i,"=",json[i])

    #-----------------------------------------------------------------------------------------------------


