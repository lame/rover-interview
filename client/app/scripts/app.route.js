(function() {
  'use strict';
  angular.module('RoverApp')
  .config(['$stateProvider','$urlRouterProvider', '$locationProvider',
           function ($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise('landing');

    $stateProvider
    .state('search-sitters', {
      url:'/search-sitters',
      templateUrl: 'views/search_sitters.html',
      controller: 'SearchSittersController'
    })

    .state('landing', {
      url:'/landing',
      templateUrl: 'views/landing.html'
    })

  }]);
})();
