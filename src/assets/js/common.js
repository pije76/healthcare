$(document).ready(function ()
{
  $('#s-Accordion').fadeOut();
  $('#arrowRight, #s-Accordion').hover(function (e)
  {

    $( "#s-Accordion" ).stop().animate(
    {
      opacity: 1,
      left: "17px",
      width: "toggle"
    }, 1500, function()
    {
    });
  });

  $('#s-canvasPanel_1').fadeOut();
  $('#arrowLeft, #s-canvasPanel_1').hover(function (e)
  {

    $( "#s-canvasPanel_1" ).stop().animate(
    {
      opacity: 1,
      right: "0px",
      width: "toggle"
    }, 1000, function()
    {
    });
  });

  var audioElement = document.createElement("audio");
  audioElement.src = "/static/audio/progress.wav";
  $('#rtr-s-Button_1_0').click(function()
  {
    audioElement.play();
  });

});
