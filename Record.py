from datetime import datetime,timedelta

def dt_parse(t):
    ret = datetime.strptime(t[0:19],'%Y-%m-%d %H:%M:%S')
    if t[21]=='+':
        ret-=timedelta(hours=int(t[19:22]),minutes=int(t[23:]))
    elif t[21]=='-':
        ret+=timedelta(hours=int(t[19:22]),minutes=int(t[23:]))
    return ret

class Record:
   'Common base class for all records'
   empCount = 0

   def __init__(self, recordType, startTime,endTime,value):
	  self.recordType = recordType
	  self.startTime = int(dt_parse(startTime).strftime("%s"))*1000
	  self.endTime = int(dt_parse(endTime).strftime("%s"))*1000
	  self.value = float(value)
   
   def displayCount(self):
	 print "Total Employee %d" % Employee.empCount

   def display(self):
	  print "recordType : ", self.recordType,  ", startTime: ", self.startTime, ", endTime: ", self.endTime, ", value: ", self.value
