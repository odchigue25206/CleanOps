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
from DataMedic.data_getter import DataGetter
from DataMedic.data_doctor import DataDoctor
from DataMedic.report_generator import ReportGenerator
from DataMedic.visualizer import DataVisualizer
from DataMedic.exporter import DataExporter
from DataMedic.pipeline import DataPipeline

# === Step 1: Load dataset ===
getter = DataGetter()
print("Loading file...")
df = getter.read_csv("sample.csv")

# === Step 2: Initialize doctor ===
doctor = DataDoctor(df)

# === Step 3: Visualizer & Exporter ===
visualizer = DataVisualizer(df)
exporter = DataExporter(df)

# === Step 4: Report Generator ===
reporter = ReportGenerator(doctor)

# === Step 5: Build pipeline ===
pipeline = DataPipeline(
    doctor=doctor,
    visualizer=visualizer,
    exporter=exporter,
    reporter=reporter
)

# === Step 6: Run everything ===
pipeline.run()

```


