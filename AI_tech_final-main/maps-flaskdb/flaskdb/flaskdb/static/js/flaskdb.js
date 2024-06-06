/* flaskdb.js - defines JavaScript functions on flaskdb. Modify this if you need */
/* Copyright (C) 2024 Yasuhiro Hayashi */
$(function() {
  $("form").submit(function() {
    $(this).find(":submit").prop("disabled", true);
    setTimeout(function() {
      $(this).find(":submit").prop("disabled", false);
    }, 10000);
  });

  $("#cancel").on("click", function() {
    history.back();
  })
});
