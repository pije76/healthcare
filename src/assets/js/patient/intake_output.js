var t = $('#t_add_row').DataTable(
{
	"order": [[ 0, "desc" ], [ 1, "asc" ]],
	rowGroup:
	{
		dataSrc: [0],
		startRender: null,
//			startRender: function(rows, group)
//			{
//				return group +' ('+rows.count()+' rows)';
//			},
		endRender: function(rows, group)
		{
			var oralSum = rows
				.data()
				.pluck(3)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			var parenteralSum = rows
				.data()
				.pluck(5)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			var otherintakeSum = rows
				.data()
				.pluck(7)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			var cumSum = rows
				.data()
				.pluck(10)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			var gastricSum = rows
				.data()
				.pluck(11)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			var otheroutputSum = rows
				.data()
				.pluck(13)
				.reduce(function (a, b)
				{
					return a + b*1;
				}, 0);

			return $('<tr/>')
				.append('<td colspan="3">12-HOUR INTAKE: </td>')
				.append('<td>'+ oralSum.toFixed(0) +'</td>')
				.append('<td/>')
				.append('<td>'+ parenteralSum.toFixed(0) +'</td>')
				.append('<td/>')
				.append('<td>'+ otherintakeSum.toFixed(0) +'</td>')
				.append('<td colspan="2">OUTPUT: </td>')
				.append('<td>'+ cumSum.toFixed(0) +'</td>')
				.append('<td>'+ gastricSum.toFixed(0) +'</td>')
				.append('<td/>')
				.append('<td>'+ otheroutputSum.toFixed(0) +'</td>')
				.append('<td/>');
		},
	},
	columnDefs: [
	{
		"searchable": false, "targets": 14,
	}]
});
