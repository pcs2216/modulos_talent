# -*- coding: utf-8 -*-
from odoo import fields, models


class Contacto_nuevo(models.Model):
	_name = 'ops4g.contactos'
	_inherit = 'mail.thread'

	name = fields.Char(
		string="Nombre del contacto",
	)

	app = fields.Char(
		string="Apellido"
	)