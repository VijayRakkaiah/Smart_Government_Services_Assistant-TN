from backend.tools.web_search_tool import search_scheme
from backend.tools.tn_gov_api_tool import fetch_scheme_details

def get_scheme_info(query):

    basic = search_scheme(query)
    details = fetch_scheme_details(query)

    return {
        "basic": basic,
        "details": details
    }
