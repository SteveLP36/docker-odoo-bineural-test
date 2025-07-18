{
    'name': 'Garantía en Productos y Ventas',
    'version': '1.0',
    'summary': 'Añade un campo de meses de garantía a productos y lo propaga a las líneas de venta.',
    'description': """
        Este módulo introduce un campo 'Meses de Garantía' en los productos,
        que se transfiere automáticamente a las líneas de las órdenes de venta.
        También facilita la inclusión de esta información en los reportes de inventario.
    """,
    'author': 'Steven Loiaza Paredes',
    'category': 'Sales/Inventory',
    'depends': ['product', 'sale_management', 'stock'],
    'data': [
        'views/product_views.xml',
        'views/sale_order_views.xml',
        # 'reports/stock_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}