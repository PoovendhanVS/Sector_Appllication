

function validateForm(event) {
    var empGen = $("#emp_gender").val();
    var empName = $("#offic_emp_name").val();
    var empDoj = $("#doj").val();
    var empRole = $("#role").val();
    var empSite = $("#site_name").val();
    var empShift = $("#gst").val();
    var empCate = $("#emp_cate").val();
    var empHead = $("#emp_head").val();
    var empSkill = $("#emp_skill").val();
    var empPhoto = $("#emp_photos").val();

    var empStatus = $("#emp_status").val();
    var dob = $("#dob").val();
    var empAge = $("#emp_age").val();
    var empBlood = $("#emp_blood").val();
    var empGender = $("#gender").val();
    var empAct = $("#emp_act").val();
    var empPys = $("#emp_pys").val();

    var empCountryS = $("#emp_countrys").val();
    var empStateS = $("#emp_states").val();
    var empDistrict = $("#emp_district").val();
    var empBild = $("#emp_bild").val();
    var empStreet = $("#emp_street").val();
    var empArea = $("#emp_area").val();
    var empPin = $("#emp_pin").val();

    var empPCountrys = $("#emp_p_countrys").val();
    var empPStates = $("#emp_p_states").val();
    var empPDistricts = $("#emp_p_districts").val();
    var empPBild = $("#emp_p_bild").val();
    var empPStreet = $("#emp_p_street").val();
    var empPArea = $("#emp_p_area").val();
    var empPPin = $("#emp_p_pin").val();


    if (empGen === '') {
      alert('Please select a gender');
      event.preventDefault();
    }
    else if (empName === '') {
      alert('Please enter a employee name');
      event.preventDefault();
    }
    else if (empDoj === "") {
      alert("Please select a date of jioning.");
      event.preventDefault();
    }
    else if (empRole === "") {
      alert("Please enter designation.");
      event.preventDefault();
    }
    else if (empSite === "") {
      alert("Please select a Company name.");
      event.preventDefault();
    }
    else if (empShift === "") {
      alert("Please select an GST number.");
      event.preventDefault();
    }
    else if (empCate === "") {
      alert("Please select a employee category.");
      event.preventDefault();
    }
    else if (empHead === "") {
      alert("Please select a staff head.");
      event.preventDefault();
    }
    else if (empSkill.length < 1) {
      alert("Please select a skill.");
      event.preventDefault();
    }
    else if (empPhoto === "") {
      alert("Please insert a employee photo.");
      event.preventDefault();
    }
    // Perform validation for each field
    else if (empStatus === "") {
      alert("Please select marital status.");
      event.preventDefault();
    }
    else if (dob === "") {
      alert("Please enter a date of birth.");
      event.preventDefault();
    }
    else if (empAge === "") {
      alert("Please enter an age.");
      event.preventDefault();
    }
    else if (empBlood === "") {
      alert("Please select a blood group.");
      event.preventDefault();
    }
    else if (empGender === "") {
      alert("Please select a gender.");
      event.preventDefault();
    }
    else if (empAct === "") {
      alert("Please enter extracurricular activities.");
      event.preventDefault();
    }
    else if (empPys === "") {
      alert("Please select disabilities.");
      event.preventDefault();
    }
    else if (empCountryS === "") {
      alert("Please select present country.");
      event.preventDefault();
    }
    else if (empStateS === "") {
      alert("Please select present state.");
      event.preventDefault();
    }
    else if (empDistrict === "") {
      alert("Please select present district.");
      event.preventDefault();
    }
    else if (empBild === "") {
      alert("Please enter building number for present address.");
      event.preventDefault();
    }
    else if (empStreet === "") {
      alert("Please enter street for present address.");
      event.preventDefault();
    }
    else if (empArea === "") {
      alert("Please enter area for present address.");
      event.preventDefault();
    }
    else if (empPin === "") {
      alert("Please enter pincode for present address.");
      event.preventDefault();
    }
    // permanent address
    else if (empPCountrys === "") {
      alert("Please select permanent country.");
      event.preventDefault();
    }
    else if (empPStates === "") {
      alert("Please select permanent state.");
      event.preventDefault();
    }
    else if (empPDistricts === "") {
      alert("Please select permanent district.");
      event.preventDefault();
    }
    else if (empPBild === "") {
      alert("Please enter building number for permanent address.");
      event.preventDefault();
    }
    else if (empPStreet === "") {
      alert("Please enter street for permanent address.");
      event.preventDefault();
    }
    else if (empPArea === "") {
      alert("Please enter area for permanent address.");
      event.preventDefault();
    }
    else if (empPPin === "") {
      alert("Please enter pincode for permanent address.");
      event.preventDefault();
    }
    else {
      alert('Employee official details stored successfully.')
    }
  }

  function sameAddress() {
    if (document.getElementById(
      "same").checked) {
      document.getElementById(
        "emp_p_countrys").value =
        document.getElementById(
          "emp_countrys").value;

      document.getElementById(
        "emp_p_states").value =
        document.getElementById(
          "emp_states").value;

      document.getElementById(
        "emp_p_districts").value =
        document.getElementById(
          "emp_district").value;

      document.getElementById(
        "emp_p_bild").value =
        document.getElementById(
          "emp_bild").value;

      document.getElementById(
        "emp_p_street").value =
        document.getElementById(
          "emp_street").value;

      document.getElementById(
        "emp_p_area").value =
        document.getElementById(
          "emp_area").value;

      document.getElementById(
        "emp_p_pin").value =
        document.getElementById(
          "emp_pin").value;


    } else {
      document.getElementById(
        "emp_p_countrys").value = "";
      document.getElementById(
        "emp_p_states").value = "";
      document.getElementById(
        "emp_p_districts").value = "";
      document.getElementById(
        "emp_p_bild").value = "";
      document.getElementById(
        "emp_p_street").value = "";
      document.getElementById(
        "emp_p_area").value = "";
      document.getElementById(
        "emp_p_pin").value = "";

    }
  }
  
  // setTimeout(function () {
  //   var messageBox = document.getElementById("message-box");
  //   messageBox.style.display = "none";
  // }, 2000);  // 2000 milliseconds = 2 seconds




