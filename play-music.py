content = """<!DOCTYPE html><html><head>
<script type="text/javascript" src="http://jplayer.org/latest/lib/jquery.min.js"></script>
<script type="text/javascript" src="http://jplayer.org/latest/dist/jplayer/jquery.jplayer.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){ var stream = { title: "ABC Jazz", mp3: "http://listen.radionomy.com/abc-lounge" }, ready = false;
$("#jquery_jplayer_1").jPlayer({ ready: function (event) { ready = true; $(this).jPlayer("setMedia", stream).jPlayer("play"); },
supplied: "mp3", }); });</script></head><body><div id="jquery_jplayer_1" class="jp-jplayer"></div></body></html>"""
from PyQt4.QtWebKit import QWebView
v = QWebView()
v.setHtml(content)
