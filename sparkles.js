document.addEventListener('mousemove', (e) => {
  const star = document.createElement('div');
  star.className = 'cursor-sparkle';
  star.textContent = ['✦', '✧', '★', '☆'][Math.floor(Math.random() * 4)];
  star.style.left = e.pageX + 'px';
  star.style.top = e.pageY + 'px';
  document.body.appendChild(star);

  setTimeout(() => star.remove(), 700);
});