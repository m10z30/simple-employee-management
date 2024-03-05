# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee.model'

    # general info


    name = fields.Char(string="Employee Name")
    birthdate = fields.Date(string='Birth Date')
    
    # employement info
    position = fields.Char(string="Position")
    department = fields.Char(string="Department")
    status = fields.Selection([ ('fulltime', 'Full-Time'),('parttime', 'Part-Time'),('temporary', 'Temporary')],'status', default='fulltime')
    salary = fields.Integer(string="Salary")
    manager = fields.Char(string="Manager/Employer Name")
    employment_date = fields.Date(string="Employement Date")
    
    # contact info
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    bank_account_info = fields.Char(string="Bank Account Info")
    
    # Address
    country = fields.Char(string="Country")
    city    = fields.Char(string="City")
    address = fields.Char(string="Address")

    # Health and safty info
    medical_conditions = fields.Char(string="Medical conditions")
    allergies          = fields.Char(string='allergies')

    
    