var App = angular.module('ta-console', ['ngRoute', 'ngSanitize', 'datatables', 'ta-console.directives', 'smart-table', 'angularMoment', 'ui.codemirror', 'ui.bootstrap']);
var directives = angular.module('ta-console.directives', []);
App.config(
    ['$routeProvider', '$httpProvider',
     function($routeProvider, $httpProvider) {

         $httpProvider.defaults.useXDomain = true;
         delete $httpProvider.defaults.headers.common['X-Requested-With'];
         $httpProvider.interceptors.push('authInterceptor');

         $routeProvider.
             when('/:course', {
                 templateUrl: 'partials/course.html',
                 controller: 'CourseCtrl',
                 title: '{{course}}',
                 loginRequired: true
             }).
             when('/:course/sets/:set_id', {
                 templateUrl: 'partials/set.html',
                 controller: 'SetCtrl',
                 title: '{{set_id}}',
                 loginRequired: true
             }).
             when('/:course/sets/:set_id/problems/:problem_id', {
                 templateUrl: 'partials/problem.html',
                 controller: 'ProblemCtrl',
                 title: '{{set_id}} #{{problem_id}}',
                 loginRequired: true
             }).
             when('/:course/sets/:set_id/problems/:problem_id/users/:user_id', {
                 templateUrl: 'partials/problem_user.html',
                 controller: 'ProblemUserCtrl',
                 title: '{{set_id}} #{{problem_id}} - {{user_id}}',
                 loginRequired: true
             }).
             when('/:course/login', {
                 templateUrl: 'partials/login.html',
                 controller: 'LoginCtrl',
                 title: 'Log In',
                 loginRequired: false
             }).
             when('/:course/console', {
                 templateUrl: 'partials/console.html',
                 controller: 'TAConsoleCtrl'
             }).
             when('/', {
                 templateUrl: 'partials/home.html',
                 controller: 'HomeCtrl'
             }).
             otherwise({
                 redirectTo: '/'
             });
     }])
    .run(function ($rootScope, $location, AUTH_EVENTS, AuthService) {
        $rootScope.$on('$routeChangeStart', function (event, next) {
            if(next.loginRequired){
                if (!AuthService.isAuthenticated()) {
                    $rootScope.$broadcast(AUTH_EVENTS.notAuthenticated);
                    if(next.params.course){
                        $location.path('/'+next.params.course+'/login');
                    } else{
                        $location.path('/');
                    }
                }
            }
        });
    });;

App.constant('APIHost', 'webwork.cse.ucsd.edu');

App.value('CurrentCourse', {name: 'Course'});

App.controller('ApplicationCtrl', function($routeParams, $route, $rootScope, $interpolate,
                                           SockJSService, CurrentCourse, Session, AUTH_EVENTS){
    if(Session.user_id){
        var sock = SockJSService.connect(4350, Session.user_id);
    }

    $rootScope.$on("$routeChangeSuccess", function(currentRoute, previousRoute){
        if($routeParams.course){
            CurrentCourse.name = $routeParams.course;
        }
        //Change page title, based on Route information
        if($route.current.title){
            var titleExp = $interpolate($route.current.title);
            $rootScope.title = titleExp($route.current.params);
        }else{
            $rootScope.title="";
        }
    });

    $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event){
    });

});
