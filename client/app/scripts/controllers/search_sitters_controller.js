angular.module('RoverApp').controller('SearchSittersController', ["$scope", "$element", "$compile", "$http", "$q", "searchSittersService", function($scope, $element, $compile, $http, $q, searchSittersService){

    getSitters = function() {
        var deferred = $q.defer();

        searchSittersService.getSitters()
            .success(function(data, status, headers, config) {
                console.log('success', status);
                console.log('sitters data', data);
                deferred.resolve(data);
            })
            .error(function(data, status, headers, config) {
                console.log('error', status);
                deferred.reject;
            });
        return deferred.promise;
    };

    $scope.gridData = function() {
        getSitters().then(function (data) {
            console.log('data: ', data);
            if (data !== undefined)
            {

                $scope.loadData = data;
            }
        });
    };

    $scope.gridOptions = {
        data: 'loadData',
        columnDefs: [
            {name: 'Image', field: 'image'},
            {name: 'Name', field: 'name'},
            {name: 'Rating', field: 'rating'},
            {name: 'Recent Owner Review', field: 'owner_review_text'}
        ],
        enableSorting: true
    };
}]);

// Different controller syntax, doesn't seem to want to work

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

