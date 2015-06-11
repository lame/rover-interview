angular.module('RoverApp').controller('SearchSittersController', ['$scope', '$http', function(SearchSittersController, $scope, $http){
    var ctrl = this;
    ctrl.sitters = {};

    ctrl.getSitters = function() {
        searchSittersService.getSitters()
            .success(function(data, status, headers, config) {
                console.log('success', status)
                console.log('data', data)
                ctrl.sitters = data
            })
            .error(function(data, status, headers, config) {
                console.log('error', status)
            });
        }
}]);

