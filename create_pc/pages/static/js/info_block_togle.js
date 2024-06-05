$(document).ready(function() {

    $('div.block_2').css("display", "none").fadeOut(300);
    $('div.block_3').css("display", "none").fadeOut(300);

    $('a.block_1_togle').click(function (event) {
        $('div.block_1').fadeIn(500);
        $('div.block_2').fadeOut(0);
        $('div.block_3').fadeOut(0);
    })
    
    $('a.block_2_togle').click(function (event) {
        $('div.block_1').fadeOut(0);
        $('div.block_2').fadeIn(500).css("display", "flex");
        $('div.block_3').fadeOut(0);
    })

    $('a.block_3_togle').click(function (event) {
        $('div.block_1').fadeOut(0);
        $('div.block_2').fadeOut(0);
        $('div.block_3').fadeIn(500).css("display", "flex");
    })
})
