
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
    $$( '.setup-progress .bar' ).each( 
      function( obj, index ) {
        obj.setStyle( { 
          width: ( val * 100 ) + '%'
        } );
      }
    );
  };

  var is_setup_screen = function() {
    if( $$( '#setup' ).length > 0 ) 
      return true;
    else 
      return false;
  };


  // FIXME: No validations yet
  var _handle_setup_events = function() {
    _update_setup_progress( 0.1 )

    $$( '.action' ).each( function( o, i ) {
      o.observe( 'click', function( e ) {
        e.preventDefault();

        var _cls = this.getAttribute( 'data-goto' )

        $( this ).
          up( '.control-group' ).
          hide();

        $$( '.' + _cls )[0].
          removeClassName( 'hide' ).
          show();

        // OOh quick progress
        _update_setup_progress( 0.7 );
      } );
    } );


  };

  document.observe( 'dom:loaded', function() {

    if( is_setup_screen() ) {
      _handle_setup_events();
    }


  } );


}();
