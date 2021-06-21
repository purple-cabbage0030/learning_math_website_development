class MemberDTO:
    def __init__(self, newmemno, newmname, newmid, newmpw, newbirth):
        self.memno = newmemno
        self.mname = newmname
        self.mid = newmid
        self.mpw = newmpw
        self.birth = newbirth

    def getMemno(self):
        return self.memno
    
    def setMemno(self, newmemno):
        self.memno = newmemno

    def getMname(self):
        return self.mname
    
    def setMname(self, newmname):
        self.mname = newmname

    def getMid(self):
        return self.mid
    
    def setMid(self, newmid):
        self.mid = newmid

    def getMpw(self):
        return self.mpw
    
    def setMpw(self, newmpw):
        self.mpw = newmpw

    def getBirth(self):
        return self.birth
    
    def setBirth(self, newbirth):
        self.birth = newbirth

class QuestionDTO:
    def __init__(self, newqsid, newtitle, newcontent, memno):
        self.qsid = newqsid
        self.title = newtitle
        self.content = newcontent
        self.memno = memno

    def getQsid(self):
        return self.qsid
    
    def setQsid(self, newqsid):
        self.qsid = newqsid

    def getTitle(self):
        return self.title
    
    def setTitle(self, newtitle):
        self.title = newtitle

    def getContent(self):
        return self.content
    
    def setContent(self, newcontent):
        self.content = newcontent

class AnswerDTO:
    def __init__(self, newasid, qsid, newtext, memno):
        self.asid = newasid
        self.qsid = qsid
        self.text = newtext
        self.memno = memno

    def getAsid(self):
        return self.asid
    
    def setAsid(self, newasid):
        self.asid = newasid


    def getText(self):
        return self.text
    
    def setText(self, newtext):
        self.text = newtext