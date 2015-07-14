/** 
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-6-11
 */

$('.login_btn').click(function() {
	var email = $('.login_email').val();
	var password = $('.login_password').val();

	if(checkEmpty(email)) {
		show_dialog_box('提示', '邮件不能为空');
		return;
	}
	if(checkEmpty(password)) {
		show_dialog_box('提示', '密码不能为空');
		return;
	}

	var send_data = {
		loginID: email,
		email: email,
		password: password
	};

	var loginCallback = function(data) {
		if(data.result) {
			reqData('POST', '/apiTemp/get', {}, function(data) {
				window.USER = data.user;
				console.log(window.USER);
				if(data.result) {
					show_dialog_box('提示', '<p class="success_tips">登陆成功,自动跳转中...</p>');
					redirect(NAV_TIME, '/');
				}
			});
		} else {
			show_dialog_box('提示', '<p class="error_tips">登陆失败:邮箱或密码错误</p>');
		}
	};

	reqData('POST', '/apiTemp/login', send_data, loginCallback);
});

$('body').on('keydown', function(e) {
	if(e.keyCode == 13 && $('.bg_mask').css('display') == 'none') {
		$('.login_btn').click();
	}
}); 
