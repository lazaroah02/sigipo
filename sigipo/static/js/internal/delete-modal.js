let deleteConfirmationModalContent = document.querySelector(
  "#delete-confirmation-content",
);
let deleteConfirmationModal = new bootstrap.Modal(
  document.querySelector("#delete-confimation-modal"),
);
let deleteConfirmationForm = document.querySelector("#delete_form");

document.querySelectorAll("a.delete").forEach((button) => {
  button.addEventListener("click", function (event) {
    event.preventDefault();
    var delete_url = new URL(button.href, window.location.href);
    delete_url.searchParams.append("modal", true);
    deleteConfirmationForm.action = delete_url;
    fetch(delete_url)
      .then(function (response) {
        return response.text();
      })
      .then(function (html) {
        // Convert the HTML string into a document object
        let parser = new DOMParser();
        let doc = parser.parseFromString(html, "text/html");
        let content = doc.querySelector("#content");
        deleteConfirmationModalContent.innerHTML = content.innerHTML;
      });
    deleteConfirmationModal.show();
  });
});
