# 
import pandas as pd 

def multi_sample_data6(df, conditions_list, sample_sizes, seed = 5000):
    sampled_df = pd.DataFrame()
    copy_df = df.copy()  # Create a copy of the DataFrame
    seed = seed
    while len(sampled_df) < sum(sample_sizes):
        for i in range(len(conditions_list)):
            condition = conditions_list[i]
            sample_size = sample_sizes[i]
            condition_df = copy_df.query(condition)
            condition_df = condition_df.drop_duplicates(subset='unique_id', keep='first')
            if len(condition_df) < sample_size:
                print(f"Available IDs = {len(condition_df)}, Required Sample = {sample_size}, break")
                continue  # Skip to the next iteration if the condition_df is smaller than sample_size
            sampled_condition_df = condition_df.sample(n=sample_size, random_state=seed)
            print("Seed: " + str(seed) + ". Sampled condition: " + condition + ". Sample size: " + str(
                sample_size) + ". Total Sample size: " + str(len(sampled_df)))
            sampled_df = pd.concat([sampled_df, sampled_condition_df])
            copy_df = copy_df[~copy_df['unique_id'].isin(sampled_condition_df['unique_id'])].copy()
        if len(condition_df) < sample_size:
            break  # Exit the while loop if any condition_df is smaller than sample_size
    return sampled_df

# new drawing: 
def multi_sample_data6_new(df, conditions_list, sample_sizes, seed = 5000):
    sampled_df = pd.DataFrame()
    copy_df = df.copy()  # Create a copy of the DataFrame
    seed = seed
    while len(sampled_df) < sum(sample_sizes):
        for i in range(len(conditions_list)):
            condition = conditions_list[i]
            sample_size = sample_sizes[i]
            condition_df = copy_df.query(condition)
            condition_df = condition_df.drop_duplicates(subset='unique_id', keep='first')
            if len(condition_df) < sample_size:
                print(f"Condition = {condition}, Available IDs = {len(condition_df)}, Required Sample = {sample_size}, break")
                sampled_condition_df = condition_df
            else:
                sampled_condition_df = condition_df.sample(n=sample_size, random_state=seed)
                print("Seed: " + str(seed) + ". Sampled condition: " + condition + ". Sample size: " + str(
                sample_size) + ". Total Sample size: " + str(len(sampled_df)))
            sampled_df = pd.concat([sampled_df, sampled_condition_df])
            copy_df = copy_df[~copy_df['unique_id'].isin(sampled_condition_df['unique_id'])].copy()
    return sampled_df
