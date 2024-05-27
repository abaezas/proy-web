$(document).ready(function () {

    let dict = {
      'STGO' : 'SANTIAGO CENTRO',
      'VALE' : 'VILLA ALEMANA',
      'VINA' : 'VINA DEL MAR',
      'VITA' : 'VITACURA'
    };

    // Estructura JSON Para solicitud de API Chilexpress
    var params = {
      "originCountyCode": "VALE",
      "destinationCountyCode": "VALE",
      "package": {
          "weight": "16",
          "height": "1",
          "width": "1",
          "length": "1"
      },
      "productType": 3,
      "contentType": 1,
      "declaredWorth": "2333",
      "deliveryTime": 0
    };

    for (let key in dict) {
      $('#dropenv').append('<option value=' + key + '>' + dict[key] + '</option>');
    };

    $("#btn-cotiza").click(function(e) {
      e.preventDefault();
      params.destinationCountyCode = $("#dropenv").val();
      $.ajax({
          type: "POST",
          url: "https://testservices.wschilexpress.com/rating/api/v1.0/rates/courier", //?" + $.param(params),
          beforeSend: function(xhrObj){
              // Request headers
              xhrObj.setRequestHeader("Content-Type","application/json");
              xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key","aa0c4ab1dd1d4ec5ba59910c7bdc0c50"); //replace value with your own key
          },
          dataType: "json",
          data: JSON.stringify(params),
          success: function(data) {
                successmessage = 'Data was succesfully captured';
                //var obj = jQuery.parseJSON( data );
                console.log(data.data)
                console.log(data.data.courierServiceOptions.serviceValue)
                $('#jqr').text("Costo envio: " + data.data.courierServiceOptions[0].serviceValue + " desde Villa Alemana a " + params.destinationCountyCode)
                //$("#jqr").text("costo: " + obj + " asda " + data + " a " + params.destinationCountyCode + " " + params.originCountyCode);
          }, 
          error: function (xhr, status, error) {
              alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
          }
      });
    });
  });