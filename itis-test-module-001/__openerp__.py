# -*- coding: utf-8 -*-
{
    'name': "itis-test-module-001",

    'summary': """
        This is a short test for apps.odoo.com
        """,

    'description': """
        This is a short test for apps.odoo.com
    """,

    'author': "IT IS AG",
    'website': "http://www.itis-odoo.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'price': 10.92,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
