import os
import pandas as pd

def sample_and_save_by_region(df, region_column, output_filename="data/external/sampled_regions.csv", n_samples=500):
    """
    Takes a pandas DataFrame, samples 500 rows per region,
    and saves the output to the local folder.
    """
    # 1. Sample 500 points from each region
    sampled_df = df.groupby(region_column).sample(n=n_samples, random_state=42)
    sampled_df = sampled_df.reset_index(drop=True)
    
    # 2. Get the current local directory path
    local_path = os.path.join(os.getcwd(), output_filename)
    
    # 3. Save to local folder
    sampled_df.to_csv(local_path, index=False)
    
    print(f"✅ Success! File saved locally at: {local_path}")
    return sampled_df

if __name__ == "__main__":
    # Load the dataset
    data_path = "data/interim/df_without_outliers.csv"  # Update this path as needed
    df = pd.read_csv(data_path)
    ## only take region and lat long columns
    df = df[["region", "pickup_latitude", "pickup_longitude"]]

    
    # Sample and save by region
    sampled_df = sample_and_save_by_region(df, region_column="region", output_filename="data/external/sampled_regions.csv", n_samples=500)
