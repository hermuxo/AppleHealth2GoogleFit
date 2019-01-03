import requests
import json
from random import randint
import config



def getDataSources():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % ACCESS_TOKEN }
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return True
    else:
        print r.status_code
        print r.content
        return False


def createStepDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleStepDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "steps",
                    "format": "integer"
                }
            ],
            "name": "com.google.step_count.delta"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print r.status_code
        print r.content
        return False


def createWeightDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleWeightDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "weight",
                    "format": "floatPoint"
                }
            ],
            "name": "com.google.weight"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print r.status_code
        print r.content
        return False


def createDistanceDataSource():
    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataStreamName": "AppleDistanceDataSource",
        "type": "derived",
        "application": {
            "name": "AppleHealth2GoogleFit",
            "version": "1"
        },
        "dataType": {
            "field": [
                {
                    "name": "distance",
                    "format": "floatPoint"
                }
            ],
            "name": "com.google.distance.delta"
        },
        "device": {
            "manufacturer": "Apple",
            "model": "RESTAPI",
            "type": "tablet",
            "uid": str(randint(0, 1000)),
            "version": "1"
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        response = json.loads(r.content)
        dataSourceId =response['dataStreamId']
        return dataSourceId
    else:
        print r.status_code
        print r.content
        return False

def sendPoints(dataSourceId,records):
    dataPoints = []


    if records[0].recordType == "HKQuantityTypeIdentifierBodyMass":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.weight",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": endTimeNanos,
                "value": [
                    {
                        "fpVal": record.value
                    }
                ]
            }
            dataPoints.append(point);

    if records[0].recordType == "HKQuantityTypeIdentifierStepCount":

        for record in records:            
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.step_count.delta",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "intVal": record.value
                    }
                ]
            }
            dataPoints.append(point);

    if records[0].recordType == "HKQuantityTypeIdentifierDistanceWalkingRunning":

        for record in records:
            endTimeNanos = record.endTime*1000000
            if endTimeNanos > 1546513741000000000:
                endTimeNanos = 1546513741000000000
            point = {
                "dataTypeName": "com.google.distance.delta",
                "startTimeNanos": record.startTime*1000000,
                "endTimeNanos": record.endTime*1000000,
                "value": [
                    {
                        "fpVal": record.value*1000
                    }
                ]
            }
            dataPoints.append(point);

    minStartTime = records[0].startTime
    maxEndTime = records[len(records)-1].endTime

    for points in chunks(dataPoints, 10000):
        addData(dataSourceId,points,minStartTime,maxEndTime)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def addData(dataSourceId,dataPoints,minStartTime ,maxEndTime):

    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/" + dataSourceId + "/datasets/" +str(minStartTime*1000000) + "-"+ str(maxEndTime*1000000)

    headers = { 'content-type': 'application/json',
                'Authorization': 'Bearer %s' % config.accessToken }
    data = {
        "dataSourceId": dataSourceId,
        "minStartTimeNs": minStartTime*1000000,
        "maxEndTimeNs": maxEndTime*1000000,
        "point": dataPoints
    }

    r = requests.patch(url, headers=headers, data=json.dumps(data))

    if r.status_code == 200:
        print str(len(dataPoints))  + " dataPoints : " + dataSourceId

        return True
    else:
        print r.status_code
        print r.content
        return False





