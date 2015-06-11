/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-6-11
 */

$('.register_btn').click(function() {
	var email = $('.register_email').val();
	var name = $('.register_name').val();
	var password = $('.register_password').val();
	var repassword = $('.register_repassword').val();

	if(password !== repassword) {

	}

	var send_data = {
		loginID: email,
		name: name,
		email: email,
		password: password
	};

	var registerCallback = function(data) {
		console.log(data);
	};

	reqData('POST', 'apiTemp/signup', send_data, registerCallback);
});
