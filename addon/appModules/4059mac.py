# NVDAext_Alcatel-Lucent-4059mac by Thibaud NEDEY - Tybot.Fr
# Copyright 2023
# Licence GNU GPL v3
# This file is part of NVDAext_Alcatel-Lucent-4059mac.
# NVDAext_Alcatel-Lucent-4059mac is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.
# NVDAext_Alcatel-Lucent-4059mac is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License version 3 (file : 'LICENSE') along with NVDAext_Alcatel-Lucent-4059mac. If not, see https://www.gnu.org/licenses/gpl-3.0.html

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

	# Fonction d'énonciation des informations du transfert d'appel
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
					elif fnt.children[0].children[1].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 1
			
			
			if espaceTravail != None:
				# Récurère les infos sur le transfert d'appel
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
		
	
	# Fonction d'énonciation des informations de l'appelant
	def script_infoAppelant (self, gesture):
		obj = api.getFocusObject()
		if sameApp(obj):
			# Récupère la fenêtre active
			fnt = api.getForegroundObject()
			
			espaceTravail = None
			if fnt.children[0].childCount >= 1: # Enfants fenêtre principale
				if fnt.children[0].children[0].childCount >= 1: # Enfants "Espace de travail"
					if fnt.children[0].children[0].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 0
					elif fnt.children[0].children[1].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 1
			
			
			if espaceTravail != None:
				# Récurère les infos sur l'appelant
				if fnt.children[0].children[espaceTravail].children[0].children[53].childCount == 1:
					appelant = str(fnt.children[0].children[espaceTravail].children[0].children[53].children[0].name)
				else:
					appelant = "None"

				
				if appelant == "None":
					ui.message("Aucun appel")
				else:
					ui.message(appelant)
			else:
				ui.message("Espace de travail introuvable")
		
		
		else:
			tones.beep(440, 10)
	
	
	# Fonction d'énonciation des informations du transfert d'appel en cours
	def script_infoTransfertEnCours (self, gesture):
		obj = api.getFocusObject()
		if sameApp(obj):
			# Récupère la fenêtre active
			fnt = api.getForegroundObject()
			
			espaceTravail = None
			if fnt.children[0].childCount >= 1: # Enfants fenêtre principale
				if fnt.children[0].children[0].childCount >= 1: # Enfants "Espace de travail"
					if fnt.children[0].children[0].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 0
					elif fnt.children[0].children[1].children[0].childCount >= 45: # Enfants "Sbc"
						espaceTravail = 1
			
			
			if espaceTravail != None:
				# Récurère les infos sur le transfert d'appel en cours
				if fnt.children[0].children[espaceTravail].children[0].children[89].childCount == 1:
					transencours = str(fnt.children[0].children[espaceTravail].children[0].children[89].children[0].name)
				else:
					transencours = "None"

				
				if transencours == "None":
					ui.message("Aucun transfert en cours")
				else:
					ui.message(transencours)
			else:
				ui.message("Espace de travail introuvable")
		
		
		else:
			tones.beep(440, 10)
	
	
	# Objet dictionnaire pour l'assignations des gestes de commandes applicatifs
	__gestures = {
		"kb:F4":"infoTransfertAppel",
		"kb:F5":"infoAppelant",
		"kb:F6":"infoTransfertEnCours"
	}