$(document).ready(function () {
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      translateHello();
    }
  });

  function translateHello() {
    const langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
