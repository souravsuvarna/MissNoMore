# MissNoMore - Missing Value Imputation Tool for CSV Datasets

MissNoMore is a Python-based missing value imputation tool designed to handle CSV datasets with missing data. It offers a range of imputation techniques, from simple mean and median strategies to more advanced methods like K-Nearest Neighbors (KNN), iterative imputation, and decision tree-based imputations. The tool provides both a "Basic" mode for quick imputations and an "Advanced" mode for more sophisticated approaches.

## Demo

Try out the deployed MissNoMore application [here](https://missnomore.streamlit.app/).

## Features

- Missing value imputation for CSV datasets
- Two modes: "Basic" (mean, median, interpolate) and "Advanced" (KNN, iterative, decision tree)
- Easy-to-use Streamlit interface
- Leveraging the power of Pandas for data manipulation
- Improves data quality by handling missing data effectively

## Getting Started

### Prerequisites

- Python 3.11+
- Pandas library
- Streamlit library
- Scikit library

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/souravsuvarna/MissNoMore.git
   cd MissNoMore
   ```
3. Install the required libraries:
```
pip install pandas
pip install streamlit
pip install scikit-learn
```

### Usage

1. Run the Streamlit app:
```
streamlit run app.py
```

2. Choose the CSV dataset with missing values you want to impute.

3. Select the desired imputation mode (Basic or Advanced).

4. For Basic mode, choose the column from drop-down list then choose appropriate imputation technique.(mean, median,interpolate,etc) .

5. For Advanced mode, appropriate imputation techniques.( KNN, iterative, decision tree-based imputations,etc).

6. Click the "Submit" button to process the data and generate the imputed dataset.

7. Download the imputed dataset for further analysis.

## Contributing

Contributions to MissNoMore are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or raise an issue.


## Acknowledgments

- The MissNoMore project was inspired by the need for a user-friendly missing value imputation tool.
- Thanks to the developers of Pandas, Streamlit, and other open-source libraries used in this project.

---


