#!/usr/bin/env python
"""
#+TITLE: DicDEnDOc : English to Occitan Automatic Translation Software 
#+AUTHOR: Joanluc <joanluc.laborda@free.fr>
#+DESCRIPTION: This program aims to be used to translate GNU GetText localisation files, org, md or plain files from English to Occitan and to generate English to Occitan translation dictionary database from existing translations ; the GNU GetText localisation files can be english POT file (Portable Object Template file of msgid) or an other lenguage PO file (Portable Object file of msgid and msgstr in French, Spanish, Italian or Catalan mainly), in that cases the program will use external ressources to translate from theses other lenguages to occitan
"""
import nltk # Natural Lenguage Tool Kit importation
import regex as re
# from colorama import Fore, Back, Style, init
# init(autoreset=True)

class DicEnDOc():
    """
    Docs
    https://www.gnu.org/software/gettext/manual/gettext.html
    ../docs/DicDEnDOc_UseCases.org
    ../docs/msgstrTranslate.org
    """
    dialectes=dict()
    en_dial=dialectes
    en_dial={'en-com':'Common english','en-eng':'England english','en-usa':'USA english','en-aus':'Austalian english'}
    oc_dial=dialectes
    oc_dial={'oc-com':'Common Occitan','oc-auv':'Occitan Auvernhan','oc-gas':'Occitan gascon','oc-lem':'Occitan lemosin','oc-len':'Occitan lengadocian','oc-pro':'Occitan provençau','oc-viv':'Occitan vivaro-alpin'}
    
    def __init__(self,paramList=list()):	# paramList=[en_file,oc_file=None,potFile=True,poLang=None,altFile=None,en_dial='en-com',oc_dial='oc-com']):
        """
    	def __init__(self,en_file,oc_file=None,potFile=True,poLang=None,altFile=None,
			  en_dial='en-com',oc_dial='oc-com')
	file type is determined by filename suffixe extension : '.pot','.po','.org','.md','.html','.txt' and if there is no filename suffixe we assume it's a simple text file with no keywords 
	en_file is the english file to translate, by default it will be a PO template file (potFile=True),
	if potFile==False then it could be a translation from an other PO lenguage (poLang!=None && poLang in ['ca','fr','it','sp']) or a plain text translation (altFile!=None && altFile in ['.po','.md','.org','.txt']
        """
        self.en_file=paramList[0]	# en_file
        if paramList[1]!=None:		# oc_file
            self.oc_file=paramList[1]
        else:
            self.oc_file=self.en_file+"-oc.po"
        self.potFile=paramList[2]	# potFile==True||False
        if paramList[3]!=None:		# poLang
            self.poLang=paramList[3]
            if paramList[4]==None:	
                raise(Exception("We need a PO file to help translation"))
			else:
				self.altFile=paramList[4]
            if self.poLang="fr"
                self.translateProc="https:\\revirada.eu"
            elif self.poLang in ("cat","it","sp"):
                try:
                    self.translateProc=input("translation motor for "+self.poLang)
                except:
                    raise(Exception("No translation motor for "+self.poLang))
                    self.poLang="en"
            else:
                self.poLang="en"
        self.altFile=altFile # Org-mode or MD file
	# Defining current dictionnaries
        self.en_dial.get(en_dial)
        self.oc_dial.get(oc_dial)

    # def __set_poLang__(self,lang="fr"):
        # self.lang=lang
               
    def __git_tools__(self,gitAct,gitDir,gitUrl,gitParams):
	"""
	gitCmd in range("init","clone","add","commit","push","pull")
	gitDir : local repo directory
	gitUrl : remote server repo URL
	https://gitpython.readthedocs.io/en/stable/tutorial.html#understanding-objects
	* Initialize a new git Repo
	  # $ git init <path/to/dir>
	  from git import Repo
	  repo = Repo.init(path_to_dir)
	* Existing local git Repo
	  repo = Repo(path_to_dir)
	* Clone from URL
	  For the rest of this tutorial we will use a clone from https://github.com/gitpython-developers/QuickStartTutorialFiles.git
	  # $ git clone <url> <local_dir>
	  repo_url = "https://github.com/gitpython-developers/QuickStartTutorialFiles.git"
	  repo = Repo.clone_from(repo_url, local_dir)
	* Latest Commit Tree
	  tree = repo.head.commit.tree
	* Any Commit Tree
	  prev_commits = list(repo.iter_commits(all=True, max_count=10))  # last 10 commits from all branches
	  tree = prev_commits[0].tree
	* Display level 1 Contents
	  files_and_dirs = [(entry, entry.name, entry.type) for entry in tree]
	  files_and_dirs
	  # Output
	  # [(< git.Tree "SHA1-HEX_HASH" >, 'Downloads', 'tree'),
	  #  (< git.Tree "SHA1-HEX_HASH" >, 'dir1', 'tree'),
	  #  (< git.Blob "SHA1-HEX_HASH" >, 'file4.txt', 'blob')]
	* Recurse through the Tree
	  def print_files_from_git(root, level=0):
	      for entry in root:
		  print(f'{"-" * 4 * level}| {entry.path}, {entry.type}')
		  if entry.type == "tree":
		      print_files_from_git(entry, level + 1)
		      print_files_from_git(tree)
	  # Output
	  # | Downloads, tree
	  # ----| Downloads / file3.txt, blob
	  # | dir1, tree
	  # ----| dir1 / file1.txt, blob
	  # ----| dir1 / file2.txt, blob
	  # | file4.txt, blob
	"""
	import git
	from git import Repo
	dicDenDoc=Repo(gitDir)
	if gitCmd=="add":
	    fileList=gitParams.split()
	    dicDenDoc.index.add(fileList)
	elif gitCmd=="commit":
	    message=gitParams.split()
	    dicDenDoc.index.commit(message)
	elif gitCmd=="status":
	    dicDenDoc.untracked_files
	    dicDenDoc.index.iff(None)
	elif gitCmd=="push":
	    dicDenDoc.index.push()
	elif gitCmd=="pull":
	    dicDenDoc.index.pull()
	else:
	    print("Unknown Git Command")
			
    def __connect_pgSql__(self,pgUser,pgPass,db_request):
	"""
	Commit database after insert or update data
	connect to central database
	"""
	import psycopg2
	from config import config
	conn = None
	res = (None,None)
	try:
	    params=config()
	    pconn = psycopg2.connect("dbname=DicDEnDocDB user="+pgUser+" password="+pgPass)
	    cur = conn.cursor()
	    cur.execute(db_request)
	    db_result = cur.fetchone()
	    res[0] = format(db_result)
	    cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
	    res[1] = format(db_request+":"+error)
	finally:
	    if conn is not None:
		conn.close()
        return(res)
        
    def __extract_file_to_dict__(self,filename):
        dic={}
        with open(filename) as f:
            for line in f:
                print(line)
                try:
                    (id,word)=line.split()
                    dic[int(id)]=word
                    print(format(dic))
                except Exception as ex:
                    print(format(ex))
            f.close()
            return(dic)

    def selectWordFromDB(self,dbTyp,EnWr):
	"""
	dbTyp in range("Postgres","MySQL","SQLite")
	or JSON files :
	    "en2ocSent.json"
	    "en2ocWord.json"
	    "enVerb.json"
	    "oc2enWord.json"
	    "ocVerb.json"
	"""
	if dbTyp in ("Postgres","MySQL","SQLite"):
	    db_request = "SELECT * FROM OcWrtb WHERE WrId "+EnWr
	    if dbTyp == "Postgres":
		result = self.__connect_pgSql__(pgUser,pgPass,db_request)
	    elif dbTyp=="MySQL":
		raise("Not implemented")
	    elif dbTyp=="SQLite":
	        raise("Not implemented")
	    else:
		# dbTyp=="JSON files ("en2ocSent.json)"
		import json
		with open("en2ocWord.json") as EnWr:
		    # enWord:{
		    #   wdGramType :[verb,noun,adjective,adverb,article,preposition,pronoun,determiners,conjunctions,interjections],
                    #   dialect in range("ComOc","AuvOc", "GasOc","LemOc","LenOc","ProOc","VivOc")
		    #   ocWord }
		    print("selectWordFromDB:open('en2ocWord.json')")

    def selectSentFromPgDB(self,EnSn):
	snid_req = "SELECT SnId FROM EnSntb WHERE EnSn = "+EnSn  
	ocsn_req = "SELECT OcSn FROM OcSntb WHERE SnId = "+snid_request
	result = self.__connect_pgSql__(pgUser,pgPass,db_request)
	return(result)

    def insertSentIntoPgDB(self,SnId,EnSn,OcSn):
	db_request = "INSERT INTO FROM EnSntb (SnId "+EnSn+")"
	result = self.__connect_pgSql__(pgUser,pgPass,db_request)
	db_request = "INSERT INTO FROM OcSntb (SnId "+OcSn+")"
	result = self.__connect_pgSql__(pgUser,pgPass,db_request)

    def insertWordIntoPgDB(self,WrId,EnSn,OcSn):
	db_request = "INSERT INTO FROM EnWrtb (WrId "+EnWr+")"
	result = self.__connect_pgSql__(pgUser,pgPass,db_request)
	db_request = "INSERT INTO FROM OcWrtb (WrId "+OcWr+")"
	result = self.__connect_pgSql__(pgUser,pgPass,db_request)
		
    def parseWordsInSentence(self,sentence):
        """
	Extract all words in a natural lenguage sentence that is of string data type to a list of separated single words
        """
        from nltk.tokenize import word_tokenize
        wordList=word_tokenize(sentence)
        print(format(wordList))
        return(wordList)

    def readFileBySentence(self,file):
        """
	Read plain text file and parse it into sentences then return them into an ordonned dictionary
	* Extraction of sentences from text files
	* nltk (Natural Language Tool Kit)
	  https://www.nltk.org/
	  https://realpython.com/nltk-nlp-python/
	  While analyzing text, we can tokenize by word or tokenize by sentence.
        * nltk.tokenize
      	  Here’s what both types of tokenization bring to the table:
          * word_tokenize
      	    Words are natural language atoms, smallest unit of meaning that still makes sense on its own.
	    They will be the base of english and occitan word directories.
	  * sent_tokenize
            When we tokenize by sentence, we can analyze how words relate one  to another and have informations on context.
        * Prerequisite : ntlk pip installation
	#+BEGIN_SRC bash
	  python -m pip install nltk==3.5
	#+END_SRC

        * NLTK Data
	  https://www.nltk.org/data
	  python -m pip install numpy matplotlib
        """
        from nltk.tokenize import sent_tokenize
        # if ntlk.download("punkt")
        with open(file) as f:
            nltk.download('punkt')
            fDict=dict()
            text=f.read()
            sentList=sent_tokenize(text)
            for idx in range(0,len(sentList)):
                fDict[idx]=sentList[idx]
            return fDict

    def rearrangeMoctable(self,line):
        """
        sort the word order to obtain a correct occitan sentence
        add idtable  to database/enSentence_table
        add moctable  to database/ocSentence_table
        """
        enSentenceTab=dict()
        ocSentenceTab=dict()
        with open("db/enSentence.db",'a') as ed:
            enSentenceTab=self.__extract_file_to_dict__("db/enSentence.db")
            # Get enSentenceTab maximum key value to add             
            id=max(enSentenceTab.values) 
            od=open("db/ocSentence.db",'a')
            ocSentenceTab=self.__extract_file_to_dict__("db/ocSentence.db")
            line=input(print(format(line)))
            od.write(line)
        return(line)

    def ocTranslateW(self,enw,enTab):
    	# Translate english word to occitan
        keywords=[',','.',';','?','!',
                  '*','#','+','/','-',
                  '\\','&','|']
        if (not type(enw)==str() or not type(enTab)==dict()):
            raise(TypeError("Type error:"+format(enw)
                            +" or "+format(enTab)))
        if enw in keywords:
            ocw=enw
        elif lambda : enw in enTab.itervalues():
            ocTab=self.__extract_file_to_dict__("../db/oc_word.db")
            ocw=ocTab[i]
        else:
            ocw=input('translate '+enw)
        return(ocw)			# translate english 'en_word' to occitan 'oc_word'

    def ocTranslateS(self,sentence):
	ocSn = self.selectSentFromDB(sentence)
	# if (ocSn != None):
	#	self.parseWordsInSentence(sentence)
        ocSent=self.rearrangeMoctable(line)
        
    def translateAlternateDocFile(self,poLang):
        """
	Begin tranlation of .org, .md, .html or simple text file such as LICENSE files
        Open and parse english file by sentences
	"""
        self.enDict=self.readFileBySentence(enFile)
        with open(self.ocFile,'a') as of:
            for i in range(0,enDict(len)):
                self.ocDict[i]=self.ocTranslateS(enDict[i])
                self.ocFile.write(ocDict[i])
        
    def en2ocDb(self):
	"""
	"""
        print(en2ocDb)                                 

    def translateFromCaFrItPtSpPoFile(self):
        """
	Begin tranlation from a Catalan, French, Italian, Portuguese or Spanish translated PoFile
	input datas:
	* self.potfile: english pot file,
	* self.pofile: translated PoFile,
	* self.poLang: pofile lenguage
	Process
	* copy file.po file-oc.po
	  open  file-oc.po for reading and writing
          for each line in  file-oc.po
              if line begins with 'msgid'
	          verify the same line is into file.pot 
                  search line begining with 'msgstr'
	          init rest of msgstr line as empty 'moctable'
                  translate using external ressource 
                  for each word in 'idtable' as 'en_word'
                  translate 'en_word' to occitan 'oc_word'
	      add 'oc_word' to 'moctable'
              rearrange 'moctable'
	"""       
        with open(self.altFile) as po:
            pot=open(self.en_file,'r')
            ocf=open(self.oc_file,'a')
            ocLine=str()
            self.enDict=self.__extract_file_to_dict__("../db/en_word.db")
            idx=0;
            for poLine in po:
                ocLine=self.externalTranslationRessource(poLang)
                enTable=enLine.split()
                ocTable=ocLine.split()
                self.enDb=open("../db/en_word.db",'a')
                self.ocDb=open("../db/oc_word.db",'a')
                for enw in enTable:
                    ocw=ocTranslateW(enw,enDict)
                    if enw not in enDict:
                        idx+=1
                        enDb.write(idx,enw)
                        ocDb.write(idx,ocw)
                ocLine=ocLine+" "+ocw
                ocLine=rearrange(ocLine)
	

    def translateFromPotFile(self):
        """
	input datas:
	* self.potfile: english pot file,
	Process
        * copy file.pot file-oc.po
          open  file-oc.po for reading and writing
          for each line in  file-oc.po
              if line begins with 'msgid'
                  copy rest of the line to memory_table 'idtable'
              search line begining with 'msgstr'
              init rest of msgstr line as empty 'moctable'
              for each word in 'idtable' as 'en_word'
                translate 'en_word' to occitan 'oc_word'
	        add 'oc_word' to 'moctable'
            rearrange 'moctable'
        """        
        with open(self.en_file) as ef:
            of=open(oc_file,'a')
            ocLine=str()
            self.enDict=self.__extract_file_to_dict__("../db/en_word.db")
            idx=0;
            for enLine in ef:
                enTable=enLine.split()
                self.enDb=open("../db/en_word.db",'a')
                self.ocDb=open("../db/oc_word.db",'a')
                for enw in enTable:
                    ocw=ocTranslateW(enw,enDict)
                    if enw not in enDict:
                        idx+=1
                        enDb.write(idx,enw)
                        ocDb.write(idx,ocw)
                ocLine=ocLine+" "+ocw
                ocLine=rearrange(ocLine)

