# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Inventory',
    'version': '12.0.0.0.0',
    'category': 'Inventory',
    'summary': 'Customs inventory',
    'sequence': '8',
    'author': 'Loomoni Morwo',
    'website': 'http://loomoni.com',
    'depends': ['stock'],
    'demo': [],
    'data': [
        'security/security.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
