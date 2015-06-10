// Default Smart Table controller, needs to be modified
(function(){

    angular.module('RoverApp').factory('searchSittersService', searchSittersService);
    searchSittersService.$inject = ['$http', 'Rover_Config'];

    function searchSittersService($http, Rover_Config){
        var searchSittersService = {
            getSitters: getSitters,
            sitterData: {},
        };

        function getSitters(){
            return $http.get(Rover_Config.apiUrl + 'api/sitters');
        }

    }

})();
