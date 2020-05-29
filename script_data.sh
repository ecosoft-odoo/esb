pg_user="odoo"
prod_db="ESB"
psql="psql -U $pg_user -d $prod_db"

# Master data
$psql -c "delete from sale_order_template_option";
$psql -c "delete from sale_order_template_line";
$psql -c "delete from stock_valuation_layer";
$psql -c "delete from mrp_bom";
$psql -c "delete from product_mrp_area";
$psql -c "delete from product_supplierinfo";
$psql -c "delete from product_product";
$psql -c "delete from product_template";
$psql -c "delete from product_template_attribute_line";
$psql -c "delete from product_template_attribute_value";
$psql -c "delete from product_variant_combination";
$psql -c "delete from product_attribute";

# External ID
$psql -c "delete from ir_model_data where model = 'product.attribute' and res_id not in (select id from product_attribute)";
$psql -c "delete from ir_model_data where model = 'product.attribute.value' and res_id not in (select id from product_attribute_value)";
$psql -c "delete from ir_model_data where model = 'product.category' and res_id not in (select id from product_category)";
$psql -c "delete from ir_model_data where model = 'product.pricelist' and res_id not in (select id from product_pricelist)";
$psql -c "delete from ir_model_data where model = 'product.pricelist.item' and res_id not in (select id from product_pricelist_item)";
$psql -c "delete from ir_model_data where model = 'product.product' and res_id not in (select id from product_product)";
$psql -c "delete from ir_model_data where model = 'product.supplierinfo' and res_id not in (select id from product_supplierinfo)";
$psql -c "delete from ir_model_data where model = 'product.template' and res_id not in (select id from product_template)";
$psql -c "delete from ir_model_data where model = 'product.template.attribute.exclusion' and res_id not in (select id from product_template_attribute_exclusion)";
$psql -c "delete from ir_model_data where model = 'product.template.attribute.line' and res_id not in (select id from product_template_attribute_line)";
$psql -c "delete from ir_model_data where model = 'product.template.attribute.value' and res_id not in (select id from product_template_attribute_value)";
