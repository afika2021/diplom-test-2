$(document).ready(function () {

var timeList = 1000;
var TimeView = 500;
var RadioBut = true;

var slideNum = 1;
var slideTime;
slideCount = $("#slider_p .slide_p").length;

var animSlide = function(arrow){
    clearTimeout(slideTime); 

    if(arrow == "next"){
	  if(slideNum == slideCount) { slideNum=1; }
	  else{slideNum++}
       translateWidth = -$('#active-slide_p').width() * (slideNum - 1);
       $('#slider_p').css({'transform': 'translate(' + translateWidth + 'px, 0)'});
    }
    else if(arrow == "prew")
    {	
       if(slideNum == 1) { slideNum=slideCount; }
	  else{slideNum-=1}
	  translateWidth = -$('#active-slide_p').width() * (slideNum - 1); 
       $('#slider_p').css({'transform': 'translate(' + translateWidth + 'px, 0)'});
    }else{
       slideNum = arrow;
	  translateWidth = -$('#active-slide_p').width() * (slideNum -1);
       $('#slider_p').css({'transform': 'translate(' + translateWidth + 'px, 0)'});
    }

    $(".ctrl-select_p.active").removeClass("active");
    $('.ctrl-select_p').eq(slideNum - 1).addClass('active');
}

    if(RadioBut){
    var $linkArrow = $('<a id="prewbutton_p" href="#">&lt;</a><a id="nextbutton_p" href="#">&gt;</a>')
        .prependTo('#active-slide_p');
        $('#nextbutton_p').click(function(){
           animSlide("next");
           return false;
           })
        $('#prewbutton_p').click(function(){
           animSlide("prew");
           return false;
           })
    }
        var adderSpan = '';
        $('.slide').each(function(index) {
               adderSpan += '<span class = "ctrl-select_p">' + index + '</span>';
           });
        $('<div class ="Radio-But_p">' + adderSpan +'</div>').appendTo('#slider-wrap_p');
        $(".ctrl-select_p:first").addClass("active");
        $('.ctrl-select_p').click(function(){
        var goToNum = parseFloat($(this).text());
        animSlide(goToNum + 1);
        });
        var pause = false;
        var rotator = function(){
               if(!pause){slideTime = setTimeout(function(){animSlide('next')}, TimeView);}
               }
        $('#slider-wrap_p').hover(
           function(){clearTimeout(slideTime); pause = true;},
           function(){pause = false; rotator();
           });
        
    var clicking = false;
    var prevX;
    $('.slide_p').mousedown(function(e){
        clicking = true;
        prevX = e.clientX;
    });

    $('.slide_p').mouseup(function() {
     clicking = false;
    });

    $(document).mouseup(function(){
        clicking = false;
    });

    $('.slide_p').mousemove(function(e){
        if(clicking == true)
         {
             if(e.clientX < prevX) { animSlide("next"); clearTimeout(slideTime); }
             if(e.clientX > prevX) { animSlide("prew"); clearTimeout(slideTime); }
           clicking = false;
        }
    });
    $('.slide_p').hover().css('cursor', 'pointer');
    rotator();  

});