# -*- coding: utf-8 -*-
# from odoo import http


# class Testmodulo(http.Controller):
#     @http.route('/testmodulo/testmodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testmodulo/testmodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('testmodulo.listing', {
#             'root': '/testmodulo/testmodulo',
#             'objects': http.request.env['testmodulo.testmodulo'].search([]),
#         })

#     @http.route('/testmodulo/testmodulo/objects/<model("testmodulo.testmodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testmodulo.object', {
#             'object': obj
#         })
