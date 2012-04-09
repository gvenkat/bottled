
! function() {

  // Add the console hack
  if( ! window.console ) {
    var __f = function() { };

    window.console = { };

    [  'log', 'warn', 'debug', 'error' ].each( 
      function( name, index ) {
        window.console[ name ] = __f;
      } 
    );

  }

  var _update_setup_progress = function( val ) {
    $( '.setup-progress .bar' ).css( {
      width: ( val * 100 ) + '%'
    } );
  };

  var is_setup_screen = function() {
    if( $( '#setup' ).length > 0 ) 
      return true;
    else 
      return false;
  };


  // FIXME: No validations yet
  var _handle_setup_events = function() {
    _update_setup_progress( 0.1 );

    $( '.action' ).click( function( e ) {
      e.preventDefault();

      var _cls = $( this ).attr( 'data-goto' );

      $( this ).
        parents( '.control-group' ).
        hide();

      $( '.' + _cls ).
        removeClass( 'hide' ).
        show();

      // OOh quick progress
      _update_setup_progress( 0.7 );
    } );
  };


  $( document ).ready( function() {
    if( is_setup_screen() ) {
      _handle_setup_events();
    }
  } );


}();
