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
