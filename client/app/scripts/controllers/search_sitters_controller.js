angular.module('RoverApp').controller('SearchSittersController', ['$scope', '$http', 'searchSittersService', function($scope, searchSittersService) {
    'use strict';
    var ctrl = this;

    ctrl.getSitters = function() {
        searchSittersService.getSitters()
            .success(function(sitters) {$scope.sitters = sitters})
    }
}]);
