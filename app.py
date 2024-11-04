from flask import Flask, render_template, request
import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_rossi  # Default dataset
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Load the default dataset from lifelines
data = load_rossi()

@app.route('/', methods=['GET', 'POST'])
def index():
    survival_data = None
    graph_url = None  # To store the URL of the generated graph

    if request.method == 'POST':
        # Get age from the form
        age = int(request.form.get('age'))

        # Filter data based on the age condition
        filtered_data = data[data['age'] == age]

        if not filtered_data.empty:
            # Use Kaplan-Meier fitter for survival analysis
            kmf = KaplanMeierFitter()
            kmf.fit(filtered_data['week'], event_observed=filtered_data['arrest'])

            # Prepare survival analysis data
            weeks = filtered_data['week'].max()
            try:
                survival_probability = kmf.survival_function_at_times(weeks).values[0]
                survival_data = {
                    "Survival Probability": round(survival_probability, 3),
                    "Coefficient": kmf.event_table.at[weeks, "observed"] if weeks in kmf.event_table.index else "N/A",
                    "Hazard Ratio": kmf.event_table.at[weeks, "censored"] if weeks in kmf.event_table.index else "N/A",
                    "P-Value": None,
                    "CI Lower": round(kmf.confidence_interval_["KM_estimate_lower_0.95"].values[0], 3) if weeks in kmf.event_table.index else "N/A",
                    "CI Upper": round(kmf.confidence_interval_["KM_estimate_upper_0.95"].values[0], 3) if weeks in kmf.event_table.index else "N/A",
                }

                # Generate and save the plot
                plt.figure(figsize=(10, 6))
                kmf.plot_survival_function(ci_show=True, color='blue', linewidth=2)
                plt.title('Kaplan-Meier Survival Function', fontsize=16)
                plt.xlabel('Weeks', fontsize=14)
                plt.ylabel('Survival Probability', fontsize=14)
                plt.grid(True, linestyle='--', alpha=0.7)

                graph_path = os.path.join('static', 'survival_plot.png')
                plt.savefig(graph_path, bbox_inches='tight')
                plt.close()

                graph_url = graph_path

            except Exception as e:
                survival_data = {"error": str(e)}
        else:
            survival_data = {"error": "No data available for this age."}

    return render_template("index.html", survival_data=survival_data, graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
