# Week 4 Capstone Project: Employee Data Analysis Project
# Demonstrates Pandas data manipulation, CSV I/O, filtering, and aggregation.

import os
import pandas as pd


class EmployeeDataAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads the dataset using Pandas with automatic sample creation for testing."""
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' not found. Generating dummy dataset...")
            self._generate_sample_csv()

        try:
            self.df = pd.read_csv(self.file_path)
            print(f"Successfully loaded dataset from '{self.file_path}'.")
            print(f"Dataset Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns.\n")
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def _generate_sample_csv(self):
        """Helper method to generate a standard Kaggle-style employee CSV."""
        sample_data = {
            "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
            "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"],
            "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "Marketing"],
            "Salary": [75000, 50000, 90000, 65000, 52000, 82000, 95000, 48000],
            "Experience_Years": [3, 2, 6, 4, 2, 5, 7, 1]
        }
        df_sample = pd.DataFrame(sample_data)
        df_sample.to_csv(self.file_path, index=False)
        print(f"Sample dataset created: {self.file_path}")

    def display_metrics(self):
        """Calculates and displays average salary and department employee counts."""
        if self.df is None:
            print("Data not loaded!")
            return

        print("=" * 45)
        print(f"{'EMPLOYEE DATA METRICS':^45}")
        print("=" * 45)

        # Average salary calculation
        avg_salary = self.df["Salary"].mean()
        print(f"Average Salary across company: ${avg_salary:,.2f}\n")

        # Department counts
        dept_counts = self.df["Department"].value_counts()
        print("Employee Count by Department:")
        print("-" * 30)
        for dept, count in dept_counts.items():
            print(f"{dept:<15} : {count} employees")
        print("-" * 30)

    def filter_and_export_high_earners(self, threshold: float, output_file: str):
        """Filters employees with salary above threshold and exports to new CSV."""
        if self.df is None:
            print("Data not loaded!")
            return

        high_earners = self.df[self.df["Salary"] > threshold]

        print(f"\nFound {len(high_earners)} employees with salary > ${threshold:,.2f}:")
        print(high_earners[["EmployeeID", "Name", "Department", "Salary"]].to_string(index=False))

        # Export to CSV
        try:
            high_earners.to_csv(output_file, index=False)
            print(f"\nFiltered results exported successfully to '{output_file}'.")
        except Exception as e:
            print(f"Error exporting data: {e}")


def main():
    input_csv = "employee_dataset.csv"
    output_csv = "high_salary_employees.csv"

    analyzer = EmployeeDataAnalyzer(input_csv)
    analyzer.load_data()
    analyzer.display_metrics()

    # Prompt user or use default threshold
    try:
        user_thresh = input("\nEnter salary threshold to filter (default 60000): ").strip()
        threshold = float(user_thresh) if user_thresh else 60000.0
    except ValueError:
        print("Invalid input! Using default threshold of 60,000.")
        threshold = 60000.0

    analyzer.filter_and_export_high_earners(threshold, output_csv)


if __name__ == "__main__":
    main()