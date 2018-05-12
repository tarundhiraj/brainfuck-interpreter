/* Initialize page */
window.onload = initPage;

function initPage() {
    attachEventsToRunBtn();
    attachEventToNeatifyBtn();
}

/*
    This function sends the Brainfuck source code to the server and populates the output in the output
    text area
*/

function interpretBFSource() {

    /* Disable Run button while waiting for result */
    document.getElementById('run-btn').disabled = true;

    /* Create HTML request */
    var htmlRequest = createRequest();

    /* URL of the REST API */
    var url = 'interpreter/';

    /* Get Brainfuck source code */
    var bfSrcCode = document.getElementById('bf-src-code-ta').value;

    /* Get Result text area object */
    var resultTaObj = document.getElementById('interpreted-result-ta');
    resultTaObj.value = '';

    if(htmlRequest == null) {
        alert('Unable to htmlRequest object');
    } else {
        htmlRequest.onreadystatechange = function() {
            if(this.readyState < 4) {
                resultTaObj.disabled = true;
            }
            if(this.readyState == 4 && this.status == 200) {
                resultTaObj.value = this.responseText;
            }
        };
        htmlRequest.open('POST', url, true);
        htmlRequest.send(bfSrcCode);
    }

    document.getElementById('run-btn').disabled = false;
}

/*
    This function sends the Brainfuck source code to the server and populates the neatified code
    in the source area
*/

function neatifyBFSource() {

    /* Disable Neatify button while waiting for result */
    document.getElementById('neatify-btn').disabled = true;

    /* Create HTML request */
    var htmlRequest = createRequest();

    /* URL of the REST API */
    var url = 'formatter/';

    /* Get Brainfuck source code text area object */
    var bfSrcTaObj = document.getElementById('bf-src-code-ta');

    /* Get Brainfuck source code */
    var bfSrcCode = bfSrcTaObj.value;

    if(htmlRequest == null) {
        alert('Unable to htmlRequest object');
    } else {
        htmlRequest.onreadystatechange = function() {
            if(this.readyState < 4) {
                /* bfSrcTaObj.disabled = true; */
            }
            if(this.readyState == 4 && this.status == 200) {
                bfSrcTaObj.value = this.responseText;
            }
        };
        htmlRequest.open('POST', url, true);
        htmlRequest.send(bfSrcCode);
    }

    document.getElementById('neatify-btn').disabled = false;
}

/*
    This function attaches event(s) to Run button
*/

function attachEventsToRunBtn() {
    var runBtn = document.getElementById('run-btn');
    addEventHandler(runBtn, 'click', interpretBFSource);
    addEventHandler(runBtn, 'click', addRecentCode);
}

/*
    This function attaches event(s) to Neatify button
*/

function attachEventToNeatifyBtn() {
    var neatifyBtn = document.getElementById('neatify-btn');
    addEventHandler(neatifyBtn, 'click', neatifyBFSource);
}


function randomString(length){
    var str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    randomstr = '';

    for(i=0; i < length; ++i){
        randomstr += str[Math.floor(Math.random()*str.length)];
    }

    return randomstr;
}

function hashCode(str){
    var hash = 17;
    for(var i = 0; i<str.length; ++i){
        hash = 31*hash + str[i]
    }

    return hash;
}


function addRecentCode(){
    var code = document.getElementById('bf-src-code-ta').value;
    //code validation
    //Code is empty
    if(code == ''){
       alert("Interpreter needs bf source code to execute.");
       return;
    }
    //Code is not bf
    var pat = /^[<>.+\[\]\s\-]+$/;
    if(code.search(pat) == -1){
        alert("Not in proper brainfuck language");
        return;
    }
    var hash = hashCode(code);
    if(localStorage.getItem(hash) != null){
        return;
    }
    //1 is dummy value
    localStorage.setItem(hash,1);
    var tag = randomString(6);
    localStorage.setItem(tag, code);

    recent_code = document.getElementById('recent_code');
    li_element = document.createElement('li');
    anchor = document.createElement('a');
    addEventHandler(anchor, 'click', function(){
        document.getElementById('bf-src-code-ta').value = localStorage.getItem(tag);
        return false;
    });
    anchor.innerHTML = tag;
    anchor.href = '#';
    li_element.appendChild(anchor);
    recent_code.appendChild(li_element);

}