angular.module('RoverApp').controller('SearchSittersController', ['$scope', '$http', '$filter', 'searchSittersService', function($scope, $http, $filter, searchSittersService){
    var ctrl = this;

    ctrl.getSitters = function() {
        searchSittersService.getSitters()
            .success(function(data, status, headers, config) {
                console.log('success', status)
                console.log('sitters data', data)
                $scope.rowCollection = data
            })
            .error(function(data, status, headers, config) {
                console.log('error', status)
            });
        };

    ctrl.getSitters();
}]);

// Different controller syntax, doesn't seem to want to work!

// (function() {
//     'use strict';

//     angular.module('RoverApp').controller('SearchSittersController', SearchSittersController);

//     SearchSittersController.$inject = ['$scope', '$http', 'searchSittersService', 'ui.grid'];

//     function SearchSittersController($scope, $http, searchSittersService, ui.grid) {

//         var ctrl = this;

//         ctrl.getSitters = function() {
//             searchSittersService.getSitters()
//                 .success(function(data, status, headers, config) {
//                     console.log('success', status)
//                     console.log('sitters data', data)
//                     $scope.rowCollection = data
//                 })
//                 .error(function(data, status, headers, config) {
//                     console.log('error', status)
//                 });
//             };

//         ctrl.getSitters();
//     };
// });

