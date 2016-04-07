#-*- coding:utf-8 -*-
{
    'name': 'OpenERP Custom widgets example',
    'version': '0.1',
    'summary': 'Custom widget example',
    'category': 'Tools',
    'author': 'KIT-XXI',
    'website': "http://kit-xxi.com.ua/",
    'description':
        """
OpenERP Custom widgets Example
==============================

        """,
    'depends': [
        'hr_contract',
        'colored_field_widget',
    ],
    'data': [
        "views/example_view.xml"
    ]
}
