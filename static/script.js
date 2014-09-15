function hexFromRGB(r, g, b) {
    var hex = [
        r.toString( 16 ),
    g.toString( 16 ),
    b.toString( 16 )
        ];
    $.each( hex, function( nr, val ) {
        if ( val.length === 1 ) {
            hex[ nr ] = "0" + val;
        }
    });
    return hex.join( "" ).toUpperCase();
}

function setColor(r, g, b) {
    $.ajax({
        url: "/set/" + r + "," + g + "," + b
    })
}

function updateLight() {
    var value = $( "#light" ).slider( "value" );
    setColor(value, value, value);
}

function updateUIColor() {
    var red = $( "#red" ).slider( "value" ),
        green = $( "#green" ).slider( "value" ),
        blue = $( "#blue" ).slider( "value" ),
        hex = hexFromRGB( red, green, blue );
    $( "#swatch" ).css( "background-color", "#" + hex );
}

function updateColor() {
    updateUIColor();
    var red = $( "#red" ).slider( "value" ),
        green = $( "#green" ).slider( "value" ),
        blue = $( "#blue" ).slider( "value" );
    setColor(red, green, blue);
}

$(function() {
    $( "#red" ).slider({
        orientation: "horizontal",
        range: "min",
        max: 255,
        value: $("#red").data("value"),
        slide: updateUIColor,
        change: updateColor
    });
    $( "#green").slider({
        orientation: "horizontal",
        range: "min",
        max: 255,
        value: $("#green").data("value"),
        slide: updateUIColor,
        change: updateColor
    });
    $( "#blue").slider({
        orientation: "horizontal",
        range: "min",
        max: 255,
        value: $("#blue").data("value"),
        slide: updateUIColor,
        change: updateColor
    });
    $( "#light").slider({
        orientation: "horizontal",
        range: "min",
        max: 255,
        value: $("#light").data("value"),
        change: updateLight
    });
    updateUIColor;
});
