# -*- coding: utf-8 -*-
{
    'name': "Multi-Branch Point of Sale",

    'summary': """POS multi branch operation""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_multi_branch', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir_rule.xml',
        'views/assets.xml',
    ],
}