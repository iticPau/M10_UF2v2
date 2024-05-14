from odoo import models, fields

class touristic_outing(models.Model):
    _name = 'testmodulo.touristic_outing'
    _description = 'Touristic Outing Model'

    name = fields.Char(string='Outing Name', required=True)
    date = fields.Date(string='Date', required=True)
    description = fields.Text(string='Description')