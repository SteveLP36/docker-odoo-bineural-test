from odoo import models, fields

class AcconuntMoveInherit(models.Model):
    _inherit = 'acconunt.move'


    clasficacion_fical = fields.Selection([
        ('a', 'Clasificacion A'),
        ('b', 'Clasificacion B'),
        ('c', 'Clasificacion C')
    ], defult='a', string='Clasficacion Fical', required=True)

