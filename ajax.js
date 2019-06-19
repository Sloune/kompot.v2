$(function () {
  $("#free-call-form").submit(function (e) {
    e.preventDefault();
    var form_data = $(this).serialize();
    $.ajax({
      type: "POST",
      url: "http://kompot.loc/wp-content/themes/kompot/call-form.php",
      dataType: "json", // Add datatype
      data: form_data,
    }).done(function (data) {
      console.log(data);
      $('#results').html('Повідомлення відправленно');
    }).fail(function (data) {
      console.log(data);
    });
  });
});


$(function () {
  $("#free-order-form").submit(function (e) {
    e.preventDefault();
    var form_data = $(this).serialize();
    $.ajax({
      type: "POST",
      url: "http://kompot.loc/wp-content/themes/kompot/order-form.php",
      dataType: "json", // Add datatype
      data: form_data,
    }).done(function (data) {
      console.log(data);
      $('#response').html('Заявка відправленна');
    }).fail(function (data) {
      console.log(data);
    });
  });
});