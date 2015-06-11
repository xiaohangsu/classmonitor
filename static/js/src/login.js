/** 
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-6-11
 */

$('.login_btn').click(function() {
	var email = $('.login_email').val();
	var password = $('.login_password').val();
	var send_data = {
		email: email,
		password: password
	};

	var loginCallback = function(data) {
		console.log(data);
	};

	reqData('POST', '/apiTemp/login', send_data, loginCallback);
});
