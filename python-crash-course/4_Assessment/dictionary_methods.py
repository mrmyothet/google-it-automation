def network(servers):
    result = ""

    for host_name, IP_address in servers.items():
        result += (
            "The IP address of {} server is {}".format(host_name, IP_address) + "\n"
        )

    return result


print(
    network(
        {
            "Domain Name Server": "8.8.8.8",
            "Gateway Server": "192.168.1.1",
            "Print Server": "192.168.1.33",
            "Mail Server": "192.168.1.190",
        }
    )
)

# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190


def reset_scores(game_scores):
    new_game_scores = game_scores.copy()

    for player, score in new_game_scores.items():
        new_game_scores[player] = 0

    return new_game_scores


game_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}

print(reset_scores(game_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}
