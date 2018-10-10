# -*- coding: utf-8 -*-
# Copyright (c) 2018, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Certificate(Document):
	pass

def emp_cert_mail():
	content = "<h4>Hello, </h4><p>Following Employee Certificate will be expiry soon. Please make a note for that.</p><table class='table table-bordered'><tr><th>Employee Certificate</th><th>Expiry Date</th></tr>"
	cert_list = frappe.db.sql("""select certificate, expiry_date, user_email 
from `tabEmployee Certificate` 
where alert_date = CURDATE() or CURDATE() = DATE_ADD(alert_date, INTERVAL repeat_alert_after DAY);""")
	for cert_obj in cert_list:
		cert = cert_obj[0]
		expiry_date = str(cert_obj[1].strftime('%d/%m/%Y'))
		user = cert_obj[2]
		content = content + "<tr><td>"+cert+"</td><td>"+expiry_date+"</td></tr>"         
	content = content + "</table>"
	recipient = user
	frappe.sendmail(recipients=[recipient],
	sender="adrianobucci99@gmail.com",
	subject="Employee Certificate To Be Expire", content=content)


def company_cert_mail():
	content = "<h4>Hello, </h4><p>Following Company Certificate will be expiry soon. Please make a note for that.</p><table class='table table-bordered'><tr><th>Company Certificate</th><th>Expiry Date</th></tr>"
	cert_list = frappe.db.sql("""select certificate, expiry_date, user_email 
from `tabCompany Certificate` 
where alert_date = CURDATE() or CURDATE() = DATE_ADD(alert_date, INTERVAL repeat_alert_after DAY);""")
	for cert_obj in cert_list:
		cert = cert_obj[0]
		expiry_date = str(cert_obj[1].strftime('%d/%m/%Y'))
		user = cert_obj[2]
		content = content + "<tr><td>"+cert+"</td><td>"+expiry_date+"</td></tr>"         
	content = content + "</table>"
	recipient = user
	frappe.sendmail(recipients=[recipient],
	sender="adrianobucci99@gmail.com",
	subject="Company Certificate To Be Expire", content=content)
