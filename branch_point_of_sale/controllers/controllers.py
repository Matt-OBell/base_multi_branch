# -*- coding: utf-8 -*-
from odoo import http

# class PointOfSale(http.Controller):
#     @http.route('/point_of_sale/point_of_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/point_of_sale/point_of_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('point_of_sale.listing', {
#             'root': '/point_of_sale/point_of_sale',
#             'objects': http.request.env['point_of_sale.point_of_sale'].search([]),
#         })

#     @http.route('/point_of_sale/point_of_sale/objects/<model("point_of_sale.point_of_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('point_of_sale.object', {
#             'object': obj
#         })