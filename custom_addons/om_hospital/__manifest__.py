# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https:///www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/medicine.xml',
        'views/obatpasien.xml',
        'views/patient.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
