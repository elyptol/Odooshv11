
{
    "name" : "Amazon e-commerce",
    "version" : "1.1",
    "depends" : ["base",'product','sale','sale_stock','stock', 'product_images_olbs', 'sale_shop','delivery','purchase',],
    "author" : "Globalteckz",
    "description": """Amazon E-commerce management""",
    "website" : "http://www.globalteckz.com/",
    "category" : "E-Commerce",
    "data" : [
                'security/amazon_security.xml',
                'security/ir.model.access.csv',
                'data/amazon_schedular_data.xml',
                'data/product_data.xml',
                'views/log_sequence_view.xml',
                'wizard/create_amazon_shop.xml',
                'wizard/amazon_product_lookup.xml',
                'wizard/upload_amazon_products.xml',
                'wizard/amazon_connector_wizard.xml',
                'wizard/cancel_amazon_order.xml',
                'wizard/update_price.xml',
                'wizard/add_listing_products_view.xml',
                'wizard/update_order_status_on_amazon.xml',
                'views/amazon_view.xml',
                'views/account_view.xml',
                'views/sale_view.xml',
                'views/product_view.xml',
                'views/amazon_inventory_view.xml',
                'views/partner_view.xml',
                'views/manage_amazon_listing_view.xml',
                'views/sale_shop.xml',
                'views/product_images_view.xml',
                'views/import_order_workflow.xml',
                'views/amazon_log_view.xml',
                'views/amazon_dashboard.xml',
                'views/sale_analysis_view.xml',
#                 'views/amazon_category_view.xml',
                'views/amazon_menu.xml',
                
                
    ],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

