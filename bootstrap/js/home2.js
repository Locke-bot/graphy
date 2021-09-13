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


var canvas = $('#canvas');
cs = canvas[0]
var ctx = canvas[0].getContext('2d');
var dropZone = $("#dnd")

function addToCanvas(file){
        window.img = new Image();
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
        	data = ctx.getImageData(0, 0, canvas.width(), canvas.height()).data
            ajax = $.ajax({
                type: 'POST',
                data: {'name': 'array', 'csrfmiddlewaretoken': csrf_token, 'rgb': `${data}`, 'dim': `${canvas.width()}, ${canvas.height()}`},
                success: function(data){
                    console.log('success inc', data);
                }
            })      	
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
  $("#header").removeClass("d-none");
})
})