var App = angular.module('ta-console');

App.controller('ProblemUserCtrl', function($scope, $location, $window, $routeParams,
                                           $sce, $interval, $timeout,
                                           WebworkService, SockJSService){
    var course = $scope.course = $routeParams.course;
    var set_id = $scope.set_id = $routeParams.set_id;
    var problem_id = $scope.problem_id = $routeParams.problem_id;
    var user_id = $scope.user_id = $routeParams.user_id;
    $scope.student_data = {answers: []};
    $scope.current_part = 0;
    $scope.problem_seed = "";
    WebworkService.answersByPart(course, set_id, problem_id, user_id).
        success(function(data){
            $scope.answersByPart = {};
            angular.forEach(data, function(value){
                if (!$scope.answersByPart[value.part_id]){
                    $scope.answersByPart[value.part_id] = [];
                }
                $scope.answersByPart[value.part_id].push(value);
            });
    });
    var sock = SockJSService.get_sock();
    $scope.current_answers = [];
    sock.onmessage = function(e) {
	    print("RECIEVED: " + e.data);
	    var data = JSON.parse(e.data);
	    if (data.type == 'student_info') {
	        var student_info = data['arguments'];
            $scope.$apply(function(){
                $scope.current_answers = student_info.current_answers;
            });
	    }
    };
    SockJSService.teacher_join('teacher', $scope.course, $scope.set_id, $scope.problem_id, $scope.user_id);
    SockJSService.request_student($scope.course, $scope.set_id, $scope.problem_id, $scope.user_id);
    SockJSService.get_student_info($scope.course, $scope.set_id, $scope.problem_id, $scope.user_id);

    WebworkService.problemSeed(course, set_id, problem_id, user_id).
        success(function(data){
            $scope.problem_seed = data;
        });
    
    WebworkService.problemPGFile(course, set_id, problem_id).success(function(data){
        $scope.pg_text = JSON.parse(data);
        var hf = WebworkService.extractHeaderFooter($scope.pg_text);
        $scope.pg_header = hf.pg_header;
        $scope.pg_footer = hf.pg_footer;
    });

    $scope.displayed_hints = [];
    $scope.hints = [];

    $scope.reload_hints = function(){
        WebworkService.problemHints(course, set_id, problem_id).success(function(data){
            $scope.hints = data;
        });
    };

    $scope.reload_hints();
    $scope.rendered_hint="";
    $scope.box="";
    $scope.preview_hint = function(hint){
        $scope.hint = hint;
        WebworkService.previewHint(hint, $scope.problem_seed, true).
            then(function(rendered_html){
                $scope.hint_html_template = rendered_html;
                $scope.rendered_hint = $sce.trustAsHtml(rendered_html);
            }, function(error){
                console.log(error);
            });
    };

    $scope.$watch('edited_hint', function(newVal, oldVal){
        if(!newVal){
            console.log("woot");
            $scope.reload_hints();
        }
    });

    $scope.send_hint = function(){
        SockJSService.add_hint(
            course, set_id, problem_id, user_id, $scope.box, $scope.hint.hint_id, $scope.hint_html_template);
    };
    $scope.cancel_hint = function(){
        $scope.rendered_hint = "";
    };

    $scope.new_hint = function(){
        $scope.edited_hint = {
            pg_header: $scope.pg_header,
            pg_footer: $scope.pg_footer,
            author: 'teacher',
            set_id: set_id,
            problem_id: problem_id
        };
    };

    $scope.edit_hint = function(hint){
        $scope.edited_hint = hint;
    };

    $scope.delete_hint = function(hint){
        WebworkService.deleteHint(course, hint.hint_id).success($scope.reload_hints);
    };

    // Auto send 'release_student' when closing window
    $scope.$on('$destroy', function(event){
        SockJSService.release_student(course, set_id, problem_id, user_id);
    });

    window.onbeforeunload = function() {
        SockJSService.release_student(course, set_id, problem_id, user_id);
    };


    $scope.showPart = function(part){
        $scope.current_part = part;
    };
    $scope.displayed_answers = [];
});
