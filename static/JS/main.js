$(document).ready(function () {
    // EVENT ON-CLICK
    // this is a jquery function. 

    var max_fields      = 10; //maximum input boxes allowed

	$("#add_ingredients").click(function () {
        e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});