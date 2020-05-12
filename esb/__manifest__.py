# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "ESB :: Custom addons",
    "summary": "Custom addons for only esb project",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "author": "Ecosoft Co., Ltd",
    "license": "AGPL-3",
    "website": "https://ecosoft.co.th",
<<<<<<< HEAD
    "depends": ["hr", "mrp", "purchase_order_secondary_unit", "stock_secondary_unit"],
=======
    "depends": ["hr", "mrp", "purchase", "stock"],
>>>>>>> [ADD] ESB Picking List for printout
    "data": [
        "mrp/views/mrp_production_views.xml",
        "product/views/product_views.xml",
        "purchase/views/purchase_views.xml",
<<<<<<< HEAD
        "purchase_form/datas/paper_format.xml",
        "purchase_form/datas/report_data.xml",
        "purchase_form/reports/purchase_form.xml",
=======
        # Picking List
        "picking_list/security/ir.model.access.csv",
        "picking_list/views/picking_list_views.xml",
>>>>>>> [ADD] ESB Picking List for printout
    ],
    "installable": True,
}
