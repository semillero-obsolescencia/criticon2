(function() {
    'use strict';

    var routeConfig = function($routeProvider) {

        $routeProvider
            .when("/", {
                templateUrl: '/static/view_templates/index.html',
                controller: 'mainController',
                controllerAs: 'main'
            })
            /*
            .when("/about", {
                templateUrl: '/static/view_templates/about.html',
                controller: 'aboutController',
                controllerAs: 'about'
            })
            .when("/contact", {
                templateUrl: '/static/view_templates/contact.html',
                controller: 'contactController',
                controllerAs: 'contact'
            })
            */
            .otherwise({ redirectTo: '/' });
    };

    var httpConfig = function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    };

    var onRun = function($rootScope, $location) {
        $rootScope.$on('$routeChangeStart', function(evt, next, current) {
            $rootScope.currentView = next.$$route.originalPath;
        });
    };

    var ExpoFactory = function($resource) {
            return $resource("/api/expo/:id");
        };

    var ObraFactory = function($resource) {
            return $resource("/api/obra/:id");
    };

    var mainController = function($route, ExpoFactory, ObraFactory, $scope) {
        ExpoFactory.get({ id: 1}, function(data) {
            $scope.expo = data;
        });

        ObraFactory.query(function(datos) {
            //console.log(data);

            $scope.obras = datos;
            console.log(datos);
        });
    };
    /*
    var aboutController = function(PageFactory, ItemFactory, $scope) {
        PageFactory.get({ id: 2}, function(data) {
            $scope.pageHeader = data;
        });

        ItemFactory.query(function(data) {
            $scope.pageItems = data;
        });
    };

    var contactController = function(PageFactory, ItemFactory, $scope) {
        PageFactory.get({ id: 3}, function(data) {
            $scope.pageHeader = data;
        });

        ItemFactory.query(function(data) {
            $scope.pageItems = data;
        });
    };
    */

    angular.module("mainModule", ["ngRoute", "ngResource"])
        .factory('ExpoFactory', ExpoFactory)
        .factory('ObraFactory', ObraFactory)
        .controller('mainController', mainController)
        //.controller('aboutController', aboutController)
        //.controller('contactController', contactController)
        .config(httpConfig)
        .config(routeConfig)
        .run(onRun);

}());
