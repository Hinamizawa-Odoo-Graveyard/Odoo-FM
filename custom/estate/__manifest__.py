# -*- coding: utf-8 -*-
{
    'name': "Real Estate",  # Module title
    'summary': "Manage Estate easily",  # Module subtitle phrase
    'description': """
Manage Estates
==============
Description related to Real Estate.
    """,  # Supports reStructuredText(RST) format
    'author': "Hinamizawa",
    'website': "alejandroatacho.github.io",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv'
    ],
}
# This data files will be loaded at the installation (commented because file is not added in this example)

# This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
# 'demo': [
#     'demo.xml'
# ],}
