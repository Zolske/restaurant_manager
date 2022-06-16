/// >>> START import functions from helper_functions.js /////////////////////////////////////////////////////////////////////////////////////////////
import {
  convertToDateString,
  setDateIdOnTable,
  getWeeksDailyAvailableTable,
  setFormRightTimeSlot,
  setFormRightMaxMinTable,
} from "./helper_functions.js";
/// <<< END import functions from helper_functions.js ///////////////////////////////////////////////////////////////////////////////////////////////

/// >>> START set variables /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// create from all weeks one array with there date and available tables
let availableTablesData = [];
for (let i = 0; i <= 7; i++) {
  let week = "week_" + i;
  availableTablesData.push(getWeeksDailyAvailableTable(week));
}

// get the first day of the week which has not passed = today, and convert to YYYY-mm-dd
let firstDayNotPassedCalender = convertToDateString(
  document.getElementsByClassName("week_0").item(0).innerHTML
);

// get the last day of the last week (week 7 after the current week), and convert to YYYY-mm-dd
let lastDayNotPassedCalender = convertToDateString(
  document.getElementsByClassName("week_7").item(6).innerHTML
);

// get from the form element the input for the date picker
let bookingDate = document.getElementById("bookingDate");

// activate bootstrap tooltips
var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
/// <<< END set variables ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/// >>> START calling functions /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// set the default date pick day to today
bookingDate.setAttribute("value", firstDayNotPassedCalender);
// set the first possible day to pick to today
bookingDate.setAttribute("min", firstDayNotPassedCalender);
// set the last possible day to pick to the last day of the 7th week after the current week
bookingDate.setAttribute("max", lastDayNotPassedCalender);
// set the initial values for the time slot select list when side is loaded
setFormRightTimeSlot(firstDayNotPassedCalender, availableTablesData);
// set the initial values for the available table select list
formTableInput();
/// <<< END calling functions ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/// >>> START add event listener ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// add an event listener to the "form input date field"
document.getElementById("bookingDate").addEventListener("input", formDateInput);
function formDateInput() {
  let bookingDate = document.getElementById("bookingDate").value;
  setFormRightTimeSlot(bookingDate, availableTablesData);
}

// add event listener to the "booking time slot select field"
document
  .getElementById("bookingTime")
  .addEventListener("change", formTableInput);
function formTableInput() {
  let bookingDate = document.getElementById("bookingDate").value;
  let bookingTable = document.getElementById("bookingTime").value;
  let timeSlotPosition = [
    "date, expected match",
    "time_slot_12",
    "time_slot_14",
    "time_slot_16",
    "time_slot_18",
    "time_slot_20",
    "time_slot_22",
  ];
  for (let position = 0; position <= 7; position++) {
    if (bookingTable == timeSlotPosition[position]) {
      timeSlotPosition = position;
    }
  }
  setFormRightMaxMinTable(bookingDate, timeSlotPosition, availableTablesData);
}
/// <<< END add event listener //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// set on every week day the id as the date
for (let i = 0; i <= 7; i++) {
  let week = "week_" + i;
  setDateIdOnTable(week);
}

function sayHello() {
  console.log(hello);
}
