from odoo import models, fields

class cleaning_schedule(models.Model):
    _name = 'testmodulo.cleaning_schedule'
    _description = 'Horas de limpieza'

    name = fields.Char(string='Nombre de limpieza', required=True)
    date = fields.Date(string='Fecha', required=True)
    description = fields.Text(string='Descripcion')