def test_DicEnDOc():
    # __init__(self,paramList=list()):	
    # paramList=[en_file,oc_file=None,potFile=True,
    # poLang in [None,'ca','fr','it','po','sp'],
    # altFile=[None,"*.po","*.org","*.md","*.html","*"],
    # en_dial='en-com',oc_dial='oc-com
    def set_params(testNb=int()):
		en_file=input("POT file to translate filename? ")
		params[0]=en_file
		params[1]=None
		params[2]=True
	    params[3]=None
		params[4]=None
		if testNb==1:
			oc_file=input("Occitan translated PO file filename? ")
			params[1]=oc_file
		elif testNb==2:
	        frpo_file=input("French PO file filename? ")
	        params[3]='fr'
			params[4]=frpo_file
		elif testNb==3:
		    frpo_file=input("French PO file filename? ") 
		    oc_file=input("Occitan translated PO file filename? ")
			params[1]=oc_file
	        params[3]='fr'
			params[4]=frpo_file
		elif testNb==4:
	        while params[3] not in ['ca','it','pt','sp']:
				params[3]=input("Catalan, Italian, Portugeese or spanish language")
		    po_file=input("Catalan, Italian, Portugeese or spanish PO file filename? ") 
			params[4]=po_file
		else:
			params[2]=False
			# No POTfile so we have .org, .md or simple text translation
		return params
		
    def revirar(params):
		try:
	        revirada=DicEnDOc(en_file)
		    return revirada
	    except Exception() es ex:
	        print(format(ex))
        
    # Test translate from POT File
	params=set_params(0)
    revirada=revirar(params)
    revirada.translateFromPotFile()
    revirada.en2ocDb()
    # Test translate from POT File and Occitan PO File is not standard
	params=set_params(1)
    revirada=revirar(params)
    revirada.translateFromPotFile()
    revirada.en2ocDb()
    # Test translate from French PO File
    # PoLang='fr' && altFile=frpo_file
	params=set_params(2)
    revirada=revirar(params)
    revirada.translateFromCaFrItPtSpPoFile()
    revirada.en2ocDb()
    # Test translate from French PO File and Occitan PO File is not standard
    # PoLang='fr' && altFile=frpo_file
	params=set_params(3)
    revirada=revirar(params)
    revirada.translateFromCaFrItPtSpPoFile()
    revirada.en2ocDb()
    # Test translate from alternate doc file
	params=set_params(4)
    revirada=revirar(params)
    revirada.translateAlternateDocFile()
    revirada.en2ocDb()

if __name__=="__main__":
    test_DicEnDOc()

               
