$(document).ready(function()
{

	$("#id_admision_form-admitted_others").prop("disabled", true);
	$("#id_patient_form-marital_status_others").prop("disabled", true);
	$("#id_patient_form-religion_others").prop("disabled", true);
	$("#id_patient_form-occupation_others").prop("disabled", true);
	$("#id_patient_form-communication_hearing_others").prop("disabled", true);
	$("#id_admision_form-vital_sign_on_oxygen_therapy_1").filter('[value="False"]').attr('checked', true)
	$("#id_admision_form-vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
	$("#id_admision_form-biohazard_infectious_disease_1").filter('[value="False"]').attr('checked', true)
	$("#id_admision_form-biohazard_infectious_disease_others").prop("disabled", true);
	$("#id_admision_form-invasive_line_insitu_others").prop("disabled", true);
	$("#id_admision_form-medical_history_others").prop("disabled", true);

	$("#id_admision_form-adaptive_aids_with_patient_others").prop("disabled", true);
	$("#id_patient_form-age").prop("disabled", true);
	$("#id_admision_form-surgical_history").prop("disabled", true);
	$("#id_admision_form-surgical_history_none_1").attr("checked", true);

	$("#id_medication_formset-0-medication_1").filter('[value="False"]').attr('checked', true)
	$('.hapus_Own').addClass("disabled");
	$('.tambah_Own').addClass("disabled");
	$("[id$='drug_name']").addClass("disabled_input");
	$("[id$='dosage']").addClass("disabled_input");
	$("[id$='tablet_capsule']").addClass("disabled_input");
	$("[id$='frequency']").addClass("disabled_input");

	if($('#id_patient_form-marital_status_others').val().length > 0)
	{
		$("#id_patient_form-marital_status_3").prop({ checked: true });
		$("#id_patient_form-marital_status_others").prop("disabled", false);
	}

	if($('#id_patient_form-religion_others').val().length > 0)
	{
		$("#id_patient_form-religion_5").prop({ checked: true });
		$("#id_patient_form-religion_others").prop("disabled", false);
	}

	if($('#id_patient_form-occupation_others').val().length > 0)
	{
		$("#id_patient_form-occupation_3").prop({ checked: true });
		$("#id_patient_form-occupation_others").prop("disabled", false);
	}

	if($('#id_patient_form-communication_hearing_others').val().length > 0)
	{
		$("#id_patient_form-communication_hearing_4").prop({ checked: true });
		$("#id_patient_form-communication_hearing_others").prop("disabled", false);
	}

//    $('input.admitted').checkbox({cls:'jquery-safari-checkbox'});
//    $(':radio[id^="id_admision_form-admitted_"]').checkbox({cls:'jquery-safari-checkbox'});

	$(':radio[id^="id_admision_form-admitted_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-admitted_1"))
		{
			if ($("#id_admision_form-admitted_1:checked").length > 0)
			{
				$("#id_admision_form-admitted_2").prop({ checked: false });
				$("#id_admision_form-admitted_3").prop({ checked: false });
				$("#id_admision_form-admitted_others").prop("disabled", true);
			}
			else
			{
				$("#id_admision_form-admitted_2").prop("disabled", false);
				$("#id_admision_form-admitted_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admision_form-admitted_2"))
		{
			if ($("#id_admision_form-admitted_2:checked").length > 0)
			{
				$("#id_admision_form-admitted_1").prop({ checked: false });
				$("#id_admision_form-admitted_3").prop({ checked: false });
				$("#id_admision_form-admitted_others").prop("disabled", true);
			}
			else
			{
				$("#id_admision_form-admitted_1").prop("disabled", false);
				$("#id_admision_form-admitted_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admision_form-admitted_3"))
		{
			if ($("#id_admision_form-admitted_3:checked").length > 0)
			{
				$("#id_admision_form-admitted_1").prop({ checked: false });
				$("#id_admision_form-admitted_2").prop({ checked: false });
				$("#id_admision_form-admitted_others").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-admitted_1").prop("disabled", false);
				$("#id_admision_form-admitted_2").prop("disabled", false);
				$("#id_admision_form-admitted_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_patient_form-gender_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_patient_form-gender_1"))
		{
			if ($("#id_patient_form-gender_1:checked").length > 0)
			{
				$("#id_patient_form-gender_2").prop({ checked: false });
			}
			else
			{
				$("#id_patient_form-gender_2").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-gender_2"))
		{
			if ($("#id_patient_form-gender_2:checked").length > 0)
			{
				$("#id_patient_form-gender_1").prop({ checked: false });
			}
			else
			{
				$("#id_patient_form-gender_1").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_patient_form-marital_status_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_patient_form-marital_status_1"))
		{
			if ($("#id_patient_form-marital_status_1:checked").length > 0)
			{
				$("#id_patient_form-marital_status_2").prop({ checked: false });
				$("#id_patient_form-marital_status_3").prop({ checked: false });
				$("#id_patient_form-marital_status_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-marital_status_2").prop("disabled", false);
				$("#id_patient_form-marital_status_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-marital_status_2"))
		{
			if ($("#id_patient_form-marital_status_2:checked").length > 0)
			{
				$("#id_patient_form-marital_status_1").prop({ checked: false });
				$("#id_patient_form-marital_status_3").prop({ checked: false });
				$("#id_patient_form-marital_status_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-marital_status_1").prop("disabled", false);
				$("#id_patient_form-marital_status_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-marital_status_3"))
		{
			if ($("#id_patient_form-marital_status_3:checked").length > 0)
			{
				$("#id_patient_form-marital_status_1").prop({ checked: false });
				$("#id_patient_form-marital_status_2").prop({ checked: false });
				$("#id_patient_form-marital_status_others").prop("disabled", false);
			}
			else
			{
				$("#id_patient_form-marital_status_1").prop("disabled", false);
				$("#id_patient_form-marital_status_2").prop("disabled", false);
				$("#id_patient_form-marital_status_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_patient_form-religion_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_patient_form-religion_1"))
		{
			if ($("#id_patient_form-religion_1:checked").length > 0)
			{
				$("#id_patient_form-religion_2").prop({ checked: false });
				$("#id_patient_form-religion_3").prop({ checked: false });
				$("#id_patient_form-religion_4").prop({ checked: false });
				$("#id_patient_form-religion_5").prop({ checked: false });
				$("#id_patient_form-religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-religion_2").prop("disabled", false);
				$("#id_patient_form-religion_3").prop("disabled", false);
				$("#id_patient_form-religion_4").prop("disabled", false);
				$("#id_patient_form-religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-religion_2"))
		{
			if ($("#id_patient_form-religion_2:checked").length > 0)
			{
				$("#id_patient_form-religion_1").prop({ checked: false });
				$("#id_patient_form-religion_3").prop({ checked: false });
				$("#id_patient_form-religion_4").prop({ checked: false });
				$("#id_patient_form-religion_5").prop({ checked: false });
				$("#id_patient_form-religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-religion_1").prop("disabled", false);
				$("#id_patient_form-religion_3").prop("disabled", false);
				$("#id_patient_form-religion_4").prop("disabled", false);
				$("#id_patient_form-religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-religion_3"))
		{
			if ($("#id_patient_form-religion_3:checked").length > 0)
			{
				$("#id_patient_form-religion_1").prop({ checked: false });
				$("#id_patient_form-religion_2").prop({ checked: false });
				$("#id_patient_form-religion_4").prop({ checked: false });
				$("#id_patient_form-religion_5").prop({ checked: false });
				$("#id_patient_form-religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-religion_1").prop("disabled", false);
				$("#id_patient_form-religion_2").prop("disabled", false);
				$("#id_patient_form-religion_4").prop("disabled", false);
				$("#id_patient_form-religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-religion_4"))
		{
			if ($("#id_patient_form-religion_4:checked").length > 0)
			{
				$("#id_patient_form-religion_1").prop({ checked: false });
				$("#id_patient_form-religion_2").prop({ checked: false });
				$("#id_patient_form-religion_3").prop({ checked: false });
				$("#id_patient_form-religion_5").prop({ checked: false });
				$("#id_patient_form-religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-religion_1").prop("disabled", false);
				$("#id_patient_form-religion_2").prop("disabled", false);
				$("#id_patient_form-religion_3").prop("disabled", false);
				$("#id_patient_form-religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-religion_5"))
		{
			if ($("#id_patient_form-religion_5:checked").length > 0)
			{
				$("#id_patient_form-religion_1").prop({ checked: false });
				$("#id_patient_form-religion_2").prop({ checked: false });
				$("#id_patient_form-religion_3").prop({ checked: false });
				$("#id_patient_form-religion_4").prop({ checked: false });
				$("#id_patient_form-religion_others").prop("disabled", false);
			}
			else
			{
				$("#id_patient_form-religion_1").prop("disabled", false);
				$("#id_patient_form-religion_2").prop("disabled", false);
				$("#id_patient_form-religion_3").prop("disabled", false);
				$("#id_patient_form-religion_4").prop("disabled", false);
				$("#id_patient_form-religion_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_patient_form-occupation_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_patient_form-occupation_1"))
		{
			if ($("#id_patient_form-occupation_1:checked").length > 0)
			{
				$("#id_patient_form-occupation_2").prop({ checked: false });
				$("#id_patient_form-occupation_3").prop({ checked: false });
				$("#id_patient_form-occupation_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-occupation_2").prop("disabled", false);
				$("#id_patient_form-occupation_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-occupation_2"))
		{
			if ($("#id_patient_form-occupation_2:checked").length > 0)
			{
				$("#id_patient_form-occupation_1").prop({ checked: false });
				$("#id_patient_form-occupation_3").prop({ checked: false });
				$("#id_patient_form-occupation_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-occupation_1").prop("disabled", false);
				$("#id_patient_form-occupation_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-occupation_3"))
		{
			if ($("#id_patient_form-occupation_3:checked").length > 0)
			{
				$("#id_patient_form-occupation_1").prop({ checked: false });
				$("#id_patient_form-occupation_2").prop({ checked: false });
				$("#id_patient_form-occupation_others").prop("disabled", false);
			}
			else
			{
				$("#id_patient_form-occupation_1").prop("disabled", false);
				$("#id_patient_form-occupation_2").prop("disabled", false);
				$("#id_patient_form-occupation_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_form-0-communication_sight_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_form-0-communication_sight_1"))
		{
			if ($("#id_form-0-communication_sight_1:checked").length > 0)
			{
				$("#id_form-0-communication_sight_2").prop({ checked: false });
				$("#id_form-0-communication_sight_3").prop({ checked: false });
				$("#id_form-0-communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-communication_sight_2").prop("disabled", false);
				$("#id_form-0-communication_sight_3").prop("disabled", false);
				$("#id_form-0-communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-communication_sight_2"))
		{
			if ($("#id_form-0-communication_sight_2:checked").length > 0)
			{
				$("#id_form-0-communication_sight_1").prop({ checked: false });
				$("#id_form-0-communication_sight_3").prop({ checked: false });
				$("#id_form-0-communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-communication_sight_1").prop("disabled", false);
				$("#id_form-0-communication_sight_3").prop("disabled", false);
				$("#id_form-0-communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-communication_sight_3"))
		{
			if ($("#id_form-0-communication_sight_3:checked").length > 0)
			{
				$("#id_form-0-communication_sight_1").prop({ checked: false });
				$("#id_form-0-communication_sight_2").prop({ checked: false });
				$("#id_form-0-communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-communication_sight_1").prop("disabled", false);
				$("#id_form-0-communication_sight_2").prop("disabled", false);
				$("#id_form-0-communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-communication_sight_4"))
		{
			if ($("#id_form-0-communication_sight_4:checked").length > 0)
			{
				$("#id_form-0-communication_sight_1").prop({ checked: false });
				$("#id_form-0-communication_sight_2").prop({ checked: false });
				$("#id_form-0-communication_sight_3").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-communication_sight_1").prop("disabled", false);
				$("#id_form-0-communication_sight_2").prop("disabled", false);
				$("#id_form-0-communication_sight_3").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_patient_form-communication_hearing_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_patient_form-communication_hearing_1"))
		{
			if ($("#id_patient_form-communication_hearing_1:checked").length > 0)
			{
				$("#id_patient_form-communication_hearing_2").prop({ checked: false });
				$("#id_patient_form-communication_hearing_3").prop({ checked: false });
				$("#id_patient_form-communication_hearing_4").prop({ checked: false });
				$("#id_patient_form-communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-communication_hearing_2").prop("disabled", false);
				$("#id_patient_form-communication_hearing_3").prop("disabled", false);
				$("#id_patient_form-communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-communication_hearing_2"))
		{
			if ($("#id_patient_form-communication_hearing_2:checked").length > 0)
			{
				$("#id_patient_form-communication_hearing_1").prop({ checked: false });
				$("#id_patient_form-communication_hearing_3").prop({ checked: false });
				$("#id_patient_form-communication_hearing_4").prop({ checked: false });
				$("#id_patient_form-communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-communication_hearing_1").prop("disabled", false);
				$("#id_patient_form-communication_hearing_3").prop("disabled", false);
				$("#id_patient_form-communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-communication_hearing_3"))
		{
			if ($("#id_patient_form-communication_hearing_3:checked").length > 0)
			{
				$("#id_patient_form-communication_hearing_1").prop({ checked: false });
				$("#id_patient_form-communication_hearing_2").prop({ checked: false });
				$("#id_patient_form-communication_hearing_4").prop({ checked: false });
				$("#id_patient_form-communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_patient_form-communication_hearing_1").prop("disabled", false);
				$("#id_patient_form-communication_hearing_2").prop("disabled", false);
				$("#id_patient_form-communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_patient_form-communication_hearing_4"))
		{
			if ($("#id_patient_form-communication_hearing_4:checked").length > 0)
			{
				$("#id_patient_form-communication_hearing_1").prop({ checked: false });
				$("#id_patient_form-communication_hearing_2").prop({ checked: false });
				$("#id_patient_form-communication_hearing_3").prop({ checked: false });
				$("#id_patient_form-communication_hearing_others").prop("disabled", false);
			}
			else
			{
				$("#id_patient_form-communication_hearing_1").prop("disabled", false);
				$("#id_patient_form-communication_hearing_2").prop("disabled", false);
				$("#id_patient_form-communication_hearing_3").prop("disabled", false);
				$("#id_patient_form-communication_hearing_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_form-0-general_condition_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_form-0-general_condition_1"))
		{
			if ($("#id_form-0-general_condition_1:checked").length > 0)
			{
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_2"))
		{
			if ($("#id_form-0-general_condition_2:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_3"))
		{
			if ($("#id_form-0-general_condition_3:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_4"))
		{
			if ($("#id_form-0-general_condition_4:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_5"))
		{
			if ($("#id_form-0-general_condition_5:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_6"))
		{
			if ($("#id_form-0-general_condition_6:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_7"))
		{
			if ($("#id_form-0-general_condition_7:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_8"))
		{
			if ($("#id_form-0-general_condition_8:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-general_condition_9"))
		{
			if ($("#id_form-0-general_condition_9:checked").length > 0)
			{
				$("#id_form-0-general_condition_1").prop({ checked: false });
				$("#id_form-0-general_condition_2").prop({ checked: false });
				$("#id_form-0-general_condition_3").prop({ checked: false });
				$("#id_form-0-general_condition_4").prop({ checked: false });
				$("#id_form-0-general_condition_5").prop({ checked: false });
				$("#id_form-0-general_condition_6").prop({ checked: false });
				$("#id_form-0-general_condition_7").prop({ checked: false });
				$("#id_form-0-general_condition_8").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-general_condition_1").prop("disabled", false);
				$("#id_form-0-general_condition_2").prop("disabled", false);
				$("#id_form-0-general_condition_3").prop("disabled", false);
				$("#id_form-0-general_condition_4").prop("disabled", false);
				$("#id_form-0-general_condition_5").prop("disabled", false);
				$("#id_form-0-general_condition_6").prop("disabled", false);
				$("#id_form-0-general_condition_7").prop("disabled", false);
				$("#id_form-0-general_condition_8").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_form-0-biohazard_infectious_disease_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_form-0-biohazard_infectious_disease_1"))
		{
			if ($("#id_form-0-biohazard_infectious_disease_1:checked").length > 0)
			{
				$("#id_form-0-biohazard_infectious_disease_2").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-biohazard_infectious_disease_2").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-biohazard_infectious_disease_2"))
		{
			if ($("#id_form-0-biohazard_infectious_disease_2:checked").length > 0)
			{
				$("#id_form-0-biohazard_infectious_disease_1").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-biohazard_infectious_disease_1").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_admision_form-vital_sign_on_oxygen_therapy_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-vital_sign_on_oxygen_therapy_1"))
		{
			if ($("#id_admision_form-vital_sign_on_oxygen_therapy_1:checked").length > 0)
			{
				$("#id_admision_form-vital_sign_on_oxygen_therapy_2").prop({ checked: false });
				$("#id_admision_form-vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
			}
			else
			{
				$("#id_admision_form-vital_sign_on_oxygen_therapy_2").prop("disabled", false);
				$("#id_admision_form-vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admision_form-vital_sign_on_oxygen_therapy_2"))
		{
			if ($("#id_admision_form-vital_sign_on_oxygen_therapy_2:checked").length > 0)
			{
				$("#id_admision_form-vital_sign_on_oxygen_therapy_1").prop({ checked: false });
				$("#id_admision_form-vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-vital_sign_on_oxygen_therapy_1").prop("disabled", false);
				$("#id_admision_form-vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
			}
		}
	});


	$(':radio[id^="id_admision_form-biohazard_infectious_disease_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-biohazard_infectious_disease_1"))
		{
			if ($("#id_admision_form-biohazard_infectious_disease_1:checked").length > 0)
			{
				$("#id_admision_form-biohazard_infectious_disease_2").prop({ checked: false });
				$("#id_admision_form-biohazard_infectious_disease_others").prop("disabled", true);
			}
			else
			{
				$("#id_admision_form-biohazard_infectious_disease_2").prop("disabled", false);
				$("#id_admision_form-biohazard_infectious_disease_others").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admision_form-biohazard_infectious_disease_2"))
		{
			if ($("#id_admision_form-biohazard_infectious_disease_2:checked").length > 0)
			{
				$("#id_admision_form-biohazard_infectious_disease_1").prop({ checked: false });
				$("#id_admision_form-biohazard_infectious_disease_others").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-biohazard_infectious_disease_1").prop("disabled", false);
				$("#id_admision_form-biohazard_infectious_disease_others").prop("disabled", true);
			}
		}
	});

	$(':input[id^="id_admision_form-invasive_line_insitu_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-invasive_line_insitu_5"))
		{
			if ($("#id_admision_form-invasive_line_insitu_5:checked").is(':checked') == true)
			{
				$("#id_admision_form-invasive_line_insitu_others").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-invasive_line_insitu_others").prop("disabled", true);
			}
		}
	});

	$(':input[id^="id_admision_form-medical_history_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-medical_history_8"))
		{
			if ($("#id_admision_form-medical_history_8").is(':checked') == true)
			{
				$("#id_admision_form-medical_history_others").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-medical_history_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_medication_formset-0-medication_"]').click(function()
	{

		var $this = $(this);
		if ($this.is("#id_medication_formset-0-medication_1"))
		{
			if ($("#id_medication_formset-0-medication_1").filter('[value="True"]').attr('checked', true))
			{
				$('.hapus_Own').addClass("disabled");
				$('.tambah_Own').addClass("disabled");
				$("[id$='drug_name']").addClass("disabled_input");
				$("[id$='dosage']").addClass("disabled_input");
				$("[id$='tablet_capsule']").addClass("disabled_input");
				$("[id$='frequency']").addClass("disabled_input");
			}
			else
			{
				$('.hapus_Own').removeClass("disabled");
				$('.tambah_Own').removeClass("disabled");
				$("[id$='drug_name']").removeClass("disabled_input");
				$("[id$='dosage']").removeClass("disabled_input");
				$("[id$='tablet_capsule']").removeClass("disabled_input");
				$("[id$='frequency']").removeClass("disabled_input");
			}
		}
		else if ($this.is("#id_medication_formset-0-medication_2"))
		{
			if ($("#id_medication_formset-0-medication_2").filter('[value="True"]').attr('checked', true))
			{
				$('.hapus_Own').removeClass("disabled");
				$('.tambah_Own').removeClass("disabled");
				$("[id$='drug_name']").removeClass("disabled_input");
				$("[id$='dosage']").removeClass("disabled_input");
				$("[id$='tablet_capsule']").removeClass("disabled_input");
				$("[id$='frequency']").removeClass("disabled_input");
			}
			else
			{
				$('.hapus_Own').addClass("disabled");
				$('.tambah_Own').addClass("disabled");
				$("[id$='drug_name']").addClass("disabled_input");
				$("[id$='dosage']").addClass("disabled_input");
				$("[id$='tablet_capsule']").addClass("disabled_input");
				$("[id$='frequency']").addClass("disabled_input");
			}
		}
	});


	$(':input[id^="id_admision_form-adaptive_aids_with_patient_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-adaptive_aids_with_patient_6"))
		{
			if ($("#id_admision_form-adaptive_aids_with_patient_6").is(':checked') == true)
			{
				$("#id_admision_form-adaptive_aids_with_patient_others").prop("disabled", false);
			}
			else
			{
				$("#id_admision_form-adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
	});


	$(':radio[id^="id_form-0-orientation_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_form-0-orientation_1"))
		{
			if ($("#id_form-0-orientation_1:checked").length > 0)
			{
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_2"))
		{
			if ($("#id_form-0-orientation_2:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_3"))
		{
			if ($("#id_form-0-orientation_3:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_4"))
		{
			if ($("#id_form-0-orientation_4:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_5"))
		{
			if ($("#id_form-0-orientation_5:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_6"))
		{
			if ($("#id_form-0-orientation_6:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_7"))
		{
			if ($("#id_form-0-orientation_7:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_8"))
		{
			if ($("#id_form-0-orientation_8:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_form-0-orientation_9"))
		{
			if ($("#id_form-0-orientation_9:checked").length > 0)
			{
				$("#id_form-0-orientation_1").prop({ checked: false });
				$("#id_form-0-orientation_2").prop({ checked: false });
				$("#id_form-0-orientation_3").prop({ checked: false });
				$("#id_form-0-orientation_4").prop({ checked: false });
				$("#id_form-0-orientation_5").prop({ checked: false });
				$("#id_form-0-orientation_6").prop({ checked: false });
				$("#id_form-0-orientation_7").prop({ checked: false });
				$("#id_form-0-orientation_8").prop({ checked: false });
			}
			else
			{
				$("#id_form-0-orientation_1").prop("disabled", false);
				$("#id_form-0-orientation_2").prop("disabled", false);
				$("#id_form-0-orientation_3").prop("disabled", false);
				$("#id_form-0-orientation_4").prop("disabled", false);
				$("#id_form-0-orientation_5").prop("disabled", false);
				$("#id_form-0-orientation_6").prop("disabled", false);
				$("#id_form-0-orientation_7").prop("disabled", false);
				$("#id_form-0-orientation_8").prop("disabled", false);
			}
		}
	});

	$(':checkbox[id^="id_admision_form-surgical_history_none_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admision_form-surgical_history_none_1"))
		{
			if ($("#id_admision_form-surgical_history_none_1:checked").length > 0)
			{
				$("#id_admision_form-surgical_history").prop("disabled", true);
			}
			else
			{
				$("#id_admision_form-surgical_history").prop("disabled", false);
			}
		}
	});
});
