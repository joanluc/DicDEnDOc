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

               
