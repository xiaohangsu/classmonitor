/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-07-18 11:28:21
 */
var CATALOG = decodeURIComponent(window.location.toString().split('=')[1]);

function loadNews() {
	var loadCallback = function(data) {
		if(data.result) {
			var time_len = data.news.length;
			if(time_len > 0) {
				data.news.map(function(news) {
					appendNews(news);
				});	
			} else {
				showNoneTips();
			}
		} else {
			console.log('获取新闻失败');
		}
	};

	reqData('POST', '/apiTemp/getNewsByCatalog', {newCatalog: CATALOG}, loadCallback);
}

function appendNews(news) {
	//创建元素
	var tr = document.createElement('tr');
	var td_title = document.createElement('td');
	var td_time = document.createElement('td');
	var td_btn = document.createElement('td');
	var read_btn = document.createElement('button');

	td_title.innerText = news.newTitle;
	td_time.innerText = news.newTime.indexOf(':') > 0 ? news.newTime.split(':')[1] : news.newTime;
	read_btn.innerText = '阅读原文';
	td_title.className = 'font_italic';
	read_btn.className = 'btn btn-embossed btn-primary read_btn';
	$(read_btn).attr('url', news.newHref);

	td_btn.appendChild(read_btn);
	tr.appendChild(td_title);
	tr.appendChild(td_time);
	tr.appendChild(td_btn);
	$('.news_table').append($(tr));

	eventBinding();
}

function eventBinding() {
	//绑定事件
	$('.read_btn').unbind().click(function() {
		var sourceURL = $(this).attr('url');
		window.open(sourceURL);
	});
}

function showNoneTips() {
	//创建元素
	var tr = document.createElement('tr');
	var td_title = document.createElement('td');
	var td_time = document.createElement('td');
	var td_btn = document.createElement('td');

	td_title.innerText = '暂无';
	td_time.innerText = '暂无';
	td_btn.innerText = '暂无';

	tr.appendChild(td_title);
	tr.appendChild(td_time);
	tr.appendChild(td_btn);
	$('.news_table').append($(tr));
}

document.body.onload = function() {
	loadNews();
};
