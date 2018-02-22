# -*- coding: utf-8 -*-
{
    'name': "Empresas - Registro",

    'summary': """
        Main items
        Registro de Empresas
        """,

    'description':
        """
            Datos principales de la empresa
        """,

    'author': "Soluciones4G",
    'website': "http://soluciones4g.com",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': [
        'base',
        'web',
        'website',
        'website_form',
        'website_partner',
        'website_mail',
    ],

    'demo': [],

    'data': [
        'data/menu_opciones.xml',
        'views/formulario_registro_empresas_view.xml',
        'data/website_data.xml',
        'views/vista_empresa.xml',
        'security/ir.model.access.csv',
    ],

    'installable':True,
    'auto_install':False,
}
