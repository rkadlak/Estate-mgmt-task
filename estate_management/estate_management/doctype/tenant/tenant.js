// Copyright (c) 2022, rohit and contributors
// For license information, please see license.txt
//
frappe.ui.form.on('Tenant' ,{

	refresh:function(frm){
		frm.set_query('room', function() {
			return {
				"filters": [["awailable","=","1"],
			
			]
			
			}
		})
	}
});
	
		

