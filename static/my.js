$(document).ready(function()
{
    var infinite_scroll_lock = false;

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

    $(window).scroll(function () { 
        if ($(window).scrollTop() >= $(document).height() - $(window).height()) {
            if (!infinite_scroll_lock) {
                infinite_scroll_lock = true;
                img_hash = $('.latest_img').last().attr('href');
                $.ajax({
                    url: '/latest/',
                    type: 'GET',
                    data: {'last': img_hash},
                    success: function (data) {
                        $('#latest_imgs').append(function() {
                            console.log(data);  
                            return data;
                        });
                        },
                    complete: function(data) {
                        if (data.responseText != '') {
                            console.log(data);
                            /*keep locked if we are at the oldest pic*/
                            infinite_scroll_lock = false;
                        };
                        }                    
                    
                });
            };
        };
    });
});