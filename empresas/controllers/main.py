# -*- coding: utf-8 -*-
from odoo import http


class Register_company(http.Controller):

    
    @http.route('/page/empresas.formulario_empresas/', auth='public', website=True)
    def get_register_company(self, **kw):
    	# Datos del modelo admision.register
        registro_admision = http.request.env['empresa_inherit']
        # Datos del modelo course
        #curso_admision = http.request.env['op.course']
        # Regreso de datos como diccionario
        return http.request.render('empresas.formulario_empresas', {
            'registros': registro_admision.search([]),
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
            #'cursos': curso_admision.search([])
        })
