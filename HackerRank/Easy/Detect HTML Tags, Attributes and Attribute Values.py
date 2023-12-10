from html.parser import HTMLParser

class MyHTMLParser( HTMLParser ):
    
    def handle_startendtag( self, tag, attrs ):
        
        print( tag )
        
        for attr, value in attrs:
            print( "->", attr, ">", value )
            
            
            
    def handle_starttag( self, tag, attrs ):
        
        print( tag )
        
        for attr, value in attrs:
            print( "->", attr, ">", value )
        
        
        
        
        
parser = MyHTMLParser()

for i in range( int( input() ) ):
    parser.feed( input() )
