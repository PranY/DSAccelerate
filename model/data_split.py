def __get_default_values(request_config):
    specification = request_config["specifications"]["training"]
    default_specifications = request_config["default_specifications"]
    train_test_split_percentage = (
        specification["split_percentage"]
        if specification["split_percentage"]
        else default_specifications["split_percentage"]
    )
    test_val_split_percentage = (
        specification["validation_split_percentage"]
        if specification["validation_split_percentage"]
        else default_specifications["validation_split_percentage"]
    )
    return train_test_split_percentage, test_val_split_percentage


def do_data_split_processing(prompt_details, request_config, project_dir):
    train_test_split_percentage, test_val_split_percentage = __get_default_values(
        request_config
    )
    prompt_unformatted_value, file_location = prompt_details
    prompt_value = prompt_unformatted_value.format(
        **{
            "train_test_split_percentage": train_test_split_percentage,
            "test_val_split_percentage": test_val_split_percentage,
            "location": project_dir + "/data/interim",
        }
    )
    return prompt_value, project_dir + file_location
