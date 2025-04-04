{
    'name': 'Percepción RG 5329',
    'version': '1.0',
    'author': 'Klap / FwCorp',
    'website': 'https://fwcorp.com.ar',
    'category': 'Accounting',
    'summary': 'Aplica percepción RG 5329 IVA 3% a productos alcanzados',
    'description': """
    Este módulo agrega la percepción RG 5329 del 3% a productos específicos,
    únicamente cuando el monto total de los productos alcanzados supera los $100.000.
    """,
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'account',
        'sale',
    ],
    'data': [
        'views/product_view.xml',     # Vista donde aparece el checkbox en el producto
        'views/product_data.xml',     # Producto para aplicar percepción
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
