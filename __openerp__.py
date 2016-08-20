# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2016-Jakc Labs. (<http://www.jakc-labs.com/>)
#
#################################################################################
{
    'name': 'HR Enhancement',
    'summary': 'Extend MRP Enhancement',
    'version': '1.0',
    'category': 'HR',
    "sequence": 1,
    'description': """
HR Enhancment
=====================================
Features:
----------------
    * Add ability to integrate with HR Device.
    * For Odoo 8
""",
    "author": "Wahyu Hidayat - Jakc Labs.",
    'website': 'http://www.jakc-labs.com',
    'depends': [
        'hr',
        ],
    'data': [
        'views/jakc_hr_device_view.xml',
        'views/jakc_hr_device_menu.xml',
        'views/jakc_hr_attendance_view.xml',
    ],    
    "installable": True,
    "application": True,
    "auto_install": False,        
}