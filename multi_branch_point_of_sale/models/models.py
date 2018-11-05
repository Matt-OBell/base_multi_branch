from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero


class PosSession(models.Model):
    _name = 'pos.session'
    _inherit = ['pos.session', 'ir.branch.company.mixin']


class PosOrder(models.Model):
    _name = 'pos.order'
    _inherit = ['pos.order', 'ir.branch.company.mixin']


class PosConfig(models.Model):
    _name = 'pos.config'
    _inherit = ['pos.config', 'ir.branch.company.mixin']

    @api.multi
    @api.constrains('branch_id', 'stock_location_id')
    def _check_branch_constrains(self):
        if self.branch_id and self.stock_location_id:
            if self.branch_id.id != self.stock_location_id.branch_id.id:
                raise UserError(
                    _("""Configuration error\nYou  must select same branch on
                        a location as asssigned on a point of sale 
                        configuration."""))


class PosCategory(models.Model):
    _name = "pos.category"
    _inherit = ['pos.category', 'ir.branch.company.mixin']


class PosOrderLine(models.Model):
    _name = "pos.order.line"
    _inherit = ['pos.order.line', 'ir.branch.company.mixin']