from odoo import models, fields

class event(models.Model):
    _name = 'testmodulo.event'
    _description = 'Event Model'

    name = fields.Char(string='Event Name', required=True)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)