{
    'name': 'To Do List',
    'version': '1.0',
    'description': '',
    'summary': 'Internal to do list management ',
    'author': 'Natnicha U.',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Productivity',
    'depends': 'base_model',
    'data': [
        'views/todo_views.xml',
        'security/ir.model.access.csv',
        'data/tag_data.xml'
    ],
    'auto_install': True,
    'application': True,
}