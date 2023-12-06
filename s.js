function convertDateFormat(inputDate) {
    // Split the input date into an array of year, month, and day
    var parts = inputDate.split("-");
    // Rearrange the array elements to form the "dd-mm-yyyy" format
    var outputDate = parts[2] + "-" + parts[1] + "-" + parts[0];
    return outputDate;
}

// Example usage:
var inputDate = "2023-12-06";
var convertedDate = convertDateFormat(inputDate);
console.log(convertedDate); 