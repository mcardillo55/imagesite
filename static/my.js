$(document).ready(function()
{
    $('#myModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var url = button.data('url'); //data from data-url parameter in modal button
        if (url) {
            $.ajax({
                url: url,
                type: 'GET',
                success: function (data) {
                    var modal = $('#myModal');
                    modal.find('.modal-content').html(data);
                }
            });
        }
    });
});