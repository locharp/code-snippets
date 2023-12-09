from html.parser import HTMLParser

class MyHTMLParser( HTMLParser ):
    
    def handle_starttag( self, tag, attrs ):
        
        print( "Start :", tag )
        
        for attr, value in attrs:
            print( "->", attr, ">", value )
            
        
        
    def handle_endtag( self, tag ):
        
        print( "End   :", tag )
        
        
        
    def handle_startendtag( self, tag, attrs ):
        
        print( "Empty :", tag )
        
        for attr, value in attrs:
            print( "->", attr, ">", value )


            
            
            
parser = MyHTMLParser()

for i in range( int( input() ) ):
    parser.feed( input() )
