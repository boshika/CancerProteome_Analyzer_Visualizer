function runSearch(term) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#protein_search').serialize();

    $.ajax({
        url: './protein.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    console.log(data);
    // set the span that lists the match count
    $('#match_count').text( data.match_count );

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;

        // create a row and append it to the body of the table
        // $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');

        // add the product column
        $('<h2/>', { "text" : item.product} ).appendTo('.protein');
        $('<td/>', { "text" : item.length} ).appendTo('#uniprot');
        $('<td/>', { "text" : item.description} ).appendTo('#uniprot');
        $('<td/>', { "text" : item.GO} ).appendTo('#uniprot');

        $('<td/>', { "text" : item.model} ).appendTo('#pdb');
        $('<td/>', { "text" : item.chains} ).appendTo('#pdb');
        $('<td/>', { "text" : item.residues} ).appendTo('#pdb');
        $('<td/>', { "text" : item.atoms} ).appendTo('#pdb');

    });

    // now show the result section that was previously hidden
    $('#results').show();
}

// run our javascript once the page is ready
$(document).ready( function() {

    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });

    $('#ERRB2').click( function() {
        alert("Works");
    });
});
