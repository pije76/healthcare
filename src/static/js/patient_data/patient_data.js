var t = $('#t_add_row').DataTable();



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
                    $("#t_add_row tbody").html(data.html_documents_list);
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
                    $("#t_add_row tbody").html(data.html_documents_list);
                    $("#exampleModal").modal("hide");
                    row.addClass('selected');
                    t.row('.selected').remove().draw(false);
                }
                else
                {
                    $("#exampleModal .modal-content").html(data.html_form);
                    row.addClass('selected');
                    t.row('.selected').remove().draw(false);
                }
            }
        });
        return false;
    };

    /* Binding */

    // Create documents
    $(".addRow").click(loadForm);


    // Update documents
    $("#t_add_row tbody").on("click", ".edit-row-btn", loadForm);
    $("#exampleModal").on("submit", ".documents-update-form", saveEditForm);

    // Delete documents
    $("#t_add_row tbody").on("click", ".delete-row-btn", loadForm);
    $("#exampleModal").on("submit", ".documents-delete-form", saveDeleteForm);


});
