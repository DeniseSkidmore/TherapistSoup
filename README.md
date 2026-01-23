# TherapistSoup
Find the keywords you're looking for in the soup of Therapist listings!

Currently extracts therapist name, profile url, license, and additional credentials.  Useful for searching for specific certifications or multi-state licenses for traveling clients or interstate families.

Not a complete application, you stil need a top level script that inputs your url and filters the results further, and that's a very individual peice of code.

## Sample use

``` Python
scraper = PsychologyTodayScraper(filtered_url)
therapists = [therapist for therapist in scraper.therapists if therapist is not None]
with open('pt_results.txt', 'w') as file:
    file.write(json.dumps(therapists))
print('')
for therepist in therapists:
    is_good = False
    is_good2 = False
    for cred in therepist['additional_qualifications']:
        if 'What I'm Looking For' in cred:
            is_good=True
        if 'The other thing I'm Looking for' in cred:
            is_good2=True
    if is_good and is_good2:
        print(therepist)
```
