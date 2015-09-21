$( "#addChore" ).dialog({
	autoOpen: false,
	height: 500,
	width: 500,
	modal: true
	});
$( ".name" ).click(function() {
	$( "#addChore" ).dialog( "open" );
});
$("#selectChore").click(function() {
	$(".starcount").append('<img class="star" src="star.png">');
});