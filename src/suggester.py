# Suggested fixes for each category
SUGGESTION_MAP = {
    "Database Error": "Check DB connection string, credentials, and network access.",
    "Authentication Error": "Verify token validity, user permissions, or session expiry.",
    "Network Error": "Ensure host is reachable, check DNS and firewall settings.",
    "File/IO Error": "Check file path, disk permissions, or space issues.",
    "Null/Value Error": "Validate objects before use; check for None or missing data.",
    "Unknown": "Try debugging manually or consult logs for more context.",
}

# Optional: Stack Overflow tags for reference
STACKOVERFLOW_TAGS = {
    "Database Error": "https://stackoverflow.com/questions/tagged/database",
    "Authentication Error": "https://stackoverflow.com/questions/tagged/authentication",
    "Network Error": "https://stackoverflow.com/questions/tagged/networking",
    "File/IO Error": "https://stackoverflow.com/questions/tagged/file-io",
    "Null/Value Error": "https://stackoverflow.com/questions/tagged/nullpointerexception",
}

def suggest_fix(category: str) -> str:
    return SUGGESTION_MAP.get(category, "No suggestion available.")

def suggest_link(category: str) -> str:
    return STACKOVERFLOW_TAGS.get(category, "https://stackoverflow.com/")

def enrich_with_suggestions(df):
    df["suggestion"] = df["category"].apply(suggest_fix)
    df["reference"] = df["category"].apply(suggest_link)
    return df

# Quick test
if __name__ == "__main__":
    from reader import read_log_file
    from parser import parse_log_dataframe
    from classifier import classify_dataframe

    df = read_log_file("logs/sample.log")
    df = parse_log_dataframe(df)
    df = classify_dataframe(df)
    df = enrich_with_suggestions(df)

    print(df[["message", "category", "suggestion", "reference"]].head())
