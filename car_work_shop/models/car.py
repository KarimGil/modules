from odoo import models, fields, _, api
from datetime import datetime
from odoo.exceptions import UserError
from . import spareparts


class Car(models.Model):
    _name = 'car'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'We provide services for this cars'
    _rec_name = 'model'


    def print_report(self):
        return self.env.ref('car_work_shop.report_vehicle_detail').report_action(self)
    def confirm_status(self):
        self.write({'state': 'confirm'})



    company_name = fields.Char('Company/Brand name', required=True)
    model = fields.Char('Model of the car', required=True)
    model_year = fields.Char('Launch Year')
    license_plate = fields.Char('License')
    odometer = fields.Float('Last Odometer')
    immatriculation_date = fields.Date('Immatriculation Date',default=datetime.today(),required=True)
    chassis = fields.Char('Chassis Number', required=True)
    color = fields.Char('Car color')
    image = fields.Binary('Image')
    reffer_id = fields.Many2many('spare.parts','car_spare_parts_rel',string="Spare Parts", required=True)
    sptype_id = fields.Char(string='Spare Part Type',related='reffer_id.sp_type', tracking=True)
    technology = fields.Char(compute='technology_used', string="Technology Used")

    @api.depends('model_year')
    def technology_used(self):
        for rec in self:
            if rec.model_year:
                if int(rec.model_year) >= 2018:
                    rec.technology = 'Latest'
                elif int(rec.model_year) >= 2000 and int(rec.model_year) < 2018:
                    rec.technology = 'Old'
                else:
                    rec.technology = 'Decade'


    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'),('cancel','Cancel')], string='Status', default='draft')
    seq_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    def unlink(self):
        for option in self:
            if option.state in ('confirm'):
                raise UserError(
                    _('You cannot delete the entry which is confirmed.'))
        return models.Model.unlink(self)

    @api.model
    def create(self, vals):
        if vals.get('seq_name', _('New')) == _('New'):
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('car.sequence') or _('New')

        result = super(Car, self).create(vals)
        return result

