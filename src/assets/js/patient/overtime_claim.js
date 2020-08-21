$(document).ready(function()
{
	var t = $('#t_add_row').DataTable(
	{
		"order": [[ 0, "desc" ]],
		dom: 'Bfrtip',
//		responsive: true,
//		pageLength: 25,
//		lengthChange: false,
		buttons: [
		{
//			'print'
			extend: 'print',
			className: 'btn btn-outline-primary',
//			text: '<i class="fa fa fa-print fa-2x">Print</i>',
			text: '<i style="font-size:24px;" class="fa fa fa-print fa-2x"></i> Print',
			autoPrint: true,
			title: 'Overtime Claim Form',
			init: function (api, node, config)
			{
				$(node).removeClass('dt-button buttons-print')
			},
//			customize: function(win)
//			{
//				$(win.document.body)
//					.css('font-size', '10pt')
//					.prepend(
//						'<img src="http://datatables.net/media/images/logo-fade.png" style="position:absolute; top:0; left:0;" />'
//					);

//				$(win.document.body).find('table')
//					.addClass('compact')
//					.css('font-size', 'inherit');
//			},
		}],

//		"drawCallback": function(settings)
//		{
//			var time_api = this.api();
//			var total = time_api.column(1)
//			.data()
//			.sum();

			//footer
//			$(time_api.column(1)
//			.footer())
//			.html(total);
//		},

		"footerCallback": function(row, data, start, end, display)
		{
			var api = this.api();

			var intVal = function(i)
			{
				return i != null ? moment.duration(i).asSeconds() : 0;
			};

			var total = api.column( 3 ).data()
			.reduce( function (a, b)
			{
				var total = intVal(a) + intVal(b);
				var totalFormatted = [
					parseInt(total / 60 / 60),
					parseInt(total / 60 % 60),
					parseInt(total % 60)
				].join(":").replace(/\b(\d)\b/g, "0$1");

				return totalFormatted;
			}, 0 );

			$(api.column(1).footer()).html(total);
		},

		//hide the column
//		"columnDefs": [
//		{
//			"targets": [ 1 ],
//			"visible": false,
//			"searchable": false
//		}]
	});

	$("#id_checked_sign_by").prop("disabled", true);


});
