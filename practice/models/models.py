# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class practice(models.Model):
#     _name = 'practice.practice'
#     _description = 'practice.practice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, _, api


class OfficeStaff(models.Model):
    _name = 'office.staff'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Maintaining record of Office Employees'
    _rec_name = 'first_name'

    first_name = fields.Char('First name', required=True)
    last_name = fields.Char('last name', required=True)
    age = fields.Integer('Age')
    notes = fields.Text('Notes')
    image = fields.Binary('Image')
    seq_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('seq_name', _('New')) == _('New'):
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('office.staff.sequence') or _('New')

        result = super(OfficeStaff, self).create(vals)
        return result
