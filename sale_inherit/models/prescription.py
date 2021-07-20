from odoo import models, fields, _, api
from datetime import datetime

class Prescription(models.Model):
    _name = 'prescription'
    _rec_name = 'seq_name'

    patient_name = fields.Char(string='Patient Name')
    patient_age = fields.Integer(string="Patient Age")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
    address = fields.Text(string='Address')
    date = fields.Date(default=datetime.today(),required=True, string='Date')
    prescription_field = fields.Text(string='Prescription')
    seq_name = fields.Char(string='Client Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('seq_name', _('New')) == _('New'):
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('prescription.sequence') or _('New')

        result = super(Prescription, self).create(vals)
        return result