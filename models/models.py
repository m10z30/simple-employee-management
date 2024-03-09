# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee.model'

    # general info


    name = fields.Char(string="Employee Name")
    birthdate = fields.Date(string='Birth Date')
    
    # employement info
    position = fields.Char(string="Position")
    department = fields.Many2one('department.model', required=False)
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


    @api.model
    def create_initial_employee(self):
        """
        Create an initial employee record when the module is installed.
        This method should be called using post_init_hook.
        """
        # Check if the initial employee record already exists
        existing_employee = self.env['employee.model'].search([], limit=1)
        if not existing_employee:
            # Create the initial employee record
            self.create({
                'name': 'Initial Employee',
                'position': 'Manager',
                'status': 'fulltime',
                'salary': 50000,  # Set the initial salary value
                'manager': 'John Doe',
                'employment_date': fields.Date.today(),  # Set the employment date to today
                'email': 'initial.employee@example.com',
                'phone': '123456789',
                'bank_account_info': '0123456789',
                'country': 'Country',
                'city': 'City',
                'address': 'Address',
                'medical_conditions': 'None',
                'allergies': 'None',
            })

    @api.model
    def post_init_hook(cls):
        """
        Hook method called after the module is installed.
        """
        cls.create_initial_employee()




class Department(models.Model):
    _name = "department.model"
    _description = "department model"

    name = fields.Char(string="Department Name")
    department_head = fields.Many2one('employee.model', string='Department Head', default=lambda self: self.env['employee.model'].search([], limit=1))



    