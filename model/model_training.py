def __get_default_model_values(request_config):
    specification = request_config["specifications"]["training"]
    default_specifications = request_config["default_specifications"]
    model_type = (
        specification["model_type"]
        if specification["model_type"]
        else default_specifications["model_type"]
    )
    return model_type


def create_model_training_code(prompt_details, request_config, project_dir):
    model_type = __get_default_model_values(request_config)
    prompt_unformatted_value, file_location = prompt_details
    prompt_value = prompt_unformatted_value.format(
        **{"model_type": model_type, "location": "models"}
    )
    return prompt_value, project_dir + file_location
