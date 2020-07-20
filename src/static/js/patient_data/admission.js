var t = $('#t_add_row').DataTable(
{
	"order": [[ 0, "desc" ]]
});

var dob = $('#id_birth_date').val();
var age = "";


$(document).ready(function()
{
	dob = new Date(dob);
    var today = new Date();
    var age = Math.floor((today-dob)/(365.25*24*60*60*1000));
    $('#id_age').html(age+' years old');
//    $grand_total=$('#age');
//    $grand_total.val(age)

    $("#id_birth_date").change(function()
    {
    	if($(this))
    	{
    		alert(val(age));
    	}
    });
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
					$("#t_add_row tbody").html(data.html_admission_list);
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
					$("#t_add_row tbody").html(data.html_admission_list);
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

	// Create admission
	$(".addRow").click(loadForm);


	// Update admission
	$("#t_add_row tbody").on("click", ".edit-row-btn", loadForm);
	$("#exampleModal").on("submit", ".admission-update-form", saveEditForm);

	// Delete admission
	$("#t_add_row tbody").on("click", ".delete-row-btn", loadForm);
	$("#exampleModal").on("submit", ".admission-delete-form", saveDeleteForm);
});

