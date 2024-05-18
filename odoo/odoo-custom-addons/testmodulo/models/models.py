from odoo import models, fields

class cleaning_schedule(models.Model):
    _name = 'testmodulo.cleaning_schedule'
    _description = 'Horario de limpieza'

    name = fields.Char(string='Nombre de limpieza', required=True)
    date = fields.Date(string='Fecha', required=True)
    description = fields.Text(string='Descripción')

class event(models.Model):
    _name = 'testmodulo.event'
    _description = 'Eventos'

    name = fields.Char(string='Nombre del evento', required=True)
    start_datetime = fields.Datetime(string='Inicio del evento', required=True)
    end_datetime = fields.Datetime(string='Fin del evento', required=True)
    description = fields.Text(string='Descripción')
    
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

class touristic_outing(models.Model):
    _name = 'testmodulo.touristic_outing'
    _description = 'Salidas turísticas'

    name = fields.Char(string='Nombre de la ruta', required=True)
    start_date = fields.Date(string='Fecha de inicio', required=True)
    end_date = fields.Date(string='Fecha de finalización', required=True)
    description = fields.Text(string='Descripción')