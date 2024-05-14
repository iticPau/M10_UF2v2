from odoo import models, fields

class cleaning_schedule(models.Model):
    _name = 'testmodulo.cleaning_schedule'
    _description = 'Cleaning Schedule Model'

    name = fields.Char(string='Schedule Name', required=True)
    date = fields.Date(string='Date', required=True)
    description = fields.Text(string='Description')