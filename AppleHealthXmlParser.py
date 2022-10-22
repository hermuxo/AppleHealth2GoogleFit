import xml.sax
from Record import Record

supportedTypes = ["HKQuantityTypeIdentifierBodyMass", "HKQuantityTypeIdentifierStepCount",
                  "HKQuantityTypeIdentifierDistanceWalkingRunning"]

records = []


class AppleHealthExport(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        if name == "Record":
            for (k, v) in attrs.items():
                if k == 'type':
                    recordType = v
                if k == 'startDate':
                    startTime = v
                if k == 'endDate':
                    endTime = v
                if k == 'value':
                    value = v

            if recordType in supportedTypes:
                record = Record(recordType, startTime, endTime, value)
                records.append(record)


def parse(filename):
    print("Reading the XML file... This might take some time...")
    parser = xml.sax.make_parser()
    parser.setContentHandler(AppleHealthExport())
    parser.parse(open(filename, "r"))
    return records
