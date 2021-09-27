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
//var canvas = $('#canvas');
//var cs = canvas[0]
//var ctx = canvas[0].getContext('2d');
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
        img.onload = function(){
            if ($(document).height > $(window).height()) {
                    dropZone.css('position', 'initial')
                }
            //var paper = new Raphael("canvas", img.width, img.height);
            var paper = new Raphael("canvas", img.width, img.height);
            var image = paper.image(img.src, 0, 0, img.width, img.height)
            dropZone.children().splice(1,).forEach(e=>e.remove())
            dropZone.css('width', 'auto')
            dropZone.css('height', 'auto')
        };
    }

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
  })

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

  /*canvas.on('click', function(ev){
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
              let img = ctx.getImageData(a, b, Math.max(p[0], x)-a+dis, Math.max(p[1], y)-b+dis)
              p.push(a, b, img)
          }
          
          if (points.length > 1){
              connectPoint(points[0], points[1])
          }
  })*/
})