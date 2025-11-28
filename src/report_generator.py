class ReportGenerator:
    """Produces reports and evaluates data quality."""

    def __init__(self, doctor):
        self._doctor = doctor
        self._report_data = {}
        self._score = 0

    def report(self):
        self._report_data = {
            "issues": self._doctor.get_summary(),
            "fixes": self._doctor.get_fix_log()
        }
        return self._report_data

    def health_score(self):
        issues = self._doctor.get_summary()
        missing = issues["missing"].sum()
        duplicates = issues["duplicates"]
        outliers = sum(issues["outliers"].values())
        total_penalty = missing + duplicates + outliers
        self._score = max(0, 100 - total_penalty)
        return self._score

    def export_report(self, file_name="report.txt"):
        with open(file_name, "w") as f:
            f.write(str(self._report_data))

    # Dunder method
    def __repr__(self):
        return f"<ReportGenerator doctor={self._doctor}>"
