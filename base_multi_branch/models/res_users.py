from odoo import api, fields, models
from odoo import SUPERUSER_ID
# from odoo.exceptions import ValidationError


class Users(models.Model):

    _inherit = "res.users"

    @api.model
    def branch_default_get(self, user):
        if not user:
            user = self._uid
        branch_id = self.env['res.users'].browse(user).default_branch_id
        if not branch_id:
            branch_id = \
                self.env['res.users'].browse(user).company_id.branch_id
        return branch_id

    @api.model
    def _get_branch(self):
        return self.env.user.default_branch_id

    @api.model
    def _get_default_branch(self):
        return self.branch_default_get(self._uid)

    def _branches_count(self):
        return self.env['res.branch'].sudo().search_count([])

    branch_ids = fields.Many2many('res.branch',
                                  'res_branch_users_rel',
                                  'user_id',
                                  'branch_id',
                                  'Branches', default=_get_branch,
                                  domain="[('company_id','=',company_id)]")
    default_branch_id = fields.Many2one('res.branch', 'Default branch',
                                        default=_get_branch,
                                        domain="[('company_id','=',company_id)"
                                               "]")
    branches_count = fields.Integer(
        compute='_compute_branches_count',
        string="Number of Companies", default=_branches_count)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id.branch_id:
            self.default_branch_id = self.company_id.branch_id.id
            self.branch_ids = [(4, self.company_id.branch_id.id)]

    @api.multi
    def _compute_branches_count(self):
        branches_count = self._branches_count()
        for user in self:
            user.branches_count = branches_count

    @api.model
    def create(self, vals):
        res = super(Users, self).create(vals)
        if 'company_id' in vals:
            vals.update({
                'default_branch_id': self.company_id.branch_id.id,
            })
        return res

    @api.multi
    def write(self, vals):
        res = super(Users, self).write(vals)
        if 'company_id' in vals:
            self.default_branch_id = self.company_id.branch_id.id
        return res
