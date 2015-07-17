/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-12 22:13:51
 */

$('.register_btn').click(function() {
	var email = $('.register_email').val();
	var name = $('.register_name').val();
	var password = $('.register_password').val();
	var repassword = $('.register_repassword').val();

	if(checkEmpty(email)) {
		show_dialog_box('提示', '邮件不能为空');
		return;
	}
	if(checkEmpty(name)) {
		show_dialog_box('提示', '昵称不能为空');
		return;
	}
	if(checkEmpty(password)) {
		show_dialog_box('提示', '密码不能为空');
		return;
	}
	if(password !== repassword) {
		show_dialog_box('提示', '两次输入的密码不一致');
		return;
	}

	var send_data = {
		loginID: email,
		name: name,
		email: email,
		password: password
	};

	var registerCallback = function(data) {
		if(data.result) {
			show_dialog_box('提示', '<p class="success_tips">注册成功,自动跳转中...</p>');
			redirect(NAV_TIME, '/login');
		} else {
			show_dialog_box('提示', '<p class="error_tips">注册失败:该用户已存在</p>');
		}
	};

	reqData('POST', 'apiTemp/signup', send_data, registerCallback);
});

$('body').on('keydown', function(e) {
	if(e.keyCode == 13 && $('.bg_mask').css('display') == 'none') {
		console.log('register_btn clicked');
		$('.register_btn').click();
	}
});
