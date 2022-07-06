# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class real_estate_management(models.Model):
    _name = "real.estate.management"
    _description = "real estate plans"
    _order = "sequence"

    name = fields.Char('Estate Name', required=True)
    number_of_months = fields.Integer('# Months', required=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)


'''    _sql_constraints = [
        ('check_number_of_months', 'CHECK(number_of_months >= 0)',
         'The number of month can\'t be negative.'),
    ]
'''
