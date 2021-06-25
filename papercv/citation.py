"""Class definition and Function to create citation file"""

import ads
class papers:
    
    def __init__(self, orcid_id, username, sort_by='year', filename='citation_list'):
        self.orcid_id = orcid_id
        self.username = username
        self.sort_by = sort_by
        self.filename = filename
        
    def query_ADS(self):
        self.first_paper_data = list(ads.SearchQuery(orcid=self.orcid_id, first_author=self.username, sort=self.sort_by, 
                               fl=['author', 'title', 'pub', 'year', 'volume', 'page', 'citation_count']))
        self.nth_paper_data = list(ads.SearchQuery(orcid=self.orcid_id, sort=self.sort_by, 
                               fl=['author', 'title', 'pub', 'year', 'volume', 'page', 'citation_count']))
        
    def generate_citation(self):

        # NOTE: Provide option for number of authors to be displayed -- print et al. after that number
        # NOTE: Formatting for nth author

        self.query_ADS()
            
        # First Author Paper Data and Citation Building
        first_paper_citations = []
        first_paper_titles = []

        for index in range(len(self.first_paper_data)):
            
            citation_string = ''
            
            if(self.first_paper_data[index].year!=None and self.first_paper_data[index].pub!=None and 
            self.first_paper_data[index].volume!=None and self.first_paper_data[index].page[0]!=None and self.first_paper_data[index].title[0]!=None):
                paper_title = self.first_paper_data[index].title[0]

                for i, author_name in enumerate(self.first_paper_data[index].author):
                    split_name = author_name.split(',')

                    if(len(split_name)==1):
                        split_name.append(split_name[0][0]+' '+split_name[0][1])

                    split_last_name = split_name[1].split(' ')

                    if(len(split_last_name)==3):
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'. '+split_last_name[2][0]+'., '
                    else:
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'., '
                    
                    
                citation_string += self.first_paper_data[index].year+', '+self.first_paper_data[index].pub+', '+self.first_paper_data[index].volume+', '+self.first_paper_data[index].page[0]
                
                first_paper_citations.append(citation_string)
                first_paper_titles.append(paper_title)

        self.first_paper_citations = first_paper_citations
        self.first_paper_titles = first_paper_titles

        ############################################
        # nth Author Paper Data and Citation Building
        nth_paper_citations = []
        nth_paper_titles = []

        for index in range(len(self.nth_paper_data)):
            
            citation_string = ''
            
            if(self.nth_paper_data[index].year!=None and self.nth_paper_data[index].pub!=None and 
            self.nth_paper_data[index].volume!=None and self.nth_paper_data[index].page[0]!=None and self.nth_paper_data[index].title[0]!=None):
                paper_title = self.nth_paper_data[index].title[0]

                for i, author_name in enumerate(self.nth_paper_data[index].author):
                    split_name = author_name.split(',')

                    if(len(split_name)==1):
                        split_name.append(split_name[0][0]+' '+split_name[0][1])

                    split_last_name = split_name[1].split(' ')

                    if(len(split_last_name)==3):
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'. '+split_last_name[2][0]+'., '
                    else:
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'., '
                    
                    
                citation_string += self.nth_paper_data[index].year+', '+self.nth_paper_data[index].pub+', '+self.nth_paper_data[index].volume+', '+self.nth_paper_data[index].page[0]
                
                if(paper_title not in self.first_paper_titles):
                    nth_paper_citations.append(citation_string)
                    nth_paper_titles.append(paper_title)

        self.nth_paper_citations = nth_paper_citations
        self.nth_paper_titles = nth_paper_titles
                
    def write_citation(self):
        cite_file = open(self.filename+'_first_author.txt',"w")
        for index in range(len(self.first_paper_titles)):
            cite_file.write(self.first_paper_titles[index])
            cite_file.write('\n')
            cite_file.write(self.first_paper_citations[index])
            cite_file.write('\n')
            cite_file.write('\n')

        cite_file.close()

        cite_file = open(self.filename+'_nth_author.txt',"w")
        for index in range(len(self.nth_paper_titles)):
            cite_file.write(self.nth_paper_titles[index])
            cite_file.write('\n')
            cite_file.write(self.nth_paper_citations[index])
            cite_file.write('\n')
            cite_file.write('\n')

        cite_file.close()

def create_citation_file(orcid_id, username, sort_by='year', filename='citation_list'):
    """Citation File Creation

    Generate .txt file with paper titles and citations for given author name.

    Args:
        orcid_id (str): Author unique ORCID identifier - ORCID ID is used to search papers.
        username (str): Name of author in 'Last Name, First Name/First Initial' format. E.g. 'Sanghi, Aniket' or 'Shah, N.'
        sort_by (str): Sort the papers queried by either 'year' or 'citation_count'
        filename (str): Filename for the .txt file with paper titles and citations. E.g. 'citation_list'
        
    Returns:
        citation file: .txt file with first and nth author paper titles and citations.
    """
    author_obj = papers(orcid_id=orcid_id, username=username, sort_by=sort_by, filename=filename)
    author_obj.generate_citation()
    author_obj.write_citation()
    
