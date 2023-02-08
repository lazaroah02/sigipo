(function () {
  const fetch_url = document.getElementById("id_fetch_url").value;
  const search_patient = document.getElementById("id_identity_card");

  async function check_patient(value) {
    let response = await fetch(fetch_url.replace("None", value)).then(
      (response) => response.json(),
    );
    if (response["exist"]) {
      search_patient.classList.remove("is-valid");
      search_patient.classList.add("is-invalid");
    } else {
      search_patient.classList.remove("is-invalid");
      search_patient.classList.add("is-valid");
    }
  }

  search_patient.addEventListener("keyup", () => {
    let value = search_patient.value.toString();
    let length = search_patient.value.toString().length;
    if (length === 8 || length === 11) {
      check_patient(value);
    } else {
      search_patient.classList.remove("is-valid");
      search_patient.classList.remove("is-invalid");
    }
  });
})();
