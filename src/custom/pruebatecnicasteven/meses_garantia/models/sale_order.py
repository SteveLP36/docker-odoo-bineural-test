# nombre_del_modulo_garantia/models/sale_order_line.py
from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    guarantee_months = fields.Integer(
        string="Meses de Garantía",
        help="Número de meses de garantía de este producto en la venta.",
        readonly=True, # El valor se copia, no se edita directamente en la línea
        store=True,
    )

    @api.onchange('product_id')
    def _onchange_product_id_set_guarantee_months(self):
        """
        Copia los meses de garantía del producto a la línea de la orden de venta.
        """
        if self.product_id:
            self.guarantee_months = self.product_id.guarantee_months
        else:
            self.guarantee_months = 0