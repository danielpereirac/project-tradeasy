// A $( document ).ready() block.
$( document ).ready(function() {
    $('.forms_cards').hide();
    $('.forms_books').hide();
    $('.forms_clothes').hide();
    $('.forms_games').hide();
    $('#category').on('change', function (e) {
        // var optionSelected = $("option:selected", this);
        // var valueSelected = this.value;
        var selected = $( "#category option:selected" ).val();
        if(selected == 'card'){
            $('.forms_cards').show();
            $('.forms_books').hide();
            $('.forms_clothes').hide();
            $('.forms_games').hide();
            
        } 
        else if(selected == 'games'){
            $('.forms_cards').hide();
            $('.forms_books').hide();
            $('.forms_clothes').hide();
            $('.forms_games').show();
        }
        else if(selected == 'books'){
            $('.forms_cards').hide();
            $('.forms_books').show();
            $('.forms_clothes').hide();
            $('.forms_games').hide();
        }
        else if(selected == 'clothes'){
            $('.forms_cards').hide();
            $('.forms_books').hide();
            $('.forms_clothes').show();
            $('.forms_games').hide();
        }
      
        
      
    });
});