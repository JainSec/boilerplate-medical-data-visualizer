# Medical Data Visualizer

## Project Overview
This project analyzes patient medical data to explore the relationship between cardiovascular disease and various health indicators, including body measurements, blood markers, and lifestyle choices. Using Pandas and Seaborn, it generates visualizations such as categorical plots and heat maps to identify patterns in the dataset.

## Dataset Information
**File Name:** `medical_examination.csv`

| Feature                          | Variable Type          | Variable      | Value Type |
|----------------------------------|------------------------|--------------|------------|
| Age                              | Objective Feature      | age          | int (days) |
| Height                           | Objective Feature      | height       | int (cm) |
| Weight                           | Objective Feature      | weight       | float (kg) |
| Gender                           | Objective Feature      | gender       | categorical code |
| Systolic Blood Pressure          | Examination Feature    | ap_hi        | int |
| Diastolic Blood Pressure         | Examination Feature    | ap_lo        | int |
| Cholesterol                      | Examination Feature    | cholesterol  | 1: normal, 2: above normal, 3: well above normal |
| Glucose                          | Examination Feature    | gluc         | 1: normal, 2: above normal, 3: well above normal |
| Smoking                          | Subjective Feature     | smoke        | binary |
| Alcohol Intake                   | Subjective Feature     | alco         | binary |
| Physical Activity                 | Subjective Feature     | active       | binary |
| Cardiovascular Disease (Target)  | Target Variable       | cardio       | binary |

## Functionality
### 1. Data Processing
- Import the dataset into a Pandas DataFrame (`df`).
- **Add Overweight Column**: Calculate BMI using `weight / (height/100)^2`. If BMI > 25, mark as overweight (1), else mark as not overweight (0).
- **Normalize Data**:
  - Set `cholesterol` and `gluc` values to 0 if they are 1 (normal) and to 1 if they are above normal.

### 2. Categorical Plot
- Create a DataFrame (`df_cat`) using `pd.melt()` with the following categorical features: `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight`.
- Group and reformat `df_cat` by `cardio`, count occurrences, and rename columns.
- Use `sns.catplot()` to generate a categorical plot showing counts of good and bad outcomes for each feature, split by `cardio`.

### 3. Heat Map
- **Clean Data** by filtering:
  - Diastolic pressure higher than systolic (`ap_lo <= ap_hi`)
  - Height outside the 2.5th and 97.5th percentiles
  - Weight outside the 2.5th and 97.5th percentiles
- **Calculate Correlation Matrix** (`corr`).
- **Generate Heat Map**:
  - Create a mask for the upper triangle (`mask`).
  - Use `sns.heatmap()` to visualize the correlation matrix.

## Installation & Setup
### Requirements
- Python 3.x
- Pandas
- Seaborn
- Matplotlib

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-url.git
   ```
2. Navigate to the project directory:
   ```sh
   cd medical-data-visualizer
   ```
3. Install dependencies:
   ```sh
   pip install pandas seaborn matplotlib
   ```
4. Run the script:
   ```sh
   python medical_data_visualizer.py
   ```

## Example Output
- **Categorical Plot:**
  ![Categorical Plot Example](examples/Figure_1.png)
- **Heat Map:**
  ![Heat Map Example](examples/Figure_2.png)


## Author
- Pulkit Jain
- Contact: jain.infosec@gmail.com



This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer
