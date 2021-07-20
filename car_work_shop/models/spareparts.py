from odoo import models, fields, _, api


class SpareParts(models.Model):
    _name = 'spare.parts'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Available Spare Parts'
    _rec_name = 'name'

    name = fields.Char('Spare Part Name', required=True, unique=True)
    sp_type = fields.Char(string='Spare parts type',default='Spare Part')