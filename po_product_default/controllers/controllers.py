# -*- coding: utf-8 -*-
from odoo import http

# class PoProductDefault(http.Controller):
#     @http.route('/po_product_default/po_product_default/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_product_default/po_product_default/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_product_default.listing', {
#             'root': '/po_product_default/po_product_default',
#             'objects': http.request.env['po_product_default.po_product_default'].search([]),
#         })

#     @http.route('/po_product_default/po_product_default/objects/<model("po_product_default.po_product_default"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_product_default.object', {
#             'object': obj
#         })