import pexpect


def pyconsole_connect(host, login, port):
    connect_command = '/usr/bin/ssh {login}@{host} -p {port}'.format(login=login, host=host, port=port)
    child = pexpect.spawn(connect_command)
    child.expect('Password:', timeout=5)

    child.sendline(login)
    child.expect('net', timeout=5)

    child.sendline('cluster-control pyconsole cellapp')
    child.expect('>>>', timeout=5)

    print('Connected successfully!')

    return child


def close_connection(child, timeout=2):
    child.sendcontrol('d')
    child.expect('Connection closed by foreign host.', timeout=timeout)
    print('Connection closed.')


def execute_python(child):
    child.sendcontrol('m')
    child.expect('>>>', timeout=2)


def get_position(child):
    child.sendline('vehicle.autoPilot.position')
    execute_python(child)
    print(child.before)


def move(child, x, y, z):
    child.sendline('vehicle.autoPilot.moveTo(({x}, {z}, {y}), True)'.format(x=x, z=z, y=y))
    execute_python(child)


def stop(child):
    child.sendline('vehicle.autoPilot.stop()')
    execute_python(child)


def import_module(child):
    child.sendline('from navigation.navigation_debug import findVehicle')
    execute_python(child)


def find_vehicle(child, tank_id):
    child.sendline('vehicle = findVehicle({})'.format(tank_id))
    execute_python(child)


def get_move_data():
    x = float(input('Enter X value: '))
    y = float(input('Enter Y value: '))
    z = float(input('Enter Z value: '))

    return x, y, z


def main():
    host = input('Enter server host: ')
    login = input('Enter login: ')
    port = input('Enter port (not required): ')

    try:
        child = pyconsole_connect(host, login, port)

        import_module(child)
        find_vehicle(child, 502)

        while True:
            operation = input('Enter operation "move" or "stop" ("exit" to finish): ')
            if operation.lower() == 'exit':
                break
            elif operation.lower() == 'move':
                move_data = get_move_data()
                move(child, *move_data)
            elif operation.lower() == 'stop':
                stop(child)
            else:
                print('Incorrect data, please repeat.')

        close_connection(child)

    except:
        print('Cannot connect to server. Please, check your data or server state.')


if __name__ == '__main__':
    main()
