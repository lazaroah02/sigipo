document.querySelectorAll("a.related-model-add").forEach((button) => {
  button.addEventListener("click", function (event) {
    event.preventDefault();
    var create_url = new URL(
      button.href + "?is_popup=true",
      window.location.href,
    );
    window.showAddPopup(create_url);
  });
});
document.querySelectorAll("a.related-model-view").forEach((button) => {
  button.addEventListener("click", function (event) {
    event.preventDefault();
    var create_url = new URL(
      button.href + "?is_popup=true",
      window.location.href,
    );
    window.showAddPopup(create_url);
  });
});
