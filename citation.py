import ads

class papers:
    
    def __init__(self, username, sort_by='year', authorship='first_author', filename='citation_list.txt'):
        self.username = username
        self.sort_by = sort_by
        self.authorship = authorship
        self.filename = filename
        
    def query_ADS_first_author(self):

        # NOTE: Wrong person papers are included because of name ambiguity

        self.paper_data = list(ads.SearchQuery(first_author=self.username, sort=self.sort_by, 
                               fl=['author', 'title', 'pub', 'year', 'volume', 'page', 'citation_count']))
        
    def query_ADS_nth_author(self):

        # NOTE: Wrong person papers are included because of name ambiguity

        self.paper_data = list(ads.SearchQuery(author=self.username, sort=self.sort_by, 
                               fl=['author', 'title', 'pub', 'year', 'volume', 'page', 'citation_count']))
    
    def generate_citation(self):

        # NOTE: Provide option for number of authors to be displayed -- print et al. after that number
        # NOTE: Formatting for nth author

        if(self.authorship == 'first_author'):
            self.query_ADS_first_author()
        else:
            # NOTE: First author papers need to be excluded
            self.query_ADS_nth_author()
            
        paper_citations = []
        paper_titles = []

        for index in range(len(self.paper_data)):
            flag=1
            citation_string = ''
            paper_title = self.paper_data[index].title[0]
            
            if(self.paper_data[index].year!=None and self.paper_data[index].pub!=None and 
            self.paper_data[index].volume!=None and self.paper_data[index].page[0]!=None):
        
                for i, author_name in enumerate(self.paper_data[index].author):
                 
                    split_name = author_name.split(',')

                    if(len(split_name)==1):
                        split_name.append(split_name[0][0]+' '+split_name[0][1])

                    split_last_name = split_name[1].split(' ')

                    if(len(split_last_name)==3):
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'. '+split_last_name[2][0]+'., '
                    else:
                        citation_string += split_name[0]+', '+split_last_name[1][0]+'., '
                    if i==0:
                        if self.authorship!= 'first_author':
                            print(citation_string[0:len(citation_string)-2])
                            print(self.username)
                            if self.username == citation_string[0:len(citation_string)-2]:
                                flag=0
                                break


                """if(self.authorship != 'first_author'):
                    if self.paper_data[index].author[0]==self.username:
                        flag=0"""
                        
                if flag:

                    citation_string += self.paper_data[index].year+', '+self.paper_data[index].pub+', '+self.paper_data[index].volume+', '+self.paper_data[index].page[0]
                    paper_citations.append(citation_string)
                    paper_titles.append(paper_title)
               

        self.paper_citations = paper_citations
        self.paper_titles = paper_titles
                
    def write_citation(self):
        cite_file = open(self.filename,"w")
        for index in range(len(self.paper_titles)):
            cite_file.write(self.paper_titles[index])
            cite_file.write('\n')
            cite_file.write(self.paper_citations[index])
            cite_file.write('\n')
            cite_file.write('\n')

        cite_file.close()

# Call to Functions -- Example
author_obj = papers(username='Blunt, S.', sort_by='year', authorship='nth_author')
author_obj.generate_citation()
author_obj.write_citation()