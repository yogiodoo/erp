# -*- coding: utf-8 -*-
# from odoo import http


# class UaeApproval(http.Controller):
#     @http.route('/uae_approval/uae_approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uae_approval/uae_approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uae_approval.listing', {
#             'root': '/uae_approval/uae_approval',
#             'objects': http.request.env['uae_approval.uae_approval'].search([]),
#         })

#     @http.route('/uae_approval/uae_approval/objects/<model("uae_approval.uae_approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uae_approval.object', {
#             'object': obj
#         })
