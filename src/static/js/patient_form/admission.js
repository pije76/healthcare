$(document).ready(function()
{
	$("#id_admitted_others").prop("disabled", true);
	$("#id_marital_status_others").prop("disabled", true);
	$("#id_religion_others").prop("disabled", true);
	$("#id_occupation_others").prop("disabled", true);
	$("#id_communication_hearing_others").prop("disabled", true);
	$("#id_vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
	$("#id_invasive_line_insitu_others").prop("disabled", true);
	$("#id_medical_history_others").prop("disabled", true);
	$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
	$("#id_age").prop("disabled", true);
	$("#id_surgical_history").prop("disabled", true);

//    $('input.admitted').checkbox({cls:'jquery-safari-checkbox'});
//    $(':radio[id^="id_admitted_"]').checkbox({cls:'jquery-safari-checkbox'});

	$(':radio[id^="id_admitted_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_admitted_1"))
		{
			if ($("#id_admitted_1:checked").length > 0)
			{
				$("#id_admitted_2").prop({ checked: false });
				$("#id_admitted_3").prop({ checked: false });
				$("#id_admitted_others").prop("disabled", true);
			}
			else
			{
				$("#id_admitted_2").prop("disabled", false);
				$("#id_admitted_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admitted_2"))
		{
			if ($("#id_admitted_2:checked").length > 0)
			{
				$("#id_admitted_1").prop({ checked: false });
				$("#id_admitted_3").prop({ checked: false });
				$("#id_admitted_others").prop("disabled", true);
			}
			else
			{
				$("#id_admitted_1").prop("disabled", false);
				$("#id_admitted_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_admitted_3"))
		{
			if ($("#id_admitted_3:checked").length > 0)
			{
				$("#id_admitted_1").prop({ checked: false });
				$("#id_admitted_2").prop({ checked: false });
				$("#id_admitted_others").prop("disabled", false);
			}
			else
			{
				$("#id_admitted_1").prop("disabled", false);
				$("#id_admitted_2").prop("disabled", false);
				$("#id_admitted_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_mode_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_mode_1"))
		{
			if ($("#id_mode_1:checked").length > 0)
			{
				$("#id_mode_2").prop({ checked: false });
				$("#id_mode_3").prop({ checked: false });
			}
			else
			{
				$("#id_mode_2").prop("disabled", false);
				$("#id_mode_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_mode_2"))
		{
			if ($("#id_mode_2:checked").length > 0)
			{
				$("#id_mode_1").prop({ checked: false });
				$("#id_mode_3").prop({ checked: false });
			}
			else
			{
				$("#id_mode_1").prop("disabled", false);
				$("#id_mode_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_mode_3"))
		{
			if ($("#id_mode_3:checked").length > 0)
			{
				$("#id_mode_1").prop({ checked: false });
				$("#id_mode_2").prop({ checked: false });
			}
			else
			{
				$("#id_mode_1").prop("disabled", false);
				$("#id_mode_2").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_gender_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_gender_1"))
		{
			if ($("#id_gender_1:checked").length > 0)
			{
				$("#id_gender_2").prop({ checked: false });
			}
			else
			{
				$("#id_gender_2").prop("disabled", false);
			}
		}
		else if ($this.is("#id_gender_2"))
		{
			if ($("#id_gender_2:checked").length > 0)
			{
				$("#id_gender_1").prop({ checked: false });
			}
			else
			{
				$("#id_gender_1").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_marital_status_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_marital_status_1"))
		{
			if ($("#id_marital_status_1:checked").length > 0)
			{
				$("#id_marital_status_2").prop({ checked: false });
				$("#id_marital_status_3").prop({ checked: false });
				$("#id_marital_status_others").prop("disabled", true);
			}
			else
			{
				$("#id_marital_status_2").prop("disabled", false);
				$("#id_marital_status_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_marital_status_2"))
		{
			if ($("#id_marital_status_2:checked").length > 0)
			{
				$("#id_marital_status_1").prop({ checked: false });
				$("#id_marital_status_3").prop({ checked: false });
				$("#id_marital_status_others").prop("disabled", true);
			}
			else
			{
				$("#id_marital_status_1").prop("disabled", false);
				$("#id_marital_status_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_marital_status_3"))
		{
			if ($("#id_marital_status_3:checked").length > 0)
			{
				$("#id_marital_status_1").prop({ checked: false });
				$("#id_marital_status_2").prop({ checked: false });
				$("#id_marital_status_others").prop("disabled", false);
			}
			else
			{
				$("#id_marital_status_1").prop("disabled", false);
				$("#id_marital_status_2").prop("disabled", false);
				$("#id_marital_status_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_religion_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_religion_1"))
		{
			if ($("#id_religion_1:checked").length > 0)
			{
				$("#id_religion_2").prop({ checked: false });
				$("#id_religion_3").prop({ checked: false });
				$("#id_religion_4").prop({ checked: false });
				$("#id_religion_5").prop({ checked: false });
				$("#id_religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_religion_2").prop("disabled", false);
				$("#id_religion_3").prop("disabled", false);
				$("#id_religion_4").prop("disabled", false);
				$("#id_religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_religion_2"))
		{
			if ($("#id_religion_2:checked").length > 0)
			{
				$("#id_religion_1").prop({ checked: false });
				$("#id_religion_3").prop({ checked: false });
				$("#id_religion_4").prop({ checked: false });
				$("#id_religion_5").prop({ checked: false });
				$("#id_religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_religion_1").prop("disabled", false);
				$("#id_religion_3").prop("disabled", false);
				$("#id_religion_4").prop("disabled", false);
				$("#id_religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_religion_3"))
		{
			if ($("#id_religion_3:checked").length > 0)
			{
				$("#id_religion_1").prop({ checked: false });
				$("#id_religion_2").prop({ checked: false });
				$("#id_religion_4").prop({ checked: false });
				$("#id_religion_5").prop({ checked: false });
				$("#id_religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_religion_1").prop("disabled", false);
				$("#id_religion_2").prop("disabled", false);
				$("#id_religion_4").prop("disabled", false);
				$("#id_religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_religion_4"))
		{
			if ($("#id_religion_4:checked").length > 0)
			{
				$("#id_religion_1").prop({ checked: false });
				$("#id_religion_2").prop({ checked: false });
				$("#id_religion_3").prop({ checked: false });
				$("#id_religion_5").prop({ checked: false });
				$("#id_religion_others").prop("disabled", true);
			}
			else
			{
				$("#id_religion_1").prop("disabled", false);
				$("#id_religion_2").prop("disabled", false);
				$("#id_religion_3").prop("disabled", false);
				$("#id_religion_5").prop("disabled", false);
			}
		}
		else if ($this.is("#id_religion_5"))
		{
			if ($("#id_religion_5:checked").length > 0)
			{
				$("#id_religion_1").prop({ checked: false });
				$("#id_religion_2").prop({ checked: false });
				$("#id_religion_3").prop({ checked: false });
				$("#id_religion_4").prop({ checked: false });
				$("#id_religion_others").prop("disabled", false);
			}
			else
			{
				$("#id_religion_1").prop("disabled", false);
				$("#id_religion_2").prop("disabled", false);
				$("#id_religion_3").prop("disabled", false);
				$("#id_religion_4").prop("disabled", false);
				$("#id_religion_others").prop("disabled", true);
			}
		}       
	});

	$(':radio[id^="id_occupation_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_occupation_1"))
		{
			if ($("#id_occupation_1:checked").length > 0)
			{
				$("#id_occupation_2").prop({ checked: false });
				$("#id_occupation_3").prop({ checked: false });
				$("#id_occupation_others").prop("disabled", true);
			}
			else
			{
				$("#id_occupation_2").prop("disabled", false);
				$("#id_occupation_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_occupation_2"))
		{
			if ($("#id_occupation_2:checked").length > 0)
			{
				$("#id_occupation_1").prop({ checked: false });
				$("#id_occupation_3").prop({ checked: false });
				$("#id_occupation_others").prop("disabled", true);
			}
			else
			{
				$("#id_occupation_1").prop("disabled", false);
				$("#id_occupation_3").prop("disabled", false);
			}
		}
		else if ($this.is("#id_occupation_3"))
		{
			if ($("#id_occupation_3:checked").length > 0)
			{
				$("#id_occupation_1").prop({ checked: false });
				$("#id_occupation_2").prop({ checked: false });
				$("#id_occupation_others").prop("disabled", false);
			}
			else
			{
				$("#id_occupation_1").prop("disabled", false);
				$("#id_occupation_2").prop("disabled", false);
				$("#id_occupation_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_communication_sight_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_communication_sight_1"))
		{
			if ($("#id_communication_sight_1:checked").length > 0)
			{
				$("#id_communication_sight_2").prop({ checked: false });
				$("#id_communication_sight_3").prop({ checked: false });
				$("#id_communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_communication_sight_2").prop("disabled", false);
				$("#id_communication_sight_3").prop("disabled", false);
				$("#id_communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_sight_2"))
		{
			if ($("#id_communication_sight_2:checked").length > 0)
			{
				$("#id_communication_sight_1").prop({ checked: false });
				$("#id_communication_sight_3").prop({ checked: false });
				$("#id_communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_communication_sight_1").prop("disabled", false);
				$("#id_communication_sight_3").prop("disabled", false);
				$("#id_communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_sight_3"))
		{
			if ($("#id_communication_sight_3:checked").length > 0)
			{
				$("#id_communication_sight_1").prop({ checked: false });
				$("#id_communication_sight_2").prop({ checked: false });
				$("#id_communication_sight_4").prop({ checked: false });
			}
			else
			{
				$("#id_communication_sight_1").prop("disabled", false);
				$("#id_communication_sight_2").prop("disabled", false);
				$("#id_communication_sight_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_sight_4"))
		{
			if ($("#id_communication_sight_4:checked").length > 0)
			{
				$("#id_communication_sight_1").prop({ checked: false });
				$("#id_communication_sight_2").prop({ checked: false });
				$("#id_communication_sight_3").prop({ checked: false });
			}
			else
			{
				$("#id_communication_sight_1").prop("disabled", false);
				$("#id_communication_sight_2").prop("disabled", false);
				$("#id_communication_sight_3").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_communication_hearing_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_communication_hearing_1"))
		{
			if ($("#id_communication_hearing_1:checked").length > 0)
			{
				$("#id_communication_hearing_2").prop({ checked: false });
				$("#id_communication_hearing_3").prop({ checked: false });
				$("#id_communication_hearing_4").prop({ checked: false });
				$("#id_communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_communication_hearing_2").prop("disabled", false);
				$("#id_communication_hearing_3").prop("disabled", false);
				$("#id_communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_hearing_2"))
		{
			if ($("#id_communication_hearing_2:checked").length > 0)
			{
				$("#id_communication_hearing_1").prop({ checked: false });
				$("#id_communication_hearing_3").prop({ checked: false });
				$("#id_communication_hearing_4").prop({ checked: false });
				$("#id_communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_communication_hearing_1").prop("disabled", false);
				$("#id_communication_hearing_3").prop("disabled", false);
				$("#id_communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_hearing_3"))
		{
			if ($("#id_communication_hearing_3:checked").length > 0)
			{
				$("#id_communication_hearing_1").prop({ checked: false });
				$("#id_communication_hearing_2").prop({ checked: false });
				$("#id_communication_hearing_4").prop({ checked: false });
				$("#id_communication_hearing_others").prop("disabled", true);
			}
			else
			{
				$("#id_communication_hearing_1").prop("disabled", false);
				$("#id_communication_hearing_2").prop("disabled", false);
				$("#id_communication_hearing_4").prop("disabled", false);
			}
		}
		else if ($this.is("#id_communication_hearing_4"))
		{
			if ($("#id_communication_hearing_4:checked").length > 0)
			{
				$("#id_communication_hearing_1").prop({ checked: false });
				$("#id_communication_hearing_2").prop({ checked: false });
				$("#id_communication_hearing_3").prop({ checked: false });
				$("#id_communication_hearing_others").prop("disabled", false);
			}
			else
			{
				$("#id_communication_hearing_1").prop("disabled", false);
				$("#id_communication_hearing_2").prop("disabled", false);
				$("#id_communication_hearing_3").prop("disabled", false);
				$("#id_communication_hearing_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_general_condition_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_general_condition_1"))
		{
			if ($("#id_general_condition_1:checked").length > 0)
			{
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_2"))
		{
			if ($("#id_general_condition_2:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_3"))
		{
			if ($("#id_general_condition_3:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_4"))
		{
			if ($("#id_general_condition_4:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_5"))
		{
			if ($("#id_general_condition_5:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_6"))
		{
			if ($("#id_general_condition_6:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_7"))
		{
			if ($("#id_general_condition_7:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_8"))
		{
			if ($("#id_general_condition_8:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_9").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_general_condition_9"))
		{
			if ($("#id_general_condition_9:checked").length > 0)
			{
				$("#id_general_condition_1").prop({ checked: false });
				$("#id_general_condition_2").prop({ checked: false });
				$("#id_general_condition_3").prop({ checked: false });
				$("#id_general_condition_4").prop({ checked: false });
				$("#id_general_condition_5").prop({ checked: false });
				$("#id_general_condition_6").prop({ checked: false });
				$("#id_general_condition_7").prop({ checked: false });
				$("#id_general_condition_8").prop({ checked: false });
			}
			else
			{
				$("#id_general_condition_1").prop("disabled", false);
				$("#id_general_condition_2").prop("disabled", false);
				$("#id_general_condition_3").prop("disabled", false);
				$("#id_general_condition_4").prop("disabled", false);
				$("#id_general_condition_5").prop("disabled", false);
				$("#id_general_condition_6").prop("disabled", false);
				$("#id_general_condition_7").prop("disabled", false);
				$("#id_general_condition_8").prop("disabled", false);
			}
		}
	});
	
	$(':radio[id^="id_biohazard_infectious_disease_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_biohazard_infectious_disease_1"))
		{
			if ($("#id_biohazard_infectious_disease_1:checked").length > 0)
			{
				$("#id_biohazard_infectious_disease_2").prop({ checked: false });
			}
			else
			{
				$("#id_biohazard_infectious_disease_2").prop("disabled", false);
			}
		}
		else if ($this.is("#id_biohazard_infectious_disease_2"))
		{
			if ($("#id_biohazard_infectious_disease_2:checked").length > 0)
			{
				$("#id_biohazard_infectious_disease_1").prop({ checked: false });
			}
			else
			{
				$("#id_biohazard_infectious_disease_1").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_vital_sign_on_oxygen_therapy_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_vital_sign_on_oxygen_therapy_1"))
		{
			if ($("#id_vital_sign_on_oxygen_therapy_1:checked").length > 0)
			{
				$("#id_vital_sign_on_oxygen_therapy_2").prop({ checked: false });
				$("#id_vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
			}
			else
			{
				$("#id_vital_sign_on_oxygen_therapy_2").prop("disabled", false);
				$("#id_vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", false);
			}
		}
		else if ($this.is("#id_vital_sign_on_oxygen_therapy_2"))
		{
			if ($("#id_vital_sign_on_oxygen_therapy_2:checked").length > 0)
			{
				$("#id_vital_sign_on_oxygen_therapy_1").prop({ checked: false });
				$("#id_vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", false);
			}
			else
			{
				$("#id_vital_sign_on_oxygen_therapy_flow_rate_1").prop("disabled", false);
				$("#id_vital_sign_on_oxygen_therapy_flow_rate").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_invasive_line_insitu_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_invasive_line_insitu_1"))
		{
			if ($("#id_invasive_line_insitu_1:checked").length > 0)
			{
				$("#id_invasive_line_insitu_2").prop({ checked: false });
				$("#id_invasive_line_insitu_3").prop({ checked: false });
				$("#id_invasive_line_insitu_4").prop({ checked: false });
				$("#id_invasive_line_insitu_5").prop({ checked: false });
				$("#id_invasive_line_insitu_6").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
			else
			{
				$("#id_invasive_line_insitu_2").prop("disabled", false);
				$("#id_invasive_line_insitu_3").prop("disabled", false);
				$("#id_invasive_line_insitu_4").prop("disabled", false);
				$("#id_invasive_line_insitu_5").prop("disabled", false);
				$("#id_invasive_line_insitu_6").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_invasive_line_insitu_2"))
		{
			if ($("#id_invasive_line_insitu_2:checked").length > 0)
			{
				$("#id_invasive_line_insitu_1").prop({ checked: false });
				$("#id_invasive_line_insitu_3").prop({ checked: false });
				$("#id_invasive_line_insitu_4").prop({ checked: false });
				$("#id_invasive_line_insitu_5").prop({ checked: false });
				$("#id_invasive_line_insitu_6").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
			else
			{
				$("#id_invasive_line_insitu_1").prop("disabled", false);
				$("#id_invasive_line_insitu_3").prop("disabled", false);
				$("#id_invasive_line_insitu_4").prop("disabled", false);
				$("#id_invasive_line_insitu_5").prop("disabled", false);
				$("#id_invasive_line_insitu_6").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_invasive_line_insitu_3"))
		{
			if ($("#id_invasive_line_insitu_3:checked").length > 0)
			{
				$("#id_invasive_line_insitu_1").prop({ checked: false });
				$("#id_invasive_line_insitu_2").prop({ checked: false });
				$("#id_invasive_line_insitu_4").prop({ checked: false });
				$("#id_invasive_line_insitu_5").prop({ checked: false });
				$("#id_invasive_line_insitu_6").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
			else
			{
				$("#id_invasive_line_insitu_1").prop("disabled", false);
				$("#id_invasive_line_insitu_2").prop("disabled", false);
				$("#id_invasive_line_insitu_4").prop("disabled", false);
				$("#id_invasive_line_insitu_5").prop("disabled", false);
				$("#id_invasive_line_insitu_6").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_invasive_line_insitu_4"))
		{
			if ($("#id_invasive_line_insitu_4:checked").length > 0)
			{
				$("#id_invasive_line_insitu_1").prop({ checked: false });
				$("#id_invasive_line_insitu_2").prop({ checked: false });
				$("#id_invasive_line_insitu_3").prop({ checked: false });
				$("#id_invasive_line_insitu_5").prop({ checked: false });
				$("#id_invasive_line_insitu_6").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
			else
			{
				$("#id_invasive_line_insitu_1").prop("disabled", false);
				$("#id_invasive_line_insitu_2").prop("disabled", false);
				$("#id_invasive_line_insitu_3").prop("disabled", false);
				$("#id_invasive_line_insitu_5").prop("disabled", false);
				$("#id_invasive_line_insitu_6").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_invasive_line_insitu_5"))
		{
			if ($("#id_invasive_line_insitu_5:checked").length > 0)
			{
				$("#id_invasive_line_insitu_1").prop({ checked: false });
				$("#id_invasive_line_insitu_2").prop({ checked: false });
				$("#id_invasive_line_insitu_3").prop({ checked: false });
				$("#id_invasive_line_insitu_4").prop({ checked: false });
				$("#id_invasive_line_insitu_6").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", false);
			}
			else
			{
				$("#id_invasive_line_insitu_1").prop("disabled", false);
				$("#id_invasive_line_insitu_2").prop("disabled", false);
				$("#id_invasive_line_insitu_3").prop("disabled", false);
				$("#id_invasive_line_insitu_4").prop("disabled", false);
				$("#id_invasive_line_insitu_6").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_invasive_line_insitu_6"))
		{
			if ($("#id_invasive_line_insitu_6:checked").length > 0)
			{
				$("#id_invasive_line_insitu_1").prop({ checked: false });
				$("#id_invasive_line_insitu_2").prop({ checked: false });
				$("#id_invasive_line_insitu_3").prop({ checked: false });
				$("#id_invasive_line_insitu_4").prop({ checked: false });
				$("#id_invasive_line_insitu_5").prop({ checked: false });
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
			else
			{
				$("#id_invasive_line_insitu_1").prop("disabled", false);
				$("#id_invasive_line_insitu_2").prop("disabled", false);
				$("#id_invasive_line_insitu_3").prop("disabled", false);
				$("#id_invasive_line_insitu_4").prop("disabled", false);
				$("#id_invasive_line_insitu_5").prop("disabled", false);
				$("#id_invasive_line_insitu_others").prop("disabled", true);
			}
		}
	});

	$(':radio[id^="id_medical_history_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_medical_history_1"))
		{
			if ($("#id_medical_history_1:checked").length > 0)
			{
				$("#id_medical_history_2").prop({ checked: false });
				$("#id_medical_history_3").prop({ checked: false });
				$("#id_medical_history_4").prop({ checked: false });
				$("#id_medical_history_5").prop({ checked: false });
				$("#id_medical_history_6").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", true);
			}
			else
			{
				$("#id_medical_history_2").prop("disabled", false);
				$("#id_medical_history_3").prop("disabled", false);
				$("#id_medical_history_4").prop("disabled", false);
				$("#id_medical_history_5").prop("disabled", false);
				$("#id_medical_history_6").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_medical_history_2"))
		{
			if ($("#id_medical_history_2:checked").length > 0)
			{
				$("#id_medical_history_1").prop({ checked: false });
				$("#id_medical_history_3").prop({ checked: false });
				$("#id_medical_history_4").prop({ checked: false });
				$("#id_medical_history_5").prop({ checked: false });
				$("#id_medical_history_6").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", true);
			}
			else
			{
				$("#id_medical_history_1").prop("disabled", false);
				$("#id_medical_history_3").prop("disabled", false);
				$("#id_medical_history_4").prop("disabled", false);
				$("#id_medical_history_5").prop("disabled", false);
				$("#id_medical_history_6").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_medical_history_3"))
		{
			if ($("#id_medical_history_3:checked").length > 0)
			{
				$("#id_medical_history_1").prop({ checked: false });
				$("#id_medical_history_2").prop({ checked: false });
				$("#id_medical_history_4").prop({ checked: false });
				$("#id_medical_history_5").prop({ checked: false });
				$("#id_medical_history_6").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", true);
			}
			else
			{
				$("#id_medical_history_1").prop("disabled", false);
				$("#id_medical_history_2").prop("disabled", false);
				$("#id_medical_history_4").prop("disabled", false);
				$("#id_medical_history_5").prop("disabled", false);
				$("#id_medical_history_6").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_medical_history_4"))
		{
			if ($("#id_medical_history_4:checked").length > 0)
			{
				$("#id_medical_history_1").prop({ checked: false });
				$("#id_medical_history_2").prop({ checked: false });
				$("#id_medical_history_3").prop({ checked: false });
				$("#id_medical_history_5").prop({ checked: false });
				$("#id_medical_history_6").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", false);
			}
			else
			{
				$("#id_medical_history_1").prop("disabled", false);
				$("#id_medical_history_2").prop("disabled", false);
				$("#id_medical_history_3").prop("disabled", false);
				$("#id_medical_history_5").prop("disabled", false);
				$("#id_medical_history_6").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_medical_history_5"))
		{
			if ($("#id_medical_history_5:checked").length > 0)
			{
				$("#id_medical_history_1").prop({ checked: false });
				$("#id_medical_history_2").prop({ checked: false });
				$("#id_medical_history_3").prop({ checked: false });
				$("#id_medical_history_4").prop({ checked: false });
				$("#id_medical_history_6").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", true);
			}
			else
			{
				$("#id_medical_history_1").prop("disabled", false);
				$("#id_medical_history_2").prop("disabled", false);
				$("#id_medical_history_3").prop("disabled", false);
				$("#id_medical_history_4").prop("disabled", false);
				$("#id_medical_history_6").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_medical_history_6"))
		{
			if ($("#id_medical_history_6:checked").length > 0)
			{
				$("#id_medical_history_1").prop({ checked: false });
				$("#id_medical_history_2").prop({ checked: false });
				$("#id_medical_history_3").prop({ checked: false });
				$("#id_medical_history_4").prop({ checked: false });
				$("#id_medical_history_5").prop({ checked: false });
				$("#id_medical_history_others").prop("disabled", true);
			}
			else
			{
				$("#id_medical_history_1").prop("disabled", false);
				$("#id_medical_history_2").prop("disabled", false);
				$("#id_medical_history_3").prop("disabled", false);
				$("#id_medical_history_4").prop("disabled", false);
				$("#id_medical_history_5").prop("disabled", false);
				$("#id_medical_history_others").prop("disabled", true);
			}
		}
	});

		
	$(':radio[id^="id_own_medication_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_own_medication_1"))
		{
			if ($("#id_own_medication_1:checked").length > 0)
			{
				$("#id_own_medication_2").prop({ checked: false });
			}
			else
			{
				$("#id_own_medication_2").prop("disabled", false);
			}
		}
		else if ($this.is("#id_own_medication_2"))
		{
			if ($("#id_own_medication_2:checked").length > 0)
			{
				$("#id_own_medication_1").prop({ checked: false });
			}
			else
			{
				$("#id_own_medication_1").prop("disabled", false);
			}
		}
	});

	$(':radio[id^="id_adaptive_aids_with_patient_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_adaptive_aids_with_patient_1"))
		{
			if ($("#id_adaptive_aids_with_patient_1:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_2"))
		{
			if ($("#id_adaptive_aids_with_patient_2:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_3"))
		{
			if ($("#id_adaptive_aids_with_patient_3:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_4"))
		{
			if ($("#id_adaptive_aids_with_patient_4:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_5"))
		{
			if ($("#id_adaptive_aids_with_patient_5:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_6"))
		{
			if ($("#id_adaptive_aids_with_patient_6:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_7").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", false);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_7").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
		else if ($this.is("#id_adaptive_aids_with_patient_7"))
		{
			if ($("#id_adaptive_aids_with_patient_7:checked").length > 0)
			{
				$("#id_adaptive_aids_with_patient_1").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_2").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_3").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_4").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_5").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_6").prop({ checked: false });
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
			else
			{
				$("#id_adaptive_aids_with_patient_1").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_2").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_3").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_4").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_5").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_6").prop("disabled", false);
				$("#id_adaptive_aids_with_patient_others").prop("disabled", true);
			}
		}
	});

	
	$(':radio[id^="id_orientation_"]').click(function()
	{
		var $this = $(this);
		if ($this.is("#id_orientation_1"))
		{
			if ($("#id_orientation_1:checked").length > 0)
			{
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_2"))
		{
			if ($("#id_orientation_2:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_3"))
		{
			if ($("#id_orientation_3:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_4"))
		{
			if ($("#id_orientation_4:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_5"))
		{
			if ($("#id_orientation_5:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_6"))
		{
			if ($("#id_orientation_6:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_7"))
		{
			if ($("#id_orientation_7:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_8"))
		{
			if ($("#id_orientation_8:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_9").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_9").prop("disabled", false);
			}
		}
		else if ($this.is("#id_orientation_9"))
		{
			if ($("#id_orientation_9:checked").length > 0)
			{
				$("#id_orientation_1").prop({ checked: false });
				$("#id_orientation_2").prop({ checked: false });
				$("#id_orientation_3").prop({ checked: false });
				$("#id_orientation_4").prop({ checked: false });
				$("#id_orientation_5").prop({ checked: false });
				$("#id_orientation_6").prop({ checked: false });
				$("#id_orientation_7").prop({ checked: false });
				$("#id_orientation_8").prop({ checked: false });
			}
			else
			{
				$("#id_orientation_1").prop("disabled", false);
				$("#id_orientation_2").prop("disabled", false);
				$("#id_orientation_3").prop("disabled", false);
				$("#id_orientation_4").prop("disabled", false);
				$("#id_orientation_5").prop("disabled", false);
				$("#id_orientation_6").prop("disabled", false);
				$("#id_orientation_7").prop("disabled", false);
				$("#id_orientation_8").prop("disabled", false);
			}
		}
	});
	

	$(':checkbox[id^="id_surgical_history_none_"]').click(function()
	{
		$("#id_surgical_history").prop("disabled", true);
		var $this = $(this);
		if ($this.is("#id_surgical_history_none_1"))
		{
			if ($("#id_surgical_history_none_1:checked").length > 0)
			{
				$("#id_surgical_history").prop("disabled", true);
			}
			else
			{
				$("#id_surgical_history").prop("disabled", false);
			}
		}
	});
});


