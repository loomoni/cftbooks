# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Expenses',
    'version': '12.0.0.0.0',
    'category': 'expenses',
    'summary': 'Custom Expenses',
    'sequence': '8',
    'author': 'Loomoni Morwo',
    'website': 'http://loomoni.com',
    'depends': ['hr_expense', 'hr'],
    'demo': [],
    'data': [
        'security/security.xml',
        'views/views.xml',
        'data/email_template.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
