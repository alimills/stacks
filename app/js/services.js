/* http://docs.angularjs.org/#!angular.service */

/**
 * App service which is responsible for the main configuration of the app.
 */
angular.service('myAngularApp', function($route, $location, $window) {

  $route.when('/observations', {template: 'partials/observations.html', controller: Observations});
  $route.when('/observation', {template: 'partials/observation.html', controller: Observation});

  var self = this;

  $route.onChange(function() {
    if ($location.hash === '') {
      $location.updateHash('/observations');
      self.$eval();
    } else {
      $route.current.scope.params = $route.current.params;
      $window.scrollTo(0,0);
    }
  });

}, {$inject:['$route', '$location', '$window'], $eager: true});
