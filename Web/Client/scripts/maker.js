
// This just displays the first parameter passed to it
// in an alert.
function show(json) {
	alert(json);
}

function run() {
	$.getJSON(
	"/maker/hello.php", // The server URL 
	{ id: 567 }, // Data you want to pass to the server.
	show // The function to call on completion.
	);
}
