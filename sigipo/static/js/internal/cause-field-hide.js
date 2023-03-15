var checkbox = document.querySelector("input[name=suspended]");
var cause_field = document.querySelector("#id_cause").parentNode;

function check_status(checkbox) {
  if (checkbox.checked) {
    cause_field.style.display = "block";
  } else {
    cause_field.style.display = "none";
  }
}

check_status(checkbox);

checkbox.addEventListener("change", function () {
  check_status(this);
});
