/** 
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-18 11:29:25
 */

function updateBinding() {
	$('.update_btn').click(function() {
		var email = $('.update_email').val(),
			name = $('.update_name').val(),
			password = $('.update_password').val();

		if (checkEmpty(email)) {
			show_dialog_box('提示', '邮件不能为空');
			return;
		}
		if (checkEmpty(name)) {
			show_dialog_box('提示', '昵称不能为空');
			return;
		}
		if (checkEmpty(password)) {
			show_dialog_box('提示', '密码不能为空');
			return;
		}
		if (!checkEmpty(password) && password.length < 6) {
			show_dialog_box('提示', '密码长度不能少于6位');
			return;
		}

		var send_data = {
			email: email,
			name: name,
			password: password
		};

		var updateCallback = function(data) {
			if (data.result) {
				show_dialog_box('提示', '<p class="success_tips">更新成功,请重新登陆</p>');
				var logoutCallback = function(data) {
					if (data.result) {
						redirect(NAV_TIME, '/');
					}
				};

				reqData('POST', '/apiTemp/logout', {}, logoutCallback);
			} else {
				show_dialog_box('提示', '<p class="error_tips">更新失败</p>');
			}
		};

		reqData('POST', '/apiTemp/update', send_data, updateCallback);
	});
}

document.body.onload = function() {
	updateBinding();
};
