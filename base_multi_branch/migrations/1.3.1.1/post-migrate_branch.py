# -*- coding: utf-8 -*-
import odoo


def migrate(cr, version):
    registry = odoo.registry(cr.dbname)
    from odoo.addons.base_multi_branch.models.res_branch import \
        migrate_company_branch
    migrate_company_branch(cr, registry)
