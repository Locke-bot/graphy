$(function(){
/*function dragOverHandler(ev) {
  console.log('File(s) in drop zone'); 

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
}*/
$("#dnd").on('dragover', function (ev) {
  console.log('File(s) in drop zone'); 

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
})

var points = []
var unit= $("#unit")
var dropZone = $("#dnd")
var dis = 2 // distance from centre
var dotArray = []
var pathArray = []
var lineArray = []

function addToCanvas(file){
        img = new Image();
        img.crossOrigin = 'anonymous';
        frd = new FileReader()
        frd.onload = function(e){
            img.src = e.target.result
        }
        frd.readAsDataURL(file);
        console.log(img, typeof img)
        img.onload = function(){
            if ($(document).height > $(window).height()) {
                    dropZone.css('position', 'initial')
                }
            //var paper = new Raphael("canvas", img.width, img.height);
            var paper = new Raphael("canvas", img.width, img.height);
            console.log(paper)
            var image = paper.image(img.src, 0, 0, img.width, img.height)
            image.click(function(ev){
                let x = ev.layerX
                let y = ev.layerY
                //M10,10m-2,-2l4,4m0,-4l-4,4
                let path = paper.path(
                    Raphael.format(
                        "M{0} {1} m {2} {3} l {4} {5} m {6} {7} l {8} {9}",
                        x, y, -dis, -dis, 2*dis, 2*dis, 0, -2*dis, -2*dis, 2*dis
                    )
                );
                console.log(path)
                let svg_c = $("svg").children(); // all svg children
                $(svg_c[svg_c.length-1]).addClass("dot");
                let svg_d = $("path.dot").toArray();
                if (pathArray.length > 1){
                    pathArray.shift().remove();
                }
                pathArray.push(path);
                dotArray.unshift([x, y]);
                console.log(svg_d, "swag");
                if (dotArray.length > 1){
                    if (lineArray.length){
                        console.log(lineArray);
                        lineArray.shift().remove();
                        console.log("modebi");
                    }
                    if (!unit.val()){
                        unit.val("pixel (px)")
                    }
                    connectPoints(paper, dotArray[0], dotArray[1]);
                    let svg_c = $("svg").children(); // all svg children
                    $(svg_c[svg_c.length-1]).addClass("line");
                }
            })
            dropZone.children().splice(1,).forEach(e=>e.remove())
            dropZone.css('width', 'auto')
            dropZone.css('height', 'auto')
            
            let canvas = $('<canvas>');
            let cs = canvas[0]
            cs.width=img.width
            cs.height=img.height
            console.log(cs, 'ciess')
            let ctx = cs.getContext('2d');            
        	ctx.drawImage(img, 0, 0);
        	window.data = ctx.getImageData(0, 0, canvas.width(), canvas.height()).data
            ajax = $.ajax({
                type: 'POST',
                data: {'name': 'sendImageData', 'csrfmiddlewaretoken': csrf_token, 'rgb': `${data}`, 'dim': `${canvas.width()}, ${canvas.height()}`},
                success: function(data){
                    console.log('pre success', data);
                }
            })            
        };
    }

  function getSymbol(text){ // gives px if given "pixel (px)" has input
      return text.substr(text.indexOf('(')+1, 2)
  }

  function getLength(length, unit){ // length always in pixel, to be converted to unit
        console.log(unit)
        if (unit == 'px'){
            return length
        }
        if (unit == "in"){
            return length/ppi
        }
        if (unit == "cm"){
            return 2.54*length/ppi
        }
        if (unit == "pt"){
            return 72*length/ppi // 72 points per inch
        }
  }

  function connectPoints(paper, a, b){
        let x1=a[0], y1=a[1], x2=b[0], y2=b[1];
        let path = paper.path(
            Raphael.format(
                "M{0} {1}  L {2} {3}",
                x1, y1, x2, y2
            )
        );
        lineArray.unshift(path);
        let length = ((x1-x2)**2 + (y1-y2)**2)**0.5;
        //console.log(`distance = ${length}`);
        unit.prev().val(getLength(length, getSymbol(unit.val())))
  }

$("#get-scale").on("click", function(){
    console.log('getscale clicked')
    ajax = $.ajax({
        type: 'POST',
        data: {'name': 'getScale', 'csrfmiddlewaretoken': csrf_token},
        success: function(data){
            if (data["xunit"]){
                $("#xunit").val(data["xunit"])
            }
            if (data["yunit"]){
                $("#yunit").val(data["yunit"])
            }
            let response = data.response;
            console.log('scale success', response, data);
            sendMessage(response, 3000);
        }
    })
})
// d = ""
function sendMessage(message, timeout){
    //let message_body = `<div id="message">${message}</div>`
    console.log('instant messaging')
    message_body = $("<div />", {
                        'text': message,
                        'style': 'font-size: large;background-color: azure; display: inline-flex; padding: 2px; margin-bottom: 10px;'
                    })
    //<div style="text-align: center;"><div id="message" style="background-color: azure; display: inline; /*! padding: 10px; */ /*! margin-bottom: 10px; */justify-content: center;/*! width: 300px; */text-align: center;">mad o</div><div></div></div>
    outer_message = $("<div />", {
                    'class': 'message',
                    'style': 'text-align: center;',
    })
    outer_message.append(message_body)
    $("#dnd").parent().prepend(outer_message)
    setTimeout(function(){
        outer_message.animate({
            'height' : 0
        }, 2000, function() {
            $(".message").remove();
        });
    }, timeout)
}

$("#get-eqn").on("click", function(){
    if ($("#xscale")[0].checkValidity() && $("#yscale")[0].checkValidity()){            
        console.log('geteqn valid')
        x = $($("#xscale input")[0]).val()
        xunit = $("#xunit").val()
        lxunit = $("#lxunit").val()
        
        y = $($("#yscale input")[0]).val()
        yunit = $("#yunit").val()
        lyunit = $("#lyunit").val()
        
        ajax = $.ajax({
            type: 'POST',
            data: {'name': 'getEqn', 'csrfmiddlewaretoken': csrf_token, 'scalex': xunit, 'scaley': yunit, 'dbtx': x+lxunit.substr(x.indexOf('(')+1, 2), 'dbty': y+lyunit.substr(y.indexOf('(')+1, 2)},
            success: function(data){
                console.log('success res', data.result);
            }
        })
    }
    else {
        sendMessage("all fields are required", 3000)
    }
})

$("#dnd").on('drop', function(ev) {
  ev = ev.originalEvent
  console.log('File(s) dropped');
  dropZone.css('position', 'relative')
  // Prevent default behavior (Prevent file from being opened in new tab by browser)
  ev.preventDefault();

  if (ev.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.items.length; i++) {
      // If dropped items aren't files, reject them
      item = ev.dataTransfer.items[i]
      if (item.kind === 'file') {
        if (item.type.startsWith('image')){
            var file = item.getAsFile();
            console.log('... file[' + i + '].name = ' + file.name, file, 'iff');
            addToCanvas(file)
            //image = $('<img>')
        }
      }
    }
  } else {
    // Use DataTransfer interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.files.length; i++) {
      file = ev.dataTransfer.files[i]
      console.log('... file[' + i + '].name = ', file, typeof file, 'else');
    }
  }
  $("#title").next().next().removeClass("d-none");
  })

})