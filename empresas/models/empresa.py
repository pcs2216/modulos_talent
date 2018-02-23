# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Empresas_inherit(models.Model):
    _name='empresa_inherit'
    #_inherit = 'crm.lead'

    
    name = fields.Char(
        string=u'Empresa',
    )
    
    