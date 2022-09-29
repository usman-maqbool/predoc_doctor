// searc in tabble
    $(document).ready(function() {
  $(".search").keyup(function () {
    var searchTerm = $(".search").val();
    var listItem = $('.results tbody').children('tr');
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('")
    
  $.extend($.expr[':'], {'containsi': function(elem, i, match, array){
        return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
  });
    
  $(".results tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','false');
  });

  $(".results tbody tr:containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','true');
  });

  var jobCount = $('.results tbody tr[visible="true"]').length;
    $('.counter').text(jobCount + ' item');

  if(jobCount == '0') {$('.no-result').show();}
    else {$('.no-result').hide();}
		  });
});



  $(document).ready( function () {
  $('#myTable').DataTable();
} );

    // Loader Model
  $(document).ready(function(){
      $("#myModal").modal('show');
  });

  var elements = document.querySelectorAll('.show_div')
  for (let element of elements ){
    let expandbtn = element.querySelector('.button_show_div')
    expandbtn.addEventListener('click', (e) =>{
      setTimeout(function() {
        $('.show_able_div').removeClass('hide');
        }, 2000);
      });
      $('.button_show_div').on("click",function(){
        $(window).scrollTop(0);
    });
  }

       
  function loadingPage() {
    var div = document.getElementById("loading-wrapper")
    div.style.display = "block";
    setTimeout(function(){ 
      document.getElementById("loading-wrapper").style.display = "none"; 
  }, 
  2000);
}