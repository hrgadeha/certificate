// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Company Certificate Summery"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company"
		}
	]
}
