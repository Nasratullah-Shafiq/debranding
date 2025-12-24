# -*- coding: utf-8 -*-
from email.policy import default
from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    private_streets = fields.Char(string='Private Street', tracking=True,
                                  groups="base.group_user")