//   $(document).ready(function(){
//     $('#emp_countrys').change(function() {
//     var selectedId = $('#emp_countrys').val();
//     if (selectedId !== '') {
//         InsertStateNames(selectedId);
//     } else {
//         $('#emp_states').empty();
//     }
//   });
//   function InsertStateNames(selectedId){
//     $.ajax({
//       url: '/get_state_name/',
//       type: 'GET',
//       data: {
//           'country_id': selectedId
//       },
//       success: function(response) {
//           console.log('Sub Inserted Successfully');
//           $('#emp_states').html(response);
//       },
//       error: function() {
//           console.log('An error occurred during the AJAX request.');
//       }
//   });
//   }
  
//   function resetFields() {
//     $('#emp_states').empty();

// }
// });

//   $(document).ready(function(){
//     $('#emp_states').change(function() {
//     var selectedId = $('#emp_states').val();
//     if (selectedId !== '') {
//         InsertStateNames(selectedId);
//     } else {
//         $('#emp_district').empty();
//     }
//   });
//   function InsertStateNames(selectedId){
//     $.ajax({
//       url: '/get_district_name/',
//       type: 'GET',
//       data: {
//           'state_id': selectedId
//       },
//       success: function(response) {
//           console.log('Sub Inserted Successfully');
//           $('#emp_district').html(response);
//       },
//       error: function() {
//           console.log('An error occurred during the AJAX request.');
//       }
//   });
//   }
  
//   function resetFields() {
//     $('#emp_district').empty();

// }
// });