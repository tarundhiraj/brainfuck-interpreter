/*
    This function returns an HTML request object
*/

function createRequest(){
    try{
        request = new XMLHttpRequest();
    } catch(tryMS){
        try{
            request = new ActiveXObject("Msxml2.XMLHTTP");
        } catch(otherMS){
            try{
                request = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch(failed){
                request = null;
            }
        }
    }
    return request;
}

/*
    This function which adds multiple event handlers to an event
*/

function addEventHandler(object,eventName,handlerFunction){

  if(document.attachEvent){
    object.attachEvent("on" + eventName, handlerFunction);  //for IE
  }

  else if(document.addEventListener){
    object.addEventListener(eventName,handlerFunction,false); //for Chrome, Firefox, Safari, Opera, etc...

  }
}

/*
    This function which removes multiple event handlers from an event
*/

function removeEventHandler(object,eventName,handlerFunction){

  if(document.detachEvent){
    object.detachEvent("on" + eventName, handlerFunction);
  }

  else if(document.removeEventListener){
    object.removeEventListener(eventName,handlerFunction,false);
  }
}
