/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-12 22:13:37
 */

var FADE_TIME = 200;
var NAV_TIME = 1500;

// $('.dialog_close').bind('click', hide_dialog_box);
$('.dialog_confirm').bind('click', hide_dialog_box);


/**
 * Ajax请求数据
 * @param {string}   异步方法GET或者POST
 * @param {string}   提交的url
 * @param {object}   提交的数据对象
 * @param {function} 回调函数
 * @return {void}
 */
function reqData(method, url, data, callback) {
	$.ajax({
		method: method,
		url: url,
		data: JSON.stringify(data),
		contentType: "application/json",
		success: function(data) {
			callback(data);
		},
		error: function(err) {
			throw new Error(err);
		}
	});
}

/**
 * 检测字符串是否为空字符串
 * @param {string} 检测的字符串
 * @return {bool}  空or非空
 */
function checkEmpty(value) {
	return value === '';
}

/**
 * 显示模态框,可自定义标题和正文
 * @param {string} 模态框标题
 * @param {string} 模态框正文
 * @return {void} 
 */
function show_dialog_box(title, content) {
	$('.bg_mask').fadeIn(FADE_TIME);
	$('.dialog_box').fadeIn(FADE_TIME);

	$('.dialog_title').text(title);
	$('.dialog_body').html(content);

	$('html, body').css({
		'overflow': 'hidden',
		'height': '100%'
	});
}

/**
 * 关闭模态框
 */
function hide_dialog_box() {
	$('.bg_mask').fadeOut(FADE_TIME);
	$('.dialog_box').fadeOut(FADE_TIME);

	$('html, body').css({
		'overflow': 'auto',
		'height': 'auto'
	});
}

/**
 * 指定时间后跳转到指定页面
 * @param {number} 毫秒
 * @param {string} 跳转的url
 */
function redirect(time, url) {
	$('.dialog_confirm').attr('disabled', true);
	setTimeout(function() {
		window.location = url;
	}, time);
}

//绑定模态框的确定按钮会被Enter触发
(function() {
	$('body').on('keydown', function(e) {
		if(e.keyCode == 13 && $('.bg_mask').css('display') == 'block') {
			console.log('confirm_btn clicked');
			$('.dialog_confirm').click();
		}
	});
}());
