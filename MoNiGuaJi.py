# -*- coding: utf-8 -*- 
#KindJeff
#import urllib
import urllib2
import time

account = '1410300118'#input('input account:')
password = '888888'#input('input password:')
book = 'College_English_NEW_Century_SecEdition_Integration_3'
unit = 'Unit_06'
url = "http://10.215.27.244/Npels/CommonService.asmx"
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; MS Web Services Client Protocol 2.0.50727.8670)',
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': "",
    'Host': '10.215.27.244',
    'Content-Length': '',
    'Expect': '100-continue',
    'Connection': 'keep-alive'
}

def getHeader(add, text):
    headert = {}
    for key in header:
        if key == 'SOAPAction':
            elem = "http://www.sflep.com/npels/commonsvc/" + add
        elif key == 'Content-Length':
            elem = len(text)
        else:
            elem = header[key]
        headert[key] = elem
    return(headert)

def getResponse(add, text):
    request = urllib2.Request(url=url, headers=getHeader(add, text), data=text.encode())
    response = urllib2.urlopen(request)
    responseText = response.read().decode('utf-8').encode('gbk')
    return responseText


loginText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><Login xmlns="http://www.sflep.com/npels/commonsvc/"><Account>'+account+'</Account><Password>'+password+'</Password></Login></soap:Body></soap:Envelope>'
loginAdd= 'Login'
loginResponse = getResponse(loginAdd, loginText)
tokenPos = loginResponse.index('{')
token = loginResponse[tokenPos:tokenPos+38]


getClassListText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetClassList xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken></GetClassList></soap:Body></soap:Envelope>'
getClassListAdd = 'GetClassList'
ClassList = getResponse(getClassListAdd, getClassListText)
classListArr = ClassList.split('&lt;')
for i in classListArr[3:-1]:
    print i


getStudentInfoText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetStudentInfo xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken></GetStudentInfo></soap:Body></soap:Envelope>'
getStudentInfoAdd = 'GetStudentInfo'
StudentInfo = getResponse(getStudentInfoAdd, getStudentInfoText)
classPos = StudentInfo.index('CurrentClass')
classNo = StudentInfo[classPos+13:-91]
print "\nCurrent classNo:", classNo
newClassNo = raw_input("\ninput classNo to change your class(or just enter):")
if newClassNo != "" and len(newClassNo) == 14:
    newClassNo = newClassNo.strip()
    switchCorseText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><SwitchCourse xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken><NewClassNo>'+newClassNo+'</NewClassNo></SwitchCourse></soap:Body></soap:Envelope>'
    switchCourseAdd = 'SwitchCourse'
    getResponse(switchCourseAdd, switchCorseText)
    classNo = newClassNo
    print "\nCurrent classNo:", classNo


anHourAgo = time.strftime('%y.%m.%d %H:%M:%S',time.localtime(time.time()-3600))
updateLearnInfoText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><UpdateLearnInfo xmlns="http://www.sflep.com/npels/commonsvc/"><LearnInfoString>&lt;learninfo classNo="'+classNo+'" material="'+book+'" unit="'+unit+'" account="'+account+'" costTime="402" starttime="'+anHourAgo+'"&gt;{"AnswerSheetType":"LearnInfo","TeacherSheet":{"Test":[{"ID":1,"Answer":"","Type":"Input","Reference":"","Identifier":""}]},"StudentSheet":{"Test":[{"ID":1,"Answer":"","Type":"Input","Reference":"","Identifier":""}]},"ScoJSONStr":"{\"cmi\":{\"comments_from_learner\":[],\"completion_status\":\"not_attempted\",\"interactions\":[],\"launch_data\":\"\",\"progress_measure\":\"0\",\"score\":{\"scaled\":\"\",\"raw\":\"\"},\"session_time\":\"0\",\"success_status\":\"unknown\",\"total_time\":\"0\",\"mode\":\"normal\"},\"adl\":{\"data\":[{\"id\":\"newWordTestProgress\",\"store\":\"\"},{\"id\":\"wordATestProgress\",\"store\":\"\"},{\"id\":\"wordBTestProgress\",\"store\":\"\"}]},\"cci\":{\"service\":{\"dictionary\":{\"headword\":\"\",\"short_cuts\":\"\"},\"new_words\":[],\"cur_wordmill\":[]}}}"}&lt;/learninfo&gt;</LearnInfoString><SessionToken>'+token+'</SessionToken></UpdateLearnInfo></soap:Body></soap:Envelope>'
updateLearnInfoAdd = 'UpdateLearnInfo'
getResponse(updateLearnInfoAdd, updateLearnInfoText)


addStudentStutyTimeInfoText_0 = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><AddStudentStutyTimeInfo xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken><classNo>'+classNo+'</classNo><statType>0</statType><material /><unit /></AddStudentStutyTimeInfo></soap:Body></soap:Envelope>'
addStudentStutyTimeInfoText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><AddStudentStutyTimeInfo xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken><classNo>'+classNo+'</classNo><statType>1</statType><material>'+book+'</material><unit>'+unit+'</unit></AddStudentStutyTimeInfo></soap:Body></soap:Envelope>'
addStudentStutyTimeInfoAdd = 'AddStudentStutyTimeInfo'
addStudentStutyTimeInfo_0Response = getResponse(addStudentStutyTimeInfoAdd, addStudentStutyTimeInfoText_0)
result0 = addStudentStutyTimeInfo_0Response[328:336]
addStudentStutyTimeInfoResponse = getResponse(addStudentStutyTimeInfoAdd, addStudentStutyTimeInfoText)
result = addStudentStutyTimeInfoResponse[328:336]


updateAliveText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><updateAlive xmlns="http://www.sflep.com/npels/commonsvc/"><aliveid>'+classNo+'#'+account+'</aliveid></updateAlive></soap:Body></soap:Envelope>'
updateAliveAdd = 'updateAlive'
updateStudentStudyEndTimeText = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><UpdateStudentStudyEndTime xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken><infoID>'+result+'</infoID></UpdateStudentStudyEndTime></soap:Body></soap:Envelope>'
updateStudentStudyEndTimeAdd = 'UpdateStudentStudyEndTime'
updateStudentStudyEndTimeText0 = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><UpdateStudentStudyEndTime xmlns="http://www.sflep.com/npels/commonsvc/"><SessionToken>'+token+'</SessionToken><infoID>'+result0+'</infoID></UpdateStudentStudyEndTime></soap:Body></soap:Envelope>'
print getResponse(updateStudentStudyEndTimeAdd, updateStudentStudyEndTimeText0)
count = 0
while True:
    getResponse(updateAliveAdd, updateAliveText)
    getResponse(updateStudentStudyEndTimeAdd, updateStudentStudyEndTimeText)
    print count, "minutes"
    count+=1
    time.sleep(60)
