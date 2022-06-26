(function () {
  let birdForm = document.querySelectorAll(".medication-clyce-form");
  let container = document.querySelector("#base_form");
  let addButton = document.querySelector("#add-form");
  let totalForms = document.querySelector(
    "#id_cyclemedication_set-TOTAL_FORMS"
  );

  let formNum = birdForm.length - 1;
  addButton.addEventListener("click", addForm);

  function addForm(e) {
    e.preventDefault();

    let newForm = birdForm[0].cloneNode(true);
    let formRegex = RegExp(`cyclemedication_set-(\\d){1}-`, "g");

    formNum++;
    newForm.innerHTML = newForm.innerHTML.replace(
      formRegex,
      `cyclemedication_set-${formNum}-`
    );
    $(`#id_cyclemedication_set-${formNum}-drug`, newForm).next().remove();
    container.insertBefore(newForm, addButton);

    totalForms.setAttribute("value", `${formNum + 1}`);
    $(`#id_cyclemedication_set-${formNum}-drug`).djangoSelect2();
  }
})();
