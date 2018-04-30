var adults = "#id_confirmed_adults";
var children = "#id_confirmed_children";
var toddlers = "#id_confirmed_toddlers";
var transport = "#id_transport";
var night = "#id_night_stay";
var food = "#id_food_type";
var dis = "disabled";
var rfc = ".reveal-for-confirm";

var confirm = function(delay){
  if(($("#id_confirm")).val() == "on"){
    $(rfc).show(delay);
    $(adults).removeAttr(dis);
    $(children).removeAttr(dis);
    $(toddlers).removeAttr(dis);
    $(transport).removeAttr(dis);
    $(night).removeAttr(dis);
    $(food).removeAttr(dis);
  } else {
    $(rfc).hide(delay);
    $(adults).attr(dis, dis);
    $(children).attr(dis, dis);
    $(toddlers).attr(dis, dis);
    $(transport).attr(dis, dis);
    $(night).attr(dis, dis);
    $(food).attr(dis, dis);
  }
}

$( document ).ready(function(){
  $("#id_confirm").change(function(){
    confirm(500);
  });
  confirm(0);
});
