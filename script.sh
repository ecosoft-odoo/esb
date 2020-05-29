pg_user="odoo"
prod_db="ESB"
psql="psql -U $pg_user -d $prod_db"

# Sales
$psql -c "delete from sale_order";
$psql -c "delete from sale_order_line";

# Purchase
$psql -c "delete from purchase_order";
$psql -c "delete from purchase_order_line";

# MRP
$psql -c "delete from mrp_production";
$psql -c "delete from mrp_unbuild";

# Stock
$psql -c "delete from esb_packing_list_line_detail";
$psql -c "delete from esb_packing_list_line";
$psql -c "delete from esb_packing_list";
$psql -c "delete from stock_inventory";
$psql -c "delete from stock_picking";
$psql -c "delete from stock_move";
$psql -c "delete from stock_scrap";
$psql -c "delete from stock_quant";
$psql -c "delete from stock_production_lot";

# Accounting
$psql -c "delete from account_partial_reconcile";
$psql -c "delete from account_move_line";
$psql -c "delete from account_move";
$psql -c "delete from tax_adjustments_wizard";
$psql -c "delete from withholding_tax_cert";
$psql -c "delete from account_payment";
$psql -c "delete from account_bank_statement";
$psql -c "delete from account_analytic_line";

# Miscellaneous
$psql -c "delete from mail_mail";
$psql -c "delete from mail_message";
