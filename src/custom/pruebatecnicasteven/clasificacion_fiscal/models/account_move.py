from odoo import models, fields

class AcconuntMoveInheritFiscal(models.Model):
    _inherit = 'account.move'

    clasificacion_fiscal = fields.Selection([
        ('a', 'Clasificacion A'),
        ('b', 'Clasificacion B'),
        ('c', 'Clasificacion C')
    ], default='a', string='Clasficacion Fical', required=True)


