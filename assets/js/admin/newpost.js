
$( function() {
  $( 'textarea.rich' ).tinymce( {
    script_url: "/js/tinymce/tiny_mce.js",
    theme: "advanced",
    plugins:  "autolink,lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,iespell,inlinepopups,insertdatetime," +
              "media,print,contextmenu,paste,noneditable,nonbreaking",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resizing : true,

    content_css: "/css/content.css"
  } );
} );
