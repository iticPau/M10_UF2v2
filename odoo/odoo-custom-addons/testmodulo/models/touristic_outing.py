from odoo import models, fields

class touristic_outing(models.Model):
    _name = 'testmodulo.touristic_outing'
    _description = 'Rutas turisticas'

    name = fields.Char(string='Nombre de la ruta', required=True)
    start_date = fields.Date(string='Fecha de inicio', required=True)
    end_date = fields.Date(string='Fecha de finalizacion', required=True)
    description = fields.Text(string='Descripcion')
