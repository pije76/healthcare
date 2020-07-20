var t = $('#t_add_row').DataTable(
	{
		"order": [[ 0, "desc" ]],

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



$(document).ready(function()
{
	var loadForm = function()
	{
		$.ajax(
		{
			url: $(this).attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: function()
			{
				$("#exampleModal").modal("show");
			},
			success: function(data)
			{
				$("#exampleModal .modal-content").html(data.html_form);
			}
		});
	};

	var saveEditForm = function()
	{

		var row = $(this).parents('tr:first');
		$.ajax(
		{
			url: $(this).attr("action"),
			data: $(this).serialize(),
			type: $(this).attr("method"),
			dataType: 'json',
			success: function(data)
			{
				if (data.form_is_valid)
				{
					$("#t_add_row tbody").html(data.html_appointment_list);
					$("#exampleModal").modal("hide");
				}
				else
				{
					$("#exampleModal .modal-content").html(data.html_form);
				}
			}
		});
		return false;
	};

	var saveDeleteForm = function()
	{

		var row = $(this).parents('tr:first');
		$.ajax(
		{
			url: $(this).attr("action"),
			data: $(this).serialize(),
			type: $(this).attr("method"),
			dataType: 'json',
			success: function(data)
			{
				if (data.form_is_valid)
				{
					$("#t_add_row tbody").html(data.html_appointment_list);
					$("#exampleModal").modal("hide");
				}
				else
				{
					$("#exampleModal .modal-content").html(data.html_form);
				}
			}
		});
		return false;
	};

	/* Binding */

	// Create appointment
	$(".addRow").click(loadForm);


	// Update appointment
	$("#t_add_row tbody").on("click", ".edit-row-btn", loadForm);
	$("#exampleModal").on("submit", ".appointment-update-form", saveEditForm);

	// Delete appointment
	$("#t_add_row tbody").on("click", ".delete-row-btn", loadForm);
	$("#exampleModal").on("submit", ".appointment-delete-form", saveDeleteForm);


});
