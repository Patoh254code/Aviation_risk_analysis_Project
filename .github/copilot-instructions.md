# Aviation Risk Assessment Project - AI Agent Guide

This project analyzes aviation accident data to assess risks for commercial and private aircraft operations. The analysis is primarily done in Python using Jupyter notebooks and produces visualizations that inform strategic business decisions.

## Project Structure

- `index.ipynb`: Main analysis notebook containing data preprocessing, analysis, and visualization code
- `Data/`: Contains raw and processed datasets
  - `AviationData.csv`: Raw NTSB aviation accident data
  - `CleanAviationData.csv`: Preprocessed dataset
- `Images/`: Generated visualizations for key findings
- `pdf/`: Documentation including dashboard and presentation materials

## Data Analysis Workflow

1. **Data Loading and Preprocessing**
   - Data is loaded from `Data/AviationData.csv` using pandas with `latin-1` encoding
   - Use `low_memory=False` when reading CSV due to mixed data types
   ```python
   df = pd.read_csv('Data/AviationData.csv', encoding='latin-1', low_memory=False)
   ```

2. **Key Features for Analysis**
   - Aircraft details: Make, Model, Aircraft Category
   - Risk factors: Weather Condition, Broad Phase of Flight
   - Operation type: FAR Description, Schedule, Purpose of Flight
   - Injury data: Total Fatal/Serious/Minor Injuries

3. **Visualization Conventions**
   - Use Matplotlib with `%matplotlib inline` for notebook displays
   - Key visualizations are saved to `Images/` directory
   - Standard plot types:
     - Bar charts for comparative analysis
     - Line charts for temporal trends
     - Additional plots in Tableau dashboard

## Integration Points

- **Tableau Dashboard**: Project includes an interactive dashboard at [public.tableau.com](https://public.tableau.com/views/learn-project-03-28-25-PO/Dashboard1)
- **GitHub**: Project uses Git for version control with findings documented in README.md

## Development Workflows

1. **Running Analysis**
   - Execute notebook cells sequentially from top to bottom
   - Key data cleaning and preprocessing must complete before visualization cells

2. **Generating Visualizations**
   - Charts are automatically saved to `Images/` directory
   - Follow naming convention: descriptive-name.jpg (e.g., `Weather-impact.jpg`)

3. **Adding New Analysis**
   - Add new code cells after related existing analysis
   - Document findings in both notebook markdown and README.md
   - Update Tableau dashboard if needed

## Project Conventions

- **Data Quality**
  - Handle missing values explicitly (don't drop without justification)
  - Document data cleaning steps in markdown cells
  - Save cleaned datasets to `Data/` with "Clean" prefix

- **Code Organization**
  - Use helper functions for repeated operations (see `unique_values()` function)
  - Include docstrings for custom functions
  - Keep visualization code organized by analysis objective