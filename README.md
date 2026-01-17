# Aadhaar Enrolment Data Analysis (UIDAI Data Hackathon)

## Objective
To analyze UIDAI Aadhaar enrolment data and uncover meaningful demographic, temporal, and regional trends that can support evidence-based policy planning and operational decision-making.

---

## Dataset
The project uses the official Aadhaar enrolment dataset downloaded from **data.gov.in**.  
Due to large data volume, the dataset is split into multiple CSV files and merged programmatically during analysis.

### Dataset Features
- `date` – Date of enrolment/update  
- `state` – State name  
- `district` – District name  
- `pincode` – Area pincode  
- `age_0_5` – Enrolments for age group 0–5  
- `age_5_17` – Enrolments for age group 5–17  
- `age_18_greater` – Enrolments for age group 18+  

---

## Project Structure
aadhar_analysis_data_hackathon/
├── data/
│ └── aadhar_enrolment_data/
│ ├── api_data_aadhar_enrolment_0_500000.csv
│ ├── api_data_aadhar_enrolment_500000_1000000.csv
│ └── api_data_aadhar_enrolment_1000000_1006029.csv
├── outputs/
│ ├── enrolments_by_age.png
│ ├── top_states.png
│ └── enrolment_trend.png
├── src/
│ └── analysis.py
├── requirements.txt
└── README.md


---

## Analysis Performed
The following analyses were conducted:

- **Demographic Analysis**  
  Aadhaar enrolment distribution across age groups (0–5, 5–17, 18+)

- **Temporal Analysis**  
  Time-based trends to identify spikes, drops, and campaign-driven enrolment patterns

- **Geographic Analysis**  
  Identification of top states contributing to Aadhaar enrolments

---

## Key Insights
- Aadhaar enrolment activity is dominated by the **0–5 age group**, indicating a strong focus on early-life registration.
- Enrolment trends show **sharp temporal spikes**, suggesting campaign-driven or policy-triggered registration drives.
- High enrolment volumes are concentrated in **high-population states**, reflecting demographic structure rather than economic factors.

---

## Use Cases
- **Policy Planning:** Support targeted Aadhaar enrolment initiatives for children.
- **Resource Allocation:** Optimize staffing and infrastructure during peak enrolment periods.
- **Operational Monitoring:** Detect anomalies and sudden demand surges.
- **Program Evaluation:** Measure the impact of government enrolment campaigns.

---

## How to Run the Project

### Prerequisites
- Python 3.8 or above

### Steps
```bash
pip install -r requirements.txt
cd src
python analysis.py


Output

All generated visualizations are automatically saved in the outputs/ folder.

Conclusion

This project demonstrates how large-scale Aadhaar enrolment data can be transformed into actionable insights using data analysis and visualization techniques, supporting better governance and operational efficiency.
