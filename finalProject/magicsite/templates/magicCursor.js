function YY_Mousetrace(evnt) { 
if (yyns4) 
{if (evnt.pageX) {yy_ml=evnt.pageX; yy_mt=evnt.pageY;} 
}
else{
yy_ml=(event.clientX + document.body.scrollLeft);
yy_mt=(event.clientY + document.body.scrollTop);
}
if (yy_tracescript)eval(yy_tracescript)
}


function m()
{
document.all.cursor.style.left=yy_ml-85
document.all.cursor.style.top=yy_mt
}

var yyns4=window.Event?true:false;
var yy_mt = 0;
var yy_ml = 0;
if (yyns4) document.captureEvents(Event.MOUSEMOVE);
document.onmousemove = YY_Mousetrace;
yy_tracescript = 'm()';


