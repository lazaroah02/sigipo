document
  .querySelector("#id_submit_filters")
  .addEventListener("click", function () {
    new bootstrap.Collapse(document.getElementById("collapseFilters"), {
      hide: true,
    });
    document.querySelectorAll("input").forEach((element) => {
      if (element.value == "") {
        element.setAttribute("disabled", true);
      }
    });
    document.querySelectorAll("select").forEach((element) => {
      if (element.value == "") {
        element.setAttribute("disabled", true);
      }
    });
    document.querySelectorAll("textarea").forEach((element) => {
      if (element.value == "") {
        element.setAttribute("disabled", true);
      }
    });
  });
