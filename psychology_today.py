from bs4 import BeautifulSoup
import main

class PsychologyTodayScraper:
    BASE_URL = 'https://www.psychologytoday.com'

    def __init__(self, url):
        """_summary_

        Args:
            url (_type_): url to scrape.  Use the online filters to narrow down the list to start with, then copy that url here.
        """
        self.therapists = []
        next = url
        while next:
            page_content = main.fetch_page(next)
            soup = BeautifulSoup(page_content, 'html.parser')
            therapist_divs = soup.find_all('div', class_='results-row')
            #note, list can contain None for therapists with no qualifications listed
            self.therapists += [self.parse_therapist_div(div) for div in therapist_divs]
            previous_next = soup.find_all('a', class_='previous-next-btn directory-button grey outline small previous-next-btn')
            if 'Next' in previous_next[-1]['title']:
                next = previous_next[-1]['href']
                print()
                print(next)
            else:
                next = None


    def parse_therapist_div(self, div):
        name_tag = div.find('a', class_='profile-title')
        name = name_tag.get_text(strip=True) if name_tag else 'N/A'
        profile_url = name_tag['href']
        try:
            details_page = main.fetch_page(profile_url)
        except:
            return None
        details_soup = BeautifulSoup(details_page, 'html.parser')
        qualifications_tag = details_soup.find('div', class_='qualifications')
        if not qualifications_tag:
            return None
        license = qualifications_tag.find('span', class_='primary-details').get_text(strip=True)
        additional = [li.get_text(strip=True) for li in qualifications_tag.find_all('li', class_='qualifications-element')]

        return {
            'name': name,
            'profile_url': profile_url,
            'license': license,
            'additional_qualifications': additional
        }