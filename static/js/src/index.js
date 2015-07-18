/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-18 11:23:06
 */

var SUBSCRIBE = [];

function loadCatalog(sub) {
	var loadCallback = function(data) {
		data.data.map(function(obj) {
			obj.list.map(function(catalog) {
				appendCatalog(obj.source, catalog, sub);
			});
		});
	};

	reqData('POST', '/apiTemp/getNewsCatalog', {}, loadCallback);
}

function appendCatalog(source, catalog, sub) {
	//创建元素
	var tr = document.createElement('tr');
	var td_s = document.createElement('td');
	var td_c = document.createElement('td');
	var td_b = document.createElement('td');
	var sub_btn = document.createElement('button');

	var isSubscribe = isContain(sub, catalog);

	td_s.innerText = source;
	td_c.innerHTML = "<span class='catalog_link' catalog=" + catalog + ">" + catalog + "</span>";
	sub_btn.innerText = isSubscribe ? '退订' : '订阅';
	sub_btn.className = isSubscribe ? 'btn btn-embossed btn-primary subscribe_btn unsubscribe_btn' :
		'btn btn-embossed btn-primary subscribe_btn';
	$(sub_btn).attr('catalog', catalog);

	td_b.appendChild(sub_btn);
	tr.appendChild(td_s);
	tr.appendChild(td_c);
	tr.appendChild(td_b);
	$('.catalog_table').append($(tr));

	eventBinding(sub);
}

function eventBinding(sub) {
	//订阅退订事件绑定
	$('.subscribe_btn').unbind().click(function() {
		var self = $(this);
		var targetCatalog = $(this).attr('catalog');
		//订阅
		if ($(this).text() == '订阅') {
			sub.push(targetCatalog);

			var handleSubscribe = function(data) {
				if (data.result) {
					self.text('退订');
					self.toggleClass('unsubscribe_btn');
					show_dialog_box('提示', '订阅成功');
				} else {
					console.log('订阅失败');
					sub.pop();
				}
			};

			reqData('POST', '/apiTemp/update', {
				subscribe: sub
			}, handleSubscribe);
			//取消订阅
		} else if ($(this).text() == '退订') {
			remove(sub, targetCatalog);

			var handleUnsubscribe = function(data) {
				if (data.result) {
					self.text('订阅');
					self.toggleClass('unsubscribe_btn');
					show_dialog_box('提示', '退订成功');
				} else {
					console.log('退订失败');
					sub.push(targetCatalog);
				}
			};

			reqData('POST', '/apiTemp/update', {
				subscribe: sub
			}, handleUnsubscribe);
		}
	});

	$('.catalog_link').unbind().click(function() {
		window.location = '/news?catalog=' + $(this).attr('catalog');
	});
}

window.onload = function() {
	getSubscribeList(SUBSCRIBE, loadCatalog);
};
