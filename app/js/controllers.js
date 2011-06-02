/* App Controllers */


function ObservationsCtrl($xhr) {
  var self = this;

  $xhr("POST", "api/observations.all", "JSON", function(code, response) {
    self.observations = response;
    alert(">> got " + response);
  });
}
ObservationsCtrl.$inject = ['$xhr'];


function ObservationCtrl() {}
ObservationCtrl.$inject = [];
