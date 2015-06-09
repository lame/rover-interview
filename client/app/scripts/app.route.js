(function() {
  'use strict';
  angular.module('RoverApp')
  .config(['$stateProvider','$urlRouterProvider', '$locationProvider',
           function ($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise('/index');

    $stateProvider
    .state('search-sitters', {
      url:'/search-sitters',
      templateUrl: 'views/search_sitters.html',
      controller: 'SearchSitterController'
    })
  }]);
})();
