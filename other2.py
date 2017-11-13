from HTMLParser import HTMLParser

class Seeker(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for (attribute, value) in attrs:
                if attribute == 'src':
                    print value

parser = Seeker()
parser.feed('''
</div>
			<h1 id="firstHeading" class="firstHeading" lang="en"><i>Haider</i> (film)</h1>
									<div id="bodyContent" class="mw-body-content">
									<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>
								<div id="contentSub"></div>
												<div id="jump-to-nav" class="mw-jump">
					Jump to:					<a href="#mw-head">navigation</a>, 					<a href="#p-search">search</a>
				</div>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><table class="infobox vevent" style="width:22em;font-size:90%;">
<tr>
<th colspan="2" class="summary" style="text-align:center;font-size:125%;font-weight:bold;font-size:110%;font-style:italic;">Haider</th>
</tr>
<tr>
<td colspan="2" style="text-align:center"><a href="/wiki/File:Haider_Poster.jpg" class="image"><img alt="Haider Poster.jpg" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f1/Haider_Poster.jpg/220px-Haider_Poster.jpg" width="220" height="317" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/en/f/f1/Haider_Poster.jpg 1.5x" data-file-width="262" data-file-height="378" /></a>
<div style="font-size:95%;padding:0.35em 0.35em 0.25em;line-height:1.25em;">Theatrical release poster</div>
</td>
</tr>
''')
