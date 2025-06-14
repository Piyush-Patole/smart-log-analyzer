import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_summary(df):
    """
    Returns a summary DataFrame: counts of each error category
    """
    return df['category'].value_counts().reset_index(name='count').rename(columns={'index': 'category'})

def export_reports(df, output_dir="reports"):
    """
    Save the full enriched DataFrame to CSV and JSON
    """
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, "log_report.csv"), index=False)
    df.to_json(os.path.join(output_dir, "log_report.json"), orient="records", lines=True)
    print(f"Reports saved in '{output_dir}' folder.")

def plot_error_summary(df, output_dir="reports"):
    """
    Creates and saves a bar chart of error categories
    """
    summary_df = generate_summary(df)

    plt.figure(figsize=(10, 5))
    sns.barplot(x="category", y="count", data=summary_df, palette="Set2")
    plt.title("Error Category Summary")
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "error_summary.png"))
    print(f"Summary chart saved as 'error_summary.png'.")

# Quick test
if __name__ == "__main__":
    from reader import read_log_file
    from parser import parse_log_dataframe
    from classifier import classify_dataframe
    from suggester import enrich_with_suggestions

    df = read_log_file("logs/sample.log")
    df = parse_log_dataframe(df)
    df = classify_dataframe(df)
    df = enrich_with_suggestions(df)

    print("\n🔍 Error Summary:")
    print(generate_summary(df))

    export_reports(df)
    plot_error_summary(df)
