# -*- coding: utf-8 -*-
# from odoo import http


# class StockExtension(http.Controller):
#     @http.route('/stock_extension/stock_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_extension/stock_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_extension.listing', {
#             'root': '/stock_extension/stock_extension',
#             'objects': http.request.env['stock_extension.stock_extension'].search([]),
#         })

#     @http.route('/stock_extension/stock_extension/objects/<model("stock_extension.stock_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_extension.object', {
#             'object': obj
#         })
