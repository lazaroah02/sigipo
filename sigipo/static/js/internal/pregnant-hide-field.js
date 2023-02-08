var checkbox = document.querySelector("input[name=is_pregnant]");
var trimester_layout = document.querySelector("#id_trimester").parentNode;

function check_status(checkbox) {
  if (checkbox.checked) {
    trimester_layout.style.display = "block";
  } else {
    trimester_layout.style.display = "none";
  }
}

check_status(checkbox);

checkbox.addEventListener("change", function () {
  check_status(this);
});
