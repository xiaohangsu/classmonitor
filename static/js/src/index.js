/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-6-11
 */

function loadCatalog() {
	var loadCallback = function(data) {
		data.data.map(function(obj) {
			obj.list.map(function(catalog) {
				appendCatalog(obj.source, catalog);
			});
		});
	};

	reqData('POST', '/apiTemp/getNewsCatalog', {}, loadCallback);
}

function appendCatalog(source, catalog) {
	var tr = document.createElement('tr');
	var td_s = document.createElement('td');
	var td_c = document.createElement('td');
	var td_b = document.createElement('td');
	var sub_btn = document.createElement('button');

	td_s.innerText = source;
	td_c.innerText = catalog;
	sub_btn.innerText = '订阅';
	sub_btn.className = 'btn btn-embossed btn-primary subscribe_btn';

	td_b.appendChild(sub_btn);
	tr.appendChild(td_s);
	tr.appendChild(td_c);
	tr.appendChild(td_b);

	$('.catalog_table').append($(tr));
	$('.subscribe_btn').unbind().click(function() {
		var self = $(this);
		//订阅
		if ($(this).text() == '订阅') {
			console.log(1);
			show_dialog_box('提示', '订阅成功');

			self.text('退订');
			self.css({
				'background-color': 'grey'
			});

			//取消订阅
		} else if ($(this).text() == '退订') {
			console.log(2);
			show_dialog_box('提示', '退订成功');

			self.text('订阅');
			self.css({
				'background-color': '#1abc9c'
			});
		}
	});
}

function logoutBinding() {
	$('.logout_li').click(function() {
		var logoutCallback = function(data) {
			if(data.result) {
				show_dialog_box('提示', '<p class="success_tips">登出成功,跳转中...</p');
				redirect(NAV_TIME, '/');
			}
		};

		reqData('POST', '/apiTemp/logout', {}, logoutCallback);
	});
}

function avatarBinding() {
	$('.user_avatar').on('mouseover', function() {
		
	});

	$('.user_avatar').on('mouseout', function() {

	});
}

window.onload = function() {
	loadCatalog();
	logoutBinding();
	avatarBinding();
};
