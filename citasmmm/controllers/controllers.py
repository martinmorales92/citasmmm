# -*- coding: utf-8 -*-
from odoo import http

# class Citasmmm(http.Controller):
#     @http.route('/citasmmm/citasmmm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasmmm/citasmmm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasmmm.listing', {
#             'root': '/citasmmm/citasmmm',
#             'objects': http.request.env['citasmmm.citasmmm'].search([]),
#         })

#     @http.route('/citasmmm/citasmmm/objects/<model("citasmmm.citasmmm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasmmm.object', {
#             'object': obj
#         })