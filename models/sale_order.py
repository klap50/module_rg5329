from odoo import models, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_rg5329_product(self):
        product = self.env.ref('modulo_rg5329.producto_rg_5329', raise_if_not_found=False)
        if not product:
            raise UserError("Debe existir un producto con el XML ID 'modulo_rg5329.producto_rg_5329'.")
        return product

    def aplicar_percepcion_rg5329(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue

            total_afectado = sum(
                line.price_subtotal
                for line in order.order_line
                if line.product_id.product_tmpl_id.x_studio_rg_5329_iva_3
            )

            ya_aplicado = order.order_line.filtered(
                lambda l: l.product_id == self._get_rg5329_product()
            )

            if total_afectado > 100000 and not ya_aplicado:
                order.order_line.create({
                    'order_id': order.id,
                    'product_id': self._get_rg5329_product().id,
                    'product_uom_qty': 1,
                    'price_unit': total_afectado * 0.03,
                    'name': 'Percepción RG 5329 IVA 3%',
                })