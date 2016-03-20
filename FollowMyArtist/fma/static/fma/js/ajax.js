var csrftoken = $("input[name=csrfmiddlewaretoken]").val();

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});