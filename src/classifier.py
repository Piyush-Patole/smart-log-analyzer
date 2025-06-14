import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")

# Define basic error categories with keywords
ERROR_CATEGORIES = {
    "Database Error": ["sql", "database", "connection refused", "db"],
    "Authentication Error": ["unauthorized", "forbidden", "login failed", "invalid token"],
    "Network Error": ["timeout", "unreachable", "connection reset", "dns"],
    "File/IO Error": ["file not found", "permission denied", "read-only", "disk full"],
    "Null/Value Error": ["nullpointerexception", "typeerror", "attributeerror", "valueerror"],
}

def classify_error_message(message: str) -> str:
    """
    Classifies a single log message into an error category.
    """
    doc = nlp(message.lower())
    for category, keywords in ERROR_CATEGORIES.items():
        for keyword in keywords:
            if keyword in doc.text:
                return category
    return "Unknown"

def classify_dataframe(df):
    """
    Classifies the 'message' column in a DataFrame.
    Adds a new column 'category'.
    """
    df["category"] = df["message"].apply(classify_error_message)
    return df

# Quick test
if __name__ == "__main__":
    from reader import read_log_file
    from parser import parse_log_dataframe

    df = read_log_file("logs/sample.log")
    parsed_df = parse_log_dataframe(df)
    classified_df = classify_dataframe(parsed_df)
    print(classified_df[["level", "message", "category"]].head())
