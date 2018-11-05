from odoo import api, fields, models
from odoo import SUPERUSER_ID
# from odoo.exceptions import ValidationError


def migrate_company_branch(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    company = env.ref('base.main_company')
    company.write({'branch_id': env.ref('base_multi_branch.data_branch_1').id})
    cr.commit()
    user_ids = env['res.users'].search([])
    for user_id in user_ids:
        if not user_id.user_has_groups('base_multi_branch.group_multi_branch'):
            user_id.sudo().write({'default_branch_id': user_id.company_id.branch_id.id,
                                  'branch_ids': [(6, 0, [user_id.company_id.branch_id.id])]})
            cr.commit()


class Company(models.Model):
    _name = "res.company"
    _inherit = ["res.company"]

    branch_id = fields.Many2one('res.branch', 'Branch', ondelete="cascade")

    @api.model
    def create(self, vals):
        branch = self.env['res.branch'].create({
            'name': vals['name'],
            'code': vals['name'],
        })
        vals['branch_id'] = branch.id
        self.clear_caches()
        company = super(Company, self).create(vals)
        branch.write({'partner_id': company.partner_id.id,
                      'company_id': company.id})
        return company


class ResBranch(models.Model):
    _name = "res.branch"

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(string='Active', default=True)
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 ondelete='restrict')
    company_id = fields.Many2one(
        'res.company', string="Company",
        default=lambda self: self.env.user.company_id, required=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State',
                               ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country',
                                 ondelete='restrict')
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()

    _sql_constraints = [('branch_code_company_uniq',
                         'unique (code,company_id)',
                         'The branch code must be unique per company!')]

    @api.model
    def create(self, vals):
        res = super(ResBranch, self).create(vals)
        vals.pop("name", None)
        vals.pop("code", None)
        vals.pop("partner_id", None)
        vals.update({'branch_id': res.id})
        res.partner_id.write(vals)
        return res

    @api.multi
    def write(self, vals):
        res = super(ResBranch, self).write(vals)
        vals.pop("name", None)
        vals.pop("code", None)
        vals.pop("company_id", None)
        vals.pop("partner_id", None)
        ctx = self.env.context.copy()
        if 'branch' not in ctx:
            for record in self:
                record.partner_id.write(vals)
        return res

    @api.model
    def _branch_default_get(self):
        """ Returns the default branch (usually the user's branch with a company).
        """
        return self.env['res.users']._get_branch()
