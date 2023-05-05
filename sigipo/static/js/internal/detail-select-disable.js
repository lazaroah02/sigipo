const disable = () => {
  let selects = document.getElementsByTagName("select");
  for (let i = 0; i < selects.length; i++) {
    const e = selects[i];
    e.disabled = true;
  }
};

$(document).ready(function () {
  disable();
});
