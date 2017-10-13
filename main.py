import GoogleFitness
import AppleHealthXmlParser
import sys

weightRecords = []
stepRecords = []
distanceRecords = []

records = AppleHealthXmlParser.parse(sys.argv[1]);

for record in records:
	if record.recordType == "HKQuantityTypeIdentifierBodyMass":
		weightRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierStepCount":
		stepRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierDistanceWalkingRunning":
		distanceRecords.append(record)

weightDataSource = GoogleFitness.createWeightDataSource()
stepDataSource = GoogleFitness.createStepDataSource()
distanceDataSource = GoogleFitness.createDistanceDataSource()

if weightDataSource and len(weightRecords) > 0 :
	GoogleFitness.sendPoints(weightDataSource, weightRecords)

if stepDataSource and len(stepRecords) > 0 :
	GoogleFitness.sendPoints(stepDataSource, stepRecords)

if distanceDataSource and len(distanceRecords) > 0 :
	GoogleFitness.sendPoints(distanceDataSource, distanceRecords)







