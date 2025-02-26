import requests
from bs4 import BeautifulSoup

# List of URLs to process
urls = [
    "https://thelfer.github.io/tfel/web/Default-keywords.html",
    "https://thelfer.github.io/tfel/web/DefaultCZM-keywords.html",
    "https://thelfer.github.io/tfel/web/DefaultFiniteStrain-keywords.html",
    "https://thelfer.github.io/tfel/web/DefaultGenericBehaviour-keywords.html",
    "https://thelfer.github.io/tfel/web/DefaultModel-keywords.html",
    "https://thelfer.github.io/tfel/web/Implicit-keywords.html",
    "https://thelfer.github.io/tfel/web/ImplicitCZM-keywords.html",
    "https://thelfer.github.io/tfel/web/ImplicitFiniteStrain-keywords.html",
    "https://thelfer.github.io/tfel/web/ImplicitGenericBehaviour-keywords.html",
    "https://thelfer.github.io/tfel/web/ImplicitModel-keywords.html",
    "https://thelfer.github.io/tfel/web/ImplicitII-keywords.html",
    "https://thelfer.github.io/tfel/web/IsotropicMisesCreep-keywords.html",
    "https://thelfer.github.io/tfel/web/IsotropicMisesPlasticFlow-keywords.html",
    "https://thelfer.github.io/tfel/web/IsotropicPlasticMisesFlow-keywords.html",
    # "https://thelfer.github.io/tfel/web/IsotropicStrainHardeningMisesCreep-keywords.html", # does not exist
    "https://thelfer.github.io/tfel/web/MaterialLaw-keywords.html",
    "https://thelfer.github.io/tfel/web/MaterialProperty-keywords.html",
    "https://thelfer.github.io/tfel/web/Model-keywords.html",
    "https://thelfer.github.io/tfel/web/MultipleIsotropicMisesFlows-keywords.html",
    "https://thelfer.github.io/tfel/web/RungeKutta-keywords.html",
    "https://thelfer.github.io/tfel/web/RungeKuttaFiniteStrain-keywords.html",
    "https://thelfer.github.io/tfel/web/RungeKuttaGenericBehaviour-keywords.html",
    "https://thelfer.github.io/tfel/web/RungeKuttaModel-keywords.html",
]

# Function to fetch keywords from a URL
def fetch_keywords(url):
    try:
        # Request the HTML content of the page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the #TOC section and extract keywords
        toc_section = soup.select("div#TOC ul li a code")
        
        # Extract and clean the keywords
        # keywords = [code.text.replace("@", "") for code in toc_section]
        keywords = [code.text[1:] for code in toc_section if code.text != ';']
        return keywords
    except Exception as e:
        print(f"Error fetching keywords from {url}: {e}")
        return []

# Collect keywords from all URLs
set_of_all_keywords = set()
# keywords_lists = []
for url in urls:
    print(f"Processing {url}")
    keywords = fetch_keywords(url)
    set_of_all_keywords.update(keywords)
    # keywords_lists.append(keywords)

print("Number of keywords:", len(set_of_all_keywords))
print("Regex for syntax definition (YAML):")
print( "|".join(sorted(set_of_all_keywords)) )