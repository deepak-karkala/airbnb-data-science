

function set_dropdown_options(file, dropdown_id, dropdown_name) {
    /*
    var list = '';
    data.forEach(function(d,i) {
        console.log(d);
        list += `<option value="`+d+`">`+d+`</option>`;
    })
    $(dropdown_id).append(list);
    */

    d3.csv(file, function(data) {
        var list = '';
        data.forEach(function(d,i) {
            list += `<option value="`+d[dropdown_name]+`">`+d[dropdown_name]+`</option>`;
        })
        $(dropdown_id).append(list);
    })
}

set_dropdown_options("static/data/list_countries.csv", "#combobox_country", "Country");
set_dropdown_options("static/data/list_cities.csv", "#combobox_city", "City");
set_dropdown_options("static/data/list_neighbourhood.csv", "#combobox_neighbourhood", "Neighbourhood Cleansed");
set_dropdown_options("static/data/list_propertytype.csv", "#combobox_propertytype", "Property Type");
set_dropdown_options("static/data/list_roomtype.csv", "#combobox_roomtype", "Room Type");
set_dropdown_options("static/data/list_bedtype.csv", "#combobox_bedtype", "Bed Type");
set_dropdown_options("static/data/list_cancellationpolicy.csv", "#combobox_cancellationpolicy", "Cancellation Policy");
set_dropdown_options("static/data/list_hostresponsetime.csv", "#combobox_hostresponsetime", "Host Response Time");

