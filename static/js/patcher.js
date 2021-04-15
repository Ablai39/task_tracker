$(document).ready(function(){
	var checkboxes = $("input[name='patch']"),
	submitButt = $("input[id='Remove']");
	checkboxes.click(function() {
		$(this).closest("tr").toggleClass('active');
		submitButt.attr("disabled", !checkboxes.is(":checked"));
		});
	$('.datepicker').datepicker();
	var checkboxes = $("input[name='point']");
	checkboxes.click(function() {
		$(this).closest("tr").toggleClass('active');
		});
	$("#Upload, #New, #Detach, #Update").click(function() {
		$('#UploadModal, #SendModal').modal('hide');
		$('#Main_Div').toggleClass('blur');
		$("#Loadpage").show();
	});
	setTimeout(function() {
		$('#message_div').fadeOut('slow');
	}, 5000);
});