# -*- coding: utf-8 -*-
{

    'name' : 'Car Workshop',
    'version' : '13.0.0',
    'category' : 'Mechanical',
    'summary' : 'Get new spare parts for your car',
    'author' : 'Karim Gilani',
    'maintainer' : 'Karim Gilani',
    'depends' : ['mail'],
    'demo' : [],
    'data' : [
                'views/car.xml',
                'views/spareparts.xml',
                'security/ir.model.access.csv',
                'data/sequence.xml',
                'report/report.xml',
                'report/vehicle_detail_template.xml',

              ],
    'installable' : True,
    'application' : True,
    'auto_install' : False

}