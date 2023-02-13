import appModuleHandler
import addonHandler
import eventHandler
import mouseHandler
import api
import ui
import speech
import tones
import oleacc
import winUser
import windowUtils
import controlTypes
import NVDAObjects
import NVDAObjects.IAccessible
from NVDAObjects.behaviors import RowWithFakeNavigation
from cursorManager import CursorManager
from NVDAObjects.window.edit import EditTextInfo
from scriptHandler import script
from NVDAObjects.UIA import UIA

def sameApp(obj=None):
	if obj is None:
		obj = api.getNavigatorObject()
	return api.getFocusObject().appModule == obj.appModule


def nomObjet (obj):
	nom = obj.name
	nom = str(nom)
	
	if nom == "":
		nom = " ~"
	
	return nom


# Création de la classe héritée de appModuleHandler
class AppModule(appModuleHandler.AppModule):

	def script_infoTransfertAppel (self, gesture):
		obj = api.getFocusObject()
		if sameApp(obj):
			# Récupère la fenêtre active
			fnt = api.getForegroundObject()
			
			espaceTravail = None
			if fnt.children[0].childCount >= 1: # Enfants fenêtre principale
				if fnt.children[0].children[0].childCount >= 1: # Enfants "Espace de travail"
					if fnt.children[0].children[0].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 0
						print("espace0 : " + str(espaceTravail))
					elif fnt.children[0].children[1].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 1
						print("espace1 : " + str(espaceTravail))
			
			
			print("espace : " + str(espaceTravail))
			if espaceTravail != None:
				#récurère les infos sur le transfert d'appel
				nomPosteRenvoi = str(fnt.children[0].children[espaceTravail].children[0].children[39].name)
				etatPosteRenvoi = str(fnt.children[0].children[espaceTravail].children[0].children[41].name)
				etatAppel = str(fnt.children[0].children[espaceTravail].children[0].children[43].name)
				barreEtatRenvoi = str(fnt.children[0].children[espaceTravail].children[0].children[45].name) + str(fnt.children[0].children[1].children[0].children[46].name)

				
				if etatAppel == "None":
					ui.message("Aucun appel en acheminement")
				elif etatPosteRenvoi == "DestRv Extérieur":
					ui.message(barreEtatRenvoi + " - " + nomPosteRenvoi)
				else:
					ui.message(etatAppel + " - " + barreEtatRenvoi + " - " + nomPosteRenvoi)
			else:
				ui.message("Espace de travail introuvable")
		
		
		else:
			tones.beep(440, 10)
		
		
		
	
	
	
	# Objet dictionnaire pour l'assignations des gestes de commandes applicatifs
	__gestures = {
		"kb:F4":"infoTransfertAppel"
	}