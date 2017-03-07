from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.utils
from frappe.utils import cstr, flt

@frappe.whitelist()
def item_validate(item,method):
	if item.get("accise_tax_applied")==1:
		if item.get("accise_tax_weight")==0 or item.get("accise_tax_value")==0:
			frappe.throw("Accise Tax weight cant be blank")

def sales_order_accise_value(sales_order,method):
	tax =0
	for d in sales_order.get("items"):
		item = frappe.db.get_values("Item",{"name":d.item_code},["accise_tax_applied","accise_tax_value","accise_tax_weight"],as_dict=True)
		if item.accise_tax_applied==1:
			tax+=(flt(item.accise_tax_value)*flt(item.accise_tax_weight)*flt(d.qty))
	if tax > 0:
		company = frappe.db.get_values("Company",{"name":sales_order.get("company")},["accise_tax_account","accise_tax_cost_center"],as_dict=True)
		found =0
		for td in sales_order.get("taxes"):
			if td.account_head ==company.accise_tax_account and td.cost_center == company.accise_tax_cost_center :
				found=1
				if td.tax_amount!=tax:
					td.tax_amount=tax
		if found==0:
			#sales_order.set("taxes", [])
			new_tax = sales_order.append("taxes",{})
			new_tax.charge_type = "Actual"
			new_tax.account_head=company.accise_tax_account
			new_tax.cost_center = company.accise_tax_cost_center
			new_tax.description = "Accise Tax"
			new_tax.tax_amount=tax