#-*- coding:utf-8 -*-
{
    'name': 'OpenERP Custom widgets',
    'version': '0.1',
    'summary': 'Some custom widgets',
    'category': 'Tools',
    'description':
        """
OpenERP Custom widgets
=================

A collection of custom widgets:
- Colored ListView field
        """,
    'data': [
        "custom_widget.xml"
    ],
    'qweb':[
         'static/src/xml/template_update.xml'
    ]
}
