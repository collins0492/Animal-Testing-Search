angular.module('search', ['ngAnimate', 'ngSanitize', 'ui.bootstrap'], function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});
angular.module('search').controller('TypeaheadCtrl', function($scope, $http) {
	var _selected;

	$scope.selected = undefined;
	$scope.companies = JSON.parse( $( '#testerData' ).attr('data-data') );
	//Append date to last updated
	$( '#disclaimerLastUpdated' ).append( $scope.companies[0].timestamp );

	$scope.searchResults = function( value ) {
		var result = "N/A";
		var bgColor = "";
		var thumb = $( "#thumb" );
		var icon = "";
		switch( $scope.selected.status ){
			case true:
				result = "<strong>DO</strong>";
				bgColor = "redBg";
				icon = "<span class='glyphicon glyphicon-thumbs-down'></span>";
			break;
			case false:
				result = "<strong>DO NOT</strong>";
				bgColor = "greenBg";
				icon = "<span class='glyphicon glyphicon-thumbs-up'></span>";
			break;
		}
		var msg = $scope.selected.company + " " + $scope.selected.parent + " " + result + " test on animals";
		$( '#searchResults' ).empty().removeClass( 'hide redBg greenBg' ).addClass( bgColor ).append( msg );
		thumb.empty().append( icon );
	};
});