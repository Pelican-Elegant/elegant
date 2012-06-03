====================
COLUMNAL GRID SYSTEM
====================

Columnal is a project created by Pulp+Pixels - www.pulpandpixels.com

The Columnal CSS grid system is a "remix" of a couple others with some custom code thrown in. The elastic grid system is borrowed from cssgrid.net, while some code inspiration (and the idea for subcolumns) are taken from 960.gs. The CSS reset is the famous reset created by the CSS rockstar, Eric Meyer.

Please visit columnal.com for more information on the grid system.

===============================================

The Columnal CSS includes necessary at the top of an html page should appear like the demo page, but similar to this: 

<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  
<!-- The Columnal Grid (base, load first) -->
	<link rel="stylesheet" href="css/columnal.css" type="text/css" media="screen" />

<!-- Fixes for IE -->
	<!--[if lt IE 9]>
    	<link rel="stylesheet" href="css/ie.css" type="text/css" media="screen" />
	<![endif]-->

	<!-- use "fixed-984px-ie.css" or "fixed-960px-ie.css for a 984px or 960px fixed width for IE6 and 7 -->
	<!--[if lte IE 7]>
		<link rel="stylesheet" href="css/fixed-984px-ie.css" type="text/css" media="screen" />
	<![endif]-->
	
<!-- Fixes for IE6, only needed if IE 6 will be supported - width must match 984px or 960px of css file used above -->
<!-- Use .imagescale to fix IE6 issues with full-column width images (class must be added to any image wider than the column it is placed into) -->
	<!--[if lte IE 6]>
		<link rel="stylesheet" href="css/ie6-984px.css" type="text/css" media="screen" />
	<![endif]-->
  <!-- End fixes for IE -->

<!-- Page building tools - Gray box colors and page debugging tools -->
    <link rel="stylesheet" href="css/build.css" type="text/css" media="screen" />

====================
CSS FILES
====================

columnal.css
	• HTML Reset (Eric Meyer HTML Reset)
	• Type and image settings (Columnal comes with basic type presets, but custom type control is encouraged, another option is a CSS type framework such as Tripoli CSS from devkick
    • Common base code for the CSS framework - this is where the columns are defined across browsers, and basic functions are added. Also includes Eric Meyer reset.
	• Mobile stylesheet (moves the layout to a single column for mobile viewing)

custom.css
    • Place custom page layouts here - see notes in file

build.css
	• Page building tools - Gray box colors and page debugging tools

====================
CSS Files for Internet Explorer
====================

ie.css
    CSS "fixes" for Internet Explorer (across versions), the fixed width for Internet Explorer 8 can be set at the bottom of this page, it is NOT SET by default. This means IE8 will follow the width of the browser down to a ridiculously thin dimension.

fixed-984px-ie.css or fixed-960px-ie.css
    CSS "fixes" for Internet Explorer 6 and 7. This sets the page width to a fixed width of either 984px or 960px, adding better support for the older browsers.

ie6-984px.css or ie6-960px.css
    CSS "fixes" unique to Internet Explorer 6. Fixes for IE6, only needed if IE 6 will be supported - use .imagescale to fix IE6 issues with full-column width images (class must be added to any image wider than the column it is placed into)