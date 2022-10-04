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

  // Model Show Load
  $(document).ready(function(){
      $("#myModal").modal('show');
  });


  //  Spinner
  function loadingPage() {
    var div = document.getElementById("loading-wrapper")
    div.style.display = "block";
    setTimeout(function(){ 
      document.getElementById("loading-wrapper").style.display = "none"; 
  }, 
  2000);
}
// axios request
let get_ajax_request = document.querySelectorAll('.button_show_div')
var show_data = document.getElementById('show_able_div')
for (let element of get_ajax_request){
  element.addEventListener('click',(e) => {
    setTimeout(function() {
    // spinner timeout
      $('.show_able_div').removeClass('hide');
      }, 2000);
    // scroll top
      $('.button_show_div').on("click",function(){
        $(window).scrollTop(0);
    });
    // axios request
    id = element.getAttribute('data-target').slice(4)
    axios.get('/all-patient/' +id).then(function(resp){
      show_data.innerHTML = resp.data
    }).catch(function(err){
      console.log(err)
    })
    // Hide current div
    var current_div = document.getElementById('current_div')
    if( current_div.style.display = 'block'){
      current_div.style.display = 'none'
    }
  })
}    
   