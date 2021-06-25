# PaperCV
A easy-to-use tool to generate references for your academic CV in astronomy.
#### Authors: Aniket Sanghi and Neev Shah
#### Credit: Organizers of Code/Astro for the brilliant workshop that has led to the building and releasing of our first python package!

## Features
Get formatted citation for all first author and nth author papers by a given author. This pacakge queries using an author's unique ORCID ID. If you don't already have one, get one here - https://orcid.org - and start claiming your papers on ADS.

Upcoming features:
1. Get total number of papers and citation count statistics.
2. Increase the number of pages retrieved from ADS for longer list of papers. 
3. Specify number of authors to print in the citations.
4. Generate formatted text for input to LaTeX

## Quick Start
Install this package:
   
    pip install PaperCV==0.3
    
This package uses the ads package (https://github.com/andycasey/ads) to perform queries. Install this package:

    pip install ads
                
You’ll need an API key from NASA ADS labs. Sign up for the newest version of ADS search at https://ui.adsabs.harvard.edu, visit account settings and generate a new API token. The official documentation is available at https://github.com/adsabs/adsabs-dev-api
When you get your API key, set the ads.config.token variable to your API key as shown below, and you are good to go!

![alt text](img.jpg?raw=true)

## Examples
        
    import ads
    from papercv import citation
    ads.config.token = 'my token' # Provide your ADS API Token
        
    # Your ORCID ID
    orcid_id = '0000-0002-1838-4757'
    
    # Your name in 'Last Name, First Name Initial. Middle Name Initial.' format (middle initial if applicable)
    username = 'Sanghi, A.' 
    
    # Example: Get all first and nth author papers sorted by year
    citation.create_citation_file(orcid_id, username, sort_by='year', filename='citation_list')
    
    # Example: Get all first and nth author papers sorted by citation count
    citation.create_citation_file(orcid_id, username, sort_by='citation_count', filename='citation_list')
   
   
