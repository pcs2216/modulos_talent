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
        'openeducat_core',
        'website',
        'website_form',
        'openeducat_admission',
        'website_partner',
        'website_mail',
        'hr'
    ],

    'demo': [],

    'data': [
        'data/menu_opciones.xml',
        'views/formulario_registro_empresas_view.xml',
        'data/website_data.xml',
        #'views/vista_empresa.xml',
        #'views/carrera_view.xml',
        #'views/facultades_view.xml',
        #'views/niveleducativo_view.xml',
        #'views/planestudios_view.xml',
        #'views/areas_view.xml',
        #'views/company_data_edit_view.xml',
        #'security/ops4g_security.xml',
        #'security/ir.model.access.csv',
        #'views/turnos_view.xml',
        #'views/periodos_view.xml',
        #'data/periodo_consecutivo.xml',
        #'demo/areas_demo.xml',
        #'demo/facultades_demo.xml',
        #'demo/niveleseducativos_demo.xml',
        #'demo/periodos_demo.xml',
        #'demo/carreras_demo.xml',
        #'demo/turnos_demo.xml',
    ],

    'installable':True,
    'auto_install':False,
}
