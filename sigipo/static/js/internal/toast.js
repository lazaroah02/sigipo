document.addEventListener(
  "DOMContentLoaded",
  function () {
    var toastElList = [].slice.call(
      document.querySelectorAll(".auto-show-toast"),
    );
    var toastList = toastElList.map(function (toastEl) {
      return new bootstrap.Toast(toastEl);
    });
    toastList.forEach((toast) => {
      toast.show();
    });
  },
  false,
);
