# __manifest__.py

{
    'name': 'debranding',
    'version': '17.0.0.0.1',
    'category': 'debranding ',
    'summary': 'this will remove the odoo brand from logout option and other section ',
    'sequence': 1,
    'description': """
      this is belongs to all odoo debranding
    """,
    'author': 'Nasrat Nasrati',
    'website': 'https://www.example.com',
    'depends': ['web', 'hr'],
    'data': [
        'views/remove_powered_by_odoo.xml',
        'views/res_config.xml',
        'views/res_company.xml',
        'views/web_login.xml',
        'data/demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'qweb': [
        'static/src/xml/user_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'debranding/static/src/js/extended_user_menu.js',
            'debranding/static/src/js/web_window_title.js',
        ],
    }

}
