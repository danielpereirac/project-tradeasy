    $(document).ready(function(){

        $('#my-itens-toggle').click(function(){
            $('#my-itensShow').slideToggle('slow');
            $('.plus').toggle();
            $('.minus').toggle();
        });
    });

