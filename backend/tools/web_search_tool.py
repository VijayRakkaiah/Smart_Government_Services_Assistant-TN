def search_scheme(query: str):
    mock_db = {
        "income certificate": "Apply via TN eSevai portal with Aadhaar, ration card.",
        "community certificate": "Submit application through VAO office or online portal."
    }
    return mock_db.get(query.lower(), "No scheme found.")
