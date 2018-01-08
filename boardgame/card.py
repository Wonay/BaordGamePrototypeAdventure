# -*- coding: utf-8 -*-


"""boardgame.card: card module within the boardgame package."""


class Card(object):
     def __init__(self, serial, name, description):
     	self.serial = serial
     	self.name = name
     	self.description = description