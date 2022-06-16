/**
 * The function converts a date string into the right formate for the calender.
 * For example "15. Jun 2022" to "2022-06-15"
 * @param {string} dateString "15. Jun 2022"
 * @returns {string} formate "YYYY-mm-dd" for example "2022-06-15"
 */
export function convertToDateString(dateString) {
  let formattedDate = dateString.slice(8, 12) + "-";
  let monthArray = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  let monthWord = dateString.slice(4, 7);
  let monthNum = monthArray.findIndex((element) => element == monthWord);
  monthNum = monthNum + 1;
  if (String(monthNum).length == 1) {
    monthNum = "0" + monthNum;
  }
  formattedDate += monthNum + "-";
  formattedDate += dateString.slice(0, 2);
  return formattedDate;
}

/**
 * Set the date id for the week on every single day in the HTML.
 * @param {string} className name of the week class which is given in HTML
 */
export function setDateIdOnTable(className) {
  let weekClass = document.getElementsByClassName(className);
  for (let i = 0; i < weekClass.length; i++) {
    let dateOriginal = weekClass[i].innerHTML;
    let dateFormatted = convertToDateString(dateOriginal);
    weekClass[i].setAttribute("id", dateFormatted);
  }
}

/**
 * Get the available tables of each day from the week which has been passed as parameter.
 * @param {string} className class name of the week
 * @returns {array} each week is its own array, e.g. ['2022-06-15', '0', '4', '4', '1', '7', '2']
 * but all weeks are combined in one array.
 */
export function getWeeksDailyAvailableTable(className) {
  let weekClass = document.getElementsByClassName(className);
  let weekArray = [];
  for (let i = 0; i < weekClass.length; i++) {
    let dateOriginal = weekClass[i].innerHTML;
    let dayArray = [convertToDateString(dateOriginal)];
    let childrenOfTheWeek = weekClass[i].parentElement.children;
    for (let i = 2; i < childrenOfTheWeek.length; i++) {
      dayArray.push(childrenOfTheWeek[i].innerHTML);
    }
    weekArray.push(dayArray);
  }
  return weekArray;
}

/**
 * Set's the time slot in the form according to the date and available tables,
 * if there are no tables available than there is no time slot open.
 * @param {string} bookingDate in the format "YYYY-mm-dd" e.g. '2022-06-16'
 * @param {array} availableTablesData is the array containing the data from Django
 */
export function setFormRightTimeSlot(bookingDate, availableTablesData) {
  for (let week = 0; week <= 7; week++) {
    for (let day = 0; day < availableTablesData[week].length; day++) {
      if (availableTablesData[week][day][0] == bookingDate) {
        // change the displayed week should be week => week_'week'
        let bookingDate = document.getElementById("bookingDate");
        bookingDate.setAttribute("value", availableTablesData[week][day][0]);
        // get the time slot element
        let timeSlotOption = document.getElementById("bookingTime");
        // remove all children if it has any
        while (timeSlotOption.hasChildNodes()) {
          timeSlotOption.removeChild(timeSlotOption.firstChild);
        }
        // array containing the possible values for the option list which will be send with the form
        let timeSlotValue = [
          "time_slot_12",
          "time_slot_14",
          "time_slot_16",
          "time_slot_18",
          "time_slot_20",
          "time_slot_22",
        ];
        // array containing the description for the options in the browser
        let timeSlotDisplay = [
          "12:00-14:00",
          "14:00-16:00",
          "16:00-18:00",
          "18:00-20:00",
          "20:00-22:00",
          "22:00-24:00",
        ];
        // empty select field which can not be selected and has no value, is needed to clear previous selection
        let option = document.createElement("option");
        option.setAttribute("selected", "");
        option.setAttribute("disabled", "");
        option.setAttribute("value", "");
        timeSlotOption.appendChild(option);
        // write the new options according to the 'availableTablesData' array
        for (
          let table = 1;
          table < availableTablesData[week][day].length;
          table++
        ) {
          let option = document.createElement("option");
          if (availableTablesData[week][day][table] == "0") {
            option.setAttribute("class", "bg-secondary bg-opacity-25");
            option.setAttribute(
              "title",
              "Sorry, there are no tables available at this time."
            );
            option.setAttribute("disabled", "");
          }
          option.setAttribute("value", timeSlotValue[table - 1]);
          option.textContent = timeSlotDisplay[table - 1];
          timeSlotOption.appendChild(option);
        }
      }
    }
  }
}
/**
 * Sets the maximum value for the tables which can be booked in the booking form.
 * @param {string} bookingDate the date which was chosen for the booking, must be "YYYY-mm-dd"
 * @param {num} timeSlot must be a number between 1-6 (1 = 12:00-14:00, ... )
 * @param {array} availableTablesData is the array created from the date send by Django
 */
export function setFormRightMaxMinTable(
  bookingDate,
  timeSlot,
  availableTablesData
) {
  let bookingTable = document.getElementById("bookingTable");
  while (bookingTable.hasChildNodes()) {
    bookingTable.removeChild(bookingTable.firstChild);
  }
  // empty select field which can not be selected and has no value, is needed to clear previous selection
  let option = document.createElement("option");
  // option.setAttribute("selected", "");
  option.setAttribute("disabled", "");
  option.setAttribute("value", "");
  bookingTable.appendChild(option);
  for (let week = 0; week <= 7; week++) {
    for (let day = 0; day < availableTablesData[week].length; day++) {
      if (availableTablesData[week][day][0] == bookingDate) {
        let availableTable = availableTablesData[week][day][timeSlot];
        if (availableTable == "0") {
          let option = document.createElement("option");
          option.setAttribute("class", "bg-secondary bg-opacity-25");
          option.setAttribute("value", "");
          option.setAttribute(
            "title",
            "Sorry, there are no tables available at this time."
          );
          // bookingTable.setAttribute("disabled", "");
          bookingTable.appendChild(option);
        } else {
          for (let table = 1; table <= availableTable; table++) {
            let option = document.createElement("option");
            option.setAttribute("value", table);
            option.textContent = table;
            bookingTable.appendChild(option);
          }
        }
      }
    }
  }
}

// setFormRightTimeSlot("2022-06-17", availableTablesData);
// export function formDateInput(bookingDate, availableTablesData) {
//   let bookingDate = document.getElementById("bookingDate").value;
//   setFormRightTimeSlot(bookingDate, availableTablesData);
// }
