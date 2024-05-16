from odoo import models, fields

class event(models.Model):
    _name = 'testmodulo.event'
    _description = 'Eventos'

    name = fields.Char(string='Nombre del evento', required=True)
    start_datetime = fields.Datetime(string='Inicio de evento ', required=True)
    end_datetime = fields.Datetime(string='Final de evento', required=True)
    
    # Servicios con hora de inicio y fin
    spa_service_start = fields.Datetime(string='Inicio de spa')
    spa_service_end = fields.Datetime(string='Cierre de spa')
    
    pool_service_start = fields.Datetime(string='Inicio de piscina')
    pool_service_end = fields.Datetime(string='Cierre de piscina')
    
    breakfast_start = fields.Datetime(string='Inicio de desayuno')
    breakfast_end = fields.Datetime(string='Cierre de desayuno')
    
    lunch_start = fields.Datetime(string='Inicio de comida')
    lunch_end = fields.Datetime(string='Cierre de comida')
    
    dinner_start = fields.Datetime(string='Inicio de cena')
    dinner_end = fields.Datetime(string='Cierre de cena')
    
    night_dj_start = fields.Datetime(string='Inicio de DJ')
    night_dj_end = fields.Datetime(string='Cierre de DJ')

