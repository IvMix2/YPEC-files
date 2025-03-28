def generate_prompt(
        rows,
        column_names,
        min_num_of_repetitions=0,
        max_num_of_repetitions=0,
):
    prompt = f"Сгенерируй {rows} записей для таблицы в базе данных со стобцами: "

    for i in range(len(column_names)):
        if i == len(column_names) - 1:
            prompt += f"{column_names[i]}. "
            break
        prompt += f"{column_names[i]}, "

    if min_num_of_repetitions > max_num_of_repetitions:
        raise ValueError("min > max!")
    else:
        if min_num_of_repetitions >= 0:
            if max_num_of_repetitions > 0:
                prompt += f"Сгенерируй так, чтобы встречались повторения в разных(по возможности(не должно быть повторений тех данных, которые по логике не должны повторятся)) столбцах и чтобы было хотя бы {min_num_of_repetitions} повторений и максимум {max_num_of_repetitions}. "
            else:
                prompt += f"Сгенерируй так, чтобы не было повторений в записях. "

    data_patterns = {
        "phone_number": "+7-999-999-99-99"
    }
    prompt += f"Для следующих видов данных при их наличии используй эти шаблон: {data_patterns} "
    prompt += "ГЕНЕРИРУЙ ПОЛНЫЙ СПИСОК!!!! Результат выдай в виде json кода, без лишних слов, без комментариеви и пояснений, чтобы твой ответ можно было спокойно спарсить и без ```"

    return prompt