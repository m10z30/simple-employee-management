# -*- coding: utf-8 -*-
# from odoo import http


# class Employee-managment(http.Controller):
#     @http.route('/employee-managment/employee-managment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee-managment/employee-managment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee-managment.listing', {
#             'root': '/employee-managment/employee-managment',
#             'objects': http.request.env['employee-managment.employee-managment'].search([]),
#         })

#     @http.route('/employee-managment/employee-managment/objects/<model("employee-managment.employee-managment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee-managment.object', {
#             'object': obj
#         })

