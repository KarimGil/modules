# -*- coding: utf-8 -*-
# from odoo import http


# class CarWorkShop(http.Controller):
#     @http.route('/car_work_shop/car_work_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_work_shop/car_work_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_work_shop.listing', {
#             'root': '/car_work_shop/car_work_shop',
#             'objects': http.request.env['car_work_shop.car_work_shop'].search([]),
#         })

#     @http.route('/car_work_shop/car_work_shop/objects/<model("car_work_shop.car_work_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_work_shop.object', {
#             'object': obj
#         })
