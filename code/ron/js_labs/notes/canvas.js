


const cnv = document.querySelector('canvas');
const ctx = cnv.getContext('2d')

const w = 750;
const h = 750;

//basic rectangle inside canvas
ctx.beginPath()
ctx.rect(250, 200, 250, 350);
ctx.fillstyle = 'green';
ctx.stroke();
ctx.fill();
ctx.lineWidth = 2;

//basic triangle inside canvas
ctx.beginPath() // first, call beginPath() to start a new path
ctx.moveTo(175, 525) // imagine the path is being drawn by a pencil; moveTo says pick up the pencil and put it down here, at these (x, y) coordinates
ctx.lineTo(375, 225) // lineTo says draw a straight line from the previous coordinates to this point
ctx.lineTo(575, 525) // then to this point
ctx.closePath() // finally, closePath will draw a line back to where we started
ctx.fillStyle = 'yellow'
ctx.fill()
ctx.stroke()



