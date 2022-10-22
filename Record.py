from datetime import datetime, timedelta


def dt_parse(t):
    #Example value: 2019-08-25 22:02:44 +0100
    ret = datetime.strptime(t[0:19],'%Y-%m-%d %H:%M:%S')
    if t[20]=='+':
        ret-=timedelta(hours=int(t[21:23]),minutes=int(t[23:]))
    elif t[20]=='-':
        ret+=timedelta(hours=int(t[21:23]),minutes=int(t[23:]))
    return ret

def unix_time_millis(dt):
    epoch = datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds()) * 1000

class Record:
    'Common base class for all records'
    empCount = 0

    def __init__(self, recordType, startTime,endTime,value):
        self.recordType = recordType
        self.startTime = unix_time_millis(dt_parse(startTime))
        self.endTime = unix_time_millis(dt_parse(endTime))
        self.value = float(value)

    def display(self):
        print("recordType : ", self.recordType,  ", startTime: ", self.startTime, ", endTime: ", self.endTime, ", value: ", self.value)
