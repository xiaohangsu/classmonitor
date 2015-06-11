/**
 * Author   : VenDream
 * Email    : yeshenxue@qq.com
 * UpdateAt : 2015-6-11
 */

function reqData(method, url, data, callback) {
	$.ajax({
		method: method,
		url: url,
		data: JSON.stringify(data),
		dataType: "application/json",
		success: function(data) {
			if(data.result === true)
				callback(data);
			else
				console.log('GET_DATA_FAILED');
		},
		error: function(err) {
			console.log(err);
		}
	});
}
