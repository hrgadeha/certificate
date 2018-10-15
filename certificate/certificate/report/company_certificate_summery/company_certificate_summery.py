# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, getdate, now

def execute(filters=None):
	conditions, filters = get_conditions(filters)
	columns = get_column()
	data = get_data(conditions,filters)
	return columns,data
	
	
def get_column():
	return [_("Company")+":Link/Company:250",
		_("Company Certificate")+":Data:710",
		_("Com-CER-Expiry date")+":Date:100",
	]
	
def get_data(conditions,filters):
	certificate = frappe.db.sql(""" select o1.name, o2.certificate, o2.expiry_date from `tabCompany` o1, `tabCompany Certificate` o2 where (o1.name = o2.parent) %s;"""%conditions, filters, as_list=1)
	return certificate

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"): conditions += " and o2.expiry_date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and o2.expiry_date <= %(to_date)s"
	if filters.get("company"): conditions += "and o1.name = %(company)s"

	return conditions, filters
