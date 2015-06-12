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

    $scope.getTableStyle= function() {
        var rowHeight=142;
        var headerHeight=45;
        return {
            height: ($scope.loadData.length * rowHeight + headerHeight) + "px"
        };
    };

    $scope.gridOptions = {
        data: 'loadData',
        columnDefs: [
            {name: 'Image', field: 'image',
             cellTemplate: '<div class="ui-grid-cell-contents"><img src="{{ COL_FIELD }}" height="142"/></div>',
             width: 150
            },
            {name: 'Name', field: 'name', width: 150},
            {name: 'Rating', field: 'rating', width: 100},
            {name: 'Recent Owner Review', field: 'owner_review_text',
            cellTemplate: '<div class="ui-grid-cell-contents overflow"><p>{{ COL_FIELD }}</p></div>'}
        ],
        enableSorting: true,
        rowHeight:142,
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

