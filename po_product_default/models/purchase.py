from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class purchase(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'


    @api.multi
    def fill_products(self):

        # sql = "delete from purchase_order_line where order_id=%s"

        company_id = self.env.user.company_id.id

        partner_id = self.partner_id
        products = self.env['product.product'].search([])

        self.order_line=None

        self.order_line = [(0,0,{
            'product_id': prod.id,
            'name': prod.name,
            'date_planned': fields.Date.context_today(self),
            'product_qty':1,
            'price_unit':prod.standard_price,
            'partner_id': partner_id.id,
            'company_id': company_id,
            'product_uom':1,
        }) for prod in products]






