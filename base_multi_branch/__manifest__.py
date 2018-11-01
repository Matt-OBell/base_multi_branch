{
    'name': 'Branch & Company Mixin',
    'version': '1.1',
    'category': 'Discuss',
    'author': 'Mattobell LTD',
    'sequence': 25,
    'summary': 'Include Branch & Company support',
    'description': """
Branch & Company
================

Main Features
-------------
* Include Branch & Company in all objects
* Just need to inherit ir.branch.company.mixin in your object
* And in your xml file add below 2 lines in your Views
    <field name="branch_id" />
    <field name="company_id" />
""",
    'website': '',
    'depends': [
        'base',
        'base_setup'
    ],

    'data': [
        'data/res_branch.xml',
        'wizard/branch_config_view.xml',
        'security/branch_security.xml',
        'security/ir.model.access.csv',
        'views/res_branch_view.xml',
        'views/res_branch_config_view.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': True
}
