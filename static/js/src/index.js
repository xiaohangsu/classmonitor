/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-16 08:51:02
 */

var SUBSCRIBE = [];

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
	//创建元素
	var tr = document.createElement('tr');
	var td_s = document.createElement('td');
	var td_c = document.createElement('td');
	var td_b = document.createElement('td');
	var sub_btn = document.createElement('button');

	var isSubscribe = isContain(SUBSCRIBE, catalog);

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

	eventBinding();
}

function eventBinding() {
	//订阅退订事件绑定
	$('.subscribe_btn').unbind().click(function() {
		var self = $(this);
		var targetCatalog = $(this).attr('catalog');
		//订阅
		if ($(this).text() == '订阅') {
			SUBSCRIBE.push(targetCatalog);
			console.log(SUBSCRIBE);

			var handleSubscribe = function(data) {
				if (data.result) {
					self.text('退订');
					self.toggleClass('unsubscribe_btn');
					show_dialog_box('提示', '订阅成功');
				} else {
					console.log('订阅失败');
					SUBSCRIBE.pop();
				}
			};

			reqData('POST', '/apiTemp/update', {
				subscribe: SUBSCRIBE
			}, handleSubscribe);
			//取消订阅
		} else if ($(this).text() == '退订') {
			remove(SUBSCRIBE, targetCatalog);
			console.log(SUBSCRIBE);

			var handleUnsubscribe = function(data) {
				if (data.result) {
					self.text('订阅');
					self.toggleClass('unsubscribe_btn');
					show_dialog_box('提示', '退订成功');
				} else {
					console.log('退订失败');
					SUBSCRIBE.push(targetCatalog);
				}
			};

			reqData('POST', '/apiTemp/update', {
				subscribe: SUBSCRIBE
			}, handleUnsubscribe);
		}
	});

	$('.catalog_link').unbind().click(function() {
		window.location = '/news?catalog=' + $(this).attr('catalog');
	});
}

function getSubscribeList() {
	var getSubscribe = function(data) {
		if (data) {
			SUBSCRIBE = data.user.subscribe;
			loadCatalog();
		} else {
			console.log('获取订阅列表失败');
		}
	};

	reqData('POST', '/apiTemp/get', {}, getSubscribe);
}

window.onload = function() {
	getSubscribeList();
};
