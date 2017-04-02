CSS Minifier
==========

A basic, portable CSS minifier which makes minified CSS files for faster access and lowering memory space usage.

This basically trims whitespace and removes comments. It doesn't do any lexical analyzing, so complex or twisted cases may make it fail.


Requirements
============

- Python 2.7.6 and higher


Use
===

- `python cssmin.py`


Example
=======

Given the following input file, `style.css`:

.description {
	max-width: 705px;
	color: grey;
	font-size: 1.875em;

}

.screenshot {
	max-width: 460px;
	max-height: 460px;
	margin-right: 20px;
}


* {
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	-ms-box-sizing: border-box;
	box-sizing: border-box;
}

.app {
	display: flex
}

/* Comment this shit */

.title {
	padding-left: 10px;
	padding-top: 20px;
	margin-bottom: 20px;
	background-color: #33bebe;
	max-width: 1165px;
	color: white;
}
,

`python cssmin.py ` will output the following result:

.description {
max-width: 705px;
color: grey;
font-size: 1.875em;
}
.screenshot {
max-width: 460px;
max-height: 460px;
margin-right: 20px;
}
* {
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
-ms-box-sizing: border-box;
box-sizing: border-box;
}
.app {
display: flex
}
.title {
padding-left: 10px;
padding-top: 20px;
margin-bottom: 20px;
background-color: #33bebe;
max-width: 1165px;
color: white;
}

