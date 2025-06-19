let images = ["img2-BMW-M4-CSL.png", "img5-Mercedes-AMG-GT.png", "img8-Audi-R8-V10-GT.png", "img11-Ferrari-SF90-Stradale.png", "img14-Lamborghini-Revuelto.png", "img17-Maserati-MC20.png", "img20-Toyota-GR-Supra.png", "img23-Honda-NSX-Type-S.png", "img26-Nissan-GT-R-Nismo.png"];
let index = 0;

let imageElement = document.getElementById("slider-image");
let leftBtn = document.getElementById("left");
let rightBtn = document.getElementById("right");

function changeImage(newIndex) {
  imageElement.style.opacity = 0;

  setTimeout(() => {
    index = newIndex;
    imageElement.src = images[index];
    imageElement.style.opacity = 1;
  }, 200);
}

leftBtn.addEventListener("click", function () {
  let newIndex = (index - 1 + images.length) % images.length;
  changeImage(newIndex);
});

rightBtn.addEventListener("click", function () {
  let newIndex = (index + 1) % images.length;
  changeImage(newIndex);
});