$(document).ready(function() {
        $(".remcom").click(function() {
            console.log('delete comment');
            var comment_id = $(this).attr('id');
            console.log(comment_id);
            $.ajax({
                url: '/details/'+ comment_id,
                success: function(response)
                {
                   console.log("success");
                    $(this).parent().parent().parent().hide();
                }
            });
          
        });


        $(".mark").click(function() {
            var article_id = $(this).attr('id');
            console.log(article_id);
            $.ajax({
                url: '/mark/'+ article_id +'/',
                success: function(response)
                {
                   console.log("success");
                   
                }
            });
          
        });



        $(".rempos").click(function() {
            console.log('delete post');
            var p_id = $(this).attr('id');
            console.log(p_id);
            $.ajax({
                url: '/delete/post/'+ p_id,
                success: function(response)
                {
                   console.log("success");
                }
            });
           $(this).parent().parent().parent().hide();
        });
        $('.show_comment').click(function(){
            $('table tr:first-child').show()

        });
    });
