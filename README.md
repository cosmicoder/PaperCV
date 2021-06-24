# PaperCV
A easy-to-use tool to generate references for your academic CV in astronomy.
#### Authors: Aniket Sanghi and Neev Shah
#### Credit: Organizers of Code/Astro for the brilliant workshop that has led to the building and releasing of our first python package!

## Features
Get formatted citation for all first author and nth author papers by a given author.

Upcoming features:
1. Get total number of papers and citation count statistics.
2. Increase the number of pages retrieved from ADS for longer list of papers. 
3. Specify number of authors to print in the citations.

## Quick Start
Install this package:
   
    pip install PaperCV
    
This package uses the ads package (https://github.com/andycasey/ads) to perform queries. Install this package:

    pip install ads
                
You’ll need an API key from NASA ADS labs. Sign up for the newest version of ADS search at https://ui.adsabs.harvard.edu, visit account settings and generate a new API token. The official documentation is available at https://github.com/adsabs/adsabs-dev-api
When you get your API key, set the ads.config.token variable to your API key as shown below, and you are good to go!
        
    import ads
    from papercv import citation
    ads.config.token = 'my token' # Provide your ADS API Token
        
    # Your name in 'Last Name, First Name Initial. Middle Name Initial.' format (middle initial if applicable)
    username = 'Sanghi, A.' 
    
    # Example: Get all first author papers sorted by year
    citation.create_citation_file(username, sort_by='year', authorship='first_author', filename='citation_list.txt')
    
    # Example: Get all first author papers sorted by citation count
    citation.create_citation_file(username, sort_by='citation_count', authorship='first_author', filename='citation_list.txt')
    
    # Example: Get all nth author papers sorted by year
    citation.create_citation_file(username, sort_by='year', authorship='nth_author', filename='citation_list.txt')
  
Known Issue: Similar names aren't differentiated. Presently, the user has to identify papers authored by researchers with a similar name as them in the output file.
