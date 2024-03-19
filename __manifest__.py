# -*- coding: utf-8 -*-
{
    'name': "stock_extension",

    'summary': """
       Add new fields to stock.production.lot model which are equipment user, the location of the equipment and customer.""",

    'description': """
        Add new fields to stock.production.lot model which are equipment user, the location of the equipment and customer. Inherits stock.production.lot model.
    """,

    'author': "Alif Ibrahim",
    'website': "https://www.sigma.myerp.com.my",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
