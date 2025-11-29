# **Project Overview — DataMedic**

**DataMedic** is a modular and extensible data processing toolkit designed to streamline the essential steps of data analysis, from loading and inspecting data to cleaning, visualizing, exporting, and reporting. The project aims to provide a structured, beginner-friendly framework that makes data workflows more organized, reusable, and easier to maintain.

Built with a medical-inspired theme, each component of the system plays a specific “role” in diagnosing and treating datasets:

- **DataGetter** – fetches and loads raw data files from a specified directory

- **DataDoctor** – performs cleaning operations such as handling missing values, duplicates, and inconsistent entries

- **DataInspector** – examines dataset structure, quality, and statistical characteristics

- **DataVisualizer** – generates charts and plots for data interpretation

- **DataExporter** – saves cleaned or transformed datasets to various file formats

- **ReportGenerator** – produces text-based summaries of data conditions and processing steps

- **DataPipeline** – orchestrates and automates the full workflow from start to finish

The modular design ensures that each component can be used independently or as part of a complete automated pipeline. This makes DataMedic effective for tasks such as exploratory analysis, data cleaning exercises, classroom demonstrations, and rapid prototyping.

By organizing the system as a Python package with clear separation of concerns, DataMedic emphasizes clean architecture, reusability, and maintainability—making the toolkit valuable for students, beginners, and anyone who needs a practical, structured approach to data analysis.

# Installation

```python
pip install datamedic
```

# Example usage

```python
# Import core modules from the DataMedic package
from DataMedic.data_getter import DataGetter
from DataMedic.data_doctor import DataDoctor
from DataMedic.data_visualizer import DataVisualizer
from DataMedic.data_exporter import DataExporter
from DataMedic.report_generator import ReportGenerator
from DataMedic.data_pipeline import DataPipeline

# 1. Load a dataset
getter = DataGetter(r"C:\Users\jorda\Documents\GitHub\DataMedic\datasets")
df = getter.read_csv("dirty_cafe_sales.csv")

# 2. Diagnose and clean using DataDoctor
doctor = DataDoctor(df)
print("Issues Found:", doctor.inspect())
print("Doctor Diagnosis:", doctor.diagnose())

cleaned_df = doctor.treat()

# 3. Visualize the cleaned dataset
viz = DataVisualizer(cleaned_df)
viz.plot_missing()          # Missing values heatmap
viz.plot_histograms()       # Numeric distributions
viz.plot_correlations()     # Correlation matrix

# 4. Generate a quality report
reporter = ReportGenerator(doctor)
report = reporter.report()
score = reporter.health_score()

print("\n--- Data Quality Report ---")
print(report)
print("Health Score:", score)

# 5. Export cleaned data
exporter = DataExporter(cleaned_df)
exporter.to_csv("cleaned_output.csv")
exporter.to_excel("cleaned_output.xlsx")

# 6. (Optional) Full automated pipeline
pipeline = DataPipeline(getter, doctor, reporter, exporter)
final_data = pipeline.run("dirty_dataset.csv")
```


