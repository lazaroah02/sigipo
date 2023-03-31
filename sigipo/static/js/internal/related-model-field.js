function updateRelatedModelField(field) {
  let view_button = field.parent().next().find(".related-model-view");
  view_button.show();
  let href = view_button.data("href");
  view_button.attr(
    "href",
    href?.replace("URL_VALUE_FOR_REPLACE", parseInt(field.val())),
  );
}

$(".related-model-field").on("change", function () {
  updateRelatedModelField($(this));
});

$(document).ready(function () {
  $(".related-model-field").each(function () {
    if ($(this).val()) {
      updateRelatedModelField($(this));
    }
  });
  $(".close-popup-btn").click(function () {
    opener.closePopup(window);
  });
});
