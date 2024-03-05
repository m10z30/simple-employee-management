# -*- coding: utf-8 -*-
{
    'name': "employee-managment",

    'summary': "Simple Employee Management",

    'description': """
    a simple model developed to test the odoo framework
    """,

    'author': "Mohammad Zohair",
    'website': "",

    'category': 'management',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

