# -*- coding: utf-8 -*-

import base64
from odoo.http import Controller, request, route

class DashboardBackground(Controller):

    @route(['/dashboard'], type='http', auth="public")
    def dashboard(self, **post):
        user = request.env.user
        company = user.company_id
        if company.bg_image:
            image = base64.b64decode(company.bg_image)
        else:
            return

        return request.make_response(
            image, [('Content-Type', 'image/jpeg')])  # or 'image/jpeg' based on the image type
