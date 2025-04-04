from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_rg_5329_iva_3 = fields.Boolean(
        string="Percepción RG 5329 IVA 3%",
        help="Marcar si el producto está alcanzado por la percepción RG 5329."
    )