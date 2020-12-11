const cnv = document.querySelector('canvas')
const ctx = cnv.getContext('2d')

const w = 750
const h = 750

// // rect x: 250, y: 200, w: 250, h: 350 lineWidth: 2
// ctx.beginPath()
// ctx.rect(250, 200, 250, 350)
// ctx.fillStyle = 'green'
// ctx.fill()
// ctx.lineWidth = 2
// ctx.stroke()

// // tri (175, 525), (375, 225), (575, 525)
// ctx.beginPath()
// ctx.moveTo(175, 525)
// ctx.lineTo(375, 225)
// ctx.lineTo(575, 525)
// ctx.closePath()
// ctx.fillStyle = 'yellow'
// ctx.fill()
// ctx.stroke()

function animate (yChange, mouthChange) {
  ctx.clearRect(0, 0 + yChange, w, h)
  // circle x: 375, y: 375, r: 300, start: 0, end: 2π
  ctx.beginPath()
  ctx.arc(375, 375 + yChange, 300, 0, 2 * Math.PI)
  ctx.fillStyle = 'yellow'
  ctx.fill()
  ctx.lineWidth = 5
  ctx.stroke()

  // ellipse x: 375, y; 450, xr: 225, yr: 85, start: 0, end: 2π
  ctx.beginPath()
  ctx.ellipse(375, 450 + yChange, 225 + mouthChange, 85, 0, 0, 2 * Math.PI)
  ctx.fillStyle = 'red'
  ctx.fill()
  ctx.stroke()

  // // eyes x: [275, 475], y: 250, r: 50, start: 0, end: π
  // // pupils x: [275, 475], y: 250, r: 25, start: 0, end: π
  function drawEyes (x) {
    ctx.beginPath()
    ctx.arc(x, 250 + yChange, 50, 0, Math.PI)
    ctx.closePath()
    ctx.fillStyle = 'white'
    ctx.fill()
    ctx.stroke()

    ctx.beginPath()
    ctx.arc(x, 250 + yChange, 25, 0, Math.PI)
    ctx.closePath()
    ctx.fillStyle = 'black'
    ctx.fill()
    ctx.stroke()
  }

  drawEyes(275)
  drawEyes(475)
  yChange--
  mouthChange--
  if (225 + mouthChange <= 85) {
    mouthChange++
  }
  window.requestAnimationFrame(() => animate(yChange, mouthChange))
}

animate(0, 0)
