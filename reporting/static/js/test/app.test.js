describe('app', function() {
  "use strict";
  var scope, Episode, $controller, controller;

  beforeEach(function(){
    module('opal.reports');
  });

  describe('always true', function(){
    it("should run tests", function(){
      expect(true).toBe(true);
    })
  });
});