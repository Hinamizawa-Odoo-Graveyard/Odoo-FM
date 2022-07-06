# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class estate_property(models.Model):
    _name = "estate.model"
    _description = "real estate plans"
    _order = "sequence"

    name = fields.Char('Estate Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char(string="Postcode", required=True)
    date_availability = fields.Date(string="Date Available", required=True)
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", required=True)
    bedrooms = fields.Integer(string="Bedrooms", required=True)
    living_area = fields.Integer(string="Living Area", required=True)
    facades = fields.Integer(string="Facades", required=True)
    garage = fields.Boolean(string="Garage", required=True)
    garden = fields.Boolean(string="Garden", required=True)
    garden_area = fields.Integer(string="Garden Area", required=True)
    garden_orientation = fields.Selection(
        'North, South, East, West', string="Garden Orientation", required=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)


'''    _sql_constraints = [
        ('check_number_of_months', 'CHECK(number_of_months >= 0)',
         'The number of month can\'t be negative.'),
    ]
'''
