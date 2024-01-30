import socket


def port_scanner(target: str, target_ports: list[str]) -> dict[str, str]:
    """"
    Essa função simula um comando NetCat,
    tenta realizar a conexão com as portas específicadas
    e retorna um hashmap com no formato porta = estado
    """
    result: dict[str, str] = dict()
    for porta in target_ports:
        try:
            client: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target, int(porta)))
            client.close()
            result[porta] = "open"
        except:
            result[porta] = "closed"

    return result


if __name__ == '__main__':
    ip_domain: str = input('Ip domain para escanear: ')
    ports: str = input('Porta ou range de portas para escanear(Multiplas portas devem ser separadas por espaços): ')
    data: dict[str, str] = port_scanner(ip_domain, [port for port in ports.split()])
    print(data)
