$(document).ready(function () {
  let link = $("main").data("path");
  let urlParam = new URLSearchParams(window.location.search);
  link = link.split("?")[0];
  link = urlParam.has("module-name")
    ? link + `?module-name=${urlParam.get("module-name")}`
    : link;
  $(`a[href="${link}"]`).addClass("active-link");
  $(`a[href="${link}"]`).parents("div.collapse").addClass("show");
  $(`a[href="${link}"]`)
    .parents("div.collapse")
    .find("button.btn-toggle")
    .attr("aria-expanded", true)
    .removeClass("collapsed");
});
