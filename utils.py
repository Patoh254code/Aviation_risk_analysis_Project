"""
Utility functions for aviation risk assessment analysis.
Contains reusable functions for data cleaning, analysis, and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in a DataFrame:
      - Numeric columns -> 0
      - Categorical/object columns -> 'Unknown'

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame whose missing values should be filled.

    Returns
    -------
    pd.DataFrame
        A copy of the DataFrame with missing values replaced.
    """
    df_filled = df.copy()

    # Identify numeric and categorical columns
    num_cols = df_filled.select_dtypes(include=[np.number]).columns
    cat_cols = df_filled.select_dtypes(exclude=[np.number]).columns

    # Fill missing numeric values with 0
    df_filled[num_cols] = df_filled[num_cols].fillna(0)

    # Fill missing categorical values with 'Unknown'
    df_filled[cat_cols] = df_filled[cat_cols].fillna('Unknown')

    # Optional: summary
    print(f"✅ Filled missing values in {len(num_cols)} numeric columns with 0.")
    print(f"✅ Filled missing values in {len(cat_cols)} categorical columns with 'Unknown'.")
    print(f"Total remaining NaNs: {df_filled.isna().sum().sum()}")

    return df_filled

def assess_data_quality(df, print_samples=False):
    """
    Perform a comprehensive data quality assessment on the DataFrame.
    
    Parameters:
    -----------
    df : pandas DataFrame
        The DataFrame to analyze
    print_samples : bool
        Whether to print sample values for categorical columns
        
    Returns:
    --------
    dict
        Dictionary containing quality metrics
    """
    quality_metrics = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': {},
        'unique_values': {},
        'data_types': df.dtypes.to_dict()
    }
    
    for column in df.columns:
        # Calculate missing values
        missing = df[column].isnull().sum()
        missing_pct = (missing / len(df)) * 100
        quality_metrics['missing_values'][column] = {
            'count': missing,
            'percentage': missing_pct
        }
        
        # Count unique values
        unique_count = df[column].nunique()
        quality_metrics['unique_values'][column] = unique_count
        
        # Print sample values for categorical columns if requested
        if print_samples and df[column].dtype == 'object':
            print(f"\nSample values for {column}:")
            print(df[column].value_counts().head())
            
    return quality_metrics

def standardize_text(text):
    """
    Standardize text fields to title case and handle special cases.
    
    Parameters:
    -----------
    text : str
        Text to standardize
    
    Returns:
    --------
    str
        Standardized text
    """
    if pd.isna(text):
        return "Unknown"
    return str(text).strip().title()

def clean_weather_condition(condition):
    """
    Convert weather condition abbreviations to full text.
    
    Parameters:
    -----------
    condition : str
        Weather condition abbreviation
    
    Returns:
    --------
    str
        Full weather condition text
    """
    weather_map = {
        'VMC': 'Visual Meteorological Conditions',
        'IMC': 'Instrument Meteorological Conditions',
        'UNK': 'Unknown'
    }
    condition = str(condition).upper()
    return weather_map.get(condition, standardize_text(condition))

def categorize_operation(purpose, private_ops=None, commercial_ops=None):
    """
    Categorize flight purpose into private or commercial operations.
    
    Parameters:
    -----------
    purpose : str
        Purpose of flight
    private_ops : list, optional
        List of private operation types
    commercial_ops : list, optional
        List of commercial operation types
    
    Returns:
    --------
    str
        Operation category
    """
    if private_ops is None:
        private_ops = ['Personal', 'Executive/Corporate', 'Business', 'Ferry']
    if commercial_ops is None:
        commercial_ops = ['Aerial Application', 'Aerial Observation', 'Public Aircraft']
        
    if purpose in private_ops:
        return 'Private'
    elif purpose in commercial_ops:
        return 'Commercial'
    return 'Other'

def analyze_aircraft_safety(df, min_accidents=23):
    """
    Analyze aircraft safety based on accident frequency and severity.
    
    Parameters:
    -----------
    df : pandas DataFrame
        Cleaned aviation data
    min_accidents : int
        Minimum number of accidents for consideration (1 per year)
    
    Returns:
    --------
    pandas DataFrame
        Safety metrics by aircraft model
    """
    safety_metrics = df.groupby('Make_and_Model').agg({
        'Event.Id': 'count',
        'Total.Fatal.Injuries': 'sum',
        'Total_Injuries': 'sum',
        'Fatality_Rate': 'mean'
    }).rename(columns={'Event.Id': 'Accident_Count'})
    
    safety_metrics = safety_metrics[safety_metrics['Accident_Count'] >= min_accidents]
    
    safety_metrics['Safety_Score'] = (
        safety_metrics['Fatality_Rate'] * 0.4 +
        safety_metrics['Accident_Count'].rank(pct=True) * 0.6
    )
    
    return safety_metrics.sort_values('Safety_Score')

def analyze_risk_factors(df):
    """
    Analyze key risk factors: weather, flight phase, and temporal trends.
    
    Parameters:
    -----------
    df : pandas DataFrame
        Cleaned aviation data
    
    Returns:
    --------
    tuple
        (weather_risk, phase_risk, yearly_trend) DataFrames
    """
    weather_risk = df.groupby('Weather.Condition').agg({
        'Event.Id': 'count',
        'Total.Fatal.Injuries': 'sum',
        'Fatality_Rate': 'mean'
    }).round(3)
    
    phase_risk = df.groupby('Broad.phase.of.flight').agg({
        'Event.Id': 'count',
        'Total.Fatal.Injuries': 'sum',
        'Fatality_Rate': 'mean'
    }).round(3)
    
    yearly_trend = df.groupby('Year')['Event.Id'].count()
    
    return weather_risk, phase_risk, yearly_trend

def analyze_operational_risks(df):
    """
    Compare safety metrics between private and commercial operations.
    
    Parameters:
    -----------
    df : pandas DataFrame
        Cleaned aviation data
    
    Returns:
    --------
    pandas DataFrame
        Risk metrics by operation category
    """
    op_risk = df.groupby('Operation_Category').agg({
        'Event.Id': 'count',
        'Total.Fatal.Injuries': 'sum',
        'Total_Injuries': 'sum',
        'Fatality_Rate': 'mean'
    }).round(3)
    
    op_risk['Accidents_per_Year'] = op_risk['Event.Id'] / df['Year'].nunique()
    
    return op_risk

def plot_save_figure(fig, title, xlabel, ylabel, filename, rotate_xticks=False):
    """
    Helper function to style and save matplotlib figures.
    
    Parameters:
    -----------
    fig : matplotlib figure
        Figure to style and save
    title : str
        Plot title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    filename : str
        Output filename (without path)
    rotate_xticks : bool, optional
        Whether to rotate x-axis labels
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if rotate_xticks:
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'Images/{filename}', dpi=300, bbox_inches='tight')
  
