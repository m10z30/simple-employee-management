# -*- coding: utf-8 -*-
{
    'name': "employee-managment",

    'sequence': -100,  
    'application': True,
    'category': 'Employee',    

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
        'views/department_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

