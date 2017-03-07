# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accisetax"
app_title = "Accise Tax"
app_publisher = "Bobby"
app_description = "To Add Accise Tax on Item"
app_icon = "octicon octicon-file-text"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accisetax/css/accisetax.css"
# app_include_js = "/assets/accisetax/js/accisetax.js"

# include js, css files in header of web template
# web_include_css = "/assets/accisetax/css/accisetax.css"
# web_include_js = "/assets/accisetax/js/accisetax.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "accisetax.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accisetax.install.before_install"
# after_install = "accisetax.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accisetax.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
fixtures = ["Custom Field"]
doc_events = {
	"Sales Order": {
		"validate": "accisetax.accise_tax.custom_method.sales_order_accise_value"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accisetax.tasks.all"
# 	],
# 	"daily": [
# 		"accisetax.tasks.daily"
# 	],
# 	"hourly": [
# 		"accisetax.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accisetax.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accisetax.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accisetax.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accisetax.event.get_events"
# }

