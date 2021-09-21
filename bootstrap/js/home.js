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
  $("#title").next().removeClass("d-none");
  })

  function connectPoint(a, b){
      ctx.moveTo(a[0], a[1])
      ctx.lineTo(b[0], b[1])
      ctx.stroke()
      //let rest = points.splice(2,)
      //for (let point of rest){
           //removePoint(point)
      //}
  }

  function removePoint(point){
      let x = point[0]
      let y = point[1]
      let img = point[2]
      console.log(typeof img)
      ctx.clearRect(x-dis, y-dis, 2*dis, 2*dis)
      ctx.putImageData(img, x-dis, y-dis)
      //ctx.save()
      //ctx.clearRect(0, 30, 50, 50)
      console.log("clearing", x-dis, y-dis, x+dis, y+dis)
  }

  canvas.on('click', function(ev){
          let oe = ev.originalEvent
          let x = oe.layerX
          let y = oe.layerY
          console.log(oe, x, y)
          let data = ctx.getImageData(x-dis, y-dis, 2*dis, 2*dis)
          //let line2 = ctx.getImageData()
          ctx.moveTo(x-dis, y-dis)
          ctx.lineTo(x+dis, y+dis)
          ctx.moveTo(x+dis, y-dis)
          ctx.lineTo(x-dis, y+dis)
          ctx.stroke()
          let point = [x, y, data]
          points.unshift(point)
          console.log(data)
          //delete ctx
          console.log(ctx)
          console.log(points, 'pre pre')
          
          if (points.length > 1){
              points[1].p
              connectPoint(points[0], points[1])
          }
          
          let rest = points.splice(2,)
          for (let point of rest){
             removePoint(point)
          }
          //console.log(points, rest, 'pre')
          points = points.concat(rest)
          console.log(points, 'post')
          //console.log(oe, oe.target.x, oe.target.y)
  })

}) // exit