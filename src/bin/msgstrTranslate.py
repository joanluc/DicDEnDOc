#!/usr/bin/env python
#+TITLE: msgstrTranslate
#+DESCRIPTION: Automatic Occitan Translations for GNU GPL Licensed Software
"""
* class Msgstr_Translate
  class var: projName = name of occtan translation project
             ex: WineHQ Occitan translation, prjName = 'wine' 
** Method potBased
   input var: potFile = messages reference file
              ocpoFile = occitan translated messages file
   inner var: msgidLine, msgstrTab, msgstrLine, word
   function
     for each line in potFile begining with msgid {
       write that line as msgidLine to ocpoFile
       copy that line as msgistrLine
       for each word  in msgistrLine {
         if word='msgid' replace with 'msgstr'
         else replace with occitan translation word
       }
       write msgistrLine to ocpoFile
     }
      
** Method frpoBased
   occitan translation based on existing french translation
   may use [["Lo Congres"|https://locongres.org]] revirada.eu french to occitan translation tool
"""
#+BEGIN-SRC :python
class  Msgstr_Translate():
    def __init__(self,projName,projDirPath):
        self.projName=projName
        self.projDirPath=projDirPath

    def word_tr(self,word):
        ocwd=input(word+'occitan translation')
        return(ocwd)

    def poOpen(self,ocpoName,ocwd):
        if exist(ocpoFile):
            po=open(ocpoFile,'r')
            if grep(ocwd,ocpoFile):
                po=open(ocpoFile,'w')
            else:
                po=open(ocpoFile,'a')
        else:
            po=open(ocpoFile,'c')
        return(po)
        
        
    def potBased(self,potName,ocpoName):
        """
        potName=projName+".pot",
                 ocpoName=projName+"oc.po")
        """
        rdLine=str()
        msgidLine=str()
        msgstrLine=str()
        word=str()
        msgTab=list()
        msgidTab=list()
        msgstrTab=list()
        with open(self.projDirPath+'/'+potName,'r') as pot:
            po=open(self.projDirPath+'/'+ocpoName,'w')
            for rdLine in pot:
                print("read "+format(pot))
                print(rdLine)
                msgTab=rdLine.split()
                print(msgTab)
                if msgTab[0]=='msgid':
                    msgidLine=rdLine
                    msgidTab=msgTab
                    po.write(msgidLine)
                elif msgstrTab[0]=='msgstr':
                    for i in enum(1,len(msgTab)):
                        msgstrTab[i]=self.word_tr(msgTab[i])
                    msgstrLine=str(msgstrTab)
                    po.write(msgstrLine)
                elif msgstrTab[0]=='msgctxt':
                    pass
                else:
                    # lines that don't begin with msgid, msgstr or msgctxt can be a ref to a source file or a continued line
                    # if previous line was msgidLine then it's a msgidLine continuation
                    # elif previous line was msgstrLine then it's a msgstrLine continuation
                    # else may be a comment line
                    # 
                    pass
def test_Msgstr_Translate():
    proj=Msgstr_Translate('WineHQ Occian translation','../wine/po')
    proj.potBased('wine.pot','oc.po')

if __name__=="__main__":
    test_Msgstr_Translate()
#+END-SRC
