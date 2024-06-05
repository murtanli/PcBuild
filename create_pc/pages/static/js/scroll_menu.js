function slowScroll(id) {
    var offset = 0;
    $('html, body').animate({
       scrollTop: $(id).offset().top - offset
    }, 800);
    return false;
 }


 $(document).ready(function(){
	$(window).scroll(function(){
		if($(window).scrollTop()>200){
			$('svg').fadeIn(800)
		}else{
			$('svg').fadeOut(600)
		}
        if($(window).scrollTop()<200){
			$('svg').css("display", "none")
		}
	});
});
