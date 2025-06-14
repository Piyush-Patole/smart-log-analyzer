import sys
import os

from src.reader import read_log_file
from src.parser import parse_log_dataframe
from src.classifier import classify_dataframe
from src.suggester import enrich_with_suggestions
from src.reporter import export_reports, plot_error_summary, generate_summary


def analyze_log_file(log_path: str, log_format: str = "default"):
    if not os.path.exists(log_path):
        print(f"❌ Log file not found: {log_path}")
        return

    print(f"\n📂 Reading log file: {log_path}")
    df = read_log_file(log_path)

    print("\n🔍 Parsing log lines...")
    df = parse_log_dataframe(df, log_format=log_format)

    print("\n🧠 Classifying error categories...")
    df = classify_dataframe(df)

    print("\n💡 Adding AI suggestions...")
    df = enrich_with_suggestions(df)

    print("\n📊 Generating reports...")
    export_reports(df)
    plot_error_summary(df)

    print("\n✅ Log analysis completed successfully!")
    print("\n📌 Summary:")
    print(generate_summary(df))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m src.main <log_file_path> <log_format>")
        print("Example: python -m src.main logs/syslog.log syslog")
        sys.exit(1)

    log_file = sys.argv[1]
    log_format = sys.argv[2]
    analyze_log_file(log_file, log_format)
