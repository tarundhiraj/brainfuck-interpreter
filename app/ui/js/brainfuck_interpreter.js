/* Initialize page */
window.onload = initPage;

function initPage() {
    attachEventToRunBtn();
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
    This function attaches event to Run button
*/

function attachEventToRunBtn() {
    var runBtn = document.getElementById('run-btn');
    addEventHandler(runBtn, 'click', interpretBFSource);
}

/*
    This function attaches event to Neatify button
*/

function attachEventToNeatifyBtn() {
    var neatifyBtn = document.getElementById('neatify-btn');
    addEventHandler(neatifyBtn, 'click', neatifyBFSource);
}