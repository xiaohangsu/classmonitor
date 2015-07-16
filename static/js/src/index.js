/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-16 08:51:02
 */

var SUBSCRIBE = [];

function loadCatalog() {
	console.log()
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

	var isSubscribe = isContain(SUBSCRIBE, catalog);

	td_s.innerText = source;
	td_c.innerText = catalog;
	sub_btn.innerText = isSubscribe ? '退订' : '订阅';
	sub_btn.className = isSubscribe ? 'btn btn-embossed btn-primary subscribe_btn unsubscribe_btn' : 
																		'btn btn-embossed btn-primary subscribe_btn';

	td_b.appendChild(sub_btn);
	tr.appendChild(td_s);
	tr.appendChild(td_c);
	tr.appendChild(td_b);

	$('.catalog_table').append($(tr));
	$('.subscribe_btn').unbind().click(function() {
		var self = $(this);
		//订阅
		if ($(this).text() == '订阅') {
			show_dialog_box('提示', '订阅成功');

			self.text('退订');
			self.toggleClass('unsubscribe_btn');

			//取消订阅
		} else if ($(this).text() == '退订') {
			show_dialog_box('提示', '退订成功');

			self.text('订阅');
			self.toggleClass('unsubscribe_btn');
		}
	});
}

window.onload = function() {
	var getSubscribe = function(data) {
		if(data) {
			SUBSCRIBE = data.user.subscribe;
			loadCatalog();
			console.log(SUBSCRIBE);
		} else {
			console.log('获取订阅列表失败');
		}
	};
	
	reqData('POST', '/apiTemp/get', {}, getSubscribe);
};
