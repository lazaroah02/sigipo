var pregnancy = document.querySelector("select[name=pregnancy]");
var surgeries = document.querySelector("select[name=last_surgeries]");
var violentDeathCauses = document.querySelector(
  "select[name=violent_death_causes]",
);
var submit = document.querySelector("form");
var pregnancyResults = document.querySelector("select[name=pregnancy_result]");
var dateOfPregnancy = document.querySelector("input[name=date_of_pregnancy]");
var surgeryReasons = document.querySelector("textarea[name=surgery_reasons]");
var dateOfInjury = document.querySelector("input[name=date_of_injury]");
var eventDescription = document.querySelector(
  "textarea[name=event_description]",
);
var placeWhereInjuryOcurred = document.querySelector(
  "textarea[name=place_where_injury_occurred]",
);
var requestingAuthority = document.querySelector(
  "input[name=requesting_authority]",
);
var actNumber = document.querySelector("input[name=act_number]");
const status_check = () => {
  if (pregnancy.value !== "1") {
    pregnancyResults.value = 5;
    pregnancyResults.disabled = true;
    dateOfPregnancy.value = "";
    dateOfPregnancy.disabled = true;
  } else {
    pregnancyResults.disabled = false;
    dateOfPregnancy.disabled = false;
  }
  if (surgeries.value !== "1") {
    surgeryReasons.value = "";
    surgeryReasons.disabled = true;
  } else {
    surgeryReasons.disabled = false;
  }
  if (violentDeathCauses.value === "5") {
    dateOfInjury.value = "";
    dateOfInjury.disabled = true;
    placeWhereInjuryOcurred.value = "";
    placeWhereInjuryOcurred.disabled = true;

    eventDescription.value = "";
    eventDescription.disabled = true;

    requestingAuthority.value = "";
    requestingAuthority.disabled = true;
    actNumber.value = "";
    actNumber.disabled = true;
  } else {
    dateOfInjury.disabled = false;
    placeWhereInjuryOcurred.disabled = false;
    eventDescription.disabled = false;
    requestingAuthority.disabled = false;
    actNumber.disabled = false;
  }
};

const to_submit = () => {
  pregnancyResults.disabled = false;
  dateOfPregnancy.disabled = false;
  surgeryReasons.disabled = false;
  dateOfInjury.disabled = false;
  placeWhereInjuryOcurred.disabled = false;
  requestingAuthority.disabled = false;
  actNumber.disabled = false;
  eventDescription.disabled = false;
};

$(document).ready(status_check());

pregnancy.addEventListener("change", status_check);
surgeries.addEventListener("change", status_check);
violentDeathCauses.addEventListener("change", status_check);
submit.addEventListener("submit", to_submit);
