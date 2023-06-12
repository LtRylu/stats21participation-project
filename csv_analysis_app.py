import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display dataset statistics
def display_dataset_stats(data):
    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])

    # Count the number of categorical, numerical, and boolean variables
    dtypes = data.dtypes
    categorical_vars = dtypes[dtypes == object].index
    numerical_vars = dtypes[(dtypes == float) | (dtypes == int)].index
    bool_vars = dtypes[dtypes == bool].index

    st.write("Number of categorical variables:", len(categorical_vars))
    st.write("Number of numerical variables:", len(numerical_vars))
    st.write("Number of boolean variables:", len(bool_vars))

# Display the five number summary and distribution plot
def display_numerical_stats(data, column):
    st.write("Five Number Summary:")
    st.table(data[column].describe())

    st.write("Distribution Plot:")
    num_bins = st.number_input("Number of Bins", min_value=1, max_value=100, value=10, step=1)
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=column, kde=True, bins=num_bins)
    st.pyplot(fig)
    plt.close(fig)

# Display proportions and bar plot for categorical data
def display_categorical_stats(data, column):
    st.write("Proportions Table:")
    proportions = data[column].value_counts(normalize=True)
    st.table(proportions)

    st.write("Bar Plot:")
    fig, ax = plt.subplots()
    sns.countplot(data=data, x=column, ax=ax)
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
    st.pyplot(fig)
    plt.close(fig)

# Main streamlit application
def main():
    st.title("CSV Data Analysis")

    # File uploader
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)

        # Display dataset statistics
        st.header("Dataset Statistics")
        display_dataset_stats(data)

        # Column selection
        selected_column = st.selectbox("Select a column", data.columns)

        # Display statistics based on column type
        if pd.api.types.is_numeric_dtype(data[selected_column]):
            st.header("Numerical Column Analysis")
            display_numerical_stats(data, selected_column)
        elif pd.api.types.is_string_dtype(data[selected_column]):
            st.header("Categorical Column Analysis")
            display_categorical_stats(data, selected_column)
        else:
            st.write("Unsupported column type. Please select a different column.")

if __name__ == '__main__':
    main()