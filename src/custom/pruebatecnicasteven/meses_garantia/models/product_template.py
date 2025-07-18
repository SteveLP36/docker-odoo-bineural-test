from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    guarantee_months = fields.Integer(
        string='Meses de Garantía',
        help='Número de meses de garantía para el producto.',
        default=0
    )

    @api.constrains('guarantee_months')
    def _check_guarantee_months(self):
        for record in self:
            if record.guarantee_months < 0:
                raise ValidationError('El número de meses de garantía no puede ser negativo.')

class ProductProduct(models.Model):
    _inherit = 'product.product'

    guarantee_months = fields.Integer(
        string='Meses de Garantía',
        related='product_tmpl_id.guarantee_months',
        help='Número de meses de garantía para la variante del producto.',
        store=True
    )

    @api.constrains('guarantee_months')
    def _check_guarantee_months(self):
        for record in self:
            if record.guarantee_months < 0:
                raise ValidationError('El número de meses de garantía no puede ser negativo.')