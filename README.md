# NCAA 2022-2024 Data 
Written by and for MIT Men's Swimming and Diving 2024-25 team

## Install requirements
To install the required packages, you can use pip. First, make sure you have Python and pip installed on your system. Then, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Download data
To download the data into a pandas data frame, do the following in a Python file:
```python
df = pd.read_pickle("ncaa_men_swive_results.pkl")
```

## Application

https://ncaa-swive-data.streamlit.app/
