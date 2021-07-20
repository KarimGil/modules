from odoo import models, fields, _, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    prescription_id = fields.Many2one('prescription','Prescription')

