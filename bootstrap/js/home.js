$(function(){
    console.log('home')

    var canvas = $('#canvas');
    cs = canvas[0]
    var ctx = canvas[0].getContext('2d');
    var dropZone = $("#dnd")
    
    $("#dnd").on('dragover', function (ev) {
      console.log('File(s) in drop zone');
      // Prevent default behavior (Prevent file from being opened)
      ev.preventDefault(true);
    })    
    
    function shower(){
        console.log(ctx)
    	const imageData = ctx.getImageData(0, 0, canvas.width(), canvas.height());
    	const data = imageData.data;
        //console.log("data coming up")
        //console.log(data);
    }
    
    function addToCanvas(file){
        var img = new Image();
        img.crossOrigin = 'anonymous';
        frd = new FileReader()
        frd.onload = function(e){
            img.src = e.target.result
            //$('span.dimension').text(e.target.size)
        }
        console.log(frd)
        frd.readAsDataURL(file)
        //dropZone.empty()
        //image.appendTo(dropZone)
        
        img.onload = function() {
            console.log(img, img.width, img.height, $(window).height())
            if ($(document).height > $(window).height()) {
                    dropZone.css('position', 'initial')
                }
            cs.width=img.width
            cs.height=img.height
            dropZone.children().splice(1,).forEach(e=>e.remove())
        	ctx.drawImage(img, 0, 0);
            dropZone.css('width', 'auto')
            dropZone.css('height', 'auto')
        	canvas.removeClass('d-none')
        };
    }    
    
    $("#dnd").on('drop', function(ev) {
      ev = ev.originalEvent
      // Prevent default behavior (Prevent file from being opened in new tab by browser)
      ev.preventDefault();
      console.log('File(s) dropped');
      /*dropZone.css('position', 'relative')*/
    
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
      shower();
    })
})