angular.module('opal.reporting').controller(
    'ReportDetailCtrl', function($scope, report){
      $scope.report = report;
      $scope.JSON = window.JSON;
    }
);
