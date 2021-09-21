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
var canvas = $('#canvas');
var unit = $('#unit')
var ppi = 96 // pixel per inch
var cs = canvas[0]
var ctx = canvas[0].getContext('2d');
var dropZone = $("#dnd")
var dis = 2 // distance from centre

function addToCanvas(file){
        img = new Image();
        img.crossOrigin = 'anonymous';
        frd = new FileReader()
        frd.onload = function(e){
            img.src = e.target.result
        }
        frd.readAsDataURL(file)
        //dropZone.empty()
        //image.appendTo(dropZone)
        
        img.onload = function() {
            if ($(document).height > $(window).height()) {
                    dropZone.css('position', 'initial')
                }
            cs.width=img.width
            cs.height=img.height
            dropZone.children().splice(1,).forEach(e=>e.remove())
            /*dropZone.remove('p')
            $('p.drop-text').remove()
            $('#file-button').parent().remove()*/
        	ctx.drawImage(img, 0, 0);
            dropZone.css('width', 'auto')
            dropZone.css('height', 'auto')
        	canvas.removeClass('d-none')
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
    //console.log('geteqn clicked', $("#xscale")[0].checkValidity() && $("#yscale")[0].checkValidity())
    //sendMessage('mad o', 5000)
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

  function getSymbol(text){ // gives px if given "pixel (px)" has input
      return text.substr(text.indexOf('(')+1, 2)
  }

  function connectPoint(a, b){
      console.log('connecting...')
      let path = new Path2D
      path.moveTo(a[0], a[1])
      path.lineTo(b[0], b[1])
      ctx.stroke(path)
      //let rest = points.splice(2,)
      //for (let point of rest){
           //removePoint(point)
      //}
  }
     
  function removeLine(point){
      //console.log(point, 'pointt', point[3], point[4], point[5].width, point[5].height)
      ctx.putImageData(point[5], point[3], point[4])
      let path = new Path2D
      //path.rect(point[3], point[4], point[5].width, point[5].height)
      //ctx.stroke(path)
  }

  function removePoint(point){
      console.log('remove', point[3])
      let x = point[0]
      let y = point[1]
      let img = point[2]
      //console.log(typeof img)
      
      //ctx.clearRect(x-dis, y-dis, 2*dis, 2*dis)
      ctx.putImageData(img, x-dis, y-dis)
      //ctx.save()
      //ctx.clearRect(0, 30, 50, 50)
      console.log("clearing", x-dis, y-dis, x+dis, y+dis)
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

  canvas.on('click', function(ev){
        let oe = ev.originalEvent
        let x = oe.layerX
        let y = oe.layerY
        let data = ctx.getImageData(x-dis, y-dis, 2*dis, 2*dis)
        
        let path = new Path2D
        path.moveTo(x-dis, y-dis)
        path.lineTo(x+dis, y+dis)
        path.moveTo(x+dis, y-dis)
        path.lineTo(x-dis, y+dis)
        ctx.strokeStyle = "black"
        ctx.stroke(path)
        
        let point = [x, y, data]
        points.unshift(point)
       
        let rest = points.splice(2,)
        for (let point of rest){
           if (point.length > 3){
               console.log('removal mode')
               removeLine(point)
           }
           removePoint(point)
           console.log('pre removal mode')
        }
        
        if (points.length > 1){
            let p = points[1], a=Math.min(p[0], x), b=Math.min(p[1], y);
            let img = ctx.getImageData(a, b, Math.max(p[0], x)-a+dis, Math.max(p[1], y)-b+dis);
            p.push(a, b, img);
        }
        
        if (points.length > 1){
            connectPoint(points[0], points[1])
            if (!unit.val()){
                unit.val("pixel (px)")
            }
            let a = points[0], b = points[1]
            let length = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
            //let length = 
            unit.prev().val(getLength(length, getSymbol(unit.val())))
        }
})
})