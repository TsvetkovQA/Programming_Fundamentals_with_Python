def generate_loading_bar(percentage):
    bar_length = 10
    complete_length = percentage // 10
    loading_bar = "[" + "%" * complete_length + "." * (bar_length - complete_length) + "]"

    if percentage < 100:
        return f"{percentage}% {loading_bar}\nStill loading..."
    else:
        return f"{percentage}% Complete!\n{loading_bar}"



percentage = int(input())


print(generate_loading_bar(percentage))
