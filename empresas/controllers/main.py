# -*- coding: utf-8 -*-
from odoo import http


class Register_company(http.Controller):

    
    @http.route('/page/empresas.formulario_empresas/', auth='public', website=True)
    def get_register_company(self, **kw):
    	# Datos del modelo admision.register
        registro_admision = http.request.env['res.partner']
        # Datos del modelo course
        estados = http.request.env['res.country.state']
        # Regreso de datos como diccionario
        return http.request.render('empresas.formulario_empresas', {
            'registros': registro_admision.search([]),            
            'estados': estados.search([])
        })
