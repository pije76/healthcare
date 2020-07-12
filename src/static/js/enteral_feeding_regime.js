var t = $('#t_add_row').DataTable(
	{
		"order": [[ 0, "desc" ]]
	});

$(document).ready(function()
{
	$('.calc').change(function()
	{
		var total = 0;
		$('.calc').each(function()
		{
			if($(this).val() != '')
			{
				total += parseInt($(this).val());
			}
		});
		$('#total').html(total);
	});
});

$(document).ready(function()
{
	//when the select changes:
	$('.calc').on("change", function()
	{
		$('#total').val($(this).val());
	});
});

$(function()
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